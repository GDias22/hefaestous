# -*- coding: utf-8 -*-
"""Etapa A — busca de números de dentes de planetários simples e compostos.

Porte fiel das células 16/17 de Dim_cinematico.ipynb (mesmos critérios e mesma ordem de verificação), com:
parâmetros explícitos (sem globais), callback de progresso, cancelamento e limite de resultados.
Resultado: lista de candidatos (dicts) com as mesmas colunas do DataFrame do notebook (chaves curtas + rótulos).
"""
import math

import numpy as np

from ..bootstrap import Eq, G
from ..params.metadata import defaults_for

# ------------------------------------------------------------------ funções auxiliares (células 8–14 do notebook)


def Z_min_basico(alpha_n, beta):
    alpha_t = math.atan(math.tan(math.radians(alpha_n)) / math.cos(math.radians(beta)))
    return math.ceil((2 * math.cos(math.radians(beta))) / (math.sin(alpha_t) ** 2))


def alpha_wt_seguro(Z1, Z2, m_t, a, alpha_t):
    try:
        return math.degrees(math.acos((((Z1 + Z2) * m_t) / (2 * a)) * math.cos(math.radians(alpha_t))))
    except (ValueError, ZeroDivisionError):
        return 0.0


def linspace_if_tol(value, tol, n=5):
    return np.array([value]) if tol == 0 else np.linspace(value - tol, value + tol, n)


def speed_ratio(Zs, Zbp, Zsp, Zr, Planetary_Type, torq_Input, torq_Output):
    if Planetary_Type == 0:
        tab = {(0, 2): Zr / Zs, (0, 1): (Zs + Zr) / Zs, (2, 0): Zs / Zr, (2, 1): (Zs + Zr) / Zr,
               (1, 0): Zs / (Zs + Zr), (1, 2): Zr / (Zs + Zr)}
    else:
        tab = {(0, 2): (Zbp * Zr) / (Zsp * Zs), (0, 1): (Zsp * Zs + Zbp * Zr) / (Zs * Zsp), (2, 0): (Zsp * Zs) / (Zbp * Zr),
               (2, 1): (Zsp * Zs + Zbp * Zr) / (Zbp * Zr), (1, 0): (Zsp * Zs) / (Zsp * Zs + Zr * Zbp), (1, 2): (Zbp * Zr) / (Zbp * Zr + Zsp * Zs)}
    if (torq_Input, torq_Output) not in tab:
        raise ValueError("entrada e saída devem ser membros diferentes")
    return tab[(torq_Input, torq_Output)]


def interf_montagem_int_num(d_b_pinhao, d_b_coroa, d_a_pinhao, d_a_coroa, a, alpha_wt, u):
    phi = math.acos((d_a_coroa ** 2 - 4 * a ** 2 - d_a_pinhao ** 2) / (4 * d_a_pinhao * abs(a)))
    alpha_at1 = math.acos(d_b_pinhao / d_a_pinhao)
    inv_alpha_at1 = math.tan(alpha_at1) - alpha_at1
    inv_alpha_wt = math.tan(math.radians(alpha_wt)) - math.radians(alpha_wt)
    nu = inv_alpha_at1 - inv_alpha_wt
    theta = math.acos((d_a_coroa ** 2 + 4 * a ** 2 - d_a_pinhao ** 2) / (4 * d_a_coroa * a))
    alpha_at2 = math.acos(d_b_coroa / d_a_coroa)
    inv_alpha_at2 = math.tan(alpha_at2) - alpha_at2
    epsilon = inv_alpha_wt - inv_alpha_at2
    xi_1 = math.atan((1 / d_b_pinhao) * math.sqrt((d_a_pinhao ** 2 * d_b_coroa ** 2 - d_a_coroa ** 2 * d_b_pinhao ** 2) / (d_a_coroa ** 2 - d_a_pinhao ** 2)))
    xi_2 = ((xi_1 + nu) / abs(u)) + epsilon
    A = 0.5 * (abs(d_a_coroa) * math.sin(xi_2) - d_a_pinhao * math.sin(xi_1))
    K = (phi + nu) / (abs(u) * (theta - epsilon))
    return K, A


def desloc_perfil_seguro(*args):
    try:
        return Eq.desloc_perfil(*args)
    except Exception:  # noqa: BLE001  (fora da tabela: descarta o candidato)
        return None


# ------------------------------------------------------------------ busca


