# -*- coding: utf-8 -*-
"""Sensibilidade: varia um parâmetro de uma malha do projeto em N pontos e devolve S_H, S_F e o fator pedido."""
import copy
import math

from .calcular import calcular_json
from .modelo import migrar_planeta

# parâmetro -> (rótulo, unidade, como aplicar no projeto, faixa relativa ou absoluta)
PARAMS = {
    "m_n":      ("Módulo m_n", "mm", "malha.m_n", ("rel", 0.6, 1.6)),
    "b":        ("Largura b", "mm", "roda.b", ("rel", 0.5, 1.8)),
    "x_pinhao": ("Deslocamento x₁", "", "malha.x_pinhao", ("abs", -0.5, 1.0)),
    "alpha_n":  ("Ângulo de pressão α_n", "°", "malha.alpha_n", ("abs", 14.5, 27.5)),
    "beta":     ("Ângulo de hélice β", "°", "malha.beta", ("abs", 0.0, 30.0)),
    "T":        ("Torque de entrada T", "N·m", "entrada.T", ("rel", 0.3, 2.0)),
    "n":        ("Rotação de entrada n", "rpm", "entrada.n", ("rel", 0.3, 2.5)),
    "IQ":       ("Qualidade ISO (ambas as rodas)", "", "roda.IQ", ("abs", 4, 10)),
    "Z_pinhao": ("Dentes do pinhão z₁ (mesma relação)", "", "malha.Z_pinhao", ("rel", 0.7, 1.5)),
}


def _alvo(proj, malha_idx):
    """Devolve (dict da malha, [dicts das rodas], tipo) para o índice da malha."""
    if proj["tipo"] == "trem":
        est = proj["estagios"][malha_idx]
        return est.setdefault("malha", {}), [est.setdefault("pinhao", {}), est.setdefault("coroa", {})], "trem"
    pl = proj["planetario"]
    maior = pl.setdefault("planeta_maior", {})
    menor = pl.setdefault("planeta_menor", {}) if pl.get("tipo") == "Composto" else maior
    if malha_idx == 0:
        return pl.setdefault("malha_ext", {}), [pl.setdefault("sol", {}), maior], "planetario"
    return pl.setdefault("malha_int", {}), [menor, pl.setdefault("anelar", {})], "planetario"


def _valor_atual(proj, malha_idx, chave, res_base):
    m, rodas, tipo = _alvo(proj, malha_idx)
    v = res_base["malhas"][malha_idx]["geometria"]["vars"] if res_base and res_base.get("malhas") and res_base["malhas"][malha_idx].get("geometria") else {}
    if chave == "m_n": return m.get("m_n", v.get("m_n"))
    if chave == "b": return rodas[0].get("b", v.get("b_pinhao"))
    if chave == "x_pinhao": return m.get("x_pinhao") if m.get("x_pinhao") is not None else v.get("x_pinhao")
    if chave == "alpha_n": return m.get("alpha_n", v.get("alpha_n"))
    if chave == "beta": return m.get("beta", v.get("beta")) or 0.0
    if chave == "T": return proj["entrada"]["T"]
    if chave == "n": return proj["entrada"]["n"]
    if chave == "IQ": return rodas[0].get("IQ", v.get("IQ_pinhao"))
    if chave == "Z_pinhao": return m.get("Z_pinhao", v.get("Z_pinhao"))
    return None


