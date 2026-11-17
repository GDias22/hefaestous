# -*- coding: utf-8 -*-
from typing import Any, Dict

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .. import fem
from ..services.serialize import to_jsonable

router = APIRouter(prefix="/api/fem", tags=["fem"])


class EmpacotarIn(BaseModel):
    projeto: Dict[str, Any]


class LerIn(BaseModel):
    conteudo: Any


@router.post("/empacotar")
def empacotar(inp: EmpacotarIn):
    """Projeto da interface -> conteúdo do arquivo .fem (com a foto dos resultados). O navegador grava o arquivo."""
    try:
        return to_jsonable(fem.empacotar(inp.projeto))
    except fem.ErroFem as ex:
        raise HTTPException(422, str(ex))


@router.post("/ler")
def ler(inp: LerIn):
    """Conteúdo (JSON) de um arquivo .fem -> projeto validado e migrado, pronto para a interface."""
    try:
        return to_jsonable(fem.ler(inp.conteudo))
    except fem.ErroFem as ex:
        raise HTTPException(422, str(ex))
