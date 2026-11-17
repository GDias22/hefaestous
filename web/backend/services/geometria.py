# -*- coding: utf-8 -*-
"""Serviço da etapa B: monta um Engrenamento a partir do payload da interface e resume os resultados."""
import copy
import inspect

from ..bootstrap import G
from ..params.metadata import PARAMS, params_for, strip_prefix
from .serialize import num, vars_numericos

SUBOBJ = {
    "material_pinhao": ("material", G.Materiais),
    "material_coroa": ("material", G.Materiais),
    "ferramenta_pinhao": ("ferramenta", G.Ferramentas),
    "ferramenta_coroa": ("ferramenta", G.Ferramentas),
    "lubrificante": ("lubrificante", G.Lubrificante),
}


# ------------------------------------------------------------------------------------------------ presets
def listar_presets():
    """Materiais, ferramentas e lubrificantes já definidos no módulo de geometria."""
    out = {"material": {}, "ferramenta": {}, "lubrificante": {}}
    for nome, obj in vars(G).items():
        if isinstance(obj, G.Materiais):
            out["material"][nome] = _preset_dict("material", obj)
        elif isinstance(obj, G.Ferramentas):
            out["ferramenta"][nome] = _preset_dict("ferramenta", obj)
        elif isinstance(obj, G.Lubrificante):
            out["lubrificante"][nome] = _preset_dict("lubrificante", obj)
    return out


def _preset_dict(stage, obj):
    d = {}
    for key, meta in params_for(stage).items():
        attr = strip_prefix(stage, {key: None})
        attr = next(iter(attr))
        if hasattr(obj, attr):
            d[key] = num(getattr(obj, attr))
    d["_apelido"] = getattr(obj, "apelido", "")
    return d


def construir_subobjeto(stage, payload):
    """payload: {"preset": "Nome"} ou dict de campos (com ou sem prefixo mat_/fer_/lub_)."""
    cls = {"material": G.Materiais, "ferramenta": G.Ferramentas, "lubrificante": G.Lubrificante}[stage]
    if payload is None:
        raise ValueError(f"{stage}: informe um preset ou os campos.")
    if isinstance(payload, str):
        payload = {"preset": payload}
    if "preset" in payload and payload["preset"]:
        obj = getattr(G, payload["preset"], None)
        if not isinstance(obj, cls):
            raise ValueError(f"Preset '{payload['preset']}' não encontrado para {stage}.")
        return copy.copy(obj)
    campos = {k: v for k, v in payload.items() if k != "preset"}
    campos = strip_prefix(stage, campos)
    if stage == "material":
        for k in ("dureza_superficial", "dureza_nucleo"):
            if isinstance(campos.get(k), str):
                import re
                m = re.search(r"[-+]?\d+(?:[.,]\d+)?", campos[k])
                if not m:
                    raise ValueError(f"'{k}' deve ser um número em HRC (ex.: 60).")
                campos[k] = float(m.group().replace(",", "."))
    kwargs = {}
    sig = inspect.signature(cls.__init__)
    for nome in sig.parameters:
        if nome == "self":
            continue
        if nome in campos:
            kwargs[nome] = _coerce(stage, nome, campos[nome])
        else:
            meta = PARAMS.get({"material": "mat_", "ferramenta": "fer_", "lubrificante": "lub_"}[stage] + nome)
            kwargs[nome] = meta["default"] if meta else None
    return cls(**kwargs)


def _coerce(stage, nome, valor):
    pref = {"material": "mat_", "ferramenta": "fer_", "lubrificante": "lub_", "geometria": "", "tensoes": "", "cinematica": ""}[stage]
    meta = PARAMS.get(pref + nome)
    if meta is None or valor is None:
        return valor
    if valor == "" and meta.get("nullable"):
        return None
    t = meta["type"]
    try:
        if t == "int":
            return int(round(float(valor)))
        if t == "number":
            return float(valor)
        if t == "choice":
            ch = meta.get("choices") or []
            if ch and isinstance(ch[0], int):
                return int(valor)
            return str(valor)
        if t == "bool":
            return bool(valor)
    except (TypeError, ValueError):
        raise ValueError(f"Valor inválido para {meta['label']}: {valor!r}")
    return valor


