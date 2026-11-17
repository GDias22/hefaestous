# -*- coding: utf-8 -*-
"""Projeto -> payloads de malha (kwargs de Engrenamento via services.geometria.kwargs_malha).

Trem: estágio i recebe n/T do estágio i-1 (n_out = n_in/u ; T_out = T_in·u·η). Planetário: elementos -> malha externa
(sol × planeta) e interna (planeta × anelar), com cinemática pelo membro fixo (services.cinematica.cinematica_membro_fixo).
Cada payload carrega `_origem`: lista de (caminho_no_projeto, chave_kwarg) para mapear erros de volta aos campos da UI."""
import math

from ..bootstrap import G, Eq
from ..params.metadata import PARAMS
from ..services.cinematica import cinematica_membro_fixo, cinematica_diferencial, MEMBROS
from .defaults import RODA, ENTRADA, OPERACAO, METODOS, MALHA, default_roda, default_malha, default_operacao, default_metodos
from .modelo import Projeto
from . import layout as lay


def _com(roda, ov, key):
    """Roda (dict) com as sobreposições do layout de eixos/mancais, quando ativo."""
    o = (ov or {}).get(key)
    return {**(roda or {}), **o} if o else (roda or {})


def _roda_kwargs(roda, lado, origem, caminho):
    """Campos de uma roda (dict sem sufixo) -> kwargs com sufixo _pinhao/_coroa."""
    kw = {}
    base = default_roda(); base.update(roda or {})
    for b, (kp, kc) in RODA.items():
        if b in base:
            k = kp if lado == "pinhao" else kc
            kw[k] = base[b]
            origem[k] = f"{caminho}.{b}"
    return kw


def _a_padrao(m_n, z1, z2, beta):
    return m_n * (z1 + z2) / (2 * math.cos(math.radians(beta or 0.0)))


def payload_malha(malha, pinhao, coroa, entrada, operacao, metodos, n_t, T, apelido, caminho, extra=None):
    """Monta um payload de malha. `caminho` é o prefixo no projeto (ex.: 'estagios[0]')."""
    origem = {}
    kw = {}
    m = default_malha(); m.update(malha or {})
    for k in MALHA:
        if k in m:
            kw[k] = m[k]; origem[k] = f"{caminho}.malha.{k}"
    z1, z2 = int(kw["Z_pinhao"]), int(kw["Z_coroa"])
    if kw.get("a") in (None, ""):
        kw["a"] = _a_padrao(float(kw["m_n"]), z1, z2, float(kw.get("beta") or 0.0))   # já carrega o sinal de z1+z2
    else:
        kw["a"] = -abs(float(kw["a"])) if z2 < 0 else abs(float(kw["a"]))             # o sinal segue z₂ (convenção DIN)
    kw.update(_roda_kwargs(pinhao, "pinhao", origem, f"{caminho}.pinhao"))
    kw.update(_roda_kwargs(coroa, "coroa", origem, f"{caminho}.coroa"))
    op = default_operacao(); op.update(operacao or {})
    for k in OPERACAO:
        if k in op:
            kw[k] = op[k]; origem[k] = f"operacao.{k}"
    kw["lubrificante"] = op.get("lubrificante") or {"preset": "base_lubrificante"}; origem["lubrificante"] = "operacao.lubrificante"
    met = default_metodos(); met.update(metodos or {})
    for k in METODOS:
        kw[k] = met[k]; origem[k] = f"metodos.{k}"
    for k in ENTRADA:
        if k in entrada:
            kw[k] = entrada[k]; origem[k] = f"entrada.{k}"
    kw["n_t"] = n_t; kw["T"] = T; kw["apelido"] = apelido
    origem["n_t"] = "entrada.n"; origem["T"] = "entrada.T"
    kw["trans"] = "Simples"
    if extra:
        kw.update(extra)
    kw["_origem"] = origem
    return kw


def montar(proj: Projeto):
    """Devolve dict: malhas (lista de payloads), eixos (tabela n/T/P por eixo), cinematica (planetário), meta."""
    if proj.tipo == "trem":
        return _montar_trem(proj)
    return _montar_planetario(proj)


