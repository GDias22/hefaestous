# -*- coding: utf-8 -*-
"""Valida os exemplos do projeto (ISO 6336-30 ex.1 e ex.6, Mazzo, Galle e as 6 planetarias) contra a interface web.

Cada caso e montado como PROJETO do app (dict como o da interface), calculado por `calcular_json`, comparado com
`_revisao/depois/resultados.json` (codigo original corrigido) e, para Norma1/Norma6, com os valores da ISO/TR 6336-30
(dict NORMA de `_revisao/comparar.py`). Em seguida grava um `.fem` por caso em `Exemplos_fem/`, relê cada arquivo com
`fem.ler` e confirma que o recalculo reproduz os mesmos fatores de seguranca.

Os kwargs dos exemplos NAO sao redigitados: sao lidos por `ast` de `_revisao/run_casos.py` (trens) e de
`exemplos_geometria.py` (planetarias) e convertidos para o formato de projeto (assim nao ha erro de transcricao).

Uso (a partir de web/):  python tools/validacao_exemplos.py > ../Exemplos_fem/LEIAME_validacao.md
"""
import ast
import json
import math
import os
import sys

WEB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(WEB)
sys.path.insert(0, WEB)
os.environ["ENGR_SEM_PDF"] = "1"

from backend import fem  # noqa: E402
from backend.projeto.calcular import calcular_json  # noqa: E402
from backend.projeto.defaults import RODA  # noqa: E402

SAIDA = os.path.join(ROOT, "Exemplos_fem")
os.makedirs(SAIDA, exist_ok=True)
REF = json.load(open(os.path.join(ROOT, "_revisao", "depois", "resultados.json"), encoding="utf-8"))


# ------------------------------------------------------------------------------------------------ leitura por ast
def _parse(path):
    return ast.parse(open(path, encoding="utf-8").read())


def _valor(node, nomes):
    """Nó -> valor Python. Name/Attribute de preset -> {"preset": nome}; Name de objeto inline (Galle) -> dict de campos."""
    if isinstance(node, ast.Attribute):
        return {"preset": node.attr}
    if isinstance(node, ast.Name):
        if node.id in nomes:
            return nomes[node.id]
        return {"preset": node.id}
    return ast.literal_eval(node)


def _kw(call, nomes):
    return {k.arg: _valor(k.value, nomes) for k in call.keywords}


def ler_run_casos():
    tree = _parse(os.path.join(ROOT, "_revisao", "run_casos.py"))
    nomes = {}      # objetos inline (Galle_material...)
    for n in tree.body:
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Attribute) and n.value.func.attr in ("Materiais", "Ferramentas", "Lubrificante"):
            stage = {"Materiais": "mat_", "Ferramentas": "fer_", "Lubrificante": "lub_"}[n.value.func.attr]
            campos = {k.arg: ast.literal_eval(k.value) for k in n.value.keywords}
            nomes[n.targets[0].id] = {stage + k: v for k, v in campos.items()}
    casos = {}
    for n in tree.body:
        if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Subscript):
            chave = ast.literal_eval(n.targets[0].slice)
            for c in ast.walk(n.value):
                if isinstance(c, ast.Call) and isinstance(c.func, ast.Name) and c.func.id == "E":
                    casos[chave] = _kw(c, nomes)
    return casos


def ler_exemplos_geometria():
    tree = _parse(os.path.join(ROOT, "exemplos_geometria.py"))
    eng, cin = {}, {}
    for n in tree.body:
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name):
            nome = n.targets[0].id
            if n.value.func.id == "Engrenamento":
                eng[nome] = {k.arg: (None if k.arg in ("n_t", "T", "n_carrier") else _valor(k.value, {})) for k in n.value.keywords}
            elif n.value.func.id == "cinematica_planetaria":
                cin[nome] = {k.arg: ast.literal_eval(k.value) for k in n.value.keywords}
    return eng, cin


def ler_norma():
    tree = _parse(os.path.join(ROOT, "_revisao", "comparar.py"))
    for n in tree.body:
        if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "NORMA":
            return {ast.literal_eval(k): {kw.arg: ast.literal_eval(kw.value) for kw in v.keywords} for k, v in zip(n.value.keys, n.value.values)}
    raise RuntimeError("NORMA nao encontrado")


