# -*- coding: utf-8 -*-
"""Conjunto montado: todas as rodas do projeto posicionadas e EM FASE (dente de uma na vão da outra), exportado como uma
montagem STEP (uma peça por roda, com nome e cor), GLB (viewer), STL e um ZIP com conjunto + peças separadas.

Convenções (iguais ao cálculo): eixo da roda = +Z; o perfil 2D de perfil2d tem UM DENTE centrado em +X (externa e anelar).
Ângulos de fase (rad), com ψ = direção do ponto de contato vista dos dois centros e θ_p a orientação da roda motriz:
  externa: θ_c = ψ + π + π/z_c + (ψ − θ_p)·z_p/z_c      (pinhão gira CCW ⇒ coroa gira CW)
  interna: θ_r = ψ + π/z_r − (ψ − θ_p)·z_p/z_r          (planeta gira CCW ⇒ anelar gira CCW)
Hélice: as duas rodas de uma malha externa têm sentidos opostos (β e −β); malha interna, o mesmo sentido. As duas rodas de
uma malha partem do MESMO plano z0 (faces inferiores alinhadas) para a fase valer em toda a largura.

Trem: estágios em série ao longo de +X (centro da coroa_i = centro do pinhão_i + |a_i|; o pinhão_{i+1} fica no eixo da
coroa_i), empilhados em z com folga. Planetário: sol na origem, N planetas em ψ_k = −π/2 + 2πk/N a |a_ext| do centro;
composto: planeta menor + anelar num segundo plano z.
"""
import hashlib
import json
import math
import os
import zipfile

from ..bootstrap import SESSIONS
from .perfil import chave_cache, gerar_3d, solido_roda

TWO_PI = 2 * math.pi


def fase_externa(psi, theta_p, z_p, z_c):
    return psi + math.pi + math.pi / z_c + (psi - theta_p) * z_p / z_c


def fase_interna(psi, theta_p, z_p, z_r):
    return psi + math.pi / z_r - (psi - theta_p) * z_p / z_r


def fase_interna_inv(psi, theta_r, z_p, z_r):
    """Orientação do planeta que engrena com uma anelar já orientada (θ_r) na direção ψ."""
    return psi - (psi + math.pi / z_r - theta_r) * z_r / z_p


def _folga(b):
    return max(4.0, 0.15 * b)


def _roda(spec_roda, beta_sinal):
    """Parâmetros efetivos da roda com o sentido da hélice imposto pela malha."""
    p = dict(spec_roda["params"])
    p["beta"] = beta_sinal * abs(float(p.get("beta") or 0.0))
    return p


