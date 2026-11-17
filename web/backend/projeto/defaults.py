# -*- coding: utf-8 -*-
"""Vocabulário do modelo de projeto (derivado do metadata) e projetos padrão para a interface.

Um projeto descreve a TRANSMISSÃO (trem de N estágios ou planetário por elementos). O montador (montar.py) traduz cada
malha em um payload de `services.geometria.kwargs_malha`. Para isso, os campos do Engrenamento são divididos em:
  - RODA  : parâmetros com sufixo _pinhao/_coroa no metadata (b, IQ, acabamento, material, ferramenta, corpo, eixo...),
            guardados por roda SEM sufixo (ex.: {"IQ": 6, "di": 0, "material": {"preset": "Material_base"}}).
  - MALHA : parâmetros do par (m_n, Z_pinhao, Z_coroa, a, alpha_n, beta, x_pinhao, tipo, ISO, metodo_x...).
  - OPERACAO / ENTRADA / METODOS : comuns a todo o projeto (vida, temperaturas, lubrificante, seguranças, irregularidades, métodos ISO).
"""
from ..params.metadata import PARAMS, params_for

_GEO = params_for("geometria")

# campos por roda: chave sem sufixo -> (chave_pinhao, chave_coroa)
RODA = {}
for k in _GEO:
    for suf in ("_pinhao", "_coroa"):
        if k.endswith(suf):
            base = k[: -len(suf)]
            RODA.setdefault(base, {})["pinhao" if suf == "_pinhao" else "coroa"] = k
RODA = {b: (v.get("pinhao"), v.get("coroa")) for b, v in RODA.items() if v.get("pinhao") and v.get("coroa")}
# z₁/z₂ e x₁ são da MALHA (z define a relação; x_coroa é derivado), não da roda
RODA.pop("Z", None)
RODA.pop("x", None)
# material/ferramenta são sub-objetos (não estão no metadata de geometria), mas seguem a mesma regra de sufixo
RODA["material"] = ("material_pinhao", "material_coroa")
RODA["ferramenta"] = ("ferramenta_pinhao", "ferramenta_coroa")

ENTRADA = ["irregularidade_motora", "irregularidade_movida", "Ka_imposto"]
OPERACAO = ["Vr", "T_op", "T_Rmd", "T_Cmd", "C_Cdil", "imersao", "S_Hmin", "S_Fmin", "S_Hmax", "S_Fmax", "ISO", "F_B_rolamento", "Proj"]
METODOS = ["metodo_YF", "metodo_YF_interno", "curva_vida", "metodo_x", "M_BS", "Lambda"]
PLANETARIO_KW = ["trans", "N_cp", "Ky", "membro_pinhao", "membro_coroa", "Tipo_planetario", "n_carrier", "n_t", "T", "apelido"]
MALHA = [k for k in _GEO if k not in {p for pair in RODA.values() for p in pair} and k not in ENTRADA + OPERACAO + METODOS + PLANETARIO_KW]
# MALHA: m_n, Z_pinhao, Z_coroa, a, alpha_n, beta, x_pinhao, tipo


def default_roda():
    d = {}
    for base, (kp, _) in RODA.items():
        if kp in PARAMS:
            d[base] = PARAMS[kp]["default"]
    d["material"] = {"preset": "Material_base"}
    d["ferramenta"] = {"preset": "base_ferramenta_pinhao"}
    d["Arranjo"] = 1
    return d


def default_malha(**over):
    d = {k: PARAMS[k]["default"] for k in MALHA}
    d["a"] = None          # None = distância entre centros padrão (sem deslocamento líquido de perfil)
    d.update(over)
    return d


def default_operacao():
    d = {k: PARAMS[k]["default"] for k in OPERACAO if k in PARAMS}
    d["lubrificante"] = {"preset": "base_lubrificante"}
    d["Proj"] = ""
    return d


def default_entrada(n=1450.0, T=100.0):
    d = {k: PARAMS[k]["default"] for k in ENTRADA}
    d.update(n=n, T=T)
    return d


def default_metodos():
    return {k: PARAMS[k]["default"] for k in METODOS}


def default_analise(k=100):
    return {"k": k, "Ck": None, "K_Hbeta_imposto": None}


def estagio_padrao(nome="Estágio 1", z1=20, z2=61, m_n=2.0, b=25.0, interno=False):
    return {
        "nome": nome, "eta": 0.98,
        "malha": default_malha(m_n=m_n, Z_pinhao=z1, Z_coroa=(-abs(z2) if interno else abs(z2)), x_pinhao=0.0, tipo="Otimização"),
        "pinhao": dict(default_roda(), b=b, di=0.0, bs=b, d_sh=0.3 * m_n * z1, L=4 * b, sh=0.0),
        "coroa": dict(default_roda(), b=b, di=0.0, bs=b, d_sh=0.3 * m_n * z1, L=4 * b, sh=0.0, Arranjo=1),
        "analise": default_analise(100),
    }


def projeto_padrao(tipo="trem"):
    p = {"nome": "Novo projeto", "tipo": tipo, "entrada": default_entrada(), "operacao": default_operacao(), "metodos": default_metodos(),
         "estagios": [], "planetario": None}
    if tipo == "trem":
        p["estagios"] = [estagio_padrao("Estágio 1", 20, 61, 2.0, 25.0), estagio_padrao("Estágio 2", 19, 72, 3.0, 35.0)]
    else:
        roda = default_roda
        p["planetario"] = {
            "tipo": "Composto", "N_cp": 3, "Ky": 1.05, "entrada": "sol", "saida": "porta-planetas", "modo": "fixo", "n_livre": 0.0,
            "sol": dict(roda(), z=15, b=26.0, di=0.0, bs=14.0, d_sh=10.5, L=134.0, sh=25.0, Arranjo=2),
            "planeta_maior": dict(roda(), z=48, b=26.0, di=10.0, bs=14.0, d_sh=10.0, L=32.0, sh=4.0, Arranjo=1),
            "planeta_menor": dict(roda(), z=21, b=14.0, di=10.0, bs=18.0, d_sh=10.0, L=30.0, sh=4.0, Arranjo=7),
            "anelar": dict(roda(), z=69, b=14.0, D_ext=114.0, bs=18.0, d_sh=0.0, L=10.0, sh=4.0, Arranjo=1, IQ=8, op_acabamento="Fresamento", Ra_flanco=5.0),
            "malha_ext": default_malha(m_n=1.0, alpha_n=25.0, beta=0.0, x_pinhao=0.15, a=31.166666),
            "malha_int": default_malha(m_n=1.3, alpha_n=25.0, beta=0.0, x_pinhao=0.3),
            "analise_ext": default_analise(100), "analise_int": default_analise(50),
        }
        p["entrada"] = default_entrada(n=13000.0, T=31.0)
        p["entrada"].update(i_alvo=11.5, tol_i=0.5)
        p["entrada"]["irregularidade_motora"] = p["entrada"]["irregularidade_movida"] = "Choque leve"
        p["operacao"].update(Vr=115.0, T_Rmd=80.0, T_op=80.0, S_Hmin=1.1, S_Fmin=1.2, S_Hmax=1.3, S_Fmax=1.4)
    return p