# ------------------------------------------------------------------------------------------------ conversao kwargs -> projeto
MALHA_KEYS = ["tipo", "m_n", "Z_pinhao", "Z_coroa", "alpha_n", "beta", "x_pinhao", "a"]
OPER_KEYS = ["Vr", "T_op", "T_Rmd", "T_Cmd", "C_Cdil", "imersao", "S_Hmin", "S_Fmin", "S_Hmax", "S_Fmax", "ISO", "F_B_rolamento"]
BASES = [b for b in RODA if b != "membro"]


def roda_de(kw, lado):
    suf = "_pinhao" if lado == "pinhao" else "_coroa"
    return {b: kw[b + suf] for b in BASES if b + suf in kw}


def operacao_de(kw, proj_nome=None):
    op = {k: kw[k] for k in OPER_KEYS}
    op["Proj"] = kw.get("Proj") or ""
    op["lubrificante"] = kw["lubrificante"]
    return op


def metodos_de(kw):
    return {"metodo_YF": kw.get("metodo_YF", "B"), "metodo_YF_interno": kw.get("metodo_YF_interno", "cortador"), "curva_vida": kw.get("curva_vida", "ISO"),
            "metodo_x": kw["metodo_x"], "M_BS": kw.get("M_BS"), "Lambda": kw.get("Lambda")}


def projeto_trem(nome, kw):
    entrada = {"n": kw["n_t"], "T": kw["T"], "irregularidade_motora": kw["irregularidade_motora"], "irregularidade_movida": kw["irregularidade_movida"]}
    if kw.get("Ka_imposto") is not None:
        entrada["Ka_imposto"] = kw["Ka_imposto"]
    est = {"nome": kw["apelido"], "eta": 0.98, "malha": {k: kw[k] for k in MALHA_KEYS if k in kw},
           "pinhao": roda_de(kw, "pinhao"), "coroa": roda_de(kw, "coroa"), "analise": {"k": 100}}
    return {"nome": nome, "tipo": "trem", "entrada": entrada, "operacao": operacao_de(kw), "metodos": metodos_de(kw), "estagios": [est]}


def projeto_planetario(nome, e, i, c):
    """e/i: kwargs da malha externa/interna; c: kwargs de cinematica_planetaria (n_sol, T_sol, N_cp, Ky, Tipo, Ring)."""
    assert c["Ring"] == "Fixo" and c["Tipo"] == "Composto"
    for k in OPER_KEYS + ["irregularidade_motora", "irregularidade_movida", "metodo_x", "N_cp", "Ky", "Proj"]:
        assert e.get(k) == i.get(k), f"{nome}: {k} difere entre malha externa e interna"
    sol = dict(roda_de(e, "pinhao"), z=e["Z_pinhao"])
    maior = dict(roda_de(e, "coroa"), z=e["Z_coroa"])
    menor = dict(roda_de(i, "pinhao"), z=i["Z_pinhao"])
    anel = roda_de(i, "coroa")
    D_ext = -anel.pop("di")
    anel.update(z=abs(i["Z_coroa"]), D_ext=D_ext)
    return {"nome": nome, "tipo": "planetario",
            "entrada": {"n": c["n_sol"], "T": c["T_sol"], "irregularidade_motora": e["irregularidade_motora"], "irregularidade_movida": e["irregularidade_movida"]},
            "operacao": operacao_de(e), "metodos": metodos_de(e),
            "planetario": {"tipo": c["Tipo"], "N_cp": c["N_cp"], "Ky": c["Ky"], "entrada": "sol", "saida": "porta-planetas",
                           "sol": sol, "planeta_maior": maior, "planeta_menor": menor, "anelar": anel,
                           "malha_ext": {k: e[k] for k in MALHA_KEYS}, "malha_int": {k: i[k] for k in MALHA_KEYS},
                           "analise_ext": {"k": 100}, "analise_int": {"k": 50}}}


# ------------------------------------------------------------------------------------------------ extracao (copia de run_casos.extrai)
def num(v):
    try:
        import numpy as np
        if isinstance(v, np.generic):
            v = v.item()
    except Exception:  # noqa: BLE001
        pass
    if isinstance(v, bool):
        return v
    if isinstance(v, (int, float)):
        return float(v)
    return v


