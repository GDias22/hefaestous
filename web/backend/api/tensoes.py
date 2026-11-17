# -*- coding: utf-8 -*-
import traceback
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..services.geometria import calcular_malha, dados_malha
from ..services.tensoes import calcular_tensoes, dados_tensoes
from ..services.serialize import to_jsonable
from .. import sessions

router = APIRouter(prefix="/api", tags=["tensoes"])


class TensoesIn(BaseModel):
    session_id: Optional[str] = None
    malhas: Optional[List[Dict[str, Any]]] = None     # usado quando não há sessão (etapa B pulada): calcula as malhas aqui
    indices: Optional[List[int]] = None               # quais malhas da sessão usar (0-based), máx. 2
    params: Dict[str, Any] = {}


@router.post("/tensoes")
def tensoes(inp: TensoesIn):
    # `todas` mantém a posição de cada malha da sessão (None = malha que falhou na etapa B); os índices do frontend
    # referem-se SEMPRE a essa lista completa.
    todas = None
    sid = inp.session_id
    if sid:
        sessions.validar_id(sid)
        todas = sessions.malhas(sid)
        if not todas or all(o is None for o in todas):
            raise HTTPException(404, "sessão sem malhas calculadas; refaça a etapa B")
    if inp.malhas:
        try:
            todas = [calcular_malha(p) for p in inp.malhas]
        except Exception as ex:
            raise HTTPException(422, f"erro ao calcular malha: {ex}")
        sid = sid or sessions.nova_sessao()
        sessions.salvar(sid, {"titulo": inp.params.get("an_apelido") or "Sessão", "entradas_geometria": to_jsonable(inp.malhas),
                              "geometria": [dados_malha(o) for o in todas], "malhas": todas, "svgs": {}})
    if not todas:
        raise HTTPException(400, "informe session_id com malhas calculadas ou as malhas")
    indices = inp.indices if inp.indices else [i for i, o in enumerate(todas) if o is not None]
    sel = []
    for i in indices:
        if not (0 <= i < len(todas)):
            raise HTTPException(400, f"índice de malha {i} fora da faixa (a sessão tem {len(todas)} malha(s))")
        if todas[i] is None:
            raise HTTPException(400, f"a malha {i + 1} não foi calculada na etapa B (corrija as entradas e recalcule)")
        sel.append(todas[i])
    if len(sel) > 2:
        sel = sel[:2]
    m1 = sel[0]
    m2 = sel[1] if len(sel) > 1 else None
    try:
        an = calcular_tensoes(m1, m2, inp.params)
    except Exception as ex:
        raise HTTPException(422, {"mensagem": f"erro na análise de tensões: {ex}", "trace": traceback.format_exc()[-2000:]})
    res = dados_tensoes(an, [m1, m2])
    geometria = [dados_malha(o) if o is not None else None for o in todas]   # avisos de tensões foram anexados às malhas
    sessions.salvar(sid, {"analise": an, "tensoes": res, "entradas_tensoes": to_jsonable(inp.params), "geometria": geometria})
    return {"session_id": sid, "tensoes": res, "geometria": geometria}