def buscar(job, p):
    """p: dict com os parâmetros da etapa A (ver metadata stage 'cinematica'). job: objeto Job (ou None)."""
    d = defaults_for("cinematica"); d.update({k: v for k, v in p.items() if v is not None})
    p = d
    tipo = int(p["Planetary_Type"])
    N_Cp = int(p["N_Cp"]); torq_in = int(p["torq_Input"]); torq_out = int(p["torq_Output"])
    red, tol_red = float(p["reduction"]), float(p["tol_reduction"])
    an_e, an_i = float(p["alpha_n_ext"]), float(p["alpha_n_int"])
    eps_min, sx_max, dawt, max_res = float(p["eps_alpha_min"]), float(p["sum_x_max"]), float(p["d_alpha_wt"]), int(p["max_resultados"])
    Sr, Dup, tol_a = float(p["Sr_ring"]), float(p["Upright_Diameter"]), float(p["tol_dist_centros"])
    ka = {k: float(p[f"k_a_{k}"]) for k in ("sun", "bp", "sp", "r")}
    cp = {k: float(p[f"cp_dedendo_{k}"]) for k in ("sun", "bp", "sp", "r")}
    if torq_in == torq_out:
        raise ValueError("Membro de entrada e de saída devem ser diferentes.")
    out = []

    def progresso(i, total):
        if job is not None:
            job.progresso = 100.0 * i / max(total, 1)
            job.contagem = len(out)
            job.mensagem = f"{len(out)} candidatos"

    if tipo == 1:
        _buscar_composto(job, p, N_Cp, torq_in, torq_out, red, tol_red, an_e, an_i, eps_min, sx_max, dawt, max_res, Sr, Dup, tol_a, ka, cp, out, progresso)
    else:
        _buscar_simples(job, p, N_Cp, torq_in, torq_out, red, tol_red, an_e, eps_min, sx_max, dawt, max_res, Sr, Dup, tol_a, ka, cp, out, progresso)
    # ordena: menor erro de redução, menor diâmetro externo da anelar
    out.sort(key=lambda r: (abs(r["i_real"] - red), r["D_ext_anelar"]))
    for k, r in enumerate(out):
        r["idx"] = k
    return {"tipo": "Composto" if tipo == 1 else "Simples", "n": len(out), "limite_atingido": len(out) >= max_res, "candidatos": out, "entradas": p}


def _geom_roda(m_n, alpha_n, beta, Z, x, k_a, h_f, K, IQ):
    d = Eq.diametro_ref(Z, m_n, beta)
    alpha_t = Eq.alpha_t(alpha_n, beta)
    db = Eq.diametro_base(d, alpha_t)
    h_a, d_a, _, _ = Eq.diam_cabeca2(m_n, d, x, k_a, IQ, K)
    _, d_f, _, _ = Eq.diam_pe(m_n, alpha_n, x, d, h_f, 0.05, "r")
    return d, db, d_a, d_f, h_a