def extrai(an, i, par):
    g = lambda n: getattr(an, n, None)  # noqa: E731
    d = {}
    d['Ka'] = par.Ka; d['Kv'] = g(f'Kv{i}'); d['K_Hbeta'] = g(f'K_Hbeta{i}'); d['K_Fbeta'] = g(f'K_Fbeta{i}')
    d['K_Halpha'] = g(f'K_Halpha{i}'); d['K_Falpha'] = g(f'K_Falpha{i}')
    d['Z_H'] = g(f'Z_H{i}'); d['Z_E'] = g(f'Z_E{i}'); d['Z_epsilon'] = g(f'Z_epsilon{i}'); d['Z_beta'] = g(f'Z_beta{i}')
    d['Z_L'] = g(f'Z_L{i}'); d['Z_V'] = g(f'Z_V{i}'); d['Z_R'] = g(f'Z_R{i}')
    d['Z_W_p'] = g(f'Z_W{i}_pinhao'); d['Z_W_c'] = g(f'Z_W{i}_coroa'); d['Z_X_p'] = g(f'Z_X_pinhao{i}'); d['Z_X_c'] = g(f'Z_X_coroa{i}')
    d['Z_B'] = g(f'Z_B{i}'); d['Z_D'] = g(f'Z_D{i}')
    d['Z_NT_p'] = g(f'Z_NT_pinhao{i}'); d['Z_NT_c'] = g(f'Z_NT_coroa{i}'); d['Z_GT_p'] = g(f'Z_GT_pinhao{i}'); d['Z_GT_c'] = g(f'Z_GT_coroa{i}')
    d['Y_F_p'] = par.Yf_pinhao; d['Y_F_c'] = par.Yf_coroa; d['Y_S_p'] = g(f'Y_S_pinhao{i}'); d['Y_S_c'] = g(f'Y_S_coroa{i}'); d['Y_beta'] = g(f'Y_beta{i}')
    d['Y_B_p'] = g(f'Y_B{i}_pinhao'); d['Y_B_c'] = g(f'Y_B{i}_coroa'); d['Y_d_p'] = g(f'Y_delta_RefT_pinhao{i}'); d['Y_d_c'] = g(f'Y_delta_RefT_coroa{i}')
    d['Y_R_p'] = g(f'Y_R_RefT_pinhao{i}'); d['Y_R_c'] = g(f'Y_R_RefT_coroa{i}'); d['Y_X_p'] = g(f'Y_X_pinhao{i}'); d['Y_X_c'] = g(f'Y_X_coroa{i}')
    d['Y_NT_p'] = g(f'Y_NT_pinhao{i}'); d['Y_NT_c'] = g(f'Y_NT_coroa{i}')
    d['sigma_H0'] = g(f'sigma_H0{i}'); d['sigma_H_p'] = g(f'sigma_Hpinhao{i}'); d['sigma_H_c'] = g(f'sigma_Hcoroa{i}')
    d['sigma_F_p'] = g(f'sigma_Fpinhao{i}'); d['sigma_F_c'] = g(f'sigma_Fcoroa{i}')
    d['sigma_HP_p'] = g(f'sigma_HP_pinhao{i}'); d['sigma_HP_c'] = g(f'sigma_HP_coroa{i}'); d['sigma_FP_p'] = g(f'sigma_FP_pinhao{i}'); d['sigma_FP_c'] = g(f'sigma_FP_coroa{i}')
    d['S_H_p'] = g(f'S_Hpinhao{i}'); d['S_H_c'] = g(f'S_Hcoroa{i}'); d['S_F_p'] = g(f'S_Fpinhao{i}'); d['S_F_c'] = g(f'S_Fcoroa{i}')
    d['n_e'] = g(f'n_e{i}'); d['zona'] = g(f'zona{i}')
    d['T_HP_p'] = g(f'T_HP1{i}'); d['T_FP_p'] = g(f'T_FP1{i}'); d['T_FP_c'] = g(f'T_FP2{i}')
    d['n_t'] = par.n_t; d['n_rel'] = getattr(par, 'n_rel', None); d['v_t'] = par.v_t; d['Ft'] = par.Ft; d['eps_a'] = par.epsilon_alpha; d['eps_b'] = par.epsilon_beta
    d['s_coroa'] = par.s_coroa; d['s_pinhao'] = par.s_pinhao; d['jn7_max'] = par.jn7_max; d['k_W_c'] = par.k_coroa; d['Zmin_p'] = par.Z_min_pinhao
    d['S_na_c'] = par.S_na_coroa; d['N_L_p'] = getattr(par, 'N_L_pinhao', None); d['N_L_c'] = getattr(par, 'N_L_coroa', None)
    return {k: num(v) for k, v in d.items()}


