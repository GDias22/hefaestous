# -*- coding: utf-8 -*-
"""Serviço da etapa C: Analise_de_tensao sobre 1 ou 2 malhas já calculadas e resumo dos fatores ISO 6336."""
import threading

from ..bootstrap import A, Eq
from .serialize import num, vars_numericos

_kv_lock = threading.Lock()


class _ComoParSimples:
    """Proxy de um Engrenamento planetário que se apresenta como par 'Simples' só para o cálculo de K_v
    (o modelo de inércias acopladas do planetário em Eq.kv exige as DUAS malhas)."""
    trans = "Simples"

    def __init__(self, e):
        object.__setattr__(self, "_e", e)

    def __getattr__(self, n):
        return getattr(self._e, n)


def calcular_tensoes(malha1, malha2, params):
    """params: dict com an_apelido, k1, k2, Ck1, Ck2, Tipo_planetario_an, Ring, K_Hbeta_imposto1/2."""
    tipo = params.get("Tipo_planetario_an") or getattr(malha1, "Tipo_planetario", None) or "Composto"
    ring = params.get("Ring") or "Fixo"
    kw = dict(
        apelido=params.get("an_apelido") or "Análise",
        Proj=params.get("Proj") or getattr(malha1, "Proj", None),
        Par_engrenado_1=malha1,
        Par_engrenado_2=malha2,
        k1=params.get("k1") if params.get("k1") not in (None, "") else 100,
        k2=params.get("k2") if params.get("k2") not in (None, "") else (50 if malha2 is not None else None),
        Ck1=_none(params.get("Ck1")),
        Ck2=_none(params.get("Ck2")),
        Tipo_planetario=tipo,
        Ring=ring,
        K_Hbeta_imposto1=_none(params.get("K_Hbeta_imposto1")),
        K_Hbeta_imposto2=_none(params.get("K_Hbeta_imposto2")),
    )
    # cada execução recomeça dos avisos da geometria (Analise_de_tensao anexa avisos ao Engrenamento; sem isto acumulam)
    for mlh in (malha1, malha2):
        if mlh is not None:
            if not hasattr(mlh, "_avisos_geometria"):
                mlh._avisos_geometria = list(mlh.AVISOS)
            mlh.AVISOS = list(mlh._avisos_geometria)
    if malha2 is not None and malha1.trans == "Planetário":
        if malha1.Z_coroa < 0 or malha2.Z_coroa > 0:
            raise ValueError("Para o modelo de K_v do planetário a malha 1 deve ser a externa (sol × planeta) e a malha 2 a interna (planeta × anelar). Inverta a ordem de seleção.")
    if malha2 is None and malha1.trans == "Planetário":
        # uma malha só: K_v pelo modelo de par simples com a rotação relativa ao porta-planetas (ISO 6336-1 §6.1.2)
        aviso = ("AVISO : K_v calculado pelo modelo de par simples (inércias do pinhão e da coroa, rotação relativa ao "
                 "porta-planetas). Para o modelo acoplado do planetário selecione as duas malhas (externa e interna). \n")
        with _kv_lock:
            orig = A.Eq_tensao.kv
            A.Eq_tensao.kv = lambda e1, e2, *a: orig(_ComoParSimples(e1), e2, *a)
            try:
                an = A.Analise_de_tensao(**kw)
            finally:
                A.Eq_tensao.kv = orig
        if aviso not in malha1.AVISOS:
            malha1.AVISOS.append(aviso)
        return an
    return A.Analise_de_tensao(**kw)


def _none(v):
    return None if v in (None, "") else float(v)


def _g(an, nome):
    return num(getattr(an, nome, None))


