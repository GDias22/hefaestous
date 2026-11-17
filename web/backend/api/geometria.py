# -*- coding: utf-8 -*-
import traceback
from datetime import datetime
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..services.geometria import calcular_malha, dados_malha
from ..services.serialize import to_jsonable
from .. import sessions

router = APIRouter(prefix="/api", tags=["geometria"])


class GeometriaIn(BaseModel):
    session_id: Optional[str] = None
    titulo: Optional[str] = None
    malhas: List[Dict[str, Any]]
    cinematica: Optional[Dict[str, Any]] = None   # resultado da etapa A (opcional, só armazenado)


@router.post("/geometria")
def geometria(inp: GeometriaIn):
    if not inp.malhas:
        raise HTTPException(400, "informe ao menos uma malha")
    objetos, resultados, erros = [], [], []
    for i, payload in enumerate(inp.malhas):
        try:
            e = calcular_malha(payload)
            objetos.append(e)
            resultados.append(dados_malha(e))
        except Exception as ex:   # erro de um cálculo não derruba a resposta
            erros.append({"malha": i, "erro": str(ex), "trace": traceback.format_exc()[-2000:]})
            objetos.append(None)
            resultados.append(None)
    if all(o is None for o in objetos):
        raise HTTPException(422, {"mensagem": "nenhuma malha pôde ser calculada", "erros": erros})
    if inp.session_id:
        sessions.validar_id(inp.session_id)
    sid = inp.session_id or sessions.nova_sessao()
    sessions.salvar(sid, {
        "svgs": {},                       # desenhos embutidos no relatório pertencem à geometria anterior
        "titulo": inp.titulo or (resultados[0] or {}).get("apelido") or "Sessão",
        "criado": datetime.now().isoformat(timespec="seconds"),
        "cinematica": inp.cinematica,
        "entradas_geometria": to_jsonable(inp.malhas),
        "geometria": resultados,
        "malhas": objetos,
        "analise": None,
        "tensoes": None,
    })
    return {"session_id": sid, "malhas": resultados, "erros": erros}