def _aplicar(proj, malha_idx, chave, val):
    m, rodas, tipo = _alvo(proj, malha_idx)
    if chave in ("m_n", "alpha_n", "beta", "x_pinhao"):
        m[chave] = val
        if chave in ("m_n", "alpha_n", "beta") and tipo == "trem":
            m["a"] = None                      # mantém a distância entre centros padrão para o novo módulo/ângulo
        if chave == "beta" and tipo == "planetario":
            m["a"] = None
    elif chave == "b":
        for r in rodas: r["b"] = val
    elif chave == "IQ":
        for r in rodas: r["IQ"] = int(round(val))
    elif chave in ("T", "n"):
        proj["entrada"][chave] = val
    elif chave == "Z_pinhao":
        z1 = int(round(val)); u = m["Z_coroa"] / m["Z_pinhao"]
        if tipo == "trem":
            m["Z_pinhao"] = z1; m["Z_coroa"] = int(round(z1 * u)); m["a"] = None
        else:
            raise ValueError("variação de z no planetário muda as condições de montagem; use a busca de dentes")


def _fator(res, malha_idx, fator, roda):
    m = res["malhas"][malha_idx]
    if not m or m.get("erro") or not m.get("tensoes"):
        return None, None, None
    cards = {(c["fator"], c["roda"]): c["valor"] for c in m["cards"]}
    lado = "coroa" if (roda or "").startswith("c") else "pinhão"
    SH, SF = cards.get(("S_H", lado)), cards.get(("S_F", lado))
    f = None
    if fator in ("S_H", "S_F"):
        f = SH if fator == "S_H" else SF
    else:
        flat = {}
        for s in m["tensoes"]["secoes"]:
            for l in s["linhas"]:
                flat[l["k"]] = l
        key = {"Z_D": "Z_B"}.get(fator, fator)
        l = flat.get(key)
        if l:
            f = (l["pc"][1] if lado == "coroa" else l["pc"][0]) if "pc" in l else l["v"]
        elif fator == "eps_alpha":
            f = m["geometria"]["vars"].get("epsilon_alpha")
        elif fator == "x":
            f = m["geometria"]["vars"].get("x_coroa" if lado == "coroa" else "x_pinhao")
    return f, SH, SF


def sensibilidade(proj, malha_idx, parametro, fator, roda=None, n=13):
    if parametro not in PARAMS:
        raise ValueError(f"parâmetro desconhecido: {parametro}")
    label, unid, _, (modo, lo, hi) = PARAMS[parametro]
    if proj.get("planetario"):
        proj = {**proj, "planetario": migrar_planeta(proj["planetario"])}
    base_res, _, _ = calcular_json(copy.deepcopy(proj))
    atual = _valor_atual(proj, malha_idx, parametro, base_res)
    if atual is None:
        raise ValueError("valor atual indisponível")
    if modo == "rel":
        xs = [atual * (lo + (hi - lo) * k / (n - 1)) for k in range(n)]
    else:
        xs = [lo + (hi - lo) * k / (n - 1) for k in range(n)]
    if parametro in ("IQ", "Z_pinhao"):
        xs = sorted(set(int(round(x)) for x in xs))
    if atual not in xs:
        xs = sorted(xs + [atual])
    out = {"x": [], "series": {"fator": [], "S_H": [], "S_F": []}, "label_x": label, "unidade_x": unid, "atual_x": atual, "atual_y": {}, "minimo": {}, "rotulo_fator": fator, "nota": ""}
    falhas = 0
    for x in xs:
        p = copy.deepcopy(proj)
        try:
            _aplicar(p, malha_idx, parametro, x)
            res, _, _ = calcular_json(p)
            f, SH, SF = _fator(res, malha_idx, fator, roda)
        except Exception:  # noqa: BLE001
            f = SH = SF = None
        if f is None and SH is None:
            falhas += 1
        out["x"].append(x); out["series"]["fator"].append(f); out["series"]["S_H"].append(SH); out["series"]["S_F"].append(SF)
        if x == atual:
            out["atual_y"] = {"fator": f, "S_H": SH, "S_F": SF}
    op = proj.get("operacao", {})
    out["minimo"] = {"S_H": op.get("S_Hmin", 1.0), "S_F": op.get("S_Fmin", 1.2), "fator": None}
    if falhas:
        out["nota"] = f"{falhas} ponto(s) sem solução (geometria inválida nessa faixa)."
    return out