def _buscar_composto(job, p, N_Cp, ti, to, red, tol_red, an_e, an_i, eps_min, sx_max, dawt, max_res, Sr, Dup, tol_a, ka, cp, out, progresso):
    be, bi = float(p["beta_ext"]), float(p["beta_int"])
    Zmin_s = Zmin_b = Z_min_basico(an_e, be)
    Zmin_sp = Zmin_r = Z_min_basico(an_i, bi)
    Zmax_s, Zmax_b, Zmax_sp, Zmax_r = int(p["Z_max_sun"]), int(p["Z_max_big"]), int(p["Z_max_small"]), int(p["Z_max_ring"])
    total = max(1, (Zmax_s - Zmin_s) * (Zmax_b - Zmin_b) * (Zmax_sp - Zmin_sp))
    it = 0
    mns = linspace_if_tol(float(p["m_n_ext"]), float(p["tol_m_n_ext"]))
    mni = linspace_if_tol(float(p["m_n_int"]), float(p["tol_m_n_int"]))
    bes = linspace_if_tol(be, float(p["tol_beta_ext"]))
    bis = linspace_if_tol(bi, float(p["tol_beta_int"]))
    for Zs in range(Zmin_s, Zmax_s):
        for Zbp in range(Zmin_b, Zmax_b):
            for Zsp in range(Zmin_sp, Zmax_sp):
                it += 1
                if it % 10 == 0:
                    progresso(it, total)
                if len(out) >= max_res:
                    progresso(total, total); return
                for Zr_abs in range(Zmin_r, Zmax_r):
                    if job is not None and job.cancel.is_set():
                        return
                    Zr = -Zr_abs
                    sr = speed_ratio(Zs, Zbp, Zsp, Zr_abs, 1, ti, to)
                    if not (red - tol_red <= sr <= red + tol_red):
                        continue
                    for m_e in mns:
                        for m_i in mni:
                            for b_e in bes:
                                for b_i in bis:
                                    m_e, m_i, b_e, b_i = float(m_e), float(m_i), float(b_e), float(b_i)
                                    a_std = m_e * ((Zs + Zbp) / (2 * math.cos(math.radians(b_e))))
                                    for a in np.linspace(a_std - tol_a, a_std + tol_a, 10):
                                        a = float(a)
                                        m_t_e, m_t_i = Eq.m_t(m_e, b_e), Eq.m_t(m_i, b_i)
                                        at_e, at_i = Eq.alpha_t(an_e, b_e), Eq.alpha_t(an_i, b_i)
                                        awt_e = alpha_wt_seguro(Zs, Zbp, m_t_e, a, at_e)
                                        awt_i = alpha_wt_seguro(Zsp, Zr, m_t_i, -a, at_i)
                                        if not (an_e - dawt <= awt_e <= an_e + dawt and an_i - dawt <= awt_i <= an_i + dawt):
                                            continue
                                        bb_e, bb_i = Eq.beta_b(an_e, b_e), Eq.beta_b(an_i, b_i)
                                        zn_s, zn_bp = Eq.z_virt(Zs, bb_e, b_e), Eq.z_virt(Zbp, bb_e, b_e)
                                        zn_sp, zn_r = Eq.z_virt(Zsp, bb_i, b_i), Eq.z_virt(Zr, bb_i, b_i)
                                        aw_e = Eq.dist_centros(Zs, Zbp, m_e, b_e, at_e, awt_e)
                                        aw_i = Eq.dist_centros(Zsp, Zr, m_i, b_i, at_i, awt_i)
                                        r1 = desloc_perfil_seguro(Zs, Zbp, an_e, "DIN", None, 0.625, zn_s, zn_bp, at_e, awt_e, Zbp / Zs)
                                        if r1 is None or not (-sx_max <= r1[0] <= sx_max):
                                            continue
                                        sx_e, x_s, x_bp, _ = r1
                                        r2 = desloc_perfil_seguro(Zsp, Zr, an_i, "DIN", None, 0.625, zn_sp, zn_r, at_i, awt_i, Zr / Zsp)
                                        if r2 is None or not (-sx_max <= r2[0] <= sx_max):
                                            continue
                                        sx_i, x_sp, x_r, _ = r2
                                        K_e, _ = Eq.corre_blank(Zs, Zbp, x_s, x_bp, b_e, at_e, awt_e)
                                        K_i, _ = Eq.corre_blank(Zsp, Zr, x_sp, x_r, b_i, at_i, awt_i)
                                        d_s, db_s, da_s, df_s, ha_s = _geom_roda(m_e, an_e, b_e, Zs, x_s, ka["sun"], cp["sun"], K_e, 5)
                                        d_bp, db_bp, da_bp, df_bp, ha_bp = _geom_roda(m_e, an_e, b_e, Zbp, x_bp, ka["bp"], cp["bp"], K_e, 5)
                                        d_sp, db_sp, da_sp, df_sp, ha_sp = _geom_roda(m_i, an_i, b_i, Zsp, x_sp, ka["sp"], cp["sp"], K_i, 5)
                                        d_r, db_r, da_r, df_r, ha_r = _geom_roda(m_i, an_i, b_i, Zr, x_r, ka["r"], cp["r"], K_i, 9)
                                        dp_s, dp_bp = Eq.diametro_primi(Zs, Zbp, a)
                                        dp_sp, dp_r = Eq.diametro_primi(Zsp, Zr, -a)
                                        D_ext = (aw_e + da_bp / 2) * 2
                                        if not D_ext < Dup - 3:
                                            continue
                                        D_anel = abs(df_r) + 2 * Sr
                                        if not D_anel < Dup:
                                            continue
                                        try:
                                            Kin, Ain = interf_montagem_int_num(db_sp, db_r, da_sp, da_r, aw_i, awt_i, Zr / Zsp)
                                        except (ValueError, ZeroDivisionError):
                                            continue
                                        if not (Kin > 1 and Ain > 0):
                                            continue
                                        ea_e = Eq.grau_recob_perfil(Zbp, m_e, an_e, db_s, db_bp, da_s, da_bp, awt_e, at_e)
                                        ea_i = Eq.grau_recob_perfil(Zr, m_i, an_i, db_sp, db_r, da_sp, da_r, awt_i, at_i)
                                        if not (ea_e >= eps_min and ea_i >= eps_min):
                                            continue
                                        clearance = 2 * math.sin(math.radians(180 / N_Cp)) * aw_e - da_bp
                                        if not clearance >= 2 * ha_bp:
                                            continue
                                        Fc = math.gcd(int(Zbp), int(Zsp)); Pr = Zsp / Fc; Ps = Zbp / Fc
                                        I_va = (Zs * Pr + Zr_abs * Ps) / N_Cp
                                        if I_va % 1 != 0:
                                            continue
                                        if not (math.gcd(Zs, Zbp) == 1 and math.gcd(Zr_abs, Zsp) == 1):
                                            continue
                                        Is, Ir = Zs / N_Cp, Zr_abs / N_Cp
                                        base = dict(Zs=Zs, Zbp=Zbp, Zsp=Zsp, Zr=Zr, m_n_ext=m_e, m_n_int=m_i, beta_ext=b_e, beta_int=b_i,
                                                    i_real=sr, a_ext=aw_e, a_int=aw_i, sum_x_ext=sx_e, sum_x_int=sx_i, x_sun=x_s, x_bp=x_bp, x_sp=x_sp, x_r=x_r,
                                                    d_sun=d_s, dw_sun=dp_s, df_sun=df_s, da_sun=da_s, d_bp=d_bp, dw_bp=dp_bp, df_bp=df_bp, da_bp=da_bp,
                                                    d_sp=d_sp, dw_sp=dp_sp, df_sp=df_sp, da_sp=da_sp, d_r=d_r, dw_r=dp_r, df_r=df_r, da_r=da_r,
                                                    D_envolvente_planetas=D_ext, D_ext_anelar=D_anel, eps_alpha_ext=ea_e, eps_alpha_int=ea_i,
                                                    folga_planetas=clearance, K_interf=Kin, A_montagem=Ain)
                                        if Is % 1 == 0 and Ir % 1 == 0:
                                            out.append(dict(base, defasagem="NÃO", m0=0, L2=0))
                                        else:
                                            Is_f, Ir_c = math.floor(Is), math.ceil(Ir)
                                            for m in range(0, int(Zsp / Fc) - 1):
                                                L2 = ((I_va - (Ir_c - m) * Ps) / Pr) - Is_f
                                                if L2 % 1 == 0:
                                                    out.append(dict(base, defasagem="SIM", m0=m, L2=L2))
                                                    break
                                        if len(out) >= max_res:
                                            return
    progresso(total, total)