def comparar(calc, ref, chaves=None, tol=1e-6):
    """Devolve (n_comparados, max_dev_rel, chave_do_max, [(chave, calc, ref, dev)] com dev > tol)."""
    n, mx, kmx, bad = 0, 0.0, None, []
    for k in (chaves or ref.keys()):
        if k in ("avisos",) or k not in ref or ref[k] is None:
            continue
        a, b = calc.get(k), ref[k]
        if isinstance(b, str):
            n += 1
            if a != b:
                bad.append((k, a, b, float("inf")))
            continue
        n += 1
        if a is None:
            bad.append((k, a, b, float("inf"))); continue
        dev = abs(a - b) / max(abs(b), 1e-12) if abs(b) > 1e-12 else abs(a - b)
        if dev > mx:
            mx, kmx = dev, k
        if dev > tol:
            bad.append((k, a, b, dev))
    return n, mx, kmx, bad


# ------------------------------------------------------------------------------------------------ checagens fisicas
def checar_malha(rotulo, e, an, i, res_malha, minimos):
    out = []
    g = lambda n: getattr(an, n, None)  # noqa: E731
    for c in res_malha.get("cards") or []:
        if c["valor"] is not None and c["status"] not in ("ok",):
            out.append(f"{rotulo}: {c['fator']} {c['roda']} = {c['valor']:.4f} (min {c['minimo']}) status={c['status']}")
        if c["fator"] == "S_F" and c["valor"] is not None and c["valor"] > 15:
            out.append(f"{rotulo}: S_F {c['roda']} = {c['valor']:.2f} muito alto (>15)")
    if g(f"Kv{i}") is not None and g(f"Kv{i}") < 1:
        out.append(f"{rotulo}: Kv = {g(f'Kv{i}'):.4f} < 1")
    if e.epsilon_alpha < 1.2:
        out.append(f"{rotulo}: eps_alpha = {e.epsilon_alpha:.3f} < 1.2")
    if e.epsilon_alpha > 2.2:
        out.append(f"{rotulo}: eps_alpha = {e.epsilon_alpha:.3f} > 2.2 (atipico)")
    if e.jn7_min < 0 or e.jn1_min < 0:
        out.append(f"{rotulo}: jogo negativo jn7_min={e.jn7_min:.4f} jn1_min={e.jn1_min:.4f}")
    for lado in ("pinhao", "coroa"):
        da, df = abs(getattr(e, f"d_a_{lado}")), abs(getattr(e, f"d_f_{lado}"))
        interna = (lado == "coroa" and e.Z_coroa < 0)
        if (not interna and df >= da) or (interna and df <= da):
            out.append(f"{rotulo}: d_f/d_a incoerente na {lado} (|d_a|={da:.3f}, |d_f|={df:.3f}, interna={interna})")
        s, smin = getattr(e, f"s_{lado}"), getattr(e, f"s_min_{lado}")
        if s is not None and smin is not None and abs(s) < abs(smin):
            out.append(f"{rotulo}: espessura de aro s_{lado} = {s:.3f} < s_min = {smin:.3f}")
        sna = getattr(e, f"S_na_{lado}")
        if sna is not None and abs(sna) < 0.2 * e.m_n:
            out.append(f"{rotulo}: espessura de cabeca s_na_{lado} = {sna:.3f} mm < 0.2 m_n ({0.2 * e.m_n:.3f}) (dente pontiagudo)")
    if abs(abs(e.a_conferencia) - abs(e.a)) > 1e-3:
        out.append(f"{rotulo}: a_conferencia = {e.a_conferencia:.5f} difere de a = {e.a:.5f}")
    for a in res_malha.get("avisos") or []:
        if a["nivel"] == "aviso":
            out.append(f"{rotulo}: AVISO app: {a['texto'][:230]}")
    return out


