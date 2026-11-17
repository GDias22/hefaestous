# -*- coding: utf-8 -*-
"""Explicação didática de cada fator/grandeza: fórmula LaTeX, variáveis com os valores DO PROJETO, resultado, notas,
texto do caderno (docs) e lista de parâmetros para o gráfico de sensibilidade.

Entrada: Engrenamento `e` (malha), Analise `an` + índice i (1 ou 2), nome do fator e roda ('pinhão'/'coroa'/None)."""
import math

from ..api.docs import doc as _doc
from ..services.serialize import num


def _g(an, nome, default=None):
    return num(getattr(an, nome, default))


def _roda(roda):
    return "coroa" if roda and roda.startswith("c") else "pinhao"


def _lado(roda):
    return "coroa" if _roda(roda) == "coroa" else "pinhão"


def _V(simbolo, nome, valor, unidade=None):
    return {"simbolo": simbolo, "nome": nome, "valor": num(valor) if valor is not None else None, "unidade": unidade}


def _sens_padrao(e):
    s = [("m_n", "Módulo m_n"), ("b", "Largura b"), ("x_pinhao", "Deslocamento x₁"), ("alpha_n", "Ângulo de pressão α_n"), ("beta", "Ângulo de hélice β"), ("T", "Torque T"), ("n", "Rotação n"), ("IQ", "Qualidade ISO"), ("Z_pinhao", "Dentes do pinhão z₁")]
    return [{"key": k, "label": l} for k, l in s]