def _buscar_simples(job, p, N_Cp, ti, to, red, tol_red, an_e, eps_min, sx_max, dawt, max_res, Sr, Dup, tol_a, ka, cp, out, progresso):
    be = float(p["beta_ext"])
    Zmin = Z_min_basico(an_e, be)
    Zmax_s, Zmax_b, Zmax_r = int(p["Z_max_sun"]), int(p["Z_max_big"]), int(p["Z_max_ring"])
    total = max(1, (Zmax_s - Zmin) * (Zmax_b - Zmin))
    it = 0
    mns = linspace_if_tol(float(p["m_n_ext"]), float(p["tol_m_n_ext"]))
    bes = linspace_if_tol(be, float(p["tol_beta_ext"]))
    for Zs in range(Zmin, Zmax_s):
        for Zbp in range(Zmin, Zmax_b):
            it += 1
            if it % 5 == 0:
                progresso(it, total)
            if len(out) >= max_res:
                progresso(total, total); return
            for Zr_abs in range(Zmin, Zmax_r):
                if job is not None and job.cancel.is_set():
                    return
                Zr = -Zr_abs
                sr = speed_ratio(Zs, Zbp, Zbp, Zr_abs, 0, ti, to)
                if not (red - tol_red <= sr <= red + tol_red):
                    continue
                for m_e in mns:
                    for b_e in bes:
                        m_e, b_e = float(m_e), float(b_e)
                        a_std = m_e * ((Zs + Zbp) / (2 * math.cos(math.radians(b_e))))
                        for a in np.linspace(a_std - tol_a, a_std + tol_a, 10):
                            a = float(a)
                            m_t_e = Eq.m_t(m_e, b_e); at_e = Eq.alpha_t(an_e, b_e)
                            awt_e = alpha_wt_seguro(Zs, Zbp, m_t_e, a, at_e)
                            awt_i = alpha_wt_seguro(Zbp, Zr, m_t_e, -a, at_e)
                            # notebook: ±2° no planetário simples
                            lim = min(dawt, 2.0)
                            if not (an_e - lim <= awt_e <= an_e + lim and an_e - lim <= awt_i <= an_e + lim):
                                continue
                            bb_e = Eq.beta_b(an_e, b_e)
                            zn_s, zn_bp, zn_r = Eq.z_virt(Zs, bb_e, b_e), Eq.z_virt(Zbp, bb_e, b_e), Eq.z_virt(Zr, bb_e, b_e)
                            aw_e = Eq.dist_centros(Zs, Zbp, m_e, b_e, at_e, awt_e)
                            aw_i = Eq.dist_centros(Zbp, Zr, m_e, b_e, at_e, awt_i)
                            r1 = desloc_perfil_seguro(Zs, Zbp, an_e, "DIN", None, 0.625, zn_s, zn_bp, at_e, awt_e, Zbp / Zs)
                            if r1 is None or not (-sx_max <= r1[0] <= sx_max):
                                continue
                            sx_e, x_s, x_bp, _ = r1
                            r2 = desloc_perfil_seguro(Zbp, Zr, an_e, "DIN", None, 0.625, zn_bp, zn_r, at_e, awt_i, Zr / Zbp)
                            if r2 is None:
                                continue
                            sx_i = r2[0]; x_r = sx_i - x_bp     # planeta único: x do planeta é o da malha externa
                            if not (-sx_max <= sx_i <= sx_max):
                                continue
                            K_e, _ = Eq.corre_blank(Zs, Zbp, x_s, x_bp, b_e, at_e, awt_e)
                            d_s, db_s, da_s, df_s, ha_s = _geom_roda(m_e, an_e, b_e, Zs, x_s, ka["sun"], cp["sun"], K_e, 5)
                            d_bp, db_bp, da_bp, df_bp, ha_bp = _geom_roda(m_e, an_e, b_e, Zbp, x_bp, ka["bp"], cp["bp"], K_e, 5)
                            d_r, db_r, da_r, df_r, ha_r = _geom_roda(m_e, an_e, b_e, Zr, x_r, ka["r"], cp["r"], K_e, 9)
                            dp_s, dp_bp_s = Eq.diametro_primi(Zs, Zbp, a)
                            dp_bp_r, dp_r = Eq.diametro_primi(Zbp, Zr, -a)
                            D_ext = (aw_e + da_bp / 2) * 2
                            if not D_ext < Dup - 3:
                                continue
                            D_anel = abs(df_r) + 2 * Sr
                            if not D_anel < Dup:
                                continue
                            try:
                                Kin, Ain = interf_montagem_int_num(db_bp, db_r, da_bp, da_r, aw_i, awt_i, Zr / Zbp)
                            except (ValueError, ZeroDivisionError):
                                continue
                            if not (Kin > 1 and Ain > 0):
                                continue
                            ea_e = Eq.grau_recob_perfil(Zbp, m_e, an_e, db_s, db_bp, da_s, da_bp, awt_e, at_e)
                            ea_i = Eq.grau_recob_perfil(Zr, m_e, an_e, db_bp, db_r, da_bp, da_r, awt_i, at_e)
                            if not (ea_e >= eps_min and ea_i >= eps_min):
                                continue
                            clearance = 2 * math.sin(math.radians(180 / N_Cp)) * aw_e - da_bp
                            if not clearance >= 2 * ha_bp:
                                continue
                            if ((Zs + Zr_abs) / N_Cp) % 1 != 0:
                                continue
                            if not (math.gcd(Zs, Zbp) == 1 and math.gcd(Zr_abs, Zbp) == 1):
                                continue
                            Is, Ir = Zs / N_Cp, Zr_abs / N_Cp
                            if not (Is % 1 == 0 and Ir % 1 == 0):
                                continue
                            out.append(dict(Zs=Zs, Zbp=Zbp, Zsp=Zbp, Zr=Zr, m_n_ext=m_e, m_n_int=m_e, beta_ext=b_e, beta_int=b_e,
                                            i_real=sr, a_ext=aw_e, a_int=aw_i, sum_x_ext=sx_e, sum_x_int=sx_i, x_sun=x_s, x_bp=x_bp, x_sp=x_bp, x_r=x_r,
                                            d_sun=d_s, dw_sun=dp_s, df_sun=df_s, da_sun=da_s, d_bp=d_bp, dw_bp=dp_bp_s, dw_bp_r=dp_bp_r, df_bp=df_bp, da_bp=da_bp,
                                            d_sp=d_bp, dw_sp=dp_bp_r, df_sp=df_bp, da_sp=da_bp, d_r=d_r, dw_r=dp_r, df_r=df_r, da_r=da_r,
                                            D_envolvente_planetas=D_ext, D_ext_anelar=D_anel, eps_alpha_ext=ea_e, eps_alpha_int=ea_i,
                                            folga_planetas=clearance, K_interf=Kin, A_montagem=Ain, defasagem="NÃO", m0=0, L2=0))
                            if len(out) >= max_res:
                                return
    progresso(total, total)


