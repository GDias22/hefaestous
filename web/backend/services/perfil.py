# -*- coding: utf-8 -*-
"""Serviço de perfis 2D/3D e sobremetal a partir de uma malha calculada (Engrenamento) ou de parâmetros soltos."""
import hashlib
import json
import math
import os

from ..bootstrap import SESSIONS
from ..geom import perfil2d, sobremetal
from .serialize import to_jsonable


def parametros_roda(eng, roda):
    """Extrai de um Engrenamento os parâmetros da roda ('pinhao'|'coroa') necessários ao perfil."""
    s = "pinhao" if roda == "pinhao" else "coroa"
    fer = getattr(eng, f"ferramenta_{s}")
    z = getattr(eng, f"Z_{s}")
    p = dict(m_n=eng.m_n, z=z, x=getattr(eng, f"x_{s}"), alpha_n=eng.alpha_n, beta=eng.beta,
             h_fP_star=fer.cp_dedendo, h_aP_star=fer.k_a, rho=getattr(eng, f"rk_{s}", None) or 0.0,
             pr0=fer.pr or 0.0, q=getattr(eng, f"SM_{s}", 0.0) or 0.0, op=getattr(eng, f"op_acabamento_{s}"),
             d_a=getattr(eng, f"d_a_{s}"), d_f=getattr(eng, f"d_f_{s}"), d=getattr(eng, f"d_{s}"), db=getattr(eng, f"db_{s}"),
             d_Na=getattr(eng, f"d_na_{s}"), d_Nf=getattr(eng, f"d_nf_{s}"), b=getattr(eng, f"b_{s}"),
             d_i=getattr(eng, f"di_{s}"), d_sh=getattr(eng, f"d_sh_{s}", None), z0=fer.Z_shaper, apelido=f"{eng.apelido} — {'pinhão' if s == 'pinhao' else 'coroa'}",
             membro=getattr(eng, f"membro_{s}", None))
    if p["op"] not in ("Retificação", "Rasqueteamento"):
        p["q"] = 0.0
    return p


def perfil_de_parametros(p, incluir_roda=True):
    """p: dict (ver parametros_roda). Devolve resultado JSON com perfil final, pré-usinagem, sobremetal e círculos."""
    z = int(p["z"]); interna = z < 0
    m_n = float(p["m_n"]); x = float(p["x"]); an = float(p["alpha_n"]); beta = float(p.get("beta") or 0.0)
    hf = float(p["h_fP_star"]); rho = float(p.get("rho") or 0.0); pr0 = float(p.get("pr0") or 0.0); q = float(p.get("q") or 0.0)
    r_a = abs(float(p["d_a"])) / 2
    sm = sobremetal.calcular(m_n, z, x, an, hf, q, pr0, rho, beta=beta)
    if interna:
        z0 = p.get("z0") or max(12, int(round(abs(z) / 3)))
        if int(z0) >= abs(z):
            raise ValueError(f"o pinhão-cortador deve ter menos dentes que a anelar (z0 = {z0}, |z| = {abs(z)})")
        res = perfil2d.perfil_interno(m_n, z, x, an, hf, r_a, z0=int(z0), x0=float(p.get("x0") or 0.0), rho0=min(rho, 0.3 * m_n), beta=beta,
                                      D_ext=abs(float(p["d_i"])) if p.get("d_i") else None)
        res["z0_usado"] = int(z0)
    else:
        res = perfil2d.perfil_externo(m_n, z, x, an, hf, r_a, beta=beta, rho=rho, pr0=pr0, q=q)
    sc = perfil2d.secao_critica_30(res)
    out = dict(apelido=p.get("apelido"), interna=interna, z=z, m_n=m_n, x=x, alpha_n=an, beta=beta, b=p.get("b"), d_i=p.get("d_i"),
               circulos=dict(res["circulos"], d_Na=p.get("d_Na"), d_Nf=p.get("d_Nf")), final=res["dente"],
               pre=(res["pre"]["dente"] if res.get("pre") else None), sobremetal=sm, secao_critica=sc,
               retificado=bool(res.get("retificado")), s_t_ref=res.get("s_t_ref"), avisos=list(res.get("avisos") or []))
    if incluir_roda:
        out["roda"] = res["roda"]
        out["roda_pre"] = res["pre"]["roda"] if res.get("pre") else None
    out["_perfil"] = res
    return out


