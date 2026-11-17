# -*- coding: utf-8 -*-
from typing import Any, Dict, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .. import jobs
from ..services.cinematica import buscar, prefill, COLUNAS
from ..services.serialize import to_jsonable

router = APIRouter(prefix="/api/cinematica", tags=["cinematica"])


class CinIn(BaseModel):
    params: Dict[str, Any]


class PrefillIn(BaseModel):
    job_id: str
    idx: int
    n_sol: Optional[float] = None
    T_sol: Optional[float] = None
    N_Cp: Optional[int] = None


@router.post("/jobs")
def iniciar(inp: CinIn):
    job = jobs.iniciar("cinematica", buscar, inp.params)
    return job.info()


@router.get("/jobs/{job_id}")
def status(job_id: str):
    j = jobs.obter(job_id)
    if j is None:
        raise HTTPException(404, "job não encontrado")
    return j.info()


@router.get("/jobs/{job_id}/result")
def resultado(job_id: str, limit: int = 300, offset: int = 0):
    j = jobs.obter(job_id)
    if j is None:
        raise HTTPException(404, "job não encontrado")
    if j.status not in ("concluido", "cancelado") or j.resultado is None:
        return {"status": j.status, "pronto": False, **j.info()}
    res = j.resultado
    cands = res["candidatos"][offset: offset + limit]
    return {"pronto": True, "status": j.status, "tipo": res["tipo"], "n": res["n"], "limite_atingido": res["limite_atingido"],
            "colunas": COLUNAS, "candidatos": to_jsonable(cands), "entradas": to_jsonable(res["entradas"])}


@router.delete("/jobs/{job_id}")
def cancelar(job_id: str):
    j = jobs.cancelar(job_id)
    if j is None:
        raise HTTPException(404, "job não encontrado")
    return j.info()


@router.post("/prefill")
def pre(inp: PrefillIn):
    j = jobs.obter(inp.job_id)
    if j is None or j.resultado is None:
        raise HTTPException(404, "resultado não disponível")
    cands = j.resultado["candidatos"]
    if not (0 <= inp.idx < len(cands)):
        raise HTTPException(400, "índice fora da faixa")
    try:
        return to_jsonable(prefill(cands[inp.idx], j.resultado["entradas"], inp.n_sol, inp.T_sol, inp.N_Cp))
    except ValueError as ex:
        raise HTTPException(422, str(ex))