def posicoes(spec):
    """Lista de peças {key, nome, cor, params, x, y, z, rot_deg} + avisos. Pura (sem CAD): testável."""
    tipo = spec.get("tipo", "trem")
    malhas = spec["malhas"]
    pecas, avisos = [], []
    if tipo == "trem":
        X, z0 = 0.0, 0.0
        for i, m in enumerate(malhas):
            a = abs(float(m["a"]))
            pin, cor = m["pinhao"], m["coroa"]
            zp, zc = abs(int(pin["params"]["z"])), abs(int(cor["params"]["z"]))
            interna = int(cor["params"]["z"]) < 0
            pp = _roda(pin, +1.0)
            pc = _roda(cor, +1.0 if interna else -1.0)
            if interna:
                psi = math.pi                                   # pinhão dentro da anelar, deslocado para −X do centro dela
                th_c = fase_interna(psi, 0.0, zp, zc)
            else:
                psi = 0.0
                th_c = fase_externa(psi, 0.0, zp, zc)
            pecas.append(dict(key=pin["key"], nome=pin["nome"], cor=pin["cor"], params=pp, x=X, y=0.0, z=z0, rot_deg=0.0))
            pecas.append(dict(key=cor["key"], nome=cor["nome"], cor=cor["cor"], params=pc, x=X + a, y=0.0, z=z0, rot_deg=math.degrees(th_c)))
            bp, bc = float(pp.get("b") or 10.0), float(pc.get("b") or 10.0)
            X += a
            z0 += max(bp, bc) + _folga(max(bp, bc))
        return pecas, avisos
    # ---------------- planetário
    N = int(spec.get("N_cp") or 3)
    comp = (spec.get("planetario_tipo") or "Simples") == "Composto"
    ext, inte = malhas[0], malhas[1]
    a = abs(float(ext["a"])); a_int = abs(float(inte["a"]))
    if abs(a - a_int) > 0.01:
        avisos.append(f"Distâncias entre centros diferentes nas duas malhas (ext {a:.3f} × int {a_int:.3f} mm): o conjunto usa a externa.")
    sol, pma = ext["pinhao"], ext["coroa"]
    pme, an = inte["pinhao"], inte["coroa"]
    zs, zb = abs(int(sol["params"]["z"])), abs(int(pma["params"]["z"]))
    zm, zr = abs(int(pme["params"]["z"])), abs(int(an["params"]["z"]))
    ps = _roda(sol, +1.0); pb = _roda(pma, -1.0)
    pm = _roda(pme, +1.0) if comp else pb
    pr = _roda(an, +1.0 if comp else -1.0)
    b_ext = max(float(ps.get("b") or 10.0), float(pb.get("b") or 10.0))
    z_int = (b_ext + _folga(b_ext)) if comp else 0.0
    pecas.append(dict(key=sol["key"], nome=sol["nome"], cor=sol["cor"], params=ps, x=0.0, y=0.0, z=0.0, rot_deg=0.0))
    psis = [-math.pi / 2 + TWO_PI * k / N for k in range(N)]
    th_b = [fase_externa(psi, 0.0, zs, zb) for psi in psis]
    if comp:
        th_m0 = 0.0
        th_r = fase_interna(psis[0], th_m0, zm, zr)
        th_m = [th_m0] + [fase_interna_inv(psi, th_r, zm, zr) for psi in psis[1:]]
        avisos.append("Planetário composto: a fase entre planeta maior e menor em cada pino segue a montagem com a anelar (pode diferir de pino para pino).")
    else:
        th_rs = [fase_interna(psi, t, zb, zr) for psi, t in zip(psis, th_b)]
        th_r = th_rs[0]
        passo = TWO_PI / zr
        if any(abs(((t - th_r) + passo / 2) % passo - passo / 2) > 1e-6 for t in th_rs[1:]):
            avisos.append(f"Condição de montagem não satisfeita ((z_sol + z_anelar)/N = {(zs + zr) / N:.3f} não é inteiro): os planetas 2…{N} não engrenam em fase com a anelar.")
    for k, psi in enumerate(psis):
        x, y = a * math.cos(psi), a * math.sin(psi)
        pecas.append(dict(key=pma["key"], nome=f"{pma['nome']} {k + 1}", cor=pma["cor"], params=pb, x=x, y=y, z=0.0, rot_deg=math.degrees(th_b[k])))
        if comp:
            pecas.append(dict(key=pme["key"], nome=f"{pme['nome']} {k + 1}", cor=pme["cor"], params=pm, x=x, y=y, z=z_int, rot_deg=math.degrees(th_m[k])))
    pecas.append(dict(key=an["key"], nome=an["nome"], cor=an["cor"], params=pr, x=0.0, y=0.0, z=z_int, rot_deg=math.degrees(th_r)))
    return pecas, avisos


def _cor(hex_or_rgb):
    import build123d as b3d
    if isinstance(hex_or_rgb, str):
        h = hex_or_rgb.lstrip("#")
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        return b3d.Color(r, g, b)
    if hex_or_rgb:
        return b3d.Color(*hex_or_rgb)
    return b3d.Color(0.56, 0.6, 0.67)


