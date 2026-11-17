# -*- coding: utf-8 -*-
"""Verificação e aplicação de atualizações do HEFAESTOUS (mesmo padrão do Argus: a aplicação consulta o repositório de
produção, avisa o usuário na interface e, se ele aceitar, baixa e aplica a nova versão).

Fonte da versão: `instalador/versao.json` no repositório PÚBLICO de produção (GitHub — o GitLab da Unicamp exige login até para
leitura, então não serve para máquinas de terceiros). A versão instalada é lida do mesmo arquivo na pasta de instalação.

Aplicar: baixa o ZIP da branch main, extrai numa pasta temporária, valida (tem web/app.py e versao.json com a versão esperada)
e grava um script `atualizar.bat` que, DEPOIS que o servidor encerrar, substitui os arquivos da aplicação (web\\, *.py, Figuras\\,
Exemplos_fem\\, instalador\\, *.exe, docs) preservando runtime\\ (Python + bibliotecas), web\\sessions, erros.txt e logs\\, e relança
o HEFAESTOUS.exe. Se requirements.txt mudou, o .bat roda `pip install -r` antes de relançar. O servidor então responde ao cliente e
se encerra; o lançador (Job Object) morre junto; o .bat segue sozinho.
"""
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import threading
import time
import urllib.request
import zipfile

from . import logs

REPO = os.environ.get("HEFAESTOUS_REPO", "GDias22/hefaestous")
URL_VERSAO = f"https://raw.githubusercontent.com/{REPO}/main/instalador/versao.json"
URL_VERSAO_API = f"https://api.github.com/repos/{REPO}/contents/instalador/versao.json?ref=main"
URL_ZIP = f"https://github.com/{REPO}/archive/refs/heads/main.zip"
URL_PAGINA = f"https://github.com/{REPO}"
BASE = logs.BASE                                   # pasta de instalação (HEFAESTOUS_HOME) ou raiz do projeto em dev
CREATE_NO_WINDOW = 0x08000000
_cache = {"t": 0.0, "res": None}
_lock = threading.Lock()


def versao_instalada():
    try:
        with open(os.path.join(BASE, "instalador", "versao.json"), encoding="utf-8") as f:
            return json.load(f).get("versao", "0")
    except Exception:  # noqa: BLE001
        return "0"


def _tupla(v):
    return tuple(int(x) for x in re.findall(r"\d+", str(v))[:4]) or (0,)


def instalacao_gerenciada():
    """True quando rodamos a partir de uma instalação feita pelo instalador (há runtime\\python.exe): aí podemos aplicar."""
    return os.path.exists(os.path.join(BASE, "runtime", "python.exe"))


def _ler_versao_remota(timeout):
    """versao.json do repositório público. 1º a API de conteúdo do GitHub (sem cache de CDN: reflete o push na hora);
    2º o raw.githubusercontent (CDN, pode atrasar ~5 min)."""
    import base64
    erros = []
    for url, decodificar in ((URL_VERSAO_API, True), (URL_VERSAO + f"?t={int(time.time())}", False)):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "HEFAESTOUS-updater", "Cache-Control": "no-cache", "Accept": "application/vnd.github+json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                corpo = r.read()
            if decodificar:
                corpo = base64.b64decode(json.loads(corpo)["content"])
            return json.loads(corpo.decode("utf-8"))
        except Exception as ex:  # noqa: BLE001
            erros.append(f"{type(ex).__name__}: {ex}")
    raise RuntimeError(" | ".join(erros))


def verificar(forcar=False, timeout=6):
    """Consulta a versão remota (cache de 1 h). Nunca lança: offline → disponivel=False com motivo."""
    with _lock:
        if not forcar and _cache["res"] and time.time() - _cache["t"] < 3600:
            return _cache["res"]
    atual = versao_instalada()
    res = {"atual": atual, "remota": None, "disponivel": False, "pagina": URL_PAGINA, "pode_aplicar": instalacao_gerenciada(), "erro": None}
    try:
        d = _ler_versao_remota(timeout)
        res["remota"] = d.get("versao"); res["data"] = d.get("data"); res["notas"] = d.get("notas")
        res["disponivel"] = _tupla(res["remota"]) > _tupla(atual)
    except Exception as ex:  # noqa: BLE001
        res["erro"] = f"{type(ex).__name__}: {ex}"
    with _lock:
        _cache["t"] = time.time(); _cache["res"] = res
    return res


