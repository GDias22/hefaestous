# -*- coding: utf-8 -*-
import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from ..bootstrap import FIGURAS
from ..params.metadata import PARAMS, GROUPS, STAGES
from ..services.geometria import listar_presets
from .. import sessions

router = APIRouter(prefix="/api", tags=["meta"])


@router.get("/meta/params")
def meta_params():
    return {"stages": STAGES, "groups": GROUPS, "params": PARAMS}


@router.get("/presets")
def presets():
    return listar_presets()


@router.get("/figuras/{nome}")
def figura(nome: str):
    nome = os.path.basename(nome)
    p = os.path.join(FIGURAS, nome)
    if not os.path.exists(p):
        raise HTTPException(404, "figura não encontrada")
    return FileResponse(p)


@router.get("/sessoes")
def sessoes():
    return sessions.listar()


@router.get("/sessoes/{session_id}")
def sessao(session_id: str):
    s = sessions.snapshot(session_id)
    if s is None:
        raise HTTPException(404, "sessão não encontrada")
    return s
