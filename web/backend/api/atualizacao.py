# -*- coding: utf-8 -*-
"""API de atualização: GET /api/update/check · POST /api/update/apply (padrão do Argus)."""
import os
import signal
import threading
import time

from fastapi import APIRouter, HTTPException

from .. import atualizacao

router = APIRouter(prefix="/api", tags=["update"])


@router.get("/update/check")
def update_check(forcar: bool = False):
    return atualizacao.verificar(forcar=forcar)


def _encerrar_servidor():
    """Encerra o processo do servidor (o lançador, via Job Object, cai junto; o atualizar.bat espera isso e relança)."""
    time.sleep(0.5)
    os.kill(os.getpid(), signal.SIGTERM)
    time.sleep(3)
    os._exit(0)  # noqa: WPS437


@router.post("/update/apply")
def update_apply():
    try:
        return atualizacao.aplicar(_encerrar_servidor)
    except RuntimeError as ex:
        raise HTTPException(409, {"mensagem": str(ex)})
    except Exception as ex:  # noqa: BLE001
        raise HTTPException(500, {"mensagem": f"Falha ao preparar a atualização: {ex}"})
