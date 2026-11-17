# -*- coding: utf-8 -*-
"""Sólido 3D da engrenagem (build123d / OCP) a partir do perfil 2D: STEP + GLB + STL.

Externa: face dentada (roda completa) menos furo d_i, extrudada por b (reta) ou com torção (β ≠ 0:
         ângulo de torção = b·tan β / r_ref, o que gera uma hélice exata no cilindro de referência).
Interna: disco D_ext menos o sólido dentado (o perfil 2D da anelar descreve o CONTORNO DO FURO dentado).
Import de build123d é preguiçoso: se OCP não estiver instalado, lança RuntimeError (API devolve 501).
"""
import math
import os

import numpy as np


def _b3d():
    try:
        import build123d as b3d  # noqa: WPS433
        return b3d
    except Exception as ex:  # noqa: BLE001
        raise RuntimeError(f"build123d/OCP indisponível neste interpretador: {ex}")


def _reamostrar_fechado(x, y, n):
    """Reamostra uma polilinha fechada por comprimento de arco em n pontos (remove duplicados)."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    if math.hypot(x[0] - x[-1], y[0] - y[-1]) > 1e-9:
        x = np.append(x, x[0]); y = np.append(y, y[0])
    d = np.hypot(np.diff(x), np.diff(y)); s = np.concatenate([[0], np.cumsum(d)])
    keep = np.concatenate([[True], d > 1e-9])
    x, y, s = x[keep], y[keep], s[keep]
    t = np.linspace(0, s[-1], n, endpoint=False)
    return np.interp(t, s, x), np.interp(t, s, y)


def _reamostrar_aberto(x, y, n):
    x = np.asarray(x, float); y = np.asarray(y, float)
    d = np.hypot(np.diff(x), np.diff(y)); s = np.concatenate([[0], np.cumsum(d)])
    keep = np.concatenate([[True], d > 1e-9]); x, y, s = x[keep], y[keep], s[keep]
    t = np.linspace(0, s[-1], n)
    return np.interp(t, s, x), np.interp(t, s, y)


def _wire_polilinha(b3d, xs, ys, z_dentes, pts_por_dente=40):
    """Contorno dentado como Wire fechado de polilinha (anti-horário). Robusto para anelares grandes.
    (A Spline periódica única de build123d/OCC com centenas de pontos dá área ~20 % menor — não usar.)"""
    n = max(360, pts_por_dente * z_dentes)
    X, Y = _reamostrar_fechado(xs, ys, n)
    area = 0.5 * np.sum(X * np.roll(Y, -1) - np.roll(X, -1) * Y)
    if area < 0:
        X, Y = X[::-1], Y[::-1]
    pts = [(float(a), float(c)) for a, c in zip(X, Y)]
    return b3d.Wire(b3d.Polyline(*pts, close=True).edges())


def _wire_splines_por_dente(b3d, perfil, pts_por_dente=80):
    """Contorno dentado como z splines (uma por dente, ponta a ponta no círculo de pé): superfície lisa e STEP leve.
    Usado em rodas externas; o dente de perfil2d vai de −π/z a +π/z (anti-horário)."""
    z = perfil["z"]
    X, Y = _reamostrar_aberto(perfil["dente"]["x"], perfil["dente"]["y"], pts_por_dente)
    edges = []
    for k in range(z):
        a = TWO_PI * k / z; c, s = math.cos(a), math.sin(a)
        pts = [(float(X[i] * c - Y[i] * s), float(X[i] * s + Y[i] * c)) for i in range(len(X))]
        edges.append(b3d.Spline(*pts))
    w = b3d.Wire(edges)
    if not w.is_closed:
        raise ValueError("contorno por dente não fechou")
    return w


TWO_PI = 2 * math.pi


def area_perfil(perfil):
    """Área da seção transversal da roda dentada (polígono do perfil completo), em mm²."""
    X, Y = _reamostrar_fechado(perfil["roda"]["x"], perfil["roda"]["y"], max(720, 60 * perfil["z"]))
    return abs(0.5 * float(np.sum(X * np.roll(Y, -1) - np.roll(X, -1) * Y)))


def solido_engrenagem(perfil, b, d_i=0.0, beta=0.0, interna=False, D_ext=None):
    """perfil: dict de perfil2d (usa perfil['roda'] e perfil['dente']). b: largura [mm]; d_i: furo (externa); D_ext: diâmetro
    externo (interna). Furo/contorno externo entram como furo da face (sem booleanos). β ≠ 0: extrusão com torção
    (hélice exata no cilindro de referência; sinal de β define o sentido)."""
    b3d = _b3d()
    xs, ys = perfil["roda"]["x"], perfil["roda"]["y"]
    z = perfil["z"]
    r_ref = perfil["circulos"]["d"] / 2
    if interna:
        wire = _wire_polilinha(b3d, xs, ys, z)
    else:
        try:
            wire = _wire_splines_por_dente(b3d, perfil)
        except Exception:  # noqa: BLE001
            wire = _wire_polilinha(b3d, xs, ys, z)
    if interna:
        R = (D_ext if D_ext else abs(perfil["circulos"]["d_f"]) * 1.15) / 2
        outer = b3d.Circle(R).face().outer_wire()
        inner = [wire]
    else:
        outer = wire
        inner = [b3d.Circle(d_i / 2).face().outer_wire()] if (d_i and d_i > 0) else []
    face = b3d.Face(outer, inner)
    twist = math.degrees(b * math.tan(math.radians(beta)) / r_ref) if abs(beta) > 1e-9 else 0.0
    if twist:
        corpo = b3d.Solid.extrude_linear_with_rotation(outer, (0, 0, 0), (0, 0, b), twist, inner_wires=inner)
    else:
        corpo = b3d.extrude(face, amount=b)
    if corpo.volume < 0:
        corpo = b3d.Solid(corpo.wrapped.Reversed())
    return corpo


def verificar_solido(part):
    """Garante que o resultado é UM sólido fechado e válido (BRepCheck) antes de exportar — senão o STEP sairia como casca."""
    from OCP.BRepCheck import BRepCheck_Analyzer
    solids = part.solids()
    if len(solids) != 1:
        raise ValueError(f"CAD: esperado 1 sólido, obtido {len(solids)}")
    if len(part.shells()) != 1 or not BRepCheck_Analyzer(part.wrapped).IsValid():
        raise ValueError("CAD: o sólido gerado não é válido (shell aberta ou topologia inconsistente)")
    return solids[0]


def exportar(part, pasta, nome):
    """Grava STEP (AP214, mm, MANIFOLD_SOLID_BREP), GLB (viewer) e STL (impressão); devolve dict com caminhos e volume."""
    b3d = _b3d()
    verificar_solido(part)
    os.makedirs(pasta, exist_ok=True)
    step = os.path.join(pasta, nome + ".step"); glb = os.path.join(pasta, nome + ".glb"); stl = os.path.join(pasta, nome + ".stl")
    b3d.export_step(part, step)
    b3d.export_gltf(part, glb, binary=True, linear_deflection=0.03, angular_deflection=0.25)
    b3d.export_stl(part, stl, tolerance=0.01, angular_tolerance=0.15)
    vol = float(part.volume) if hasattr(part, "volume") else None   # GProp: aproximado em superfícies spline (~5 %)
    return {"step": step, "glb": glb, "stl": stl, "volume_mm3": vol}
