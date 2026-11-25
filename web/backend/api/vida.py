# -*- coding: utf-8 -*-
"""Batimento da interface — encerra o servidor sozinho quando nenhuma aba do HEFAESTOUS está mais aberta.

O lançador (HEFAESTOUS.exe) não tem janela: sobe o servidor e abre o navegador. Para o servidor não ficar rodando para sempre
depois que o usuário fecha a aba, a página manda `POST /api/vida/ping` a cada poucos segundos e `POST /api/vida/adeus` ao ser
fechada (sendBeacon). Com `ativar()` (só quando o servidor é iniciado pelo lançador, flag --auto-encerrar), um vigia encerra o
processo quando:
  - passou PRAZO_SEM_PING sem nenhum ping depois de já ter havido algum (aba fechada, navegador fechado, PC dormiu…), ou
  - a página mandou "adeus" e PRAZO_ADEUS depois nenhuma outra aba pingou (um F5 manda adeus e pinga de novo em seguida), ou
  - passou PRAZO_INICIAL sem nenhum ping desde o início (navegador não abriu).
Em desenvolvimento (run.bat / app.py sem a flag) o vigia não existe: a página pinga, o servidor só responde.
"""
import os
import threading
import time

from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["vida"])

PRAZO_SEM_PING = 45.0      # s sem ping (a página pinga a cada 5 s)
PRAZO_ADEUS = 6.0          # s após "adeus" sem um novo ping
PRAZO_INICIAL = 180.0      # s sem o primeiro ping (navegador não abriu, ou demorou a carregar)

_estado = {"ativo": False, "inicio": time.monotonic(), "ultimo": None, "adeus": None, "abas": 0}
_lock = threading.Lock()


@router.post("/vida/ping")
def ping():
    with _lock:
        _estado["ultimo"] = time.monotonic(); _estado["adeus"] = None
    return {"ok": True, "auto_encerrar": _estado["ativo"]}


@router.post("/vida/adeus")
def adeus():
    with _lock:
        _estado["adeus"] = time.monotonic()
    return {"ok": True}


def ativar(encerrar=None):
    """Liga o vigia (chamado por app.py quando iniciado com --auto-encerrar)."""
    _estado["ativo"] = True; _estado["inicio"] = time.monotonic()
    encerrar = encerrar or _encerrar_padrao
    threading.Thread(target=_vigia, args=(encerrar,), daemon=True, name="vida-vigia").start()


def _vigia(encerrar):
    while True:
        time.sleep(1.0)
        agora = time.monotonic()
        with _lock:
            ultimo, adeus, inicio = _estado["ultimo"], _estado["adeus"], _estado["inicio"]
        if ultimo is None:
            if agora - inicio > PRAZO_INICIAL:
                encerrar("nenhuma aba abriu em %.0f s" % PRAZO_INICIAL); return
            continue
        if adeus is not None and agora - adeus > PRAZO_ADEUS and ultimo <= adeus:
            encerrar("a última aba foi fechada"); return
        if agora - ultimo > PRAZO_SEM_PING:
            encerrar("sem resposta da interface há %.0f s" % PRAZO_SEM_PING); return


def _encerrar_padrao(motivo):
    import logging
    logging.getLogger("hefaestous").info("encerrando o servidor: %s", motivo)
    time.sleep(0.3)
    os._exit(0)  # noqa: WPS437  (saída normal: o lançador não mostra erro)
