# -*- coding: utf-8 -*-
from typing import Dict, Optional

from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse, Response
from pydantic import BaseModel

from .. import sessions
from ..report.render import render_relatorio, exportar_json, exportar_xlsx
from ..services.perfil import parametros_roda
from ..geom import sobremetal

router = APIRouter(prefix="/api", tags=["export"])


class RelatorioIn(BaseModel):
    svgs: Optional[Dict[str, str]] = None     # SVGs já renderizados pelo navegador (planetario, perfil_i_pinhao, ...)


def _sessao(session_id):
    s = sessions.snapshot(session_id)
    if s is None:
        raise HTTPException(404, "sessão não encontrada")
    return s


def _extras(session_id):
    out = {"sobremetal": []}
    for o in (sessions.malhas(session_id) or []):
        if o is None:
            out["sobremetal"].append(None); continue
        d = {}
        for roda in ("pinhao", "coroa"):
            p = parametros_roda(o, roda)
            d[roda] = sobremetal.calcular(p["m_n"], p["z"], p["x"], p["alpha_n"], p["h_fP_star"], p["q"], p["pr0"], p["rho"], beta=p["beta"])
        out["sobremetal"].append(d)
    return out


@router.get("/relatorio/{session_id}.html", response_class=HTMLResponse)
def relatorio_get(session_id: str):
    s = _sessao(session_id)
    return render_relatorio(s, session_id, svgs=s.get("svgs") or {}, extras=_extras(session_id))


@router.post("/relatorio/{session_id}.html", response_class=HTMLResponse)
def relatorio_post(session_id: str, inp: RelatorioIn):
    """O navegador envia os SVGs (planetário, perfis) para embutir no relatório; substituem os guardados na sessão."""
    _sessao(session_id)
    if inp.svgs is not None:
        sessions.salvar(session_id, {"svgs": inp.svgs})
    s = _sessao(session_id)
    return render_relatorio(s, session_id, svgs=s.get("svgs") or {}, extras=_extras(session_id))


@router.get("/export/{session_id}.json")
def export_json(session_id: str):
    s = _sessao(session_id)
    return Response(exportar_json(s, session_id), media_type="application/json",
                    headers={"Content-Disposition": f'attachment; filename="{session_id}.json"'})


@router.get("/export/{session_id}.xlsx")
def export_xlsx(session_id: str):
    s = _sessao(session_id)
    return Response(exportar_xlsx(s, session_id), media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    headers={"Content-Disposition": f'attachment; filename="{session_id}.xlsx"'})