COLUNAS = [
    ("idx", "#"), ("Zs", "z sol"), ("Zbp", "z planeta maior"), ("Zsp", "z planeta menor"), ("Zr", "z anelar"),
    ("i_real", "Redução real"), ("m_n_ext", "m_n ext [mm]"), ("m_n_int", "m_n int [mm]"), ("beta_ext", "β ext [°]"), ("beta_int", "β int [°]"),
    ("a_ext", "a ext [mm]"), ("a_int", "a int [mm]"), ("sum_x_ext", "Σx ext"), ("sum_x_int", "Σx int"),
    ("x_sun", "x sol"), ("x_bp", "x planeta maior"), ("x_sp", "x planeta menor"), ("x_r", "x anelar"),
    ("eps_alpha_ext", "ε_α ext"), ("eps_alpha_int", "ε_α int"), ("D_envolvente_planetas", "Ø envolvente planetas [mm]"), ("D_ext_anelar", "Ø externo anelar [mm]"),
    ("folga_planetas", "Folga entre planetas [mm]"), ("defasagem", "Defasagem?"), ("m0", "m"), ("L2", "L2"),
    ("d_sun", "d sol"), ("dw_sun", "d_w sol"), ("df_sun", "d_f sol"), ("da_sun", "d_a sol"),
    ("d_bp", "d planeta maior"), ("dw_bp", "d_w planeta maior"), ("df_bp", "d_f planeta maior"), ("da_bp", "d_a planeta maior"),
    ("d_sp", "d planeta menor"), ("dw_sp", "d_w planeta menor"), ("df_sp", "d_f planeta menor"), ("da_sp", "d_a planeta menor"),
    ("d_r", "d anelar"), ("dw_r", "d_w anelar"), ("df_r", "d_f anelar"), ("da_r", "d_a anelar"),
]