def chave_conjunto(spec):
    pecas, _ = posicoes(spec)
    s = json.dumps([(p["key"], chave_cache(p["params"]), round(p["x"], 4), round(p["y"], 4), round(p["z"], 4), round(p["rot_deg"], 5)) for p in pecas], sort_keys=True)
    return hashlib.sha1(s.encode()).hexdigest()[:12]


def montar(spec):
    """Compound build123d do conjunto + lista de peças com volume; gera cada sólido distinto uma vez (chave_cache dos params)."""
    import build123d as b3d
    from ..geom import cad3d
    pecas, avisos = posicoes(spec)
    cache = {}
    filhos, saida, vol = [], [], 0.0
    for pc in pecas:
        k = chave_cache(pc["params"])
        if k not in cache:
            part, info = solido_roda(pc["params"])
            cad3d.verificar_solido(part)
            cache[k] = (part, info)
            if info["aviso"]:
                avisos.append(f"{pc['nome']}: {info['aviso']}")
        part, info = cache[k]
        s = part.rotate(b3d.Axis.Z, pc["rot_deg"]).translate((pc["x"], pc["y"], pc["z"]))
        s.label = pc["nome"]; s.color = _cor(pc["cor"])
        filhos.append(s); vol += info["volume_mm3"]
        saida.append({k2: pc[k2] for k2 in ("key", "nome", "cor", "x", "y", "z", "rot_deg")} | {"volume_mm3": info["volume_mm3"], "b": info["b"], "furo_mm": info["furo_mm"]})
    comp = b3d.Compound(children=filhos); comp.label = spec.get("nome") or "Conjunto"
    return comp, saida, vol, avisos


def _slug(s):
    import re
    return re.sub(r"[^\w.-]+", "_", str(s or "conjunto")).strip("_") or "conjunto"


def gerar_conjunto(spec, pasta=None):
    import build123d as b3d
    pasta = pasta or os.path.join(SESSIONS, "cad")
    os.makedirs(pasta, exist_ok=True)
    k = chave_conjunto(spec)
    nome = f"conj_{k}"
    paths = {ext: os.path.join(pasta, f"{nome}.{ext}") for ext in ("step", "glb", "stl", "zip", "json")}
    if all(os.path.exists(v) for v in paths.values()):
        with open(paths["json"], encoding="utf-8") as f:
            info = json.load(f)
        return {"id": nome, **paths, **info, "cache": True}
    comp, pecas, vol, avisos = montar(spec)
    b3d.export_step(comp, paths["step"])
    b3d.export_gltf(comp, paths["glb"], binary=True, linear_deflection=0.03, angular_deflection=0.25)
    b3d.export_stl(comp, paths["stl"], tolerance=0.01, angular_tolerance=0.15)
    # peças separadas (reaproveita o cache por roda) + conjunto + posições, num ZIP
    base = _slug(spec.get("nome"))
    with zipfile.ZipFile(paths["zip"], "w", zipfile.ZIP_DEFLATED) as zf:
        for ext in ("step", "glb", "stl"):
            zf.write(paths[ext], f"{base}_conjunto.{ext}")
        vistos = set()
        for pc, pos in zip(posicoes(spec)[0], pecas):
            ck = chave_cache(pc["params"])
            if ck in vistos:
                continue
            vistos.add(ck)
            r = gerar_3d(pc["params"], pasta)
            nm = _slug(pc["key"].replace(":", "_"))
            for ext in ("step", "stl"):
                zf.write(r[ext], f"pecas/{nm}.{ext}")
        zf.writestr("posicoes.json", json.dumps({"unidade": "mm", "eixo_roda": "+Z", "rotacao": "graus em torno de +Z", "pecas": pecas, "avisos": avisos}, ensure_ascii=False, indent=1))
    info = {"volume_mm3": vol, "pecas": pecas, "avisos": avisos, "n_pecas": len(pecas)}
    with open(paths["json"], "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False)
    return {"id": nome, **paths, **info, "cache": False}
