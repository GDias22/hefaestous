# -*- coding: utf-8 -*-
"""Geração numérica do perfil do dente (plano transversal) pela envoltória da ferramenta.

Externa: cremalheira (hob) com flanco reto, protuberância opcional e arredondamento de ponta ρ_aP0; rolamento sobre o
         círculo de referência com deslocamento x·m_n. Dentado helicoidal: o perfil normal da cremalheira é esticado por
         1/cos β ao longo da cremalheira (o que produz m_t, α_t e o arco de ponta elíptico exatos).
Interna: pinhão-cortador (shaper) z0, x0, ρ_a0 em engrenamento interno com a anelar (relação z0/|z|).
Retífica: flanco reto (cremalheira sem pé) no deslocamento final x; o perfil final é a união do material removido pela
         pré-usinagem (x_pre, protuberância) e pela retífica — por raio, o maior ângulo de vão.

Método: cada ponto da ferramenta (com sua tangente) toca a peça quando a normal passa pelo ponto primitivo
(equação de engrenamento). Transforma-se o ponto para o referencial da peça e reamostra-se o vão por raio tomando
o MAIOR semi-ângulo de vão entre todos os ramos (envoltória exterior do material removido: trata undercut, união
trocoide/evolvente e protuberância sem casos especiais). A ponta reta da cremalheira / círculo de ponta do cortador
geram exatamente o círculo de pé.

Saída: dict com r (mm), theta_vao (rad, semi-ângulo do vão por raio), theta_dente (= π/z − theta_vao), pontos do dente
(x,y) centrado no eixo +x, pontos da roda completa, diâmetros notáveis (d_f, d_Ff, d_b, d, d_a) e espessura s_t de verificação.
"""
import math

import numpy as np
from scipy.optimize import brentq

TWO_PI = 2 * math.pi


def inv(a):
    return math.tan(a) - a


def inv_inverse(y, guess=0.35):
    if y <= 0:
        raise ValueError("função evolvente inversa de argumento não positivo: deslocamentos de perfil incompatíveis com o engrenamento do cortador")
    return brentq(lambda a: inv(a) - y, 1e-6, 1.4)


