# -*- coding: utf-8 -*-
"""Instalador do HEFAESTOUS (Windows).

Distribuição: a pasta do projeto (clonada do git ou baixada como ZIP) contém este instalador compilado como
`Instalar_HEFAESTOUS.exe`. O usuário descompacta, executa o .exe e o instalador:

  1. copia os arquivos da aplicação (módulos .py, Figuras, Exemplos_fem, web/) para a pasta de instalação
     (padrão: %LOCALAPPDATA%\\Programs\\HEFAESTOUS — não precisa de administrador);
  2. baixa o Python 3.13 "embeddable" oficial (python.org, ~11 MB) para <instalação>\\runtime;
  3. instala o pip e as dependências de web/requirements.txt (inclui o kernel CAD cadquery-ocp, ~300 MB)
     — ou, sem internet, usa as wheels de uma pasta `wheels/` ao lado do instalador, se existir;
  4. cria os atalhos (Área de Trabalho e Menu Iniciar) para HEFAESTOUS.exe, com o ícone do app, e registra o
     programa em "Aplicativos instalados" (HKCU) com um Desinstalar.bat.

Uso silencioso (automação/testes):  Instalar_HEFAESTOUS.exe --silent --dest <pasta> [--sem-atalhos] [--log arquivo]
Compilação: instalador\\build.bat (PyInstaller, no venv web\\.venv313).
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import threading
import time
import traceback
import urllib.request
import zipfile

APP = "HEFAESTOUS"


def _env_limpo():
    """Ambiente para os processos filhos SEM as variáveis que o PyInstaller/venv injetam (PYTHONHOME, PYTHONPATH, VIRTUAL_ENV…):
    com elas o Python embeddable enxergava o pip do processo pai e a verificação passava, mas o pip real não existia."""
    env = {k: v for k, v in os.environ.items() if not k.upper().startswith(("PYTHON", "VIRTUAL_ENV", "_PYI", "PYI_", "TCL_", "TK_"))}
    env["PYTHONIOENCODING"] = "utf-8"; env["PYTHONUTF8"] = "1"
    return env


PY_VER = "3.13.9"
PY_URL = f"https://www.python.org/ftp/python/{PY_VER}/python-{PY_VER}-embed-amd64.zip"
GETPIP_URL = "https://bootstrap.pypa.io/get-pip.py"
CREATE_NO_WINDOW = 0x08000000

# O que da pasta de origem vai para a instalação (lista branca na raiz; web/ é copiada com exclusões).
RAIZ_ARQUIVOS_EXT = {".py", ".md"}
RAIZ_PASTAS = ["Figuras", "Exemplos_fem"]
RAIZ_EXTRAS = ["HEFAESTOUS.exe"]
WEB_EXCLUIR_DIRS = {".venv313", "node_modules", "sessions", "__pycache__", "tests", ".pytest_cache", "_legado_v1"}
WEB_EXCLUIR_ARQ = {"web_server.log", "package.json", "package-lock.json"}


def origem():
    """Pasta da distribuição: onde está o .exe (congelado) ou a raiz do projeto (fonte)."""
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def versao(src):
    try:
        with open(os.path.join(src, "instalador", "versao.json"), encoding="utf-8") as f:
            return json.load(f).get("versao", "1.0")
    except Exception:  # noqa: BLE001
        return "1.0"


def destino_padrao():
    base = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
    return os.path.join(base, "Programs", APP)


# --------------------------------------------------------------------------------------------- etapas
class Instalacao:
    def __init__(self, src, dest, atalhos=True, log=print, progresso=lambda frac, txt: None):
        self.src, self.dest, self.atalhos = src, os.path.abspath(dest), atalhos
        self.log, self.prog = log, progresso
        self.py = os.path.join(self.dest, "runtime", "python.exe")

    def run(self):
        etapas = [("Copiando a aplicação", self.copiar), ("Baixando o Python 3.13", self.python),
                  ("Instalando o pip", self.pip), ("Instalando as dependências (pode levar alguns minutos)", self.dependencias),
                  ("Verificando", self.verificar), ("Criando atalhos e registro", self.registrar)]
        for i, (nome, fn) in enumerate(etapas):
            self.prog(i / len(etapas), nome)
            self.log(f"\n== {nome}")
            fn()
        self.prog(1.0, "Concluído")
        self.log(f"\nInstalação concluída em {self.dest}")

    # 1 ----------------------------------------------------------------------------------------
    def copiar(self):
        os.makedirs(self.dest, exist_ok=True)
        n = 0
        for a in os.listdir(self.src):
            p = os.path.join(self.src, a)
            if os.path.isfile(p) and (os.path.splitext(a)[1].lower() in RAIZ_ARQUIVOS_EXT or a in RAIZ_EXTRAS):
                shutil.copy2(p, os.path.join(self.dest, a)); n += 1
        for d in RAIZ_PASTAS:
            p = os.path.join(self.src, d)
            if os.path.isdir(p):
                n += self._copytree(p, os.path.join(self.dest, d), set(), set())
        n += self._copytree(os.path.join(self.src, "web"), os.path.join(self.dest, "web"), WEB_EXCLUIR_DIRS, WEB_EXCLUIR_ARQ)
        os.makedirs(os.path.join(self.dest, "web", "sessions"), exist_ok=True)
        if not os.path.exists(os.path.join(self.dest, "web", "app.py")):
            raise RuntimeError("web/app.py não encontrado na pasta de origem: execute o instalador de dentro da pasta descompactada do HEFAESTOUS.")
        self.log(f"   {n} arquivos copiados")

    def _copytree(self, a, b, ex_dirs, ex_arq):
        n = 0
        for raiz, dirs, arqs in os.walk(a):
            dirs[:] = [d for d in dirs if d not in ex_dirs and not d.startswith(".")]
            rel = os.path.relpath(raiz, a)
            alvo = os.path.join(b, rel) if rel != "." else b
            os.makedirs(alvo, exist_ok=True)
            for f in arqs:
                if f in ex_arq or f.endswith(".pyc"):
                    continue
                shutil.copy2(os.path.join(raiz, f), os.path.join(alvo, f)); n += 1
        return n

    # 2 ----------------------------------------------------------------------------------------
    def python(self):
        rt = os.path.join(self.dest, "runtime")
        if os.path.exists(self.py):
            self.log("   runtime já existe — mantido"); return
        os.makedirs(rt, exist_ok=True)
        zp = os.path.join(rt, "python-embed.zip")
        local = os.path.join(self.src, "instalador", os.path.basename(PY_URL))
        if os.path.exists(local):
            shutil.copy2(local, zp); self.log("   usando o zip do Python incluído na distribuição")
        else:
            self._baixar(PY_URL, zp)
        with zipfile.ZipFile(zp) as z:
            z.extractall(rt)
        os.remove(zp)
        # habilita site-packages no Python embeddable (linha "#import site" do ._pth)
        for f in os.listdir(rt):
            if f.endswith("._pth"):
                p = os.path.join(rt, f)
                with open(p, encoding="utf-8") as fh:
                    txt = fh.read()
                txt = txt.replace("#import site", "import site")
                if "Lib\\site-packages" not in txt:
                    txt += "\nLib\\site-packages\n"
                with open(p, "w", encoding="utf-8") as fh:
                    fh.write(txt)
        self.log("   " + self._saida([self.py, "-c", "import sys; print(sys.version)"]).strip())

    # 3 ----------------------------------------------------------------------------------------
    def pip(self):
        if self._ok([self.py, "-m", "pip", "--version"]):
            self.log("   pip já disponível"); return
        gp = os.path.join(self.dest, "runtime", "get-pip.py")
        local = os.path.join(self.src, "instalador", "get-pip.py")
        if os.path.exists(local):
            shutil.copy2(local, gp)
        else:
            self._baixar(GETPIP_URL, gp)
        self._rodar([self.py, gp, "--no-warn-script-location", "--quiet"])
        os.remove(gp)

    # 4 ----------------------------------------------------------------------------------------
    def dependencias(self):
        req = os.path.join(self.dest, "web", "requirements.txt")
        cmd = [self.py, "-m", "pip", "install", "--no-warn-script-location", "--disable-pip-version-check", "-r", req]
        wheels = os.path.join(self.src, "instalador", "wheels")
        if os.path.isdir(wheels) and os.listdir(wheels):
            cmd += ["--no-index", "--find-links", wheels]; self.log("   modo offline: wheels de " + wheels)
        self._rodar(cmd)

    # 5 ----------------------------------------------------------------------------------------
    def verificar(self):
        out = self._saida([self.py, "-c", "import fastapi, uvicorn, numpy, scipy, build123d; print('fastapi', fastapi.__version__, '| build123d', build123d.__version__)"])
        self.log("   " + out.strip())

    # 6 ----------------------------------------------------------------------------------------
    def registrar(self):
        exe = os.path.join(self.dest, "HEFAESTOUS.exe")
        ico = os.path.join(self.dest, "web", "frontend", "img", "hefaestous.ico")
        if not os.path.exists(exe):      # distribuição sem o lançador compilado: atalho para o python + app.py
            exe = os.path.join(self.dest, "runtime", "pythonw.exe")
        desinst = os.path.join(self.dest, "Desinstalar.bat")
        with open(desinst, "w", encoding="cp1252", errors="replace") as f:
            f.write(DESINSTALAR_BAT.format(dest=self.dest, app=APP))
        if self.atalhos:
            self._atalho(os.path.join(os.path.join(os.environ.get("USERPROFILE", ""), "Desktop"), f"{APP}.lnk"), exe, ico)
            menu = os.path.join(os.environ.get("APPDATA", ""), "Microsoft", "Windows", "Start Menu", "Programs")
            self._atalho(os.path.join(menu, f"{APP}.lnk"), exe, ico)
            self.log("   atalhos criados (Área de Trabalho e Menu Iniciar)")
        # "Aplicativos instalados" (somente o usuário atual; sem administrador)
        chave = rf"HKCU\Software\Microsoft\Windows\CurrentVersion\Uninstall\{APP}"
        v = versao(self.src)
        for nome, tipo, val in [("DisplayName", "REG_SZ", f"{APP} — Dimensionamento de engrenagens"), ("DisplayVersion", "REG_SZ", v),
                                ("Publisher", "REG_SZ", "FEM/Unicamp — LAMAR · Gabriel Dias"), ("InstallLocation", "REG_SZ", self.dest),
                                ("DisplayIcon", "REG_SZ", ico), ("UninstallString", "REG_SZ", f'"{desinst}"'), ("NoModify", "REG_DWORD", "1"), ("NoRepair", "REG_DWORD", "1")]:
            self._ok(["reg", "add", chave, "/v", nome, "/t", tipo, "/d", val, "/f"])
        self.log("   registrado em Configurações › Aplicativos (Desinstalar.bat)")

    def _atalho(self, lnk, alvo, ico):
        args = "" if alvo.lower().endswith("hefaestous.exe") else f'"{os.path.join(self.dest, "web", "app.py")}"'
        ps = ("$s=(New-Object -ComObject WScript.Shell).CreateShortcut('%s');$s.TargetPath='%s';$s.Arguments='%s';$s.WorkingDirectory='%s';"
              "$s.IconLocation='%s,0';$s.Description='HEFAESTOUS - Dimensionamento de engrenagens';$s.Save()") % (lnk, alvo, args, self.dest, ico)
        os.makedirs(os.path.dirname(lnk), exist_ok=True)
        self._rodar(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps])

    # util ----------------------------------------------------------------------------------------
    def _baixar(self, url, destino):
        self.log(f"   baixando {url}")
        req = urllib.request.Request(url, headers={"User-Agent": f"{APP}-installer"})
        with urllib.request.urlopen(req, timeout=60) as r, open(destino, "wb") as f:
            total = int(r.headers.get("Content-Length") or 0); lido = 0; t0 = time.time()
            while True:
                b = r.read(1 << 16)
                if not b:
                    break
                f.write(b); lido += len(b)
                if total and time.time() - t0 > 0.5:
                    t0 = time.time(); self.log(f"   {lido / 1e6:.1f} / {total / 1e6:.1f} MB", transient=True)
        self.log(f"   {lido / 1e6:.1f} MB")

    def _rodar(self, cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, text=True,
                             encoding="utf-8", errors="replace", creationflags=CREATE_NO_WINDOW, cwd=self.dest, env=_env_limpo())
        for linha in p.stdout:
            linha = linha.rstrip()
            if linha:
                self.log("   " + linha)
        p.wait()
        if p.returncode != 0:
            raise RuntimeError(f"comando falhou ({p.returncode}): {' '.join(cmd[:3])} …")

    def _saida(self, cmd):
        return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", creationflags=CREATE_NO_WINDOW, check=True, stdin=subprocess.DEVNULL, env=_env_limpo()).stdout

    def _ok(self, cmd):
        try:
            subprocess.run(cmd, capture_output=True, creationflags=CREATE_NO_WINDOW, check=True, stdin=subprocess.DEVNULL, env=_env_limpo()); return True
        except Exception:  # noqa: BLE001
            return False


DESINSTALAR_BAT = r"""@echo off
title Desinstalar {app}
echo Isto remove o {app} de "{dest}" e os atalhos. Seus arquivos .fem salvos em outras pastas nao sao afetados.
set /p ok=Continuar? (S/N):
if /i not "%ok%"=="S" exit /b
del "%USERPROFILE%\Desktop\{app}.lnk" 2>nul
del "%APPDATA%\Microsoft\Windows\Start Menu\Programs\{app}.lnk" 2>nul
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Uninstall\{app}" /f >nul 2>&1
cd /d "%TEMP%"
start "" /b cmd /c "timeout /t 1 >nul & rmdir /s /q "{dest}""
echo Removido.
"""


# --------------------------------------------------------------------------------------------- GUI
def gui(src):
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk

    root = tk.Tk(); root.title(f"Instalar {APP}"); root.resizable(False, False)
    ico = os.path.join(src, "web", "frontend", "img", "hefaestous.ico")
    if os.path.exists(ico):
        try:
            root.iconbitmap(ico)
        except Exception:  # noqa: BLE001
            pass
    frm = ttk.Frame(root, padding=16); frm.grid(sticky="nsew")
    ttk.Label(frm, text=APP, font=("Segoe UI", 16, "bold")).grid(row=0, column=0, columnspan=3, sticky="w")
    ttk.Label(frm, text=f"Dimensionamento de engrenagens · DIN 3960/3967 · ISO 6336 · versão {versao(src)}\n"
                        "FEM/Unicamp — LAMAR · Desenvolvido por Gabriel Dias", foreground="#555").grid(row=1, column=0, columnspan=3, sticky="w", pady=(0, 12))
    ttk.Label(frm, text="Pasta de instalação:").grid(row=2, column=0, sticky="w")
    dest = tk.StringVar(value=destino_padrao())
    ttk.Entry(frm, textvariable=dest, width=58).grid(row=2, column=1, sticky="we", padx=6)
    ttk.Button(frm, text="…", width=3, command=lambda: dest.set(filedialog.askdirectory(initialdir=dest.get()) or dest.get())).grid(row=2, column=2)
    atalhos = tk.BooleanVar(value=True); abrir = tk.BooleanVar(value=True)
    ttk.Checkbutton(frm, text="Criar atalhos na Área de Trabalho e no Menu Iniciar", variable=atalhos).grid(row=3, column=0, columnspan=3, sticky="w", pady=(8, 0))
    ttk.Checkbutton(frm, text="Abrir o HEFAESTOUS ao terminar", variable=abrir).grid(row=4, column=0, columnspan=3, sticky="w")
    ttk.Label(frm, text="O instalador baixa o Python 3.13 (python.org) e as bibliotecas necessárias (~400 MB, inclui o kernel CAD).\n"
                        "Precisa de internet; não precisa de administrador.", foreground="#555").grid(row=5, column=0, columnspan=3, sticky="w", pady=(8, 8))
    barra = ttk.Progressbar(frm, length=560, mode="determinate"); barra.grid(row=6, column=0, columnspan=3, sticky="we")
    etapa = ttk.Label(frm, text=""); etapa.grid(row=7, column=0, columnspan=3, sticky="w")
    log = tk.Text(frm, height=12, width=78, font=("Consolas", 9), state="disabled", bg="#f7f8fa", relief="flat"); log.grid(row=8, column=0, columnspan=3, pady=(6, 10))
    btn = ttk.Button(frm, text="Instalar"); btn.grid(row=9, column=2, sticky="e")
    fechar = ttk.Button(frm, text="Cancelar", command=root.destroy); fechar.grid(row=9, column=1, sticky="e", padx=(0, 6))

    def escreve(txt, transient=False):
        def _():
            log.configure(state="normal")
            if transient and getattr(log, "_trans", False):
                log.delete("end-2l", "end-1l")
            log.insert("end", txt + "\n"); log._trans = transient; log.see("end"); log.configure(state="disabled")
        root.after(0, _)

    def progresso(frac, txt):
        root.after(0, lambda: (barra.configure(value=frac * 100), etapa.configure(text=txt)))

    def iniciar():
        btn.configure(state="disabled"); fechar.configure(state="disabled")

        def trabalho():
            try:
                inst = Instalacao(src, dest.get(), atalhos.get(), escreve, progresso); inst.run()
                if abrir.get():
                    exe = os.path.join(inst.dest, "HEFAESTOUS.exe")
                    if os.path.exists(exe):
                        subprocess.Popen([exe], cwd=inst.dest, creationflags=0x00000008, env=_env_limpo())   # DETACHED_PROCESS
                    else:
                        subprocess.Popen([os.path.join(inst.dest, "runtime", "pythonw.exe"), os.path.join(inst.dest, "web", "app.py")], cwd=inst.dest, creationflags=CREATE_NO_WINDOW, env=_env_limpo())
                root.after(0, lambda: (fechar.configure(text="Fechar", state="normal"), messagebox.showinfo(APP, f"Instalado em\n{inst.dest}\n\nAtalho na Área de Trabalho: {APP}")))
            except Exception as ex:  # noqa: BLE001
                escreve("\nERRO: " + str(ex)); escreve(traceback.format_exc()[-800:])
                root.after(0, lambda: (btn.configure(state="normal"), fechar.configure(state="normal"), messagebox.showerror(APP, f"A instalação falhou:\n{ex}")))
        threading.Thread(target=trabalho, daemon=True).start()

    btn.configure(command=iniciar)
    root.mainloop()


# --------------------------------------------------------------------------------------------- CLI
def main():
    ap = argparse.ArgumentParser(description=f"Instalador do {APP}")
    ap.add_argument("--silent", action="store_true", help="sem interface: instala direto")
    ap.add_argument("--dest", default=None)
    ap.add_argument("--sem-atalhos", action="store_true")
    ap.add_argument("--log", default=None, help="arquivo de log (modo silencioso)")
    a = ap.parse_args()
    src = origem()
    if not a.silent:
        gui(src); return
    fh = open(a.log, "a", encoding="utf-8") if a.log else None

    def log(txt, transient=False):
        if fh:
            fh.write(txt + "\n"); fh.flush()
        if sys.stdout:
            try:
                print(txt, flush=True)
            except Exception:  # noqa: BLE001
                pass
    try:
        Instalacao(src, a.dest or destino_padrao(), not a.sem_atalhos, log).run()
    except Exception as ex:  # noqa: BLE001
        log("ERRO: " + str(ex)); log(traceback.format_exc()); sys.exit(1)
    finally:
        if fh:
            fh.close()


if __name__ == "__main__":
    main()
