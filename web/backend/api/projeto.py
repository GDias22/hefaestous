# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Any, Dict, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, ValidationError

from .. import sessions
from ..projeto.calcular import calcular_json
from ..projeto.defaults import projeto_padrao, RODA, MALHA, ENTRADA, OPERACAO, METODOS
from ..services.serialize import to_jsonable

router = APIRouter(prefix="/api/projeto", tags=["projeto"])


class ProjetoIn(BaseModel):
    projeto: Dict[str, Any]
    com_tensoes: bool = True
    session_id: Optional[str] = None


@router.get("/padrao/{tipo}")
def padrao(tipo: str):
    if tipo not in ("trem", "planetario"):
        raise HTTPException(400, "tipo deve ser 'trem' ou 'planetario'")
    return projeto_padrao(tipo)


@router.get("/vocabulario")
def vocabulario():
    """Como os campos do metadata se distribuem no modelo de projeto (para a interface montar o inspetor)."""
    return {"roda": {b: list(p) for b, p in RODA.items()}, "malha": MALHA, "entrada": ENTRADA, "operacao": OPERACAO, "metodos": METODOS}


@router.post("/layout_padrao")
def layout_padrao_api(inp: ProjetoIn):
    from ..projeto import layout as lay
    from ..projeto.modelo import Projeto
    try:
        return lay.layout_padrao(Projeto.model_validate(inp.projeto))
    except ValidationError:
        raise HTTPException(422, "projeto inválido")


@router.post("/calcular")
def calcular(inp: ProjetoIn):
    try:
        res, objetos, analises = calcular_json(inp.projeto, inp.com_tensoes)
    except ValidationError as ex:
        raise HTTPException(422, {"mensagem": "projeto inválido", "erros": [{"campo": ".".join(map(str, e["loc"])), "msg": e["msg"]} for e in ex.errors()]})
    return res


@router.post("/salvar")
def salvar(inp: ProjetoIn):
    try:
        res, objetos, analises = calcular_json(inp.projeto, True)
    except ValidationError as ex:
        raise HTTPException(422, {"mensagem": "projeto inválido", "erros": [{"campo": ".".join(map(str, e["loc"])), "msg": e["msg"]} for e in ex.errors()]})
    if inp.session_id:
        sessions.validar_id(inp.session_id)
    sid = inp.session_id or sessions.nova_sessao()
    geometria = [m.get("geometria") for m in res["malhas"]]
    tens = None
    if analises:
        tens = {"apelido": inp.projeto.get("nome"), "malhas": [m["tensoes"] for m in res["malhas"] if m.get("tensoes")]}
    sessions.salvar(sid, {
        "titulo": inp.projeto.get("nome") or "Projeto", "criado": datetime.now().isoformat(timespec="seconds"),
        "projeto": to_jsonable(inp.projeto), "resultado": res, "transmissao": res["transmissao"],
        "geometria": geometria, "malhas": objetos, "analise": analises[0] if analises else None, "tensoes": tens,
        "entradas_geometria": None, "svgs": {},
    })
    return {"session_id": sid, "resultado": res}


class ExplicarIn(BaseModel):
    projeto: Dict[str, Any]
    malha: int = 0
    fator: str
    roda: Optional[str] = None


class SensIn(BaseModel):
    projeto: Dict[str, Any]
    malha: int = 0
    parametro: str
    fator: str = "S_H"
    roda: Optional[str] = None


@router.post("/explicar")
def explicar_api(inp: ExplicarIn):
    from ..projeto.explicar import explicar
    try:
        res, objetos, analises = calcular_json(inp.projeto, True)
    except ValidationError as ex:
        raise HTTPException(422, "projeto inválido")
    if not objetos or inp.malha >= len(objetos) or objetos[inp.malha] is None:
        raise HTTPException(422, "malha sem resultado; corrija as entradas")
    e = objetos[inp.malha]
    if inp.projeto.get("tipo") == "planetario":
        an, i = (analises[0] if analises else None), inp.malha + 1
    else:
        an, i = (analises[inp.malha] if inp.malha < len(analises) else None), 1
    if an is None:
        raise HTTPException(422, "análise de tensões indisponível")
    return to_jsonable(explicar(e, an, i, inp.fator, inp.roda))


@router.post("/sensibilidade")
def sensibilidade_api(inp: SensIn):
    from ..projeto.sensibilidade import sensibilidade
    try:
        return to_jsonable(sensibilidade(inp.projeto, inp.malha, inp.parametro, inp.fator, inp.roda))
    except ValueError as ex:
        raise HTTPException(422, str(ex))


class BuscaTremIn(BaseModel):
    i_alvo: float
    n_estagios: int = 2
    alpha_n: float = 20.0
    beta: float = 0.0
    z1_min: Optional[int] = None
    z1_max: int = 30
    z2_max: int = 150
    tol_rel: float = 0.02
    hunting: bool = True
    i_max_estagio: float = 8.0
    distribuicao: str = "equilibrada"
    max_resultados: int = 200


@router.post("/busca_trem")
def busca_trem_api(inp: BuscaTremIn):
    from ..projeto.cinematica_trem import buscar_trem
    try:
        return buscar_trem(inp.i_alvo, inp.n_estagios, inp.alpha_n, inp.beta, inp.z1_min, inp.z1_max, inp.z2_max, inp.tol_rel, inp.max_resultados, inp.hunting, inp.i_max_estagio, inp.distribuicao)
    except ValueError as ex:
        raise HTTPException(422, str(ex))


@router.get("/{session_id}")
def carregar(session_id: str):
    s = sessions.snapshot(session_id)
    if s is None or not s.get("projeto"):
        raise HTTPException(404, "projeto não encontrado")
    return {"session_id": session_id, "projeto": s["projeto"], "titulo": s.get("titulo"), "criado": s.get("criado")}