def _montar_trem(proj):
    entrada = proj.entrada.model_dump()
    n, T = float(entrada["n"]), float(entrada["T"])
    P_in = abs(T * n) * 2 * math.pi / 60000
    eixos = [{"nome": "Entrada", "n": n, "T": T, "P_kW": P_in}]
    malhas = []
    i_total = 1.0
    ov = lay.overrides(proj)
    for idx, est in enumerate(proj.estagios):
        m = default_malha(); m.update(est.malha or {})
        z1, z2 = int(m["Z_pinhao"]), int(m["Z_coroa"])
        u = z2 / z1
        pl = payload_malha(est.malha, _com(est.pinhao, ov, f"estagio:{idx}:pinhao"), _com(est.coroa, ov, f"estagio:{idx}:coroa"), entrada, proj.operacao, proj.metodos, n, T,
                           est.nome or f"Estágio {idx + 1}", f"estagios[{idx}]")
        pl["_estagio"] = idx; pl["_analise"] = est.analise.model_dump()
        malhas.append(pl)
        n_out = n / u                      # interna: u < 0 -> inverte o sentido
        T_out = T * abs(u) * float(est.eta)
        i_total *= u
        eixos.append({"nome": f"Saída do {est.nome or f'estágio {idx + 1}'}", "n": n_out, "T": T_out, "P_kW": abs(T_out * n_out) * 2 * math.pi / 60000,
                      "i_estagio": u, "eta": est.eta})
        n, T = n_out, T_out
    return {"malhas": malhas, "eixos": eixos, "i_total": i_total, "eta_total": math.prod([e.eta for e in proj.estagios]) if proj.estagios else 1.0,
            "cinematica": None, "tipo": "trem"}


