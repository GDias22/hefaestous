# -*- coding: utf-8 -*-
"""Sobremetal de retífica e perfil de pré-usinagem com protuberância (DIN 3972 / ISO 6336-3 / KISSsoft).

Convenções (tudo em mm, fatores * em múltiplos de m_n):
    q        : sobremetal por flanco deixado pela pré-usinagem (medido normal ao flanco)
    pr0      : protuberância da ferramenta de pré-usinagem (saliência da ponta além do flanco)
    h_fP*    : dedendo da cremalheira de referência FINAL (define d_f da roda acabada)
    rho_aP0  : raio de ponta da ferramenta de pré-usinagem
    alpha_prP: ângulo de flanco da protuberância (padrão 10°, informativo)

Modelo (idêntico ao KISSsoft "Pré-usinagem com protuberância"):
    - A pré-usinagem gera o dente com sobremetal q no flanco. Para uma cremalheira de ângulo alpha_n, deixar q
      no flanco equivale a afastar a ferramenta de q/sin(alpha_n):   x_pre = x + q/(m_n sin alpha_n).
    - A ferramenta de pré-usinagem tem o mesmo dedendo h_fP*; por isso o diâmetro de pé GERADO é
      d_f_pre = d - 2 m_n (h_fP* - x_pre) — maior que o nominal d_f = d - 2 m_n (h_fP* - x) em 2 q/sin(alpha_n).
    - A retífica remove q do flanco (volta a x) e não toca o pé: o d_f final é o da pré-usinagem. Expresso em
      relação ao x final, o dedendo efetivo da peça acabada é  h_fP*_final = h_fP* - (x_pre - x).
    - A protuberância efetiva (rebaixo que sobra no pé após a retífica) é  s_pr = pr0 - q  (>0: alívio; <0: a
      retífica entra no pé e forma degrau — aviso).
    - Diâmetro de início da protuberância/da evolvente retificada d_Ff: interseção da evolvente final com a
      trocoide da pré-usinagem (calculada em perfil2d).

Teste (KISSsoft 2024, m=3, z=15, x=0.5513, q=0.09, pr0=0.22, h_fP*=1.4 ⇒ x_pre=0.6390, h_fP*_final=1.312, d_f 40.434 vs 39.908, s_pr=0.13).
"""
import math


def calcular(m_n, z, x, alpha_n, h_fP_star, q, pr0, rho_aP0=None, h_aP0_star=None, alpha_prP=10.0, beta=0.0):
    """Devolve dict com x_pre, d_f_pre, d_f_nominal, h_fP_final_star, s_pr, h_prP (altura da protuberância) e avisos."""
    al = math.radians(alpha_n)
    z_abs = abs(z)
    sinal = 1 if z > 0 else -1
    d = sinal * m_n * z_abs / math.cos(math.radians(beta or 0.0))   # diâmetro de referência (helicoidal: m_t = m_n/cos β)
    q = float(q or 0.0); pr0 = float(pr0 or 0.0)
    dx = q / (m_n * math.sin(al)) if q else 0.0
    x_pre = x + dx
    # convenção do programa (Eq.diam_pe): d_f = d − 2 m_n (h_fP* − x) com d NEGATIVO para interna → |d_f| = |d| + 2 m_n (h_fP* − x)
    d_f_nom = d - 2 * m_n * (h_fP_star - x)
    d_f_pre = d - 2 * m_n * (h_fP_star - x_pre)
    h_fP_final = h_fP_star - dx
    s_pr = pr0 - q
    avisos = []
    if q and pr0 == 0:
        avisos.append("Retífica sem protuberância: a ferramenta de pré-usinagem não tem alívio; o rebolo pode gerar degrau no pé (s_pr = −q).")
    if s_pr < 0 and pr0 > 0:
        avisos.append(f"Protuberância menor que o sobremetal (pr₀ = {pr0:.3f} < q = {q:.3f}): a retífica alcança o pé e deixa degrau.")
    if q and s_pr > 0.4 * m_n * 0.3:
        pass
    # altura da protuberância na ferramenta (ponto onde o flanco de protuberância encontra o flanco reto), estimativa DIN 3972
    rho = rho_aP0 if rho_aP0 is not None else 0.0
    h_prP = (rho * (1 - math.sin(al)) + pr0 / math.tan(al)) if pr0 else 0.0
    res = dict(m_n=m_n, z=z, x=x, alpha_n=alpha_n, beta=beta, h_fP_star=h_fP_star, q=q, pr0=pr0, rho_aP0=rho_aP0, alpha_prP=alpha_prP,
               x_pre=x_pre, delta_x=dx, d_f_nominal=d_f_nom, d_f_pre=d_f_pre, d_f_final=d_f_pre, h_fP_final_star=h_fP_final,
               s_pr=s_pr, h_prP=h_prP, avisos=avisos)
    return res


def de_malha(eng, roda, q=None):
    """Monta o cálculo a partir de um Engrenamento e da roda ('pinhao' | 'coroa'); q padrão = sobremetal do programa."""
    suf = "pinhao" if roda == "pinhao" else "coroa"
    fer = getattr(eng, f"ferramenta_{suf}")
    if q is None:
        q = getattr(eng, f"SM_{suf}", 0.0) or 0.0
    return calcular(eng.m_n, getattr(eng, f"Z_{suf}"), getattr(eng, f"x_{suf}"), eng.alpha_n, fer.cp_dedendo, q,
                    fer.pr or 0.0, getattr(eng, f"rk_{suf}", None), beta=eng.beta)