def fatores_malha(an, i, par):
    """Fatores, tensões e seguranças da malha i (1 ou 2) organizados por seção."""
    g = lambda n: _g(an, n)  # noqa: E731
    sec = []

    def add(titulo, linhas):
        sec.append({"titulo": titulo, "linhas": [l for l in linhas if l is not None]})

    def v(k, label, val, unit=None):
        return {"k": k, "label": label, "unit": unit, "v": num(val)}

    def pc(k, label, vp, vc, unit=None):
        return {"k": k, "label": label, "unit": unit, "pc": [num(vp), num(vc)]}

    add("Fatores gerais de influência (ISO 6336-1)", [
        v("Ka", "Fator de aplicação K_A", par.Ka), v("Ky", "Fator entre planetas K_γ", par.Ky if par.trans == "Planetário" else 1.0),
        v("Kv", "Fator dinâmico K_v", g(f"Kv{i}")), v("n_e", "Rotação de ressonância n_E1", g(f"n_e{i}"), "rpm"), v("zona", "Zona de K_v", g(f"zona{i}")),
        v("K_Hbeta", "Distribuição longitudinal K_Hβ", g(f"K_Hbeta{i}")), v("K_Fbeta", "Distribuição longitudinal K_Fβ", g(f"K_Fbeta{i}")),
        v("K_Halpha", "Distribuição transversal K_Hα", g(f"K_Halpha{i}")), v("K_Falpha", "Distribuição transversal K_Fα", g(f"K_Falpha{i}")),
        v("c_linha", "Rigidez de um par c'", g(f"c_linha{i}"), "N/(mm·µm)"), v("c_gamma_alpha", "Rigidez de malha c_γα", g(f"c_gamma_alpha{i}"), "N/(mm·µm)"),
        v("c_gamma_beta", "Rigidez de malha c_γβ", g(f"c_gamma_beta{i}"), "N/(mm·µm)"), v("b_cal", "Largura de cálculo", g(f"b_cal{i}"), "mm"),
    ])
    add("Fatores de pitting (ISO 6336-2)", [
        v("Z_H", "Fator de zona Z_H", g(f"Z_H{i}")), v("Z_E", "Fator de elasticidade Z_E", g(f"Z_E{i}"), "√MPa"),
        v("Z_epsilon", "Fator de recobrimento Z_ε", g(f"Z_epsilon{i}")), v("Z_beta", "Fator de hélice Z_β", g(f"Z_beta{i}")),
        v("Z_B", "Fator de contato individual Z_B", g(f"Z_B{i}")), v("Z_D", "Fator de contato individual Z_D", g(f"Z_D{i}")),
        v("Z_L", "Fator de lubrificação Z_L", g(f"Z_L{i}")), v("Z_V", "Fator de velocidade Z_V", g(f"Z_V{i}")), v("Z_R", "Fator de rugosidade Z_R", g(f"Z_R{i}")),
        pc("Z_W", "Fator de endurecimento Z_W", g(f"Z_W{i}_pinhao"), g(f"Z_W{i}_coroa")), pc("Z_X", "Fator de tamanho Z_X", g(f"Z_X_pinhao{i}"), g(f"Z_X_coroa{i}")),
        pc("Z_NT", "Fator de vida Z_NT", g(f"Z_NT_pinhao{i}"), g(f"Z_NT_coroa{i}")), pc("Z_GT", "Fator de vida (com pites) Z_GT", g(f"Z_GT_pinhao{i}"), g(f"Z_GT_coroa{i}")),
    ])
    add("Fatores de flexão (ISO 6336-3)", [
        pc("Y_F", "Fator de forma Y_F", par.Yf_pinhao, par.Yf_coroa), pc("Y_S", "Fator de concentração Y_S", g(f"Y_S_pinhao{i}"), g(f"Y_S_coroa{i}")),
        v("Y_beta", "Fator de hélice Y_β", g(f"Y_beta{i}")), pc("Y_B", "Fator de espessura de aro Y_B", g(f"Y_B{i}_pinhao"), g(f"Y_B{i}_coroa")),
        pc("Y_M", "Fator de carga alternada Y_M", par.Y_M_pinhao, par.Y_M_coroa),
        pc("Y_dRelT", "Sensibilidade ao entalhe Y_δrelT", g(f"Y_delta_RefT_pinhao{i}"), g(f"Y_delta_RefT_coroa{i}")),
        pc("Y_RRelT", "Fator de superfície Y_RrelT", g(f"Y_R_RefT_pinhao{i}"), g(f"Y_R_RefT_coroa{i}")),
        pc("Y_X", "Fator de tamanho Y_X", g(f"Y_X_pinhao{i}"), g(f"Y_X_coroa{i}")), pc("Y_NT", "Fator de vida Y_NT", g(f"Y_NT_pinhao{i}"), g(f"Y_NT_coroa{i}")),
    ])
    add("Tensões e seguranças", [
        v("sigma_H0", "Tensão de contato nominal σ_H0", g(f"sigma_H0{i}"), "MPa"),
        pc("sigma_H", "Tensão de contato σ_H", g(f"sigma_Hpinhao{i}"), g(f"sigma_Hcoroa{i}"), "MPa"),
        pc("sigma_HP", "Tensão de contato admissível σ_HP", g(f"sigma_HP_pinhao{i}"), g(f"sigma_HP_coroa{i}"), "MPa"),
        pc("S_H", "Segurança contra pitting S_H", g(f"S_Hpinhao{i}"), g(f"S_Hcoroa{i}")),
        pc("S_G", "Segurança com pites admissíveis S_G", g(f"S_Gpinhao{i}"), g(f"S_Gcoroa{i}")),
        pc("sigma_F0", "Tensão de flexão nominal σ_F0", g(f"sigma_F01{i}"), g(f"sigma_F02{i}"), "MPa"),
        pc("sigma_F", "Tensão de flexão σ_F", g(f"sigma_Fpinhao{i}"), g(f"sigma_Fcoroa{i}"), "MPa"),
        pc("sigma_FP", "Tensão de flexão admissível σ_FP", g(f"sigma_FP_pinhao{i}"), g(f"sigma_FP_coroa{i}"), "MPa"),
        pc("S_F", "Segurança contra fratura S_F", g(f"S_Fpinhao{i}"), g(f"S_Fcoroa{i}")),
        v("S_Hmin", "S_H mínimo requerido", par.S_Hmin), v("S_Fmin", "S_F mínimo requerido", par.S_Fmin),
    ])
    add("Vida e capacidade de carga", [
        pc("VH", "Vida até pitting (S_H = 1)", g(f"VH_pinhao{i}"), g(f"VH_coroa{i}"), "h"),
        pc("VF", "Vida até fratura (S_F = 1)", g(f"VF_pinhao{i}"), g(f"VF_coroa{i}"), "h"),
        v("Vr", "Vida requerida", par.Vr, "h"),
        pc("T_HP", "Torque admissível (pitting)", g(f"T_HP1{i}"), g(f"T_HP2{i}"), "N·m"),
        pc("T_FP", "Torque admissível (flexão)", g(f"T_FP1{i}"), g(f"T_FP2{i}"), "N·m"),
        pc("P_HP", "Potência admissível (pitting)", g(f"P_HP1{i}"), g(f"P_HP2{i}"), "kW"),
        pc("P_FP", "Potência admissível (flexão)", g(f"P_FP1{i}"), g(f"P_FP2{i}"), "kW"),
        v("eficiencia", "Eficiência estimada da malha", g(f"eficencia{i}")),
    ])
    return sec