def furo_eixo(p, d_f):
    """Diâmetro do furo no sólido 3D de uma roda EXTERNA: o eixo de projeto d_sh. Planeta sobre rolamentos de agulhas (d_i > d_sh,
    vindo do Layout) usa d_i, que é o furo do rolamento. Devolve (furo, aviso); furo 0 quando não cabe (≥ 90 % do pé) ou não há eixo."""
    if int(p["z"]) < 0:
        return 0.0, None
    d_sh = abs(float(p.get("d_sh") or 0.0)); d_i = abs(float(p.get("d_i") or 0.0))
    furo = d_i if (p.get("membro") == "planeta" and d_i > d_sh) else d_sh
    if furo <= 0:
        return 0.0, None
    if furo >= 0.9 * abs(d_f):
        return 0.0, f"Furo do eixo omitido: Ø {furo:g} mm ≥ 90 % do diâmetro de pé (Ø {abs(d_f):.1f} mm). Use roda integrada ao eixo (pinhão-eixo) ou reduza d_sh."
    return furo, None


# Versão da GEOMETRIA gerada: entra na chave do cache de CAD. Incrementar sempre que perfil2d/cad3d mudarem a forma do sólido,
# senão o servidor continua entregando os STEP/GLB antigos (mesmos parâmetros ⇒ mesma chave). v2: correção da ponta do cortador.
GEOM_VERSAO = 2


def chave_cache(p):
    keys = ["m_n", "z", "x", "alpha_n", "beta", "h_fP_star", "rho", "pr0", "q", "d_a", "d_i", "d_sh", "membro", "b", "z0"]
    s = json.dumps({k: p.get(k) for k in keys} | {"_v": GEOM_VERSAO}, sort_keys=True, default=str)
    return hashlib.sha1(s.encode()).hexdigest()[:12]


def solido_roda(p):
    """Sólido build123d de UMA roda a partir dos parâmetros (ver parametros_roda). Devolve (part, info) com
    info = {perfil, b, interna, furo_mm, aviso, volume_mm3, D_ext}. O volume vem da área da seção × b (exato; a torção
    helicoidal preserva a área), não do GProp do OCC, que desvia alguns % em superfícies spline."""
    from ..geom import cad3d
    res = perfil_de_parametros(p)
    perfil = res["_perfil"]
    b = float(p.get("b") or 10.0)
    interna = res["interna"]
    d_i = abs(float(p.get("d_i") or 0.0))
    D_ext = d_i if (interna and d_i) else None
    furo, aviso = furo_eixo(p, perfil["circulos"]["d_f"])
    part = cad3d.solido_engrenagem(perfil, b, d_i=furo, beta=float(p.get("beta") or 0.0), interna=interna, D_ext=D_ext)
    A = cad3d.area_perfil(perfil)
    if interna:
        R = (D_ext if D_ext else abs(perfil["circulos"]["d_f"]) * 1.15) / 2
        A = math.pi * R * R - A
    elif furo:
        A -= math.pi * (furo / 2) ** 2
    return part, {"perfil": perfil, "b": b, "interna": interna, "furo_mm": furo, "aviso": aviso, "volume_mm3": A * b, "D_ext": D_ext}


def gerar_3d(p, pasta=None):
    from ..geom import cad3d
    pasta = pasta or os.path.join(SESSIONS, "cad")
    k = chave_cache(p)
    nome = f"gear_{k}"
    step = os.path.join(pasta, nome + ".step"); glb = os.path.join(pasta, nome + ".glb"); stl = os.path.join(pasta, nome + ".stl")
    meta = os.path.join(pasta, nome + ".json")
    if os.path.exists(step) and os.path.exists(glb) and os.path.exists(stl) and os.path.exists(meta):
        with open(meta, encoding="utf-8") as f:
            info = json.load(f)
        return {"id": nome, "step": step, "glb": glb, "stl": stl, **info, "cache": True}
    part, sr = solido_roda(p)
    info = cad3d.exportar(part, pasta, nome)
    info["volume_mm3"] = sr["volume_mm3"]; info["furo_mm"] = sr["furo_mm"]; info["aviso"] = sr["aviso"]
    with open(meta, "w", encoding="utf-8") as f:
        json.dump({"volume_mm3": info["volume_mm3"], "furo_mm": sr["furo_mm"], "aviso": sr["aviso"]}, f)
    return {"id": nome, **info, "cache": False}