# ------------------------------------------------------------------------------------------------ malha
def kwargs_malha(payload):
    """Normaliza o payload da malha em kwargs completos para Engrenamento (defaults do metadata)."""
    kw = {}
    for key, meta in params_for("geometria").items():
        if key in payload:
            kw[key] = _coerce("geometria", key, payload[key])
        else:
            kw[key] = meta["default"]
    for nome, (stage, _) in SUBOBJ.items():
        kw[nome] = construir_subobjeto(stage, payload.get(nome))
    # consistências simples
    if kw["trans"] == "Simples":
        kw["N_cp"] = None if kw["N_cp"] in (None, 0) else kw["N_cp"]
        kw["Ky"] = None
        kw["membro_pinhao"] = kw["membro_coroa"] = None
        kw["n_carrier"] = None
    if kw.get("imersao") == "nenhuma":
        kw["imersao"] = None
    _validar(kw)
    return kw


class ErroEntrada(ValueError):
    """Erro de entrada com atribuição por campo: .campos = {nome_kwarg_ou_'': mensagem}."""

    def __init__(self, campos):
        self.campos = dict(campos)
        super().__init__(" ".join(self.campos.values()))


def _validar(kw):
    """Erros de entrada com mensagem clara (antes que virem 'math domain error' dentro do cálculo)."""
    erros = {}

    def add(campo, msg):
        erros[campo] = (erros[campo] + " " + msg) if campo in erros else msg

    for k in ("m_n", "Z_pinhao", "Z_coroa", "a", "alpha_n", "n_t", "T"):
        if kw.get(k) is None:
            add(k, f"'{PARAMS[k]['label']}' é obrigatório.")
    if erros:
        raise ErroEntrada(erros)
    if kw["Z_pinhao"] <= 0:
        add("Z_pinhao", "O número de dentes do pinhão deve ser positivo (a convenção de sinal negativo vale só para a coroa interna).")
    if kw["Z_coroa"] == 0:
        add("Z_coroa", "z₂ não pode ser zero.")
    if kw["a"] == 0:
        add("a", "A distância entre centros não pode ser zero.")
    if kw["m_n"] <= 0:
        add("m_n", "O módulo deve ser positivo.")
    if kw["Z_coroa"] < 0 and abs(kw["Z_coroa"]) <= kw["Z_pinhao"]:
        add("Z_coroa", "Na malha interna |z₂| deve ser maior que z₁.")
    elif kw["Z_coroa"] != 0 and kw["a"] != 0 and (kw["Z_coroa"] < 0) != (kw["a"] < 0):
        add("a", "Sinais inconsistentes: para malha interna (anelar) z₂ E a devem ser negativos; para externa, ambos positivos.")
    if kw["tipo"] == "Otimização" and kw.get("x_pinhao") is None:
        add("x_pinhao", "No modo 'Otimização' informe o deslocamento de perfil do pinhão x₁ (ou use o modo 'Inicial').")
    if kw["tipo"] == "Inicial":
        if kw["metodo_x"] == "ISO" and kw.get("Lambda") is None:
            add("Lambda", "Método ISO de repartição de Σx exige λ (0,5 a 0,75).")
        if kw["metodo_x"] == "BS" and not kw.get("M_BS"):
            add("M_BS", "Método BS de repartição de Σx exige o critério G, F ou V.")
    if kw["trans"] == "Planetário" and kw.get("n_carrier") is not None and abs(kw["n_t"] - kw["n_carrier"]) < 1e-9:
        add("n_t", "Rotação do pinhão igual à do porta-planetas: rotação relativa nula.")
    for lado in ("pinhao", "coroa"):
        if kw.get(f"Arranjo_{lado}") is None and kw.get(f"k_linha_{lado}") is None:
            add(f"Arranjo_{lado}", f"Informe o arranjo físico ou a constante K' para {'o pinhão' if lado == 'pinhao' else 'a coroa'}.")
    if erros:
        raise ErroEntrada(erros)