def cards_seguranca(an, i, par):
    """Cards S_H/S_F por roda com semáforo."""
    def card(nome, roda, val, minimo):
        val = num(val)
        if val is None:
            status = "na"
        elif val < minimo:
            status = "ruim"
        elif val < minimo * 1.1:
            status = "atencao"
        else:
            status = "ok"
        return {"fator": nome, "roda": roda, "valor": val, "minimo": minimo, "status": status}
    return [
        card("S_H", "pinhão", getattr(an, f"S_Hpinhao{i}", None), par.S_Hmin),
        card("S_H", "coroa", getattr(an, f"S_Hcoroa{i}", None), par.S_Hmin),
        card("S_F", "pinhão", getattr(an, f"S_Fpinhao{i}", None), par.S_Fmin),
        card("S_F", "coroa", getattr(an, f"S_Fcoroa{i}", None), par.S_Fmin),
    ]


def dados_tensoes(an, malhas):
    out = {"apelido": an.apelido, "malhas": [], "vars": vars_numericos(an)}
    for i, par in enumerate(malhas, start=1):
        if par is None:
            continue
        out["malhas"].append({
            "indice": i, "apelido": par.apelido,
            "cards": cards_seguranca(an, i, par),
            "secoes": fatores_malha(an, i, par),
            # só os avisos acrescentados pela análise de tensões (os de geometria já aparecem na malha)
            "avisos": [{"nivel": "aviso", "texto": str(a).strip()} for a in par.AVISOS[len(getattr(par, "_avisos_geometria", [])):] if a and "AVISO" in str(a)],
        })
    return out