def checar_planetario(res, objs, an, proj):
    out = []
    t = res["transmissao"]; cin = t["cinematica"]
    pl = proj["planetario"]
    Zs, Zbp, Zsp, Zr = pl["sol"]["z"], pl["planeta_maior"]["z"], pl["planeta_menor"]["z"], pl["anelar"]["z"]
    willis = (Zsp * Zs + Zbp * Zr) / (Zs * Zsp)
    if abs(t["i_total"] - willis) > 1e-9:
        out.append(f"i_total do app = {t['i_total']:.6f} difere de Willis = {willis:.6f}")
    e1, e2 = objs
    if abs(abs(e1.a) - abs(e2.a)) > 1e-6:
        out.append(f"|a_ext| = {abs(e1.a):.6f} != |a_int| = {abs(e2.a):.6f} (dif {abs(abs(e1.a)-abs(e2.a)):.2e} mm)")
    if abs(e1.T - pl_T(proj)) > 1e-9:
        out.append(f"T malha externa = {e1.T} != T de entrada {pl_T(proj)}")
    if abs(e2.T - e1.T * Zbp / Zs) > 1e-6:
        out.append(f"T malha interna = {e2.T:.4f} != T_ext*Zbp/Zs = {e1.T * Zbp / Zs:.4f}")
    n_in = proj["entrada"]["n"]
    if abs(cin["n_c"] - n_in / willis) > 1e-6:
        out.append(f"n_c = {cin['n_c']:.4f} != n_in/i = {n_in / willis:.4f}")
    if abs(cin["T_carrier"] - proj["entrada"]["T"] * willis) > 1e-6:
        out.append(f"T_carrier = {cin['T_carrier']:.4f} != T_in*i = {proj['entrada']['T'] * willis:.4f} (eta=1)")
    if abs(cin["P_in_kW"] - cin["P_out_kW"]) > 1e-6:
        out.append(f"P_in = {cin['P_in_kW']:.4f} kW != P_out = {cin['P_out_kW']:.4f} kW")
    # Ft e definido pelo diametro de referencia d (ISO 6336-1): Ft = 2000*T*Ky/(N_cp*d1) -> consistencia
    for nome, e in (("ext", e1), ("int", e2)):
        r = e.Ft * e.d_pinhao * pl["N_cp"] / (2000 * e.T) / pl["Ky"]
        if abs(r - 1) > 1e-6:
            out.append(f"{nome}: Ft*d1*N_cp/(2000*T*Ky) = {r:.6f} (esperado 1)")
        out.append(f"INFO {nome}: Ft = {e.Ft:.2f} N; n_rel = {e.n_rel:.2f} rpm; v_t = {e.v_t:.3f} m/s; sum_x = {e.sum_x:.4f}; a = {e.a:.6f}; d_w/d (pinhao) = {e.dw_pinhao / e.d_pinhao:.4f}; eps_a = {e.epsilon_alpha:.3f}; jn7_min = {e.jn7_min:.4f}")
    # equilibrio de momentos do planeta nos circulos de trabalho (informativo: o app usa Ft em d, nao em d_w)
    eq = e1.Ft * e1.dw_coroa / (e2.Ft * e2.dw_pinhao)
    out.append(f"INFO equilibrio do planeta com raios de trabalho: Ft_ext*dw_maior/(Ft_int*dw_menor) = {eq:.4f} (Ft calculado em d; =1 so se d_w=d nas duas malhas)")
    return out


def pl_T(proj):
    return proj["entrada"]["T"]