def calcular_malha(payload):
    kw = kwargs_malha(payload)
    try:
        eng = G.Engrenamento(**kw)
    except ErroEntrada:
        raise
    except Exception as ex:  # noqa: BLE001  (math domain error, solver sem convergência…) -> mensagem por campo, em português
        from .diagnostico import diagnosticar
        raise ErroEntrada(diagnosticar(kw, ex)) from ex
    # resultados fisicamente impossíveis que o cálculo de tensões não consegue tratar
    prob = {}
    for lado, nome in (("pinhao", "pinhão"), ("coroa", "coroa")):
        if getattr(eng, f"Yf_{lado}") <= 0 or getattr(eng, f"h_fe_{lado}") <= 0 or getattr(eng, f"S_fn_{lado}") <= 0:
            rk, rkmax = getattr(eng, f"rk_{lado}"), getattr(eng, f"rk_{lado}_max")
            if rk > rkmax:
                prob[f"ferramenta_{lado}"] = f"Raio de ponta da ferramenta ρ_aP0 = {rk:.3f} mm acima do máximo {rkmax:.3f} mm para {nome} (ferramenta de outro módulo?): pé do dente inválido (Y_F = {getattr(eng, f'Yf_{lado}'):.3f})."
            else:
                prob[f"x_{lado}" if lado == "pinhao" else "Z_coroa"] = f"Geometria do pé do dente inválida para {nome} (Y_F = {getattr(eng, f'Yf_{lado}'):.3f}, h_Fe = {getattr(eng, f'h_fe_{lado}'):.3f} mm): revise x, z e a ferramenta."
    if eng.epsilon_alpha <= 1.0:
        from .diagnostico import faixa_x1, _f
        fx = faixa_x1(kw)
        prob["a"] = (f"Grau de recobrimento de perfil ε_α = {eng.epsilon_alpha:.3f} ≤ 1: quando um par de dentes sai de contato o seguinte ainda não entrou, "
                     f"então a malha não transmite movimento contínuo. Causas comuns: distância entre centros grande demais (Σx alto), poucos dentes ou ângulo de pressão alto. "
                     f"Diminua a distância entre centros (ou deixe-a vazia para usar a padrão), reduza α_n ou aumente os números de dentes."
                     + (f" Para esta distância entre centros, x₁ entre {_f(fx[0])} e {_f(fx[1])} é geometricamente possível, mas ε_α ≥ 1,0 também depende de a." if fx else ""))
    if prob:
        raise ErroEntrada(prob)
    return eng


# ------------------------------------------------------------------------------------------------ resumo
def _pc(e, nome, nd=4):
    """Linha pinhão/coroa de um atributo com sufixo _pinhao/_coroa."""
    return [num(getattr(e, f"{nome}_pinhao", None)), num(getattr(e, f"{nome}_coroa", None))]


