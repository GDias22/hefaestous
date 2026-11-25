# -*- coding: utf-8 -*-
"""HEFAESTOUS.exe — lançador do aplicativo, SEM janela: sobe o servidor local e abre o navegador.

Procura o interpretador em <pasta>\\runtime\\python.exe (instalação feita pelo Instalar_HEFAESTOUS.exe) ou, no
ambiente de desenvolvimento, em web\\.venv313\\Scripts\\python.exe; sobe web/app.py sem console (com --auto-encerrar),
espera o servidor responder e abre o navegador. Não mostra nada: o processo fica invisível enquanto o servidor viver, e o
servidor se encerra sozinho quando a última aba da interface fechar (web/backend/api/vida.py). Se o servidor já estiver
rodando (outra instância), só abre mais uma aba. Erros: erros.txt + uma caixa de mensagem do Windows.
Compilação: instalador\\build.bat (PyInstaller --noconsole, ícone hefaestous.ico).
"""
import os
import socket
import subprocess
import sys
import time
import urllib.request
import webbrowser

APP = "HEFAESTOUS"
CREATE_NO_WINDOW = 0x08000000


def _job_kill_on_close():
    """Job Object do Windows com KILL_ON_JOB_CLOSE: o servidor filho morre junto com o lançador, mesmo se este for
    encerrado à força (Gerenciador de Tarefas, logoff). Devolve o handle ou None."""
    try:
        import ctypes
        from ctypes import wintypes
        k32 = ctypes.windll.kernel32
        job = k32.CreateJobObjectW(None, None)
        if not job:
            return None

        class IO_COUNTERS(ctypes.Structure):
            _fields_ = [(n, ctypes.c_ulonglong) for n in ("ReadOperationCount", "WriteOperationCount", "OtherOperationCount", "ReadTransferCount", "WriteTransferCount", "OtherTransferCount")]

        class JOBOBJECT_BASIC_LIMIT_INFORMATION(ctypes.Structure):
            _fields_ = [("PerProcessUserTimeLimit", ctypes.c_longlong), ("PerJobUserTimeLimit", ctypes.c_longlong), ("LimitFlags", wintypes.DWORD),
                        ("MinimumWorkingSetSize", ctypes.c_size_t), ("MaximumWorkingSetSize", ctypes.c_size_t), ("ActiveProcessLimit", wintypes.DWORD),
                        ("Affinity", ctypes.c_size_t), ("PriorityClass", wintypes.DWORD), ("SchedulingClass", wintypes.DWORD)]

        class JOBOBJECT_EXTENDED_LIMIT_INFORMATION(ctypes.Structure):
            _fields_ = [("BasicLimitInformation", JOBOBJECT_BASIC_LIMIT_INFORMATION), ("IoInfo", IO_COUNTERS), ("ProcessMemoryLimit", ctypes.c_size_t),
                        ("JobMemoryLimit", ctypes.c_size_t), ("PeakProcessMemoryUsed", ctypes.c_size_t), ("PeakJobMemoryUsed", ctypes.c_size_t)]
        info = JOBOBJECT_EXTENDED_LIMIT_INFORMATION()
        info.BasicLimitInformation.LimitFlags = 0x2000          # JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
        if not k32.SetInformationJobObject(job, 9, ctypes.byref(info), ctypes.sizeof(info)):   # JobObjectExtendedLimitInformation
            return None
        return job
    except Exception:  # noqa: BLE001
        return None


def _assign_job(job, proc):
    if job is None:
        return
    try:
        import ctypes
        ctypes.windll.kernel32.AssignProcessToJobObject(job, int(proc._handle))
    except Exception:  # noqa: BLE001
        pass


def pasta():
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def interpretador(base):
    for p in (os.path.join(base, "runtime", "python.exe"), os.path.join(base, "web", ".venv313", "Scripts", "python.exe")):
        if os.path.exists(p):
            return p
    return None


def porta_livre(host, porta):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.3)
        return s.connect_ex((host, porta)) != 0


def e_nosso(url):
    try:
        with urllib.request.urlopen(url + "api/meta/params", timeout=2) as r:
            return r.status == 200 and b'"stages"' in r.read(200)
    except Exception:  # noqa: BLE001
        return False


def registrar_erro(base, titulo, detalhe=""):
    """Acrescenta uma entrada em <instalação>\\erros.txt (histórico legível de problemas) — nunca mostra terminal.
    O log completo do servidor fica em <instalação>\\logs\\servidor.log."""
    try:
        with open(os.path.join(base, "erros.txt"), "a", encoding="utf-8") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] LANÇADOR: {titulo}\n")
            if detalhe:
                f.write("".join("    " + l + "\n" for l in str(detalhe).rstrip().splitlines()))
            f.write("\n")
    except Exception:  # noqa: BLE001
        pass


def ultimas_linhas(caminho, n=40):
    try:
        with open(caminho, encoding="utf-8", errors="replace") as f:
            return "".join(f.readlines()[-n:])
    except Exception:  # noqa: BLE001
        return ""