MEMBROS = {0: "sol", 1: "porta-planetas", 2: "anelar"}
MEMBRO_IDX = {v: k for k, v in MEMBROS.items()}


def cinematica_membro_fixo(Zs, Zbp, Zsp, Zr_abs, n_in, T_in, entrada, saida, N_Cp, tipo, Ky=1.05):
    """Cinemática e torques de malha de um planetário para qualquer par entrada/saída (o terceiro membro fica fixo).
    entrada/saida: 0 sol, 1 porta-planetas, 2 anelar (ou os nomes). n_in/T_in: rotação [rpm] e torque [N·m] do membro de
    ENTRADA. Devolve o dict de G.cinematica_planetaria acrescido de n_sol (absoluta), membro_fixo, i (= n_in/n_out) e
    n/T por membro."""
    ti = MEMBRO_IDX.get(entrada, entrada); to = MEMBRO_IDX.get(saida, saida)
    if ti == to:
        raise ValueError("Entrada e saída devem ser membros diferentes do planetário.")
    fixo = ({0, 1, 2} - {ti, to}).pop()
    k = (Zr_abs * Zbp) / (Zs * Zsp)
    if fixo == 2:        # anelar fixa
        if ti == 0:
            cin = G.cinematica_planetaria(Z_sol=Zs, Z_pla_ext=Zbp, Z_pla_int=Zsp, Z_anel=-Zr_abs, n_sol=n_in, T_sol=T_in, N_cp=N_Cp, Tipo=tipo, Ring="Fixo", Ky=Ky)
        else:            # entrada no porta-planetas: n_sol = n_c (1+k), T_sol = T_c/(1+k)
            cin = G.cinematica_planetaria(Z_sol=Zs, Z_pla_ext=Zbp, Z_pla_int=Zsp, Z_anel=-Zr_abs, n_sol=n_in * (1 + k), T_sol=T_in / (1 + k), N_cp=N_Cp, Tipo=tipo, Ring="Fixo", Ky=Ky)
    elif fixo == 1:      # porta-planetas fixo: trem ordinário sol -> planeta -> anelar
        n_s = n_in if ti == 0 else -n_in * k            # n_anel = -n_sol/k
        T_s = T_in if ti == 0 else T_in / k             # T_anel = k T_sol
        cin = G.cinematica_planetaria(Z_sol=Zs, Z_pla_ext=Zbp, Z_pla_int=Zsp, Z_anel=-Zr_abs, n_sol=n_s, T_sol=T_s, N_cp=N_Cp, Tipo=tipo, Ring="Rotativo", Ky=Ky, n_carrier=0.0)
    else:                # sol fixo: anelar <-> porta-planetas ; n_sol = 0 -> n_c = k n_anel/(1+k)
        if ti == 2:
            n_c = n_in * k / (1 + k); T_c = T_in * (1 + k) / k
        else:
            n_c = n_in; T_c = T_in
        T_s = T_c / (1 + k)                                # reação no sol
        cin = G.cinematica_planetaria(Z_sol=Zs, Z_pla_ext=Zbp, Z_pla_int=Zsp, Z_anel=-Zr_abs, n_sol=0.0, T_sol=T_s, N_cp=N_Cp, Tipo=tipo, Ring="Rotativo", Ky=Ky, n_carrier=n_c)
    n_sol = cin["n_sol_rel"] + cin["n_c"] if fixo != 0 else 0.0
    if fixo != 0 and ti == 0:
        n_sol = n_in if fixo == 2 else n_in              # entrada no sol: rotação absoluta do sol é a de entrada
    cin["n_sol"] = n_sol
    cin["membro_fixo"] = MEMBROS[fixo]; cin["entrada"] = MEMBROS[ti]; cin["saida"] = MEMBROS[to]
    n_por = {0: n_sol, 1: cin["n_c"], 2: cin["n_anel"]}
    T_por = {0: cin["T_malha_ext"], 1: cin["T_carrier"], 2: cin["T_anel"]}
    cin["n_membros"] = {MEMBROS[m]: n_por[m] for m in range(3)}
    cin["T_membros"] = {MEMBROS[m]: T_por[m] for m in range(3)}
    cin["i"] = (n_por[ti] / n_por[to]) if n_por[to] else float("inf")
    cin["P_in_kW"] = abs(T_por[ti] * n_por[ti]) * 2 * math.pi / 60000
    cin["P_out_kW"] = abs(T_por[to] * n_por[to]) * 2 * math.pi / 60000
    cin["k_basico"] = k
    return cin