# ---------------------------------------------------------------------------------------------------- ferramentas
def _poly(x, y):
    """Polilinha com tangentes por diferenças centrais."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    tx = np.gradient(x); ty = np.gradient(y)
    n = np.hypot(tx, ty); n[n == 0] = 1
    return x, y, tx / n, ty / n


def cremalheira(m_n, alpha_n, x, h_fP_star, rho=0.0, pr0=0.0, alpha_pr=10.0, beta=0.0, flanco_apenas=False, n=1500):
    """Metade direita (u ≥ 0) do DENTE da cremalheira (que corta o vão da roda), no plano transversal.
    u: ao longo da cremalheira; v: para fora da roda, origem na linha primitiva. Devolve lista de (nome, X, Y, TX, TY)
    e dados geométricos (v_tip, h_prP, v_q)."""
    al = math.radians(alpha_n); cb = math.cos(math.radians(beta))
    a = math.pi * m_n / 4
    v_dat = x * m_n
    v_tip = v_dat - h_fP_star * m_n
    um = lambda v: a + (v - v_dat) * math.tan(al)      # noqa: E731  flanco principal (seção normal)
    v_top = v_dat + 2.0 * m_n
    segs = []; info = {"v_tip": v_tip, "h_prP": 0.0, "v_q": None}
    if flanco_apenas:
        v = np.linspace(v_tip - 1.0 * m_n, v_top, n)
        X, Y, TX, TY = _poly(um(v) / cb, v)
        return [("retifica", X, Y, TX, TY)], info
    rho = float(rho or 0.0); pr0 = float(pr0 or 0.0)
    if pr0 > 0:
        apr = math.radians(alpha_pr)
        if apr >= al:
            raise ValueError("O ângulo da protuberância deve ser menor que o ângulo de pressão.")
        v_c = v_tip + rho                               # centro do arredondamento de ponta
        v_T = v_c - rho * math.sin(apr)                 # tangência arco × flanco de protuberância
        # pr0 = afastamento do flanco de protuberância em relação ao flanco principal, medido normal a este, no ponto T
        v_q = v_T + pr0 / ((math.tan(al) - math.tan(apr)) * math.cos(al))
        if v_q >= v_dat:
            raise ValueError("Protuberância alta demais: o ponto de transição ultrapassa a linha de referência da ferramenta.")
        u_q = um(v_q)
        upr = lambda v: u_q + (v - v_q) * math.tan(apr)   # noqa: E731
        u_c = upr(v_c) - rho / math.cos(apr)
        info.update(h_prP=v_q - v_tip, v_q=v_q)
        v = np.linspace(v_q, v_top, n); segs.append(("flanco",) + _poly(um(v) / cb, v))
        v = np.linspace(v_T, v_q, n // 3); segs.append(("protuberancia",) + _poly(upr(v) / cb, v))
        ang_T = -apr
    else:
        v_c = v_tip + rho
        u_c = um(v_c) - rho / math.cos(al)
        v_T = v_c - rho * math.sin(al)
        v = np.linspace(v_T, v_top, n); segs.append(("flanco",) + _poly(um(v) / cb, v))
        ang_T = -al
    if rho > 0:
        ph = np.linspace(ang_T, -math.pi / 2, n // 2)
        segs.append(("pe",) + _poly((u_c + rho * np.cos(ph)) / cb, v_c + rho * np.sin(ph)))
    u_end = u_c if rho > 0 else um(v_tip)
    u = np.linspace(u_end, 0.0, n // 6)
    segs.append(("fundo",) + _poly(u / cb, np.full_like(u, v_tip)))
    return segs, info


def cortador(m_t, alpha_t, z0, x0_n_over_cos, h_aP0_star_rad, rho=0.0, n=1500):
    """Metade superior (θ ≥ 0) do dente do pinhão-cortador centrado no eixo +x, plano transversal.
    x0_n_over_cos: deslocamento radial x0·m_n expresso em múltiplos de m_t (= x0·cos β). h_aP0_star_rad: adendo radial do
    cortador em múltiplos de m_t (= h_fP*·m_n/m_t)."""
    al = math.radians(alpha_t)
    r0 = m_t * z0 / 2; rb = r0 * math.cos(al)
    r_a0 = r0 + m_t * (h_aP0_star_rad + x0_n_over_cos)
    s0 = m_t * (math.pi / 2 + 2 * x0_n_over_cos * math.tan(al))     # espessura transversal na referência
    half0 = s0 / (2 * r0) + inv(al)

    def theta(r):
        return half0 - inv(math.acos(min(1.0, rb / r)))

    segs = []
    r_lo = max(rb * 1.0000001, r0 - 1.3 * m_t)
    # Ponta do cortador: se os flancos se cruzam antes de r_a0 (θ ≤ 0 → dente "afiado"), ou se o arredondamento ρ não cabe na
    # espessura de ponta, a cabeça é TRUNCADA no maior raio fisicamente possível (ponta afiada / totalmente arredondada).
    # Sem isso os dois flancos se cruzariam e a envoltória gerava um "V" no fundo do vão da anelar. r_a0 devolvido = efetivo.
    r_a0_nom = r_a0
    if theta(r_a0) <= 0:
        lo, hi = r_lo, r_a0
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            if theta(mid) > 0:
                lo = mid
            else:
                hi = mid
        r_a0 = lo
    rs = np.linspace(r_lo, r_a0, n)
    th = np.array([theta(r) for r in rs])
    X = rs * np.cos(th); Y = rs * np.sin(th)
    rho = float(rho or 0.0)
    if rho > 0:
        # ponto da evolvente cujo deslocamento ρ pela normal interna cai no raio r_a0 − ρ
        Xp, Yp, TX, TY = _poly(X, Y)
        nx, ny = TY, -TX                      # normal candidata
        # para DENTRO do dente = sentido de θ decrescente (a metade gerada é θ > 0): n·e_θ < 0 ⇔ nx·Yp − ny·Xp > 0.
        # (O sinal estava invertido: o centro do arco caía FORA do flanco, a ponta virava um "gancho" mais larga que o dente
        #  e a envoltória da anelar ganhava um "V" no fundo do vão — visível no 3D como um corte entre os dentes.)
        sgn = np.sign(nx * Yp - ny * Xp)
        sgn = np.where(sgn == 0, 1, sgn)
        nx = nx * sgn; ny = ny * sgn
        cx = Xp + rho * nx; cy = Yp + rho * ny
        # limite da ponta totalmente arredondada: centro do arco sobre a linha de centro do dente (cy = 0)
        ic = np.where(np.diff(np.sign(cy)) != 0)[0]
        if len(ic):
            j = ic[0]; w = cy[j] / (cy[j] - cy[j + 1])
            r_round = math.hypot(cx[j] + w * (cx[j + 1] - cx[j]), 0.0) + rho
            if r_round < r_a0:
                r_a0 = r_round
        f = np.hypot(cx, cy) - (r_a0 - rho)
        idx = np.where(np.diff(np.sign(f)) != 0)[0]
        if len(idx) == 0:
            raise ValueError("Raio de ponta do cortador grande demais para o dente.")
        i = idx[-1]
        w = f[i] / (f[i] - f[i + 1])
        C = (cx[i] + w * (cx[i + 1] - cx[i]), max(0.0, cy[i] + w * (cy[i + 1] - cy[i])))
        T = (Xp[i] + w * (Xp[i + 1] - Xp[i]), Yp[i] + w * (Yp[i + 1] - Yp[i]))
        keep = slice(0, i + 1)
        segs.append(("flanco",) + _poly(Xp[keep], Yp[keep]))
        ang_T = math.atan2(T[1] - C[1], T[0] - C[0]); ang_c = math.atan2(C[1], C[0])
        ph = np.linspace(ang_T, ang_c, n // 3)
        segs.append(("pe",) + _poly(C[0] + rho * np.cos(ph), C[1] + rho * np.sin(ph)))
        g = np.linspace(ang_c, 0.0, n // 6)
        segs.append(("fundo",) + _poly(r_a0 * np.cos(g), r_a0 * np.sin(g)))
    else:
        segs.append(("flanco",) + _poly(X, Y))
        g = np.linspace(max(th[-1], 0.0), 0.0, n // 6)
        segs.append(("fundo",) + _poly(r_a0 * np.cos(g), r_a0 * np.sin(g)))
    return segs, dict(r_a0=r_a0, r_a0_nominal=r_a0_nom, truncado=r_a0 < r_a0_nom - 1e-9, r0=r0, rb0=rb)


# ---------------------------------------------------------------------------------------------------- geração
def _gerar_rack(segs, r):
    """Envoltória da cremalheira rolando sobre o círculo de raio r. Devolve lista (nome, R, |θ|)."""
    out = []
    for nome, U, V, TU, TV in segs:
        m = np.abs(TU) > 1e-9
        U, V, TU, TV = U[m], V[m], TU[m], TV[m]
        s = -U - V * TV / TU
        X = U + s; Y = r + V
        ph = s / r
        Xg = X * np.cos(ph) - Y * np.sin(ph); Yg = X * np.sin(ph) + Y * np.cos(ph)
        R = np.hypot(Xg, Yg); th = np.abs(np.arctan2(Xg, Yg))
        out.append((nome, R, th))
    return out


def _gerar_shaper(segs, z_i, z0, a0):
    """Envoltória do cortador (centro na origem) em engrenamento interno com a anelar (centro em (−a0, 0))."""
    r_w1 = a0 * z0 / (z_i - z0)
    out = []
    for nome, X0, Y0, TX, TY in segs:
        c = (X0 * TX + Y0 * TY) / r_w1
        m = np.abs(c) <= 1
        X0, Y0, TX, TY, c = X0[m], Y0[m], TX[m], TY[m], c[m]
        ph_t = np.arctan2(TY, TX)
        Rs, Ths = [], []
        for sgn in (1, -1):
            psi = sgn * np.arccos(c) - ph_t
            Xf = X0 * np.cos(psi) - Y0 * np.sin(psi); Yf = X0 * np.sin(psi) + Y0 * np.cos(psi)
            Xr = Xf + a0; Yr = Yf
            psi2 = psi * z0 / z_i
            Xg = Xr * np.cos(-psi2) - Yr * np.sin(-psi2); Yg = Xr * np.sin(-psi2) + Yr * np.cos(-psi2)
            Rs.append(np.hypot(Xg, Yg)); Ths.append(np.abs(np.arctan2(Yg, Xg)))
        out.append((nome, np.concatenate(Rs), np.concatenate(Ths)))
    return out


def _reamostrar(ramos, r_min, r_max, z, n=700):
    """Semi-ângulo do vão por raio = máximo entre os ramos. Devolve r, θ_vão, ramo dominante."""
    rg = np.linspace(r_min, r_max, n)
    edges = np.linspace(r_min, r_max, n + 1)
    best = np.full(n, -np.inf); who = np.full(n, "", dtype=object)
    lim = math.pi / z
    for nome, R, Th in ramos:
        ok = (Th <= lim * 1.02) & (R >= r_min - 1e-9) & (R <= r_max + 1e-9) & np.isfinite(R)
        R, Th = R[ok], Th[ok]
        if len(R) == 0:
            continue
        b = np.clip(np.searchsorted(edges, R, side="right") - 1, 0, n - 1)
        mx = np.full(n, -np.inf)
        np.maximum.at(mx, b, Th)
        upd = mx > best
        best[upd] = mx[upd]; who[upd] = nome
    emp = ~np.isfinite(best)
    if emp.all():
        raise ValueError("Nenhum ponto gerado no intervalo de raios.")
    if emp.any():
        best[emp] = np.interp(rg[emp], rg[~emp], best[~emp])
        # ramo dominante dos vazios: vizinho mais próximo
        idx = np.where(~emp)[0]
        for k in np.where(emp)[0]:
            who[k] = who[idx[np.argmin(np.abs(idx - k))]]
    best = np.minimum(best, lim)
    return rg, best, who


# ---------------------------------------------------------------------------------------------------- API de alto nível
def perfil_externo(m_n, z, x, alpha_n, h_fP_star, r_a, beta=0.0, rho=None, pr0=0.0, alpha_pr=10.0, q=0.0, x_pre=None,
                   h_fP_star_pre=None, n=1500):
    """Perfil de roda EXTERNA gerada por cremalheira. Se q > 0 (ou x_pre dado): pré-usinagem em x_pre com protuberância
    pr0 e retífica final em x (flanco reto). Devolve dict com perfil final e, quando houver, pré-usinagem."""
    z = abs(int(z)); cb = math.cos(math.radians(beta))
    m_t = m_n / cb; r = m_t * z / 2
    al_t = math.atan(math.tan(math.radians(alpha_n)) / cb)
    r_b = r * math.cos(al_t)
    if rho is None:
        rho = 0.0
    retifica = (q and q > 0) or (x_pre is not None and abs(x_pre - x) > 1e-12)
    if retifica:
        if x_pre is None:
            x_pre = x + q / (m_n * math.sin(math.radians(alpha_n)))
        h_pre = h_fP_star if h_fP_star_pre is None else h_fP_star_pre
        segs_pre, info_pre = cremalheira(m_n, alpha_n, x_pre, h_pre, rho, pr0, alpha_pr, beta, n=n)
        r_f = r + (x_pre - h_pre) * m_n
        ramos_pre = _gerar_rack(segs_pre, r)
        segs_g, _ = cremalheira(m_n, alpha_n, x, h_fP_star, beta=beta, flanco_apenas=True, n=n)
        ramos_g = _gerar_rack(segs_g, r)
        # flanco de retífica só vale acima do círculo de base (abaixo, o ramo espelhado não corta)
        nome, R, Th = ramos_g[0]
        ramos_g = [(nome, R[R >= r_b * (1 - 1e-9)], Th[R >= r_b * (1 - 1e-9)])]
        rg, th_pre, who_pre = _reamostrar(ramos_pre, r_f, r_a, z, n=700)
        _, th_g, _ = _reamostrar(ramos_g + [("fundo", np.array([r_f]), np.array([0.0]))], r_f, r_a, z, n=700)
        th_fin = np.maximum(th_pre, th_g)
        who = np.where(th_g > th_pre, "retifica", who_pre)
        res = _montar(rg, th_fin, who, z, r, r_b, r_a, r_f, interna=False)
        res["pre"] = _montar(rg, th_pre, who_pre, z, r, r_b, r_a, r_f, interna=False)
        res["pre"].update(x_pre=x_pre, h_prP=info_pre["h_prP"], s_pr=pr0 - (q or 0.0))
        res.update(retificado=True, x_pre=x_pre, q=q, pr0=pr0)
        return res
    segs, info = cremalheira(m_n, alpha_n, x, h_fP_star, rho, pr0, alpha_pr, beta, n=n)
    r_f = r + (x - h_fP_star) * m_n
    ramos = _gerar_rack(segs, r)
    rg, th, who = _reamostrar(ramos, r_f, r_a, z, n=700)
    res = _montar(rg, th, who, z, r, r_b, r_a, r_f, interna=False)
    res.update(retificado=False, pre=None, h_prP=info["h_prP"])
    return res


def perfil_interno(m_n, z, x, alpha_n, h_fP_star, r_a, z0, x0=0.0, rho0=0.0, beta=0.0, D_ext=None, n=1500):
    """Perfil de ANELAR gerada por pinhão-cortador z0, x0, ρ_a0. z e x com convenção DIN (z negativo; x positivo engrossa
    o dente da anelar). r_a: raio de cabeça (interno, menor); raio de pé r_f = |d|/2 + m_n(h_fP* − x)."""
    z_i = abs(int(z)); cb = math.cos(math.radians(beta))
    m_t = m_n / cb; r = m_t * z_i / 2
    al_t = math.atan(math.tan(math.radians(alpha_n)) / cb)
    r_b = r * math.cos(al_t)
    r_f = r + (h_fP_star - x) * m_n
    # engrenamento cortador × anelar (DIN: z2 = −z_i)
    inv_aw = inv(al_t) + 2 * (x0 + x) * math.tan(math.radians(alpha_n)) / (z0 - z_i)
    aw = inv_inverse(inv_aw)
    a0 = m_t * (z_i - z0) / 2 * math.cos(al_t) / math.cos(aw)
    segs, info = cortador(m_t, math.degrees(al_t), z0, x0 * cb, h_fP_star * cb, rho0, n=n)
    ramos = _gerar_shaper(segs, z_i, z0, a0)
    # o pé real da anelar é o círculo varrido pela ponta do cortador (a0 + r_a0); o valor nominal DIN pode diferir em
    # centésimos. Usa-se o gerado para o perfil (acima dele não há material removido e a grade ficaria sem pontos).
    r_f_ger = a0 + info["r_a0"]
    rg, th, who = _reamostrar(ramos, r_a, r_f_ger, z_i, n=700)
    res = _montar(rg, th, who, z_i, r, r_b, r_a, r_f_ger, interna=True, D_ext=D_ext)
    res.update(retificado=False, pre=None, a0=a0, r_a0=info["r_a0"], r_f_gerado=r_f_ger, r_f_nominal=r_f, avisos=[])
    res["circulos"]["d_f_nominal"] = 2 * r_f
    if info.get("truncado"):
        res["avisos"].append(f"Pinhão-cortador z0 = {z0}: a cabeça do dente ficaria afiada antes do adendo nominal (h_aP0* = {h_fP_star:g}); "
                             f"a ponta foi truncada em r_a0 = {info['r_a0']:.3f} mm (nominal {info['r_a0_nominal']:.3f}). O pé real da anelar fica em "
                             f"d_f = {2 * r_f_ger:.3f} mm, acima do nominal {2 * r_f:.3f} mm. Use um cortador com mais dentes (z0) ou adendo menor.")
    return res


def _montar(rg, th_vao, who, z, r, r_b, r_a, r_f, interna=False, D_ext=None):
    th_d = math.pi / z - th_vao
    th_d = np.maximum(th_d, 0.0)
    # diâmetro de forma (início da evolvente): primeiro raio dominado pelo flanco reto/evolvente
    ev = np.isin(who, ["flanco", "retifica"])
    d_Ff = 2 * float(rg[ev][0]) if ev.any() else None
    if interna and ev.any():
        d_Ff = 2 * float(rg[ev][-1])   # na anelar a evolvente termina no maior raio dominado pelo flanco
    # espessura transversal na referência (verificação)
    s_t_ref = 2 * r * float(np.interp(r, rg, th_d)) if (rg[0] <= r <= rg[-1]) else None
    # contorno do dente centrado no eixo +x
    r_lo, r_hi = (r_a, r_f) if interna else (r_f, r_a)
    th_lo = float(np.interp(r_lo, rg, th_d)); th_hi = float(np.interp(r_hi, rg, th_d))
    xs, ys = [], []
    # ordem: fundo(−) → flanco (−θ) subindo em raio de r_f→r_a (externa) → ponta → flanco (+θ) → fundo(+)
    def arc(rad, a1, a2, k=40):
        a = np.linspace(a1, a2, k); return rad * np.cos(a), rad * np.sin(a)
    if not interna:
        ax, ay = arc(r_f, -math.pi / z, -th_lo); xs += list(ax); ys += list(ay)
        xs += list(rg * np.cos(-th_d)); ys += list(rg * np.sin(-th_d))
        ax, ay = arc(r_a, -th_hi, th_hi); xs += list(ax); ys += list(ay)
        xs += list(rg[::-1] * np.cos(th_d[::-1])); ys += list(rg[::-1] * np.sin(th_d[::-1]))
        ax, ay = arc(r_f, th_lo, math.pi / z); xs += list(ax); ys += list(ay)
    else:
        # anelar: rg cresce de r_a (ponta) a r_f (pé)
        ax, ay = arc(r_f, -math.pi / z, -th_hi); xs += list(ax); ys += list(ay)
        xs += list(rg[::-1] * np.cos(-th_d[::-1])); ys += list(rg[::-1] * np.sin(-th_d[::-1]))
        ax, ay = arc(r_a, -th_lo, th_lo); xs += list(ax); ys += list(ay)
        xs += list(rg * np.cos(th_d)); ys += list(rg * np.sin(th_d))
        ax, ay = arc(r_f, th_hi, math.pi / z); xs += list(ax); ys += list(ay)
    xs = np.array(xs); ys = np.array(ys)
    # roda completa
    rx, ry = [], []
    for k in range(z):
        a = TWO_PI * k / z
        rx.append(xs * math.cos(a) - ys * math.sin(a)); ry.append(xs * math.sin(a) + ys * math.cos(a))
    rx = np.concatenate(rx); ry = np.concatenate(ry)
    return dict(z=z, interna=interna, r=rg.tolist(), theta_vao=th_vao.tolist(), theta_dente=th_d.tolist(), ramo=list(map(str, who)),
                dente=dict(x=xs.tolist(), y=ys.tolist()), roda=dict(x=rx.tolist(), y=ry.tolist()),
                circulos=dict(d=2 * r, d_b=2 * r_b, d_a=2 * r_a, d_f=2 * r_f, d_Ff=d_Ff, D_ext=D_ext),
                s_t_ref=s_t_ref, passo_angular=TWO_PI / z)


# ---------------------------------------------------------------------------------------------------- medidas no pé
def secao_critica_30(res):
    """Espessura crítica s_Fn e raio ρ_F pela tangente a 30° (externa) / 60° (interna) com o eixo do dente, no perfil final.
    Devolve dict(s_Fn, rho_F, r_contato, h_30)."""
    rg = np.array(res["r"]); thd = np.array(res["theta_dente"])
    x = rg * np.cos(thd); y = rg * np.sin(thd)             # flanco superior do dente centrado em +x
    interna = res["interna"]
    # ordena do pé para a ponta (anelar: pé no maior raio)
    if interna:
        x, y = x[::-1], y[::-1]
    tx = np.gradient(x); ty = np.gradient(y)
    # inclinação da tangente em relação ao eixo do dente (eixo x), como ângulo não orientado em [0°, 90°]
    ang = np.degrees(np.arctan2(np.abs(ty), np.abs(tx)))
    alvo = 30.0 if not interna else 60.0                    # ISO 6336-3: 30° (externa) / 60° (interna)
    # do pé (tangente ~circunferencial, 90°) para a ponta a inclinação decresce; procura a primeira passagem
    # DESCENDENTE por `alvo`, ignorando os 2 primeiros pontos (gradiente unilateral no extremo da grade)
    f = ang - alvo
    idx = [k for k in np.where(np.diff(np.sign(f)) != 0)[0] if k >= 2 and f[k] > 0 >= f[k + 1]]
    if not idx:
        return None
    i = idx[0]
    w = f[i] / (f[i] - f[i + 1]) if f[i] != f[i + 1] else 0
    xs = x[i] + w * (x[i + 1] - x[i]); ys = y[i] + w * (y[i + 1] - y[i])
    s_Fn = 2 * ys
    # raio de curvatura local: ajuste de círculo por mínimos quadrados numa janela em torno do ponto
    lo, hi = max(0, i - 6), min(len(x), i + 8)
    rho_F = _raio_ajuste(x[lo:hi], y[lo:hi])
    return dict(s_Fn=float(s_Fn), rho_F=float(rho_F) if rho_F else None, x_30=float(xs), y_30=float(ys),
                angulo_tangente=float(ang[i]))


def _raio_ajuste(xs, ys):
    """Círculo por mínimos quadrados (Kåsa). Devolve o raio ou None."""
    if len(xs) < 3:
        return None
    A = np.column_stack([2 * xs, 2 * ys, np.ones_like(xs)])
    b = xs ** 2 + ys ** 2
    try:
        (cx, cy, c), *_ = np.linalg.lstsq(A, b, rcond=None)
    except np.linalg.LinAlgError:
        return None
    r2 = c + cx ** 2 + cy ** 2
    return math.sqrt(r2) if r2 > 0 else None