def _erro_dialogo(texto):
    """Caixa de mensagem nativa do Windows (sem Tk): o único momento em que o lançador mostra algo."""
    try:
        import ctypes
        ctypes.windll.user32.MessageBoxW(None, texto, APP, 0x10 | 0x40000)   # MB_ICONERROR | MB_TOPMOST
    except Exception:  # noqa: BLE001
        pass


def main():
    base = pasta()
    py = interpretador(base)
    app = os.path.join(base, "web", "app.py")
    # restos de uma atualização automática concluída (o .bat não consegue se apagar enquanto roda)
    for resto in ("atualizar.bat",):
        try:
            os.remove(os.path.join(base, resto))
        except OSError:
            pass
    if not py or not os.path.exists(app):
        registrar_erro(base, "instalação incompleta", f"python: {py}\napp: {app} (existe: {os.path.exists(app)})")
        _erro_dialogo("Instalação incompleta: runtime\\python.exe ou web\\app.py não encontrados.\n\nExecute o Instalar_HEFAESTOUS.exe novamente.")
        return 1
    host, porta = "127.0.0.1", 8765
    if not porta_livre(host, porta):
        url = f"http://{host}:{porta}/"
        if e_nosso(url):            # já está rodando (outra instância): só abre mais uma aba
            webbrowser.open(url); return 0
        for cand in range(porta + 1, porta + 20):
            if porta_livre(host, cand):
                porta = cand; break
    url = f"http://{host}:{porta}/"
    logs_dir = os.path.join(base, "logs"); os.makedirs(logs_dir, exist_ok=True)
    log_path = os.path.join(logs_dir, "servidor.log")
    # stdout/stderr do servidor (uvicorn + tracebacks) vão para logs\servidor.log; o app também escreve erros.txt (backend/logs.py)
    logf = open(log_path, "a", encoding="utf-8", errors="replace")
    logf.write("\n===== HEFAESTOUS iniciado em " + time.strftime("%Y-%m-%d %H:%M:%S") + " - " + py + " =====\n"); logf.flush()
    # sem as variáveis do PyInstaller (PYTHONHOME/PYTHONPATH…), senão o runtime embeddable carrega módulos do .exe
    env = {k: v for k, v in os.environ.items() if not k.upper().startswith(("PYTHON", "VIRTUAL_ENV", "_PYI", "PYI_", "TCL_", "TK_"))}
    env.update(PYTHONIOENCODING="utf-8", PYTHONUTF8="1", PYTHONUNBUFFERED="1", HEFAESTOUS_HOME=base)
    job = _job_kill_on_close()
    try:
        # --auto-encerrar: o servidor se encerra sozinho quando a última aba do navegador fechar (web/backend/api/vida.py)
        proc = subprocess.Popen([py, app, "--no-browser", "--auto-encerrar", "--host", host, "--port", str(porta)], cwd=os.path.join(base, "web"),
                                stdout=logf, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, creationflags=CREATE_NO_WINDOW, env=env)
    except Exception as ex:  # noqa: BLE001
        registrar_erro(base, "não foi possível iniciar o servidor", repr(ex))
        _erro_dialogo("Não foi possível iniciar o servidor.\n\nVeja erros.txt na pasta do programa.")
        return 1
    _assign_job(job, proc)
    for _ in range(120):
        if proc.poll() is not None:
            logf.flush()
            registrar_erro(base, f"o servidor encerrou ao iniciar (código {proc.returncode})", ultimas_linhas(log_path))
            _erro_dialogo("O servidor encerrou com erro ao iniciar.\n\nVeja erros.txt na pasta do programa.")
            return 1
        try:
            urllib.request.urlopen(url, timeout=1).read(10)
            break
        except Exception:  # noqa: BLE001
            time.sleep(0.5)
    else:
        registrar_erro(base, "o servidor não respondeu em 60 s", ultimas_linhas(log_path))
        _erro_dialogo("O servidor não respondeu em 60 s.\n\nVeja erros.txt na pasta do programa.")
        try:
            proc.terminate()
        except Exception:  # noqa: BLE001
            pass
        return 1
    try:
        if not webbrowser.open(url):
            raise RuntimeError("webbrowser.open devolveu False")
    except Exception:  # noqa: BLE001
        try:
            os.startfile(url)  # noqa: S606
        except Exception as ex:  # noqa: BLE001
            registrar_erro(base, "não foi possível abrir o navegador", f"{url}\n{ex!r}")
    # fica vivo, invisível, enquanto o servidor viver: é o dono do Job Object (se o lançador morrer, o servidor morre junto);
    # o servidor se encerra sozinho quando a última aba fechar, e então o lançador termina também.
    proc.wait()
    logf.flush()
    if proc.returncode not in (0, None, -15, 15, 0xC000013A):
        registrar_erro(base, f"o servidor encerrou com código {proc.returncode}", ultimas_linhas(log_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