def cinematica_diferencial(Zs, Zbp, Zsp, Zr_abs, n_in, T_in, entrada, saida, membro_livre, n_livre, N_Cp, tipo, Ky=1.05):
    """Planetário com DOIS graus de liberdade (diferencial / somador): nenhum membro está preso à carcaça.
    entrada: membro que recebe (n_in, T_in); membro_livre: o terceiro membro, com rotação IMPOSTA n_livre (rpm, com sinal,
    sol positivo) por outro acionamento; saida: o membro restante. A estática (torques) é a mesma do membro fixo — só a
    cinemática muda (Willis: n_sol - n_c = -k (n_anel - n_c)). A anelar sempre gira (Ring="Rotativo") a menos que n_anel = 0.
    Devolve o dict de cinematica_membro_fixo com membro_fixo=None, modo="diferencial" e n_livre."""
    ti = MEMBRO_IDX.get(entrada, entrada); to = MEMBRO_IDX.get(saida, saida); tl = MEMBRO_IDX.get(membro_livre, membro_livre)
    if len({ti, to, tl}) != 3:
        raise ValueError("No modo diferencial entrada, saída e membro livre devem ser três membros diferentes.")
    k = (Zr_abs * Zbp) / (Zs * Zsp)
    # rotações absolutas: duas conhecidas (entrada e livre), a terceira por Willis
    n = {ti: float(n_in), tl: float(n_livre)}
    if 0 in n and 1 in n:       n[2] = n[1] - (n[0] - n[1]) / k
    elif 0 in n and 2 in n:     n[1] = (n[0] + k * n[2]) / (1 + k)
    else:                       n[0] = n[1] + k * (n[1] - n[2])
    # torques pela estática (referidos ao sol): T_c = (1+k) T_s ; T_anel = k T_s
    fator = {0: 1.0, 1: 1.0 + k, 2: k}
    T_s = float(T_in) / fator[ti]
    ring = "Fixo" if abs(n[2]) < 1e-9 else "Rotativo"
    cin = G.cinematica_planetaria(Z_sol=Zs, Z_pla_ext=Zbp, Z_pla_int=Zsp, Z_anel=-Zr_abs, n_sol=n[0], T_sol=T_s, N_cp=N_Cp, Tipo=tipo,
                                  Ring=ring, Ky=Ky, n_carrier=n[1] if ring == "Rotativo" else None)
    cin["n_sol"] = n[0]
    cin["membro_fixo"] = None; cin["entrada"] = MEMBROS[ti]; cin["saida"] = MEMBROS[to]; cin["membro_livre"] = MEMBROS[tl]
    cin["modo"] = "diferencial"; cin["ring"] = ring
    T_por = {0: cin["T_malha_ext"], 1: cin["T_carrier"], 2: cin["T_anel"]}
    cin["n_membros"] = {MEMBROS[m]: n[m] for m in range(3)}
    cin["T_membros"] = {MEMBROS[m]: T_por[m] for m in range(3)}
    cin["i"] = (n[ti] / n[to]) if abs(n[to]) > 1e-12 else float("inf")
    P = {m: T_por[m] * n[m] * 2 * math.pi / 60000 for m in range(3)}   # potências com sinal: positiva entra, negativa sai (convenção pela estática)
    cin["P_in_kW"] = abs(P[ti]); cin["P_out_kW"] = abs(P[to]); cin["P_livre_kW"] = abs(P[tl])
    cin["P_membros_kW"] = {MEMBROS[m]: P[m] for m in range(3)}
    cin["k_basico"] = k
    return cin