def explicar(e, an, i, fator, roda=None):
    """Devolve dict: titulo, titulo_curto, resumo, formula, variaveis, resultado, notas, doc, sensibilidade."""
    r = _roda(roda); L = _lado(roda); suf = r
    g = lambda n: _g(an, n)  # noqa: E731
    out = {"titulo": fator, "titulo_curto": fator, "resumo": "", "formula": None, "variaveis": [], "resultado": None, "notas": [], "doc": None, "sensibilidade": _sens_padrao(e)}
    D = lambda ch: (_doc(ch) or {}).get("markdown")  # noqa: E731

    if fator in ("S_H", "S_F"):
        if fator == "S_H":
            sH = g(f"sigma_H{suf}{i}"); sHP = g(f"sigma_HP_{suf}{i}"); sH0 = g(f"sigma_H0{i}")
            out.update(titulo=f"Segurança contra pitting S_H ({L})", titulo_curto="S_H",
                       resumo="Razão entre a tensão de contato admissível (limite do material corrigido pelos fatores Z) e a tensão de contato atuante no ponto primitivo (Hertz, majorada pelos fatores K).",
                       formula=r"S_H = \frac{\sigma_{HP}}{\sigma_H} = \frac{\sigma_{H\,lim}\, Z_{NT}\, Z_L Z_V Z_R\, Z_W Z_X}{Z_{B/D}\,\sigma_{H0}\sqrt{K_A K_v K_{H\beta} K_{H\alpha}}}",
                       variaveis=[_V(r"\sigma_{H\,lim}", f"Limite de pressão do material ({L})", getattr(e, f"material_{suf}").Lim_pressao, "MPa"),
                                  _V(r"Z_{NT}", "Fator de vida (pitting)", g(f"Z_NT_{suf}{i}")), _V("Z_L", "Lubrificante", g(f"Z_L{i}")), _V("Z_V", "Velocidade", g(f"Z_V{i}")), _V("Z_R", "Rugosidade", g(f"Z_R{i}")),
                                  _V("Z_W", "Endurecimento", g(f"Z_W{i}_{suf}")), _V("Z_X", "Tamanho", g(f"Z_X_{suf}{i}")), _V(r"\sigma_{HP}", "Tensão admissível", sHP, "MPa"),
                                  _V(r"\sigma_{H0}", "Tensão nominal de contato", sH0, "MPa"), _V("Z_B" if r == "pinhao" else "Z_D", "Contato individual", g(f"Z_B{i}") if r == "pinhao" else g(f"Z_D{i}")),
                                  _V("K_A", "Aplicação", e.Ka), _V("K_v", "Dinâmico", g(f"Kv{i}")), _V(r"K_{H\beta}", "Distribuição longitudinal", g(f"K_Hbeta{i}")), _V(r"K_{H\alpha}", "Distribuição transversal", g(f"K_Halpha{i}")),
                                  _V(r"\sigma_H", "Tensão de contato atuante", sH, "MPa")],
                       resultado=f"S_H = {sHP:.1f} / {sH:.1f} = {g(f'S_H{suf}{i}'):.3f}  (mínimo {e.S_Hmin})" if sH and sHP else None,
                       notas=["σ_H0 = Z_H Z_E Z_ε Z_β √(F_t (u+1)/(d₁ b u)): depende da força tangencial, do diâmetro do pinhão e da largura de contato.",
                              "Para aumentar S_H: maior largura b ou diâmetro (módulo/dentes), material com σ_Hlim maior, melhor qualidade (reduz K_v, K_Hβ), rugosidade menor (Z_R)."],
                       doc=D("sigma_H"))
        else:
            sF = g(f"sigma_F{suf}{i}"); sFP = g(f"sigma_FP_{suf}{i}"); sF0 = g(f"sigma_F01{i}") if r == "pinhao" else g(f"sigma_F02{i}")
            out.update(titulo=f"Segurança contra fratura no pé S_F ({L})", titulo_curto="S_F",
                       resumo="Razão entre a tensão de flexão admissível no pé do dente e a tensão de flexão atuante na seção crítica (tangente a 30°), calculada pelo método da ISO 6336-3.",
                       formula=r"S_F = \frac{\sigma_{FP}}{\sigma_F} = \frac{\sigma_{F\,lim}\, Y_{ST}\, Y_M\, Y_{NT}\, Y_{\delta relT}\, Y_{RrelT}\, Y_X}{\dfrac{F_t}{b\,m_n}\, Y_F Y_S Y_\beta Y_B Y_\varepsilon\; K_A K_v K_{F\beta} K_{F\alpha}}",
                       variaveis=[_V(r"\sigma_{F\,lim}", f"Limite de flexão do material ({L})", getattr(e, f"material_{suf}").Lim_flexao, "MPa"), _V("Y_{ST}", "Fator de correção de tensão de referência", 2.0),
                                  _V("Y_M", "Carga alternada (planeta de planetário simples: 0,7)", getattr(e, f"Y_M_{suf}")), _V("Y_{NT}", "Vida (flexão)", g(f"Y_NT_{suf}{i}")),
                                  _V(r"Y_{\delta relT}", "Sensibilidade ao entalhe", g(f"Y_delta_RefT_{suf}{i}")), _V("Y_{RrelT}", "Rugosidade do pé", g(f"Y_R_RefT_{suf}{i}")), _V("Y_X", "Tamanho", g(f"Y_X_{suf}{i}")),
                                  _V(r"\sigma_{FP}", "Tensão admissível", sFP, "MPa"), _V("F_t", "Força tangencial", e.Ft, "N"), _V("b", "Largura", getattr(e, f"b_{suf}"), "mm"), _V("m_n", "Módulo", e.m_n, "mm"),
                                  _V("Y_F", "Forma do dente", getattr(e, f"Yf_{suf}")), _V("Y_S", "Concentração de tensão", g(f"Y_S_{suf}{i}")), _V(r"Y_\beta", "Hélice", g(f"Y_beta{i}")), _V("Y_B", "Espessura de aro", g(f"Y_B{i}_{suf}")),
                                  _V("K_A", "Aplicação", e.Ka), _V("K_v", "Dinâmico", g(f"Kv{i}")), _V(r"K_{F\beta}", "Distribuição longitudinal", g(f"K_Fbeta{i}")), _V(r"K_{F\alpha}", "Distribuição transversal", g(f"K_Falpha{i}")),
                                  _V(r"\sigma_{F0}", "Tensão nominal de flexão", sF0, "MPa"), _V(r"\sigma_F", "Tensão de flexão atuante", sF, "MPa")],
                       resultado=f"S_F = {sFP:.1f} / {sF:.1f} = {g(f'S_F{suf}{i}'):.3f}  (mínimo {e.S_Fmin})" if sF and sFP else None,
                       notas=["Para aumentar S_F: módulo maior (reduz F_t/(b·m_n)), deslocamento de perfil positivo no pinhão (reduz Y_F), raio de pé maior (reduz Y_S), largura maior, material com σ_Flim maior."],
                       doc=D("sigma_F"))
        return out

    tabela = {
        "Kv": dict(titulo="Fator dinâmico K_v", resumo="Majora a carga pelas forças dinâmicas internas do engrenamento (erros de passo e perfil, rigidez variável, inércias). Método B da ISO 6336-1: depende da razão N entre a rotação do pinhão e a rotação de ressonância n_E1.",
                   formula=r"N = \frac{n_1}{n_{E1}},\qquad n_{E1} = \frac{30000}{\pi z_1}\sqrt{\frac{c_\gamma}{m_{red}}},\qquad K_v = \begin{cases} N K + 1 & N < N_S \\ C_{v1}B_p + C_{v2}B_f + C_{v4}B_k + 1 & N_S \le N < 1{,}15 \\ \dots \end{cases}",
                   vars=lambda: [_V("n_1", "Rotação do pinhão (relativa ao porta-planetas em planetário)", e.n_rel, "rpm"), _V("n_{E1}", "Rotação de ressonância", g(f"n_e{i}"), "rpm"), _V("N", "Razão de ressonância", (e.n_rel / g(f"n_e{i}")) if g(f"n_e{i}") else None),
                                 _V(r"c_\gamma", "Rigidez de malha", g(f"c_gamma_alpha{i}"), "N/(mm·µm)"), _V("z_1", "Dentes do pinhão", e.Z_pinhao), _V("f_{pe}", "Desvio de passo de base (pinhão)", e.fpe_pinhao * 1000, "µm"), _V("f_f", "Desvio de forma de perfil (pinhão)", e.f_f_pinhao * 1000, "µm"),
                                 _V("F_t K_A / b", "Carga específica", e.Ft * e.Ka / e.b, "N/mm"), _V("K_v", "Resultado", g(f"Kv{i}"))],
                   resultado=lambda: f"{g(f'zona{i}')}" if g(f"zona{i}") else None,
                   notas=["Quanto melhor a qualidade (IQ menor) e maior a carga específica, menor K_v.", "Em planetário, o modelo acopla as inércias do sol, planetas e anelar; a rotação usada é a relativa ao porta-planetas."], doc="Kv"),
        "K_Hbeta": dict(titulo="Fator de distribuição longitudinal de carga K_Hβ", resumo="Corrige a distribuição desigual da carga ao longo da largura do dente causada por desvios de hélice de fabricação (f_ma) e pela deflexão/torção do eixo (f_sh), com amaciamento (y_β). Método C da ISO 6336-1; f_ma pela Eq. (64): √(f_Hβ1² + f_Hβ2²).",
                        formula=r"f_{ma} = \sqrt{f_{H\beta 1}^2 + f_{H\beta 2}^2},\quad F_{\beta x} = \max(1{,}33\,f_{sh} + f_{ma},\; F_{\beta x,b},\; F_{\beta x,c}),\quad F_{\beta y} = F_{\beta x} - y_\beta,\quad K_{H\beta} = \begin{cases}\sqrt{\dfrac{2 F_{\beta y} c_{\gamma\beta}}{F_m/b}} & \text{se } \dfrac{F_{\beta y} c_{\gamma\beta}}{2F_m/b} \ge 1\\[8pt] 1 + \dfrac{F_{\beta y} c_{\gamma\beta}}{2F_m/b} & \text{caso contrário}\end{cases}",
                        vars=lambda: [_V("F_m/b", "Carga específica média F_t K_A K_v / b", e.Ft * e.Ka * (g(f"Kv{i}") or 1) / e.b, "N/mm"), _V(r"c_{\gamma\beta}", "Rigidez de malha", g(f"c_gamma_beta{i}"), "N/(mm·µm)"),
                                      _V("f_{H\\beta 1}, f_{H\\beta 2}", "Tolerância de hélice ISO 1328-1 (pinhão / coroa)", f"{e.f_Hbeta_pinhao * 1000:.0f} / {e.f_Hbeta_coroa * 1000:.0f}", "µm"), _V("f_{ma}", "Desalinhamento de fabricação, Eq. (64)", math.hypot(e.f_Hbeta_pinhao, e.f_Hbeta_coroa) * 1000 * (0.5 if (e.crwon_s_pinhao or e.crwon_s_coroa) else 1.0), "µm"),
                                      _V("K'", "Constante de arranjo do pinhão", e.K_linha_pinhao), _V("l, s", "Vão entre mancais / desalinhamento", f"{e.L_pinhao} / {e.sh_pinhao}", "mm"),
                                      _V("d_1/d_{sh}", "Razão diâmetro/eixo", e.d_pinhao / e.d_sh_pinhao if e.d_sh_pinhao else None), _V("b/d_1", "Esbeltez", e.b / e.d_pinhao), _V(r"K_{H\beta}", "Resultado", g(f"K_Hbeta{i}"))],
                        resultado=lambda: f"Condição: {g(f'Cond{i}')}" if g(f"Cond{i}") else None,
                        notas=["Reduz-se K_Hβ com abaulamento (crowning), menor b/d₁, eixo mais rígido (d_sh maior, menor vão l), melhor qualidade de hélice e pinhão centrado entre mancais.", "Valor imposto (KISSsoft, medição) pode ser informado em 'Análise'."], doc="K_Hbeta"),
        "K_Halpha": dict(titulo="Fator de distribuição transversal K_Hα", resumo="Considera a repartição desigual da carga entre pares de dentes simultaneamente em contato, por desvios de passo de base (f_pe) e deformação dos dentes.",
                         formula=r"K_{H\alpha} = \frac{\varepsilon_\gamma}{2}\left[0{,}9 + 0{,}4\,\frac{c_\gamma (f_{pe} - y_\alpha)}{F_{tH}/b}\right]\quad(\varepsilon_\gamma \le 2),\qquad 1 \le K_{H\alpha} \le \frac{\varepsilon_\gamma}{\varepsilon_\alpha Z_\varepsilon^2}",
                         vars=lambda: [_V(r"\varepsilon_\gamma", "Recobrimento total", e.epsilon_total), _V(r"c_\gamma", "Rigidez de malha", g(f"c_gamma_alpha{i}"), "N/(mm·µm)"), _V("f_{pe}", "Desvio de passo de base (maior)", max(e.fpe_pinhao, e.fpe_coroa) * 1000, "µm"),
                                       _V("F_{tH}/b", "F_t K_A K_v K_Hβ / b", e.Ft * e.Ka * (g(f"Kv{i}") or 1) * (g(f"K_Hbeta{i}") or 1) / e.b, "N/mm"), _V(r"Z_\varepsilon", "Fator de recobrimento", g(f"Z_epsilon{i}")), _V(r"K_{H\alpha}", "Resultado", g(f"K_Halpha{i}"))],
                         doc="K_Halpha"),
        "K_Fbeta": dict(titulo="Fator de distribuição longitudinal na raiz K_Fβ", formula=r"K_{F\beta} = K_{H\beta}^{\,N_F},\qquad N_F = \frac{(b/h)^2}{1 + b/h + (b/h)^2}", vars=lambda: [_V(r"K_{H\beta}", "", g(f"K_Hbeta{i}")), _V("b/h", "Largura / altura do dente", e.b / max(e.h_dente_pinhao, 1e-9)), _V(r"K_{F\beta}", "Resultado", g(f"K_Fbeta{i}"))], doc="K_Fbeta"),
        "K_Falpha": dict(titulo="Fator de distribuição transversal na raiz K_Fα", formula=r"K_{F\alpha} = K_{H\alpha}\quad\left(1 \le K_{F\alpha} \le \frac{\varepsilon_\gamma}{0{,}25\,\varepsilon_\alpha + 0{,}75}\right)", vars=lambda: [_V(r"K_{H\alpha}", "", g(f"K_Halpha{i}")), _V(r"K_{F\alpha}", "Resultado", g(f"K_Falpha{i}"))], doc="K_Falpha"),
        "Z_H": dict(titulo="Fator de zona Z_H", resumo="Curvatura dos flancos no ponto primitivo (pressão de Hertz).", formula=r"Z_H = \sqrt{\frac{2\cos\beta_b\,\cos\alpha_{wt}}{\cos^2\alpha_t\,\sin\alpha_{wt}}}",
                    vars=lambda: [_V(r"\beta_b", "Ângulo de hélice de base", e.beta_b, "°"), _V(r"\alpha_{wt}", "Ângulo de pressão de trabalho", e.alpha_wt, "°"), _V(r"\alpha_t", "Ângulo de pressão transversal", e.alpha_t, "°"), _V("Z_H", "Resultado", g(f"Z_H{i}"))], doc="Z_H"),
        "Z_E": dict(titulo="Fator de elasticidade Z_E", formula=r"Z_E = \sqrt{\frac{1}{\pi\left(\dfrac{1-\nu_1^2}{E_1} + \dfrac{1-\nu_2^2}{E_2}\right)}}", vars=lambda: [_V("E_1, E_2", "Módulos de elasticidade", f"{e.material_pinhao.E} / {e.material_coroa.E}", "GPa"), _V(r"\nu", "Poisson", e.material_pinhao.Possion), _V("Z_E", "Resultado", g(f"Z_E{i}"), "√MPa")], doc="Z_E"),
        "Z_epsilon": dict(titulo="Fator de recobrimento Z_ε", formula=r"Z_\varepsilon = \sqrt{\frac{4-\varepsilon_\alpha}{3}(1-\varepsilon_\beta) + \frac{\varepsilon_\beta}{\varepsilon_\alpha}}\;(\varepsilon_\beta<1),\qquad Z_\varepsilon = \sqrt{\frac{1}{\varepsilon_\alpha}}\;(\varepsilon_\beta \ge 1)",
                          vars=lambda: [_V(r"\varepsilon_\alpha", "Recobrimento de perfil", e.epsilon_alpha), _V(r"\varepsilon_\beta", "Recobrimento de hélice", e.epsilon_beta), _V(r"Z_\varepsilon", "Resultado", g(f"Z_epsilon{i}"))], doc="Z_eps"),
        "Z_beta": dict(titulo="Fator de ângulo de hélice Z_β", formula=r"Z_\beta = \frac{1}{\sqrt{\cos\beta}}", vars=lambda: [_V(r"\beta", "Ângulo de hélice", e.beta, "°"), _V(r"Z_\beta", "Resultado", g(f"Z_beta{i}"))], doc="Z_beta"),
        "Z_L": dict(titulo="Fator de lubrificante Z_L", formula=r"Z_L = C_{ZL} + \frac{4(1-C_{ZL})}{\left(1{,}2 + \dfrac{134}{\nu_{40}}\right)^2}", vars=lambda: [_V(r"\nu_{40}", "Viscosidade a 40 °C", e.lubrificante.visc_40, "mm²/s"), _V(r"\sigma_{H\,lim}", "Menor limite de pressão", min(e.material_pinhao.Lim_pressao, e.material_coroa.Lim_pressao), "MPa"), _V("Z_L", "Resultado", g(f"Z_L{i}"))], doc="Z_L"),
        "Z_V": dict(titulo="Fator de velocidade Z_V", formula=r"Z_V = C_{ZV} + \frac{2(1-C_{ZV})}{\sqrt{0{,}8 + 32/v_t}}", vars=lambda: [_V("v_t", "Velocidade tangencial", e.v_t, "m/s"), _V("Z_V", "Resultado", g(f"Z_V{i}"))], doc="Z_V"),
        "Z_R": dict(titulo="Fator de rugosidade Z_R", formula=r"Z_R = \left(\frac{3}{R_{z10}}\right)^{C_{ZR}},\qquad R_{z10} = R_{zm}\sqrt[3]{\frac{10}{\rho_{red}}}", vars=lambda: [_V("R_{zm}", "Rugosidade média dos flancos (Rz)", (e.Rz_flanco_pinhao + e.Rz_flanco_coroa) / 2, "µm"), _V(r"\rho_{red}", "Raio de curvatura relativo no ponto primitivo", (0.5 * e.db_pinhao * math.tan(math.radians(e.alpha_wt)) * 0.5 * abs(e.db_coroa) * math.tan(math.radians(e.alpha_wt))) / (0.5 * e.db_pinhao * math.tan(math.radians(e.alpha_wt)) + 0.5 * abs(e.db_coroa) * math.tan(math.radians(e.alpha_wt))), "mm"), _V("Z_R", "Resultado", g(f"Z_R{i}"))], doc="Z_R"),
        "Z_W": dict(titulo="Fator de endurecimento Z_W", formula=r"Z_W = 1{,}2 - \frac{HB - 130}{1700}\quad(130 \le HB \le 470,\ \text{coroa mais macia})", vars=lambda: [_V("HRC", f"Dureza superficial ({L})", getattr(e, f"material_{suf}").dureza_superficial), _V("Z_W", "Resultado", g(f"Z_W{i}_{suf}"))], doc="Z_W"),
        "Z_X": dict(titulo="Fator de tamanho Z_X", formula=r"Z_X = f(m_n,\ \text{classe do material})", vars=lambda: [_V("m_n", "Módulo", e.m_n, "mm"), _V("Z_X", "Resultado", g(f"Z_X_{suf}{i}"))], doc="Z_X"),
        "Z_B": dict(titulo="Fator de contato individual Z_B / Z_D", resumo="Converte a tensão de contato do ponto primitivo para o ponto interior (Z_B, pinhão) ou exterior (Z_D, coroa) de engrenamento individual, onde a curvatura relativa é menor.", formula=r"Z_B = \sqrt{\frac{\tan\alpha_{wt}}{\sqrt{\left(\sqrt{\tfrac{d_{a1}^2}{d_{b1}^2}-1} - \tfrac{2\pi}{z_1}\right)\left(\sqrt{\tfrac{d_{a2}^2}{d_{b2}^2}-1} - (\varepsilon_\alpha - 1)\tfrac{2\pi}{z_2}\right)}}}",
                    vars=lambda: [_V("Z_B", "Pinhão", g(f"Z_B{i}")), _V("Z_D", "Coroa", g(f"Z_D{i}")), _V(r"\varepsilon_\alpha", "", e.epsilon_alpha)], doc="Z_B"),
        "Z_NT": dict(titulo="Fator de vida Z_NT", resumo="Permite tensões de contato maiores para vidas menores que a de referência (5·10⁷ ciclos para aço cementado). Curva ISO decai até 0,85 em 10¹⁰; curva DIN permanece em 1.", formula=r"N_L = 60\, n_{rel}\, N_{contatos}\, V_r,\qquad Z_{NT} = f(N_L,\ \text{classe})",
                     vars=lambda: [_V("n_{rel}", "Rotação relativa", e.n_rel, "rpm"), _V("N_{contatos}", f"Engrenamentos por volta ({L})", getattr(e, f"contatos_{suf}")), _V("V_r", "Vida requerida", e.Vr, "h"), _V("N_L", "Ciclos de carga", 60 * e.n_rel * getattr(e, f"contatos_{suf}") * e.Vr / (abs(e.u) if r == "coroa" else 1)), _V("Z_{NT}", "Resultado", g(f"Z_NT_{suf}{i}"))], doc="Z_NT"),
        "Y_NT": dict(titulo="Fator de vida Y_NT (flexão)", formula=r"N_L = 60\, n_{rel}\, N_{contatos}\, V_r,\qquad Y_{NT} = f(N_L,\ \text{classe})", vars=lambda: [_V("N_L", "Ciclos de carga", 60 * e.n_rel * getattr(e, f"contatos_{suf}") * e.Vr / (abs(e.u) if r == "coroa" else 1)), _V("Y_{NT}", "Resultado", g(f"Y_NT_{suf}{i}"))], doc="Y_NT"),
        "Y_F": dict(titulo=f"Fator de forma do dente Y_F ({L})", resumo="Relaciona a geometria do dente (braço de alavanca h_Fe e espessura crítica s_Fn na tangente a 30°) com a tensão nominal de flexão. Método B: carga no ponto exterior de engrenamento individual; método C: carga na ponta.",
                    formula=r"Y_F = \frac{6\,\dfrac{h_{Fe}}{m_n}\cos\alpha_{Fen}}{\left(\dfrac{s_{Fn}}{m_n}\right)^2\cos\alpha_n}",
                    vars=lambda: [_V("h_{Fe}", "Braço de alavanca", getattr(e, f"h_fe_{suf}"), "mm"), _V("s_{Fn}", "Espessura crítica (30°)", getattr(e, f"S_fn_{suf}"), "mm"), _V(r"\rho_F", "Raio de pé na seção crítica", getattr(e, f"p_f_{suf}"), "mm"), _V("x", "Deslocamento de perfil", getattr(e, f"x_{suf}")), _V("z_n", "Dentes virtuais", getattr(e, f"zn_{suf}")), _V("Y_F", "Resultado", getattr(e, f"Yf_{suf}"))],
                    notas=["x positivo engrossa o pé (s_Fn maior) e reduz Y_F.", "Dentado interno: pé gerado pelo pinhão-cortador z₀ da ferramenta da anelar (ISO 6336-3 §6.2.4/6.2.5, tangente a 60°); sem z₀ usa a cremalheira equivalente ao vão."], doc="Y_F"),
        "Y_S": dict(titulo=f"Fator de concentração de tensão Y_S ({L})", formula=r"Y_S = (1{,}2 + 0{,}13 L)\; q_s^{\frac{1}{1{,}21 + 2{,}3/L}},\qquad L = \frac{s_{Fn}}{h_{Fe}},\quad q_s = \frac{s_{Fn}}{2\rho_F}",
                    vars=lambda: [_V("s_{Fn}", "", getattr(e, f"S_fn_{suf}"), "mm"), _V("h_{Fe}", "", getattr(e, f"h_fe_{suf}"), "mm"), _V(r"\rho_F", "", getattr(e, f"p_f_{suf}"), "mm"), _V("q_s", "Parâmetro de entalhe (válido 1 ≤ q_s < 8)", getattr(e, f"S_fn_{suf}") / (2 * getattr(e, f"p_f_{suf}")) if getattr(e, f"p_f_{suf}") else None), _V("Y_S", "Resultado", g(f"Y_S_{suf}{i}"))],
                    notas=["Raio de pé maior (ferramenta com ponta arredondada, protuberância bem dimensionada) reduz q_s e Y_S."], doc="Y_S"),
        "Y_beta": dict(titulo="Fator de hélice Y_β", formula=r"Y_\beta = 1 - \varepsilon_\beta\,\frac{\beta}{120}\quad(\varepsilon_\beta \le 1,\ \beta \le 30°)", vars=lambda: [_V(r"\varepsilon_\beta", "", e.epsilon_beta), _V(r"\beta", "", e.beta, "°"), _V(r"Y_\beta", "Resultado", g(f"Y_beta{i}"))], doc="Y_beta"),
        "Y_B": dict(titulo=f"Fator de espessura de aro Y_B ({L})", formula=r"Y_B = 1{,}6\ln\!\left(2{,}242\,\frac{h_t}{s_R}\right)\ (0{,}5 < s_R/h_t < 1{,}2),\qquad Y_B = 1{,}15\ln\!\left(8{,}324\,\frac{m_n}{s_R}\right)\ (\text{interna}, 1{,}75 < s_R/m_n < 3{,}5)",
                    vars=lambda: [_V("s_R", "Espessura do aro", getattr(e, f"s_{suf}"), "mm"), _V("h_t", "Altura do dente", getattr(e, f"h_dente_{suf}"), "mm"), _V("s_R/h_t", "", getattr(e, f"s_{suf}") / getattr(e, f"h_dente_{suf}")), _V("Y_B", "Resultado", g(f"Y_B{i}_{suf}"))], doc="Y_B"),
        "Y_dRelT": dict(titulo=f"Sensibilidade relativa ao entalhe Y_δrelT ({L})", formula=r"Y_{\delta relT} = \frac{1 + \sqrt{\rho'\,\chi^*}}{1 + \sqrt{\rho'\,\chi^*_T}},\qquad \chi^* = \frac{1}{5}\left(1 + 2 q_s\right)", vars=lambda: [_V("q_s", "", getattr(e, f"S_fn_{suf}") / (2 * getattr(e, f"p_f_{suf}")) if getattr(e, f"p_f_{suf}") else None), _V(r"\rho'", "Raio de escorregamento do material", None), _V(r"Y_{\delta relT}", "Resultado", g(f"Y_delta_RefT_{suf}{i}"))], doc="Y_dRelT"),
        "Y_RRelT": dict(titulo=f"Fator de superfície do pé Y_RrelT ({L})", formula=r"Y_{RrelT} = f(R_z\ \text{do pé},\ \text{classe do material})", vars=lambda: [_V("R_z", "Rugosidade do pé", getattr(e, f"Rz_pe_{suf}"), "µm"), _V("Y_{RrelT}", "Resultado", g(f"Y_R_RefT_{suf}{i}"))], doc="Y_RRelT"),
        "Y_X": dict(titulo="Fator de tamanho Y_X", formula=r"Y_X = f(m_n,\ \text{classe})", vars=lambda: [_V("m_n", "", e.m_n, "mm"), _V("Y_X", "Resultado", g(f"Y_X_{suf}{i}"))], doc="Y_X"),
        "eps_alpha": dict(titulo="Grau de recobrimento de perfil ε_α", formula=r"\varepsilon_\alpha = \frac{g_\alpha}{p_{bt}} = \frac{\tfrac12\left(\sqrt{d_{Na1}^2 - d_{b1}^2} \pm \sqrt{d_{Na2}^2 - d_{b2}^2}\right) - a\sin\alpha_{wt}}{\pi m_t \cos\alpha_t}",
                          vars=lambda: [_V("d_{Na1}, d_{Na2}", "Diâmetros úteis de cabeça", f"{e.d_na_pinhao:.3f} / {e.d_na_coroa:.3f}", "mm"), _V("d_{b1}, d_{b2}", "Diâmetros de base", f"{e.db_pinhao:.3f} / {e.db_coroa:.3f}", "mm"), _V("a", "Distância entre centros", e.a, "mm"), _V(r"\alpha_{wt}", "", e.alpha_wt, "°"), _V(r"\varepsilon_\alpha", "Resultado", e.epsilon_alpha)], doc="recobrimento"),
        "x": dict(titulo="Deslocamento de perfil x", formula=r"\Sigma x = \frac{(\operatorname{inv}\alpha_{wt} - \operatorname{inv}\alpha_t)(z_1 + z_2)}{2\tan\alpha_n},\qquad x_2 = \Sigma x - x_1", vars=lambda: [_V(r"\Sigma x", "Soma necessária para a distância entre centros", e.sum_x), _V("x_1", "Pinhão", e.x_pinhao), _V("x_2", "Coroa", e.x_coroa), _V("x_{1,rec}", "Recomendado (método DIN)", e.x_pinhao_rec)], doc="desloc_perfil"),
    }
    if fator in ("Z_D",):
        fator = "Z_B"
    if fator not in tabela:
        d = _doc(fator)
        out.update(titulo=(d or {}).get("titulo", fator), doc=(d or {}).get("markdown"))
        return out
    t = tabela[fator]
    out.update(titulo=t["titulo"], titulo_curto=fator, resumo=t.get("resumo", ""), formula=t.get("formula"))
    try:
        out["variaveis"] = [v for v in t["vars"]() if v is not None]
    except Exception as ex:  # noqa: BLE001
        out["notas"].append(f"(variáveis indisponíveis: {ex})")
    if t.get("resultado"):
        try:
            out["resultado"] = t["resultado"]()
        except Exception:  # noqa: BLE001
            pass
    out["notas"] += t.get("notas", [])
    out["doc"] = D(t.get("doc")) if t.get("doc") else None
    return out