# ------------------------------------------------------------------------------------------------ aplicar
ATUALIZAR_BAT = r"""@echo off
title HEFAESTOUS - atualizando para v{versao}
cd /d "{base}"
echo Aguardando o HEFAESTOUS encerrar...
:espera
tasklist /FI "PID eq {pid}" 2>nul | find "{pid}" >nul && (timeout /t 1 /nobreak >nul & goto espera)
timeout /t 1 /nobreak >nul
echo Substituindo os arquivos da aplicacao...
for %%D in (web instalador Figuras Exemplos_fem) do (
  if exist "{novo}\%%D" (
    if exist "%%D" (
      rem preserva web\sessions (CAD gerado, sessoes)
      if /i "%%D"=="web" if exist "web\sessions" move /y "web\sessions" "{novo}\web\sessions" >nul
      rmdir /s /q "%%D"
    )
    move /y "{novo}\%%D" "%%D" >nul
  )
)
for %%F in ("{novo}\*.py" "{novo}\*.exe" "{novo}\*.md" "{novo}\*.txt") do if exist %%F move /y %%F . >nul
rmdir /s /q "{novo_raiz}" 2>nul
if "{instalar_deps}"=="1" (
  echo Atualizando bibliotecas Python...
  "runtime\python.exe" -m pip install --quiet --disable-pip-version-check --no-warn-script-location -r "web\requirements.txt"
)
echo Atualizado para v{versao}. Abrindo o HEFAESTOUS...
start "" "HEFAESTOUS.exe"
exit
"""


def _baixar_zip():
    req = urllib.request.Request(URL_ZIP, headers={"User-Agent": "HEFAESTOUS-updater"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def aplicar(encerrar_servidor):
    """Baixa + valida + agenda a troca. `encerrar_servidor()` é chamado (em thread) após responder. Devolve dict de status."""
    if not instalacao_gerenciada():
        raise RuntimeError("Esta cópia não foi instalada pelo Instalar_HEFAESTOUS.exe; baixe a nova versão manualmente em " + URL_PAGINA)
    info = verificar(forcar=True)
    if not info["disponivel"]:
        raise RuntimeError("Nenhuma atualização disponível." if not info["erro"] else "Não foi possível consultar a versão: " + info["erro"])
    dados = _baixar_zip()
    tmp = tempfile.mkdtemp(prefix="hefa_upd_", dir=BASE)
    with zipfile.ZipFile(io.BytesIO(dados)) as z:
        z.extractall(tmp)
    raiz = next((os.path.join(tmp, d) for d in os.listdir(tmp) if os.path.isdir(os.path.join(tmp, d))), None)
    if not raiz or not os.path.exists(os.path.join(raiz, "web", "app.py")):
        raise RuntimeError("Pacote baixado inválido (sem web/app.py).")
    with open(os.path.join(raiz, "instalador", "versao.json"), encoding="utf-8") as f:
        v_pacote = json.load(f).get("versao")
    if _tupla(v_pacote) <= _tupla(versao_instalada()):
        raise RuntimeError(f"O pacote baixado (v{v_pacote}) não é mais novo que o instalado (v{versao_instalada()}).")
    # dependências mudaram?
    def _req(p):
        try:
            with open(p, encoding="utf-8") as f:
                return sorted(l.strip() for l in f if l.strip() and not l.startswith("#"))
        except Exception:  # noqa: BLE001
            return None
    deps = "1" if _req(os.path.join(raiz, "web", "requirements.txt")) != _req(os.path.join(BASE, "web", "requirements.txt")) else "0"
    bat = os.path.join(BASE, "atualizar.bat")
    with open(bat, "w", encoding="cp1252", errors="replace") as f:
        f.write(ATUALIZAR_BAT.format(versao=v_pacote, base=BASE, pid=os.getpid(), novo=raiz, novo_raiz=tmp, instalar_deps=deps))
    logs.registrar_erro(f"atualização agendada: v{versao_instalada()} → v{v_pacote}", f"pacote em {raiz}; deps={'sim' if deps == '1' else 'não'}", "update/apply")
    # o .bat espera este PID morrer; lançamos em janela própria (o usuário vê o progresso) e encerramos o servidor em seguida
    subprocess.Popen(["cmd", "/c", "start", "", "cmd", "/c", bat], cwd=BASE, creationflags=0x00000008, close_fds=True)
    threading.Thread(target=lambda: (time.sleep(1.5), encerrar_servidor()), daemon=True).start()
    return {"ok": True, "de": versao_instalada(), "para": v_pacote, "instalar_deps": deps == "1",
            "mensagem": f"Atualizando para v{v_pacote}. O HEFAESTOUS vai fechar e reabrir sozinho em alguns segundos."}