def _montar_planetario(proj):
    pl = proj.planetario
    if pl is None:
        raise ValueError("Projeto planetário sem dados de planetário.")
    entrada = proj.entrada.model_dump()
    n_in, T_in = float(entrada["n"]), float(entrada["T"])
    tipo = pl.tipo
    ov = lay.overrides(proj)
    sol, maior, an = _com(dict(pl.sol), ov, "sol"), _com(dict(pl.planeta_maior), ov, "planeta_maior"), dict(pl.anelar)
    menor = _com(dict(pl.planeta_menor), ov, "planeta_menor") if tipo == "Composto" else dict(maior)    # Simples: o mesmo planeta nas duas malhas
    Zs = int(sol.get("z") or 15)
    Zbp = int(maior.get("z") or 48)
    Zsp = int(menor.get("z") or Zbp) if tipo == "Composto" else Zbp
    Zr = abs(int(an.get("z") or 69))
    if pl.modo == "diferencial":
        livre = next(m for m in MEMBROS.values() if m not in (pl.entrada, pl.saida))
        cin = cinematica_diferencial(Zs, Zbp, Zsp, Zr, n_in, T_in, pl.entrada, pl.saida, livre, pl.n_livre, pl.N_cp, tipo, pl.Ky)
    else:
        cin = cinematica_membro_fixo(Zs, Zbp, Zsp, Zr, n_in, T_in, pl.entrada, pl.saida, pl.N_cp, tipo, pl.Ky)
        cin["modo"] = "fixo"; cin["ring"] = "Fixo" if cin["membro_fixo"] == "anelar" else "Rotativo"
    # malha externa: sol (pinhão) × planeta maior (coroa)
    m_ext = default_malha(); m_ext.update(pl.malha_ext or {}); m_ext.update(Z_pinhao=Zs, Z_coroa=Zbp)
    pla_ext = {k: v for k, v in maior.items() if k != "z"}
    pla_int = {k: v for k, v in menor.items() if k != "z"}
    ext = payload_malha(m_ext, {k: v for k, v in sol.items() if k != "z"}, pla_ext, entrada, proj.operacao, proj.metodos,
                        cin["n_sol"], cin["T_malha_ext"], "Malha externa (sol × planeta)", "planetario",
                        extra=dict(trans="Planetário", N_cp=pl.N_cp, Ky=pl.Ky, membro_pinhao="sol", membro_coroa="planeta",
                                   Tipo_planetario=tipo, n_carrier=cin["n_c"]))
    ext["_origem"].update({k: "planetario.malha_ext." + k for k in MALHA}); ext["_origem"]["Z_pinhao"] = "planetario.sol.z"; ext["_origem"]["Z_coroa"] = "planetario.planeta_maior.z"
    for k in list(ext["_origem"]):
        if k.endswith("_pinhao") and k not in ("Z_pinhao", "x_pinhao"):
            ext["_origem"][k] = "planetario.sol." + k[:-7]
        elif k.endswith("_coroa") and k != "Z_coroa":
            ext["_origem"][k] = "planetario.planeta_maior." + k[:-6]
    ext["_estagio"] = 0; ext["_analise"] = pl.analise_ext.model_dump()
    # malha interna: planeta menor (pinhão) × anelar (coroa)
    m_int = default_malha(); m_int.update(pl.malha_int or {}); m_int.update(Z_pinhao=Zsp, Z_coroa=-Zr)
    if m_int.get("a") in (None, ""):
        m_int["a"] = -abs(float(ext["a"]))          # mesmo centro do planeta: |a_int| = |a_ext|
    an_roda = {k: v for k, v in an.items() if k not in ("z", "D_ext")}
    if an.get("D_ext"):
        an_roda["di"] = -abs(float(an["D_ext"]))
    inte = payload_malha(m_int, pla_int, an_roda, entrada, proj.operacao, proj.metodos,
                         cin["n_pla"], cin["T_malha_int"], "Malha interna (planeta × anelar)", "planetario",
                         extra=dict(trans="Planetário", N_cp=pl.N_cp, Ky=pl.Ky, membro_pinhao="planeta", membro_coroa="anelar",
                                    Tipo_planetario=tipo, n_carrier=cin["n_c"]))
    inte["_origem"].update({k: "planetario.malha_int." + k for k in MALHA}); inte["_origem"]["Z_pinhao"] = "planetario.planeta_menor.z" if tipo == "Composto" else "planetario.planeta_maior.z"; inte["_origem"]["Z_coroa"] = "planetario.anelar.z"
    for k in list(inte["_origem"]):
        if k.endswith("_pinhao") and k not in ("Z_pinhao", "x_pinhao"):
            inte["_origem"][k] = "planetario.planeta_menor." + k[:-7] if tipo == "Composto" else "planetario.planeta_maior." + k[:-7]
        elif k.endswith("_coroa") and k != "Z_coroa":
            inte["_origem"][k] = "planetario.anelar." + ("D_ext" if k == "di_coroa" else k[:-6])
    inte["_estagio"] = 1; inte["_analise"] = pl.analise_int.model_dump()
    eixos = [{"nome": "Entrada (" + cin["entrada"] + ")", "n": n_in, "T": T_in, "P_kW": cin["P_in_kW"]},
             {"nome": "Saída (" + cin["saida"] + ")", "n": cin["n_membros"][cin["saida"]], "T": cin["T_membros"][cin["saida"]], "P_kW": cin["P_out_kW"], "i_estagio": cin["i"]},
             ({"nome": "Livre (" + cin["membro_livre"] + ") — rotação imposta", "n": cin["n_membros"][cin["membro_livre"]], "T": cin["T_membros"][cin["membro_livre"]], "P_kW": cin["P_livre_kW"]}
              if cin.get("modo") == "diferencial" else
              {"nome": "Fixo (" + cin["membro_fixo"] + ") — reação", "n": 0.0, "T": cin["T_membros"][cin["membro_fixo"]], "P_kW": 0.0})]
    return {"malhas": [ext, inte], "eixos": eixos, "i_total": cin["i"], "eta_total": 1.0, "cinematica": cin, "tipo": "planetario",
            "elementos": {"sol": {"z": Zs}, "planeta_maior": {"z": Zbp}, "planeta_menor": {"z": Zsp}, "anelar": {"z": Zr}, "N_cp": pl.N_cp}}