# ------------------------------------------------------------------------------------------------ casos
def montar_casos():
    run = ler_run_casos()
    eng, cin = ler_exemplos_geometria()
    casos = []   # (arquivo, ref_keys, norma_key, projeto)
    nomes_trem = {
        "Norma1": ("Validacao_ISO6336-30_Ex1", "Validação ISO 6336-30 Ex. 1 (par externo, z=17/103, m_n=8)"),
        "Norma6": ("Validacao_ISO6336-30_Ex6", "Validação ISO 6336-30 Ex. 6 (par interno, z=15/-99, m_n=12, K_A imposto 1,3)"),
        "Mazzo": ("Validacao_Mazzo", "Validação Mazzo (par helicoidal externo z=25/61, m_n=3)"),
        "Galle": ("Validacao_Galle", "Validação Galle (par helicoidal z=15/25, m_n=3, 20MnCr5)"),
    }
    for k, (arq, nome) in nomes_trem.items():
        casos.append((arq, [k], k if k in ("Norma1", "Norma6") else None, projeto_trem(nome, run[k])))
    plan = [("Pla56_antiga", "Dim_56_ext_25_25_10_13_mat_Plat_antiga", "Dim_56_int_25_25_10_13_mat_Plat_antiga", "cin_Dim_56_25_25_10_13_mat_Plat_antiga", "Planetário composto 56 (25/25/10/13), material da planetária antiga"),
            ("Pla56_ref", "Dim_56_ext_25_25_10_13_mat_ref", "Dim_56_int_25_25_10_13_mat_ref", "cin_Dim_56_25_25_10_13_mat_ref", "Planetário composto 56 (25/25/10/13), material de referência"),
            ("Pla41_antiga", "Dim_41_ext_25_25_10_14_mat_Plat_antiga", "Dim_41_int_25_25_10_14_mat_Plat_antiga", "cin_Dim_41_25_25_10_14_mat_Plat_antiga", "Planetário composto 41 (25/25/10/14), material da planetária antiga"),
            ("Pla41_ref", "Dim_41_ext_25_25_10_14_mat_ref", "Dim_41_int_25_25_10_14_mat_ref", "cin_Dim_41_25_25_10_14_mat_ref", "Planetário composto 41 (25/25/10/14), material de referência"),
            ("Pla50_antiga", "Dim_50_ext_20_25_08_12_mat_Plat_antiga", "Dim_50_int_20_25_08_12_mat_Plat_antiga", "cin_Dim_50_20_25_08_12_mat_Plat_antiga", "Planetário composto 50 (20/25/08/12), material da planetária antiga"),
            ("Pla50_ref", "Dim_50_ext_20_25_08_12_mat_ref", "Dim_50_int_20_25_08_12_mat_ref", "cin_Dim_50_20_25_08_12_mat_ref", "Planetário composto 50 (20/25/08/12), material de referência")]
    for k, e, i, c, nome in plan:
        casos.append(("Planetario_" + k, [k + "_ext", k + "_int"], None, projeto_planetario(nome, eng[e], eng[i], cin[c])))
    return casos


def cards_de(res):
    return {(m["indice"], c["fator"], c["roda"]): c["valor"] for m in res["malhas"] for c in m.get("cards") or []}