def resumo_malha(e):
    """Resultados organizados por seção. Cada linha: {k, label, unit, v (escalar) | pc [pinhão, coroa]}."""
    S = []

    def sec(titulo, linhas):
        S.append({"titulo": titulo, "linhas": [l for l in linhas if l is not None]})

    def v(k, label, unit=None, nd=4):
        val = num(getattr(e, k, None))
        return {"k": k, "label": label, "unit": unit, "v": val}

    def pc(k, label, unit=None):
        return {"k": k, "label": label, "unit": unit, "pc": _pc(e, k)}

    sec("Identificação", [
        v("apelido", "Apelido"), v("Proj", "Engenheiro"), v("tipo", "Modo de cálculo"), v("trans", "Transmissão"),
        v("N_cp", "Número de planetas"), v("membro_pinhao", "Membro do pinhão"), v("membro_coroa", "Membro da coroa"),
        v("Tipo_planetario", "Tipo de planetário"), v("metodo_YF", "Método Y_F"), v("curva_vida", "Curva de vida"),
    ])
    sec("Geometria básica", [
        v("m_n", "Módulo normal m_n", "mm"), v("m_t", "Módulo transversal m_t", "mm"), v("m_wn", "Módulo transversal de trabalho m_wt", "mm"),
        v("alpha_n", "Ângulo de pressão normal α_n", "°"), v("alpha_t", "Ângulo de pressão transversal α_t", "°"),
        v("alpha_wt", "Ângulo de pressão de trabalho α_wt", "°"), v("alpha_wn", "Ângulo de pressão de trabalho normal α_wn", "°"),
        v("beta", "Ângulo de hélice β", "°"), v("beta_b", "Ângulo de hélice de base β_b", "°"),
        v("u", "Razão de engrenamento u"), v("a_standart", "Distância entre centros padrão a_d", "mm"),
        v("a", "Distância entre centros imposta a", "mm"), v("a_conferencia", "Distância entre centros calculada", "mm"),
        v("Aa_s", "Tolerância superior de a", "mm"), v("Aa_i", "Tolerância inferior de a", "mm"),
        pc("Z", "Número de dentes z"), pc("zn", "Dentes virtuais z_n"), pc("b", "Largura b", "mm"), v("b", "Extensão de contato", "mm"),
        v("sum_x", "Soma dos deslocamentos Σx"), pc("x", "Deslocamento de perfil x"),
        {"k": "x_rec", "label": "x recomendado pelo método", "unit": None, "pc": [num(getattr(e, "x_pinhao_rec", None)), num(getattr(e, "x_coroa_rec", None))]},
        v("K", "Coeficiente de encurtamento de cabeça k"), v("rel_aux", "(x₁+x₂)/(z₁+z₂)"),
    ])
    sec("Diâmetros", [
        pc("d", "Diâmetro de referência d", "mm"), pc("dw", "Diâmetro primitivo d_w", "mm"), pc("db", "Diâmetro de base d_b", "mm"),
        pc("d_a", "Diâmetro de cabeça d_a", "mm"), pc("A_da_s", "Tol. superior d_a", "mm"), pc("A_da_i", "Tol. inferior d_a", "mm"),
        pc("d_f", "Diâmetro de pé d_f", "mm"), pc("A_df_s", "Tol. superior d_f", "mm"), pc("A_df_i", "Tol. inferior d_f", "mm"),
        pc("d_na", "Diâmetro útil de cabeça d_Na", "mm"), pc("d_nf", "Diâmetro útil de pé d_Nf", "mm"), pc("d_nk", "Diâmetro de início do chanfro d_Nk", "mm"),
        pc("h_a", "Adendo h_a", "mm"), pc("h_f", "Dedendo h_f", "mm"), pc("h_dente", "Altura do dente h", "mm"),
        pc("Cs", "Folga no pé c", "mm"), pc("Css", "Folga no pé superior", "mm"), pc("Csi", "Folga no pé inferior", "mm"),
        pc("di", "Diâmetro de aro/alma d_i", "mm"), pc("s", "Espessura de aro s_R", "mm"), pc("s_min", "Espessura de aro mínima", "mm"),
    ])
    sec("Passos e recobrimento", [
        v("pc_n", "Passo normal p_n", "mm"), pc("pc_t", "Passo transversal p_t", "mm"), v("pb", "Passo de base p_b", "mm"),
        v("p_x", "Passo axial p_x", "mm"), v("epsilon_alpha", "Grau de recobrimento de perfil ε_α"),
        v("epsilon_beta", "Grau de recobrimento de hélice ε_β"), v("epsilon_total", "Grau de recobrimento total ε_γ"),
        v("v_ga", "Velocidade de escorregamento (cabeça) v_ga", "m/s"), v("v_gf", "Velocidade de escorregamento (pé) v_gf", "m/s"),
        pc("Z_min", "z mínimo sem undercut"),
    ])
    sec("Espessura do dente (DIN 3967)", [
        pc("S_n", "Espessura normal nominal s_n", "mm"), pc("S_ns", "Espessura normal superior", "mm"), pc("S_ni", "Espessura normal inferior", "mm"),
        pc("A_sne", "Afastamento A_sne", "mm"), pc("T_sn", "Tolerância T_sn", "mm"),
        pc("S_t", "Espessura transversal s_t", "mm"), pc("T_n", "Vão normal e_n", "mm"),
        pc("S_na", "Espessura de cabeça s_na", "mm"), pc("s_nk", "Espessura de cabeça com chanfro s_nk", "mm"),
        pc("phi_na", "Ângulo do chanfro (normal)", "°"), pc("C_a", "Comprimento do chanfro", "mm"),
    ])
    sec("Controle dimensional", [
        pc("k", "Dentes medidos k (W_k)"), pc("Wk_s", "Medida W_k superior", "mm"), pc("Wk_i", "Medida W_k inferior", "mm"),
        pc("Dm", "Diâmetro do pino/esfera D_M", "mm"), pc("Md_s", "Medida M superior", "mm"), pc("Md_i", "Medida M inferior", "mm"),
        pc("d_m_s", "Diâmetro de tangência superior", "mm"), pc("d_m_i", "Diâmetro de tangência inferior", "mm"),
    ])
    sec("Ferramenta, pé do dente e fator de forma", [
        pc("rk", "Raio de ponta da ferramenta ρ_aP0", "mm"),
        {"k": "rk_max", "label": "Raio de ponta máximo da ferramenta", "unit": "mm", "pc": [num(getattr(e, "rk_pinhao_max", None)), num(getattr(e, "rk_coroa_max", None))]},
        pc("pr", "Protuberância pr₀", "mm"), pc("SM", "Sobremetal de acabamento", "mm"),
        pc("Yf", "Fator de forma Y_F"), pc("S_fn", "Espessura crítica s_Fn", "mm"), pc("h_fe", "Braço de alavanca h_Fe", "mm"), pc("p_f", "Raio de pé ρ_F", "mm"),
    ])
    sec("Carga, rotações e forças", [
        v("T", "Torque na malha T", "N·m"), v("n_t", "Rotação do pinhão n₁", "rpm"), v("n_carrier", "Rotação do porta-planetas", "rpm"),
        v("n_rel", "Rotação relativa ao porta-planetas", "rpm"), pc("contatos", "Engrenamentos por volta"), pc("Y_M", "Fator de carga alternada Y_M"),
        v("T_out", "Torque de saída", "N·m"), v("n_t_out", "Rotação de saída", "rpm"), v("potencia", "Potência de entrada", "kW"),
        v("potencia_malha", "Potência de engrenamento", "kW"), v("v_t", "Velocidade tangencial v_t", "m/s"),
        v("Ka", "Fator de aplicação K_A"), v("Ky", "Fator entre planetas K_γ"),
        v("Ft", "Força tangencial F_t", "N"), v("F_rd", "Força radial F_r", "N"), v("F_ax", "Força axial F_a", "N"), v("F", "Força normal F_n", "N"),
        v("w", "Carga específica F_t·K_A/b", "N/mm"),
    ])
    sec("Microgeometria (ISO 1328)", [
        pc("Fr", "Desvio de concentricidade F_r", "mm"), pc("fp", "Desvio de passo individual f_p", "mm"), pc("Fp", "Erro total de passo F_p", "mm"),
        pc("fpe", "Desvio de passo de base f_pe", "mm"), pc("F_beta", "Desvio total de hélice F_β", "mm"), pc("f_Hbeta", "Desvio angular de hélice f_Hβ", "mm"),
        pc("F_f", "Desvio total de perfil F_α", "mm"), pc("f_f", "Desvio de forma de perfil f_fα", "mm"), pc("f_Halpha", "Desvio angular de perfil f_Hα", "mm"),
    ])
    sec("Jogo entre flancos (backlash)", [
        v("jn1_min", "Jogo teórico mínimo", "mm"), v("jn1_max", "Jogo teórico máximo", "mm"),
        v("jn7_min", "Jogo final mínimo (com temperatura)", "mm"), v("jn7_max", "Jogo final máximo (com temperatura)", "mm"),
    ])
    sec("Lubrificação", [
        v("V_li", "Volume de óleo mínimo", "L"), v("V_ls", "Volume de óleo máximo", "L"),
        v("P_ri", "Profundidade de imersão mínima", "mm"), v("P_rs", "Profundidade de imersão máxima", "mm"),
    ])
    return S


def avisos_malha(e):
    out = []
    for a in e.AVISOS:
        if not a:
            continue
        t = str(a).strip()
        nivel = "ok" if ("Não há interferência" in t or "É possivel" in t or "possível" in t) and "AVISO" not in t else "aviso"
        out.append({"nivel": nivel, "texto": t})
    return out


def dados_malha(e):
    """Pacote completo da malha: resumo por seção, avisos e todos os escalares (para JSON/XLSX)."""
    return {"apelido": e.apelido, "interna": bool(e.Z_coroa < 0), "secoes": resumo_malha(e),
            "avisos": avisos_malha(e), "vars": vars_numericos(e),
            "material_pinhao": vars_numericos(e.material_pinhao), "material_coroa": vars_numericos(e.material_coroa),
            "ferramenta_pinhao": vars_numericos(e.ferramenta_pinhao), "ferramenta_coroa": vars_numericos(e.ferramenta_coroa),
            "lubrificante": vars_numericos(e.lubrificante)}