def prefill(cand, entradas, n_sol=None, T_sol=None, N_Cp=None):
    """Monta os kwargs parciais das malhas externa e interna (etapa B) a partir de um candidato.
    A cinemática (rotações relativas e torques de malha) é resolvida para o membro FIXO definido por entrada/saída.
    n_sol/T_sol são a rotação e o torque do membro de ENTRADA."""
    tipo = "Composto" if int(entradas.get("Planetary_Type", 1)) == 1 else "Simples"
    N_Cp = int(N_Cp or entradas.get("N_Cp") or 3)
    if N_Cp != int(entradas.get("N_Cp") or N_Cp):
        raise ValueError(f"O candidato foi verificado (montagem, hunting, folga) para N_Cp = {entradas.get('N_Cp')}; refaça a busca para N_Cp = {N_Cp}.")
    n_in = float(n_sol if n_sol is not None else entradas.get("n_sol") or 1000)
    T_in = float(T_sol if T_sol is not None else entradas.get("T_sol") or 10)
    ti, to = int(entradas.get("torq_Input", 0)), int(entradas.get("torq_Output", 1))
    Zs, Zbp, Zsp, Zr = cand["Zs"], cand["Zbp"], cand["Zsp"], abs(cand["Zr"])
    cin = cinematica_membro_fixo(Zs, Zbp, Zsp, Zr, n_in, T_in, ti, to, N_Cp, tipo)
    n_sol = cin["n_sol"]
    ext = dict(apelido=f"Malha externa {cand['Zs']}/{cand['Zbp']}", trans="Planetário", Tipo_planetario=tipo, N_cp=N_Cp, Ky=1.05,
               m_n=cand["m_n_ext"], Z_pinhao=cand["Zs"], Z_coroa=cand["Zbp"], a=cand["a_ext"], alpha_n=entradas.get("alpha_n_ext", 20), beta=cand["beta_ext"],
               x_pinhao=cand["x_sun"], tipo="Otimização", membro_pinhao="sol", membro_coroa="planeta",
               n_t=n_sol, T=cin["T_malha_ext"], n_carrier=cin["n_c"])
    an_i = entradas.get("alpha_n_int", 25) if tipo == "Composto" else entradas.get("alpha_n_ext", 20)
    inte = dict(apelido=f"Malha interna {cand['Zsp']}/{cand['Zr']}", trans="Planetário", Tipo_planetario=tipo, N_cp=N_Cp, Ky=1.05,
                m_n=cand["m_n_int"], Z_pinhao=cand["Zsp"], Z_coroa=cand["Zr"], a=-abs(cand["a_int"]), alpha_n=an_i, beta=cand["beta_int"],
                x_pinhao=cand["x_sp"], tipo="Otimização", membro_pinhao="planeta", membro_coroa="anelar",
                n_t=cin["n_pla"], T=cin["T_malha_int"], n_carrier=cin["n_c"], di_coroa=-cand["D_ext_anelar"])
    return {"externa": ext, "interna": inte, "cinematica": cin, "candidato": cand}