def main():
    NORMA = ler_norma()
    L = []
    P = L.append
    P("# Validação dos exemplos contra a interface web\n")
    P("Gerado por `web/tools/validacao_exemplos.py`. Cada exemplo é montado como projeto do app, calculado por `calcular_json` e comparado com "
      "`_revisao/depois/resultados.json` (código original corrigido) e, para os exemplos 1 e 6, com a ISO/TR 6336-30 (`NORMA` de `_revisao/comparar.py`).\n")
    resumo_rows, achados, norma_blocos, fem_rows = [], [], [], []
    ring_extra = ""
    for arq, refkeys, normakey, proj in montar_casos():
        res, objs, ans = calcular_json(proj)
        rotulo = arq
        erros = res.get("erros") or {}
        linhas_desvio, n_tot, mx_tot, kmx_tot = [], 0, 0.0, None
        sh = [c["valor"] for m in res["malhas"] for c in m.get("cards") or [] if c["fator"] == "S_H" and c["valor"] is not None]
        sf = [c["valor"] for m in res["malhas"] for c in m.get("cards") or [] if c["fator"] == "S_F" and c["valor"] is not None]
        if not objs or any(o is None for o in objs):
            resumo_rows.append((arq, 0, None, None, "ERRO: " + json.dumps(erros, ensure_ascii=False)[:200], None, None))
            achados.append(f"[{arq}] cálculo falhou: {erros}")
            continue
        for idx, rk in enumerate(refkeys):
            e = objs[idx]
            a = ans[0] if len(ans) == 1 and len(objs) == 2 else ans[idx]
            i_idx = idx + 1 if len(objs) == 2 else 1
            calc = extrai(a, i_idx, e)
            n, mx, kmx, bad = comparar(calc, REF[rk])
            n_tot += n
            if mx > mx_tot:
                mx_tot, kmx_tot = mx, f"{rk}:{kmx}"
            linhas_desvio += [f"{rk}:{k}" + f" (app {x!r} × orig {y!r})" for k, x, y, d in bad]
            if normakey:
                nb = ["| Fator | Norma | App | Desvio rel. |", "|---|---|---|---|"]
                for k, v in NORMA[normakey].items():
                    x = calc.get(k)
                    nb.append(f"| {k} | {v} | {x:.4f} | {100 * (x - v) / v:+.2f}% |" if x is not None else f"| {k} | {v} | - | - |")
                norma_blocos.append((arq, nb))
        if normakey == "Norma6":
            from backend.services.tensoes import calcular_tensoes
            an_r = calcular_tensoes(objs[0], None, {"an_apelido": "x", "k1": 100, "Ring": "Rotativo"})
            n2, mx2, k2, bad2 = comparar(extrai(an_r, 1, objs[0]), REF["Norma6"])
            ring_extra = (f"Com Ring='Fixo' (o que o app usa em qualquer trem: `calcular._params_analise(..., 'Fixo')`) o Ex. 6 desvia do original em {len(linhas_desvio)} fatores (maior {mx_tot:.2e}); "
                          f"com Ring='Rotativo' (usado em `_revisao/run_casos.py` para o Ex. 6) calculando as mesmas geometrias: {n2} fatores comparados, maior desvio {mx2:.2e}, {len(bad2)} fatores acima de 1e-6.\n")
        # checagens
        ach = []
        for idx, e in enumerate(objs):
            a = ans[0] if len(ans) == 1 and len(objs) == 2 else ans[idx]
            i_idx = idx + 1 if len(objs) == 2 else 1
            nome = (["ext", "int"][idx] if len(objs) == 2 else "malha")
            ach += checar_malha(f"{arq}/{nome}", e, a, i_idx, res["malhas"][idx], None)
        if len(objs) == 2:
            ach += [f"{arq}: {x}" for x in checar_planetario(res, objs, ans[0], proj)]
        if erros:
            ach.append(f"{arq}: erros por campo = {erros}")
        achados += ach
        resumo_rows.append((arq, n_tot, mx_tot, kmx_tot, linhas_desvio, min(sh) if sh else None, min(sf) if sf else None))
        # .fem
        arq_fem = os.path.join(SAIDA, arq + ".fem")
        conteudo = fem.empacotar(proj)
        with open(arq_fem, "w", encoding="utf-8") as f:
            json.dump(conteudo, f, indent=2, ensure_ascii=False)
        lido = fem.ler(json.load(open(arq_fem, encoding="utf-8")))
        res2, _, _ = calcular_json(lido["projeto"])
        c1, c2 = cards_de(res), cards_de(res2)
        dif = max((abs(c1[k] - c2[k]) for k in c1 if c1[k] is not None), default=0.0) if c1.keys() == c2.keys() else float("nan")
        fem_rows.append((arq + ".fem", len(c1), dif, lido["nome"], res2["ok"]))
    if ring_extra:
        P("## Ex. 6: efeito do campo Ring (o app fixa Ring='Fixo' em trens)\n")
        P(ring_extra)
    P("## Resumo por caso (app × original corrigido)\n")
    P("| Caso | Fatores comparados | Maior desvio relativo | Fator do máx. | Fatores com desvio > 1e-6 | S_H mín | S_F mín |")
    P("|---|---|---|---|---|---|---|")
    for arq, n, mx, kmx, desv, shm, sfm in resumo_rows:
        d = ("nenhum" if not desv else "; ".join(desv)) if isinstance(desv, list) else desv
        P(f"| {arq} | {n} | {mx:.3e} | {kmx} | {d} | {shm:.4f} | {sfm:.4f} |" if mx is not None else f"| {arq} | 0 | - | - | {d} | - | - |")
    for arq, nb in norma_blocos:
        P(f"\n## {arq}: app × ISO/TR 6336-30 (valores da norma arredondados a 2 casas)\n")
        L.extend(nb)
    P("\n## Checagens físicas / avisos / incoerências (automáticas)\n")
    for a in achados:
        P(f"- {a}")
    P("\n## Arquivos .fem: releitura com `fem.ler` e recálculo\n")
    P("| Arquivo | Nº de cartões de segurança | Maior |ΔS| após reler | Nome no arquivo | ok |")
    P("|---|---|---|---|---|")
    for r in fem_rows:
        P(f"| {r[0]} | {r[1]} | {r[2]:.3e} | {r[3]} | {r[4]} |")
    print("\n".join(L))


if __name__ == "__main__":
    main()
