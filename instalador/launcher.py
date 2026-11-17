# -*- coding: utf-8 -*-
"""HEFAESTOUS.exe — lançador do aplicativo (janela pequena + servidor local + navegador).

Procura o interpretador em <pasta>\\runtime\\python.exe (instalação feita pelo Instalar_HEFAESTOUS.exe) ou, no
ambiente de desenvolvimento, em web\\.venv313\\Scripts\\python.exe; sobe web/app.py sem console, espera o servidor
responder, abre o navegador e mostra uma janela com o endereço e os botões "Abrir no navegador" e "Encerrar".
Fechar a janela encerra o servidor. Se o servidor já estiver rodando (outra instância), só abre o navegador.
Compilação: instalador\\build.bat (PyInstaller --noconsole, ícone hefaestous.ico).
"""
import os
import socket
import subprocess
import sys
import threading
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


def main():
    import tkinter as tk
    from tkinter import messagebox, ttk

    base = pasta()
    py = interpretador(base)
    app = os.path.join(base, "web", "app.py")
    # restos de uma atualização automática concluída (o .bat não consegue se apagar enquanto roda)
    for resto in ("atualizar.bat",):
        try:
            os.remove(os.path.join(base, resto))
        except OSError:
            pass
    root = tk.Tk(); root.title(APP); root.resizable(False, False)
    ico = os.path.join(base, "web", "frontend", "img", "hefaestous.ico")
    if os.path.exists(ico):
        try:
            root.iconbitmap(ico)
        except Exception:  # noqa: BLE001
            pass
    frm = ttk.Frame(root, padding=16); frm.grid()
    ttk.Label(frm, text=APP, font=("Segoe UI", 15, "bold")).grid(row=0, column=0, columnspan=2, sticky="w")
    ttk.Label(frm, text="Dimensionamento de engrenagens · FEM/Unicamp — LAMAR", foreground="#555").grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 10))
    status = tk.StringVar(value="Iniciando o servidor…")
    ttk.Label(frm, textvariable=status, wraplength=420).grid(row=2, column=0, columnspan=2, sticky="w")
    url_var = tk.StringVar(value="")
    link = ttk.Label(frm, textvariable=url_var, foreground="#0b4fa8", cursor="hand2"); link.grid(row=3, column=0, columnspan=2, sticky="w", pady=(2, 10))
    b_abrir = ttk.Button(frm, text="Abrir no navegador", state="disabled"); b_abrir.grid(row=4, column=0, sticky="w")
    b_sair = ttk.Button(frm, text="Encerrar"); b_sair.grid(row=4, column=1, sticky="e", padx=(10, 0))
    ttk.Label(frm, text="Deixe esta janela aberta enquanto usa o programa. Fechá-la encerra o servidor.\nEm caso de problema, veja erros.txt na pasta do programa.", foreground="#777", font=("Segoe UI", 8)).grid(row=5, column=0, columnspan=2, sticky="w", pady=(10, 0))

    logs_dir = os.path.join(base, "logs")
    log_path = os.path.join(logs_dir, "servidor.log")
    estado = {"proc": None, "url": None, "job": _job_kill_on_close()}

    def abrir():
        if estado["url"]:
            webbrowser.open(estado["url"])
    b_abrir.configure(command=abrir); link.bind("<Button-1>", lambda e: abrir())

    def encerrar():
        p = estado["proc"]
        if p and p.poll() is None:
            try:
                p.terminate(); p.wait(5)
            except Exception:  # noqa: BLE001
                try:
                    p.kill()
                except Exception:  # noqa: BLE001
                    pass
        root.destroy()
    b_sair.configure(command=encerrar); root.protocol("WM_DELETE_WINDOW", encerrar)

    def pronto(url):
        estado["url"] = url; url_var.set(url); status.set("Servidor em execução."); b_abrir.configure(state="normal"); webbrowser.open(url)

    def iniciar():
        if not py or not os.path.exists(app):
            registrar_erro(base, "instalação incompleta", f"python: {py}\napp: {app} (existe: {os.path.exists(app)})")
            root.after(0, lambda: (status.set("Instalação incompleta: runtime\\python.exe ou web\\app.py não encontrados.\nExecute o Instalar_HEFAESTOUS.exe novamente."), b_sair.configure(text="Fechar")))
            return
        host, porta = "127.0.0.1", 8765
        if not porta_livre(host, porta):
            url = f"http://{host}:{porta}/"
            if e_nosso(url):
                root.after(0, lambda: (status.set("O HEFAESTOUS já estava em execução (outra janela)."), pronto(url)))
                return
            for cand in range(porta + 1, porta + 20):
                if porta_livre(host, cand):
                    porta = cand; break
        url = f"http://{host}:{porta}/"
        os.makedirs(logs_dir, exist_ok=True)
        # stdout/stderr do servidor (uvicorn + tracebacks) vão para logs\servidor.log; o app também escreve erros.txt (backend/logs.py)
        logf = open(log_path, "a", encoding="utf-8", errors="replace")
        logf.write("\n===== HEFAESTOUS iniciado em " + time.strftime("%Y-%m-%d %H:%M:%S") + " - " + py + " =====\n"); logf.flush()
        # sem as variáveis do PyInstaller (PYTHONHOME/PYTHONPATH…), senão o runtime embeddable carrega módulos do .exe
        env = {k: v for k, v in os.environ.items() if not k.upper().startswith(("PYTHON", "VIRTUAL_ENV", "_PYI", "PYI_", "TCL_", "TK_"))}
        env.update(PYTHONIOENCODING="utf-8", PYTHONUTF8="1", PYTHONUNBUFFERED="1", HEFAESTOUS_HOME=base)
        try:
            estado["proc"] = subprocess.Popen([py, app, "--no-browser", "--host", host, "--port", str(porta)], cwd=os.path.join(base, "web"),
                                              stdout=logf, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, creationflags=CREATE_NO_WINDOW, env=env)
        except Exception as ex:  # noqa: BLE001
            registrar_erro(base, "não foi possível iniciar o servidor", repr(ex))
            root.after(0, lambda: (status.set("Não foi possível iniciar o servidor. Veja erros.txt na pasta do programa."), b_sair.configure(text="Fechar")))
            return
        _assign_job(estado["job"], estado["proc"])
        for _ in range(120):
            if estado["proc"].poll() is not None:
                logf.flush()
                registrar_erro(base, f"o servidor encerrou ao iniciar (código {estado['proc'].returncode})", ultimas_linhas(log_path))
                root.after(0, lambda: (status.set("O servidor encerrou com erro. Veja erros.txt na pasta do programa."), b_sair.configure(text="Fechar")))
                return
            try:
                urllib.request.urlopen(url, timeout=1).read(10)
                root.after(0, lambda: pronto(url)); return
            except Exception:  # noqa: BLE001
                time.sleep(0.5)
        registrar_erro(base, "o servidor não respondeu em 60 s", ultimas_linhas(log_path))
        root.after(0, lambda: status.set("O servidor não respondeu em 60 s. Veja erros.txt na pasta do programa."))

    threading.Thread(target=iniciar, daemon=True).start()
    try:
        root.mainloop()
    except Exception as ex:  # noqa: BLE001
        messagebox.showerror(APP, str(ex))


if __name__ == "__main__":
    main()
