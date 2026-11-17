# -*- coding: utf-8 -*-
import os
import traceback
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .. import sessions
from ..bootstrap import SESSIONS
from ..services.perfil import parametros_roda, perfil_de_parametros, gerar_3d
from ..services.conjunto import gerar_conjunto
from ..services.serialize import to_jsonable
from ..geom import sobremetal

router = APIRouter(prefix="/api", tags=["perfil"])


class PerfilIn(BaseModel):
    session_id: Optional[str] = None
    malha: Optional[int] = None          # índice da malha na sessão
    roda: Optional[str] = None           # "pinhao" | "coroa"
    params: Optional[Dict[str, Any]] = None   # alternativa: parâmetros soltos (m_n, z, x, alpha_n, h_fP_star, d_a, ...)
    q: Optional[float] = None            # sobremetal imposto (sobrepõe o da malha)
    pr0: Optional[float] = None
    rho: Optional[float] = None
    z0: Optional[int] = None
    incluir_roda: bool = True


def _params(inp: PerfilIn):
    if inp.params:
        p = dict(inp.params)
    else:
        if not inp.session_id:
            raise HTTPException(400, "informe session_id + malha + roda, ou params")
        sessions.validar_id(inp.session_id)
        objs = sessions.malhas(inp.session_id)
        if not objs:
            raise HTTPException(404, "sessão sem malhas calculadas; refaça a etapa B")
        i = inp.malha or 0
        if not (0 <= i < len(objs)):
            raise HTTPException(400, "malha fora da faixa")
        if objs[i] is None:
            raise HTTPException(400, f"a malha {i + 1} não foi calculada na etapa B")
        p = parametros_roda(objs[i], inp.roda or "pinhao")
    for k in ("q", "pr0", "rho", "z0"):
        v = getattr(inp, k)
        if v is not None:
            p[k] = v
    return p


@router.post("/perfil/2d")
def perfil_2d(inp: PerfilIn):
    p = _params(inp)
    try:
        res = perfil_de_parametros(p, incluir_roda=inp.incluir_roda)
    except ValueError as ex:
        raise HTTPException(422, {"mensagem": f"perfil: {ex}"})
    except Exception as ex:
        raise HTTPException(422, {"mensagem": f"erro no perfil: {ex}", "trace": traceback.format_exc()[-1500:]})
    res.pop("_perfil", None)
    return to_jsonable(res)


@router.post("/perfil/sobremetal")
def perfil_sobremetal(inp: PerfilIn):
    p = _params(inp)
    r = sobremetal.calcular(float(p["m_n"]), int(p["z"]), float(p["x"]), float(p["alpha_n"]), float(p["h_fP_star"]),
                            float(p.get("q") or 0), float(p.get("pr0") or 0), p.get("rho"), beta=float(p.get("beta") or 0.0))
    return to_jsonable(r)


@router.post("/perfil/3d")
def perfil_3d(inp: PerfilIn):
    p = _params(inp)
    try:
        r = gerar_3d(p)
    except RuntimeError as ex:
        raise HTTPException(501, str(ex))
    except ValueError as ex:
        raise HTTPException(422, {"mensagem": f"perfil: {ex}"})
    except Exception as ex:
        raise HTTPException(422, {"mensagem": f"erro no CAD: {ex}", "trace": traceback.format_exc()[-1500:]})
    return {"id": r["id"], "step_url": f"/api/files/{r['id']}.step", "glb_url": f"/api/files/{r['id']}.glb", "stl_url": f"/api/files/{r['id']}.stl",
            "volume_mm3": r.get("volume_mm3"), "furo_mm": r.get("furo_mm"), "aviso": r.get("aviso"), "cache": r.get("cache", False)}


class RodaConj(BaseModel):
    key: str
    nome: str
    cor: Optional[str] = None
    params: Dict[str, Any]


class MalhaConj(BaseModel):
    a: float
    pinhao: RodaConj
    coroa: RodaConj


class ConjuntoIn(BaseModel):
    nome: Optional[str] = None
    tipo: str = "trem"                      # "trem" | "planetario"
    malhas: List[MalhaConj]
    N_cp: Optional[int] = None
    planetario_tipo: Optional[str] = None   # "Simples" | "Composto"


@router.post("/perfil/3d/conjunto")
def perfil_3d_conjunto(inp: ConjuntoIn):
    """Todas as rodas do projeto montadas e em fase: STEP (montagem), GLB, STL e ZIP (conjunto + peças separadas)."""
    if not inp.malhas or (inp.tipo == "planetario" and len(inp.malhas) < 2):
        raise HTTPException(400, "conjunto: informe as malhas calculadas")
    try:
        r = gerar_conjunto(inp.model_dump())
    except RuntimeError as ex:
        raise HTTPException(501, str(ex))
    except ValueError as ex:
        raise HTTPException(422, {"mensagem": f"conjunto: {ex}"})
    except Exception as ex:
        raise HTTPException(422, {"mensagem": f"erro no CAD do conjunto: {ex}", "trace": traceback.format_exc()[-1500:]})
    i = r["id"]
    return {"id": i, "step_url": f"/api/files/{i}.step", "glb_url": f"/api/files/{i}.glb", "stl_url": f"/api/files/{i}.stl", "zip_url": f"/api/files/{i}.zip",
            "volume_mm3": r.get("volume_mm3"), "n_pecas": r.get("n_pecas"), "pecas": r.get("pecas"), "avisos": r.get("avisos") or [], "cache": r.get("cache", False)}


@router.get("/files/{nome}")
def arquivo(nome: str):
    nome = os.path.basename(nome)
    p = os.path.join(SESSIONS, "cad", nome)
    if not os.path.exists(p):
        raise HTTPException(404, "arquivo não encontrado")
    media = {"step": "model/step", "glb": "model/gltf-binary", "stl": "model/stl", "zip": "application/zip"}.get(nome.rsplit(".", 1)[-1], "application/octet-stream")
    return FileResponse(p, media_type=media, filename=nome)
