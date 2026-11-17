# -*- coding: utf-8 -*-
"""Monta a pasta de DISTRIBUIÇÃO do HEFAESTOUS: só o que o instalador precisa, nada de venv/notebooks/planilhas.

    web\\.venv313\\Scripts\\python.exe instalador\\montar_distribuicao.py [--dest <pasta>] [--zip]

Padrão: cria/atualiza  <pai do projeto>\\HEFAESTOUS\\   (apaga o conteúdo anterior) e, com --zip, também HEFAESTOUS.zip ao lado.
Conteúdo:
  Instalar_HEFAESTOUS.exe, HEFAESTOUS.exe, INSTALAR.md, LEIA-ME.txt
  *.py da raiz (módulos de cálculo), Figuras\\, Exemplos_fem\\
  web\\ (app.py, backend\\, frontend\\, tools\\, requirements.txt, README.md) — sem .venv313, node_modules, sessions, tests
  instalador\\ (fontes + versao.json; e wheels\\/zip do Python/get-pip.py se existirem, para instalação offline)
"""
import argparse
import os
import shutil
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOME = "HEFAESTOUS"

RAIZ_EXT = {".py"}
RAIZ_ARQ = ["Instalar_HEFAESTOUS.exe", "HEFAESTOUS.exe", "INSTALAR.md"]
RAIZ_PASTAS = ["Figuras", "Exemplos_fem"]
WEB_EXCLUIR_DIRS = {".venv313", "node_modules", "sessions", "__pycache__", "tests", ".pytest_cache", "_legado_v1"}
WEB_EXCLUIR_ARQ = {"web_server.log", "package.json", "package-lock.json", ".gitignore"}
INST_EXCLUIR_DIRS = {"__pycache__", "build"}

LEIAME = """HEFAESTOUS — Dimensionamento de engrenagens (DIN 3960/3967 · ISO 6336)
FEM/Unicamp — Laboratório de Máquinas Rotativas (LAMAR) · Desenvolvido por Gabriel Dias

COMO INSTALAR (Windows 10/11, 64 bits)
  1. Dê dois cliques em  Instalar_HEFAESTOUS.exe
  2. Escolha a pasta (o padrão não exige administrador) e clique em Instalar.
     O instalador baixa o Python 3.13 e as bibliotecas (~400 MB; precisa de internet) — leva alguns minutos.
  3. Use o atalho HEFAESTOUS criado na Área de Trabalho.

Se o Windows SmartScreen avisar "editor desconhecido": Mais informações → Executar assim mesmo.
Para desinstalar: Configurações › Aplicativos › HEFAESTOUS.
Detalhes e instalação sem internet: INSTALAR.md
"""


def copytree(a, b, ex_dirs=frozenset(), ex_arq=frozenset()):
    n = 0
    for raiz, dirs, arqs in os.walk(a):
        dirs[:] = sorted(d for d in dirs if d not in ex_dirs and not d.startswith("."))
        alvo = os.path.join(b, os.path.relpath(raiz, a)) if raiz != a else b
        os.makedirs(alvo, exist_ok=True)
        for f in sorted(arqs):
            if f in ex_arq or f.endswith((".pyc", ".log")):
                continue
            shutil.copy2(os.path.join(raiz, f), os.path.join(alvo, f)); n += 1
    return n


def tamanho(p):
    return sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(p) for f in fs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dest", default=os.path.join(os.path.dirname(ROOT), NOME))
    ap.add_argument("--zip", action="store_true", help="também gera <dest>.zip")
    a = ap.parse_args()
    dest = os.path.abspath(a.dest)
    for exe in ("Instalar_HEFAESTOUS.exe", "HEFAESTOUS.exe"):
        if not os.path.exists(os.path.join(ROOT, exe)):
            sys.exit(f"{exe} não encontrado na raiz: rode instalador\\build.bat antes.")
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    os.makedirs(dest)
    n = 0
    for f in sorted(os.listdir(ROOT)):
        p = os.path.join(ROOT, f)
        if os.path.isfile(p) and (os.path.splitext(f)[1].lower() in RAIZ_EXT or f in RAIZ_ARQ):
            shutil.copy2(p, os.path.join(dest, f)); n += 1
    for d in RAIZ_PASTAS:
        n += copytree(os.path.join(ROOT, d), os.path.join(dest, d))
    n += copytree(os.path.join(ROOT, "web"), os.path.join(dest, "web"), WEB_EXCLUIR_DIRS, WEB_EXCLUIR_ARQ)
    n += copytree(os.path.join(ROOT, "instalador"), os.path.join(dest, "instalador"), INST_EXCLUIR_DIRS)
    with open(os.path.join(dest, "LEIA-ME.txt"), "w", encoding="utf-8") as f:
        f.write(LEIAME)
    shutil.copy2(os.path.join(ROOT, "instalador", "README_producao.md"), os.path.join(dest, "README.md"))   # página inicial do repo público
    with open(os.path.join(dest, ".gitignore"), "w", encoding="utf-8") as f:
        f.write("__pycache__/\n*.pyc\nweb/sessions/\nweb/.venv313/\n")
    print(f"{n + 2} arquivos -> {dest}  ({tamanho(dest) / 1e6:.1f} MB)")
    if a.zip:
        zp = dest + ".zip"
        with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
            for r, _, fs in os.walk(dest):
                for f in fs:
                    p = os.path.join(r, f); z.write(p, os.path.join(NOME, os.path.relpath(p, dest)))
        print(f"zip: {zp} ({os.path.getsize(zp) / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
