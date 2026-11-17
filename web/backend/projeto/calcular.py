# -*- coding: utf-8 -*-
"""Calcula um Projeto completo: geometria + tensões por malha, resumo da transmissão, erros por campo."""
import traceback

from ..services.geometria import calcular_malha, dados_malha, ErroEntrada
from ..services.tensoes import calcular_tensoes, dados_tensoes, cards_seguranca
from ..services.serialize import to_jsonable, num
from .modelo import Projeto
from .montar import montar
from . import layout as _layout


def _params_analise(an, idx, ring):
    return {"an_apelido": "Análise", "k1": an.get("k"), "Ck1": an.get("Ck"), "K_Hbeta_imposto1": an.get("K_Hbeta_imposto"), "Ring": ring}


def calcular_projeto(proj: Projeto, com_tensoes=True):
    """Devolve dict JSON: {ok, erros:{caminho: msg}, transmissao, malhas:[{geometria, tensoes, cards, avisos}], objetos (não serializado)}."""
    erros = {}
    try:
        mont = montar(proj)
    except ErroEntrada as ex:
        return {"ok": False, "erros": {k or "": v for k, v in ex.campos.items()}, "malhas": [], "transmissao": None}
    except ValueError as ex:
        return {"ok": False, "erros": {"": str(ex)}, "malhas": [], "transmissao": None}
    objetos, saida = [], []
    for pl in mont["malhas"]:
        origem = pl.pop("_origem"); idx = pl.pop("_estagio"); analise = pl.pop("_analise")
        try:
            e = calcular_malha(pl)
        except ErroEntrada as ex:
            for k, msg in ex.campos.items():
                erros[origem.get(k, f"estagios[{idx}].malha.{k}" if mont["tipo"] == "trem" else "planetario")] = msg
            campos = {origem.get(k, f"estagios[{idx}].malha.{k}" if mont["tipo"] == "trem" else "planetario"): msg for k, msg in ex.campos.items()}
            objetos.append(None); saida.append({"indice": idx + 1, "estagio": idx, "apelido": pl.get("apelido"), "erro": str(ex), "erro_campos": campos}); continue
        except Exception as ex:  # noqa: BLE001
            erros[f"estagios[{idx}]" if mont["tipo"] == "trem" else "planetario"] = f"Erro no cálculo: {ex}"
            objetos.append(None); saida.append({"indice": idx + 1, "estagio": idx, "apelido": pl.get("apelido"), "erro": str(ex), "trace": traceback.format_exc()[-1500:]}); continue
        e._analise_params = analise
        objetos.append(e)
        saida.append({"indice": idx + 1, "estagio": idx, "apelido": e.apelido, "interna": bool(e.Z_coroa < 0), "geometria": dados_malha(e)})
    tens = None
    if com_tensoes and all(o is not None for o in objetos) and objetos:
        try:
            if mont["tipo"] == "planetario":
                a1, a2 = objetos[0]._analise_params, objetos[1]._analise_params
                ring = mont["cinematica"]["ring"]      # anelar presa à carcaça -> "Fixo"; girando (porta-planetas/sol fixo ou diferencial) -> "Rotativo"
                params = {"an_apelido": proj.nome, "k1": a1.get("k"), "k2": a2.get("k"), "Ck1": a1.get("Ck"), "Ck2": a2.get("Ck"),
                          "K_Hbeta_imposto1": a1.get("K_Hbeta_imposto"), "K_Hbeta_imposto2": a2.get("K_Hbeta_imposto"),
                          "Tipo_planetario_an": proj.planetario.tipo, "Ring": ring}
                an = calcular_tensoes(objetos[0], objetos[1], params)
                tens = dados_tensoes(an, [objetos[0], objetos[1]])
                for k, m in enumerate(tens["malhas"]):
                    saida[k]["tensoes"] = m; saida[k]["cards"] = m["cards"]
                analises = [an]
            else:
                analises = []
                for k, e in enumerate(objetos):
                    # par interno num trem: a anelar é uma roda do trem que GIRA (a cinemática de _montar_trem já a gira), então entra a inércia
                    # dela em K_v ("Rotativo", como no Ex. 6 da ISO 6336-30). "Fixo" valeria só se a anelar fosse a carcaça; par externo ignora Ring.
                    an = calcular_tensoes(e, None, _params_analise(e._analise_params, k, "Rotativo" if e.Z_coroa < 0 else "Fixo"))
                    t = dados_tensoes(an, [e, None])["malhas"][0]
                    t["indice"] = k + 1
                    saida[k]["tensoes"] = t; saida[k]["cards"] = t["cards"]
                    analises.append(an)
        except Exception as ex:  # noqa: BLE001
            erros["analise"] = f"Erro na análise de tensões: {ex}"
            analises = []
    else:
        analises = []
    for s, o in zip(saida, objetos):
        if o is not None:
            s["avisos"] = s["geometria"]["avisos"] + (s.get("tensoes", {}).get("avisos") or [])
    transmissao = {"tipo": mont["tipo"], "eixos": mont["eixos"], "i_total": mont["i_total"], "eta_total": mont["eta_total"],
                   "cinematica": mont.get("cinematica"), "elementos": mont.get("elementos")}
    # resumo global de seguranças
    minimos = []
    for s in saida:
        for c in s.get("cards") or []:
            if c["valor"] is not None:
                minimos.append((c["fator"], c["roda"], s["apelido"], c["valor"], c["minimo"], c["status"]))
    pior = min(minimos, key=lambda t: t[3] / t[4]) if minimos else None
    resumo = {"n_malhas": len(saida), "n_ok": sum(1 for o in objetos if o is not None),
              "pior": {"fator": pior[0], "roda": pior[1], "malha": pior[2], "valor": pior[3], "minimo": pior[4], "status": pior[5]} if pior else None,
              "todos_atendem": bool(minimos) and all(t[5] == "ok" or t[5] == "atencao" for t in minimos)}
    res = {"ok": not erros, "erros": erros, "transmissao": to_jsonable(transmissao), "malhas": to_jsonable(saida), "resumo": resumo,
           "layout": to_jsonable(_layout.resolver(proj))}
    return res, objetos, analises


def calcular_json(proj_dict, com_tensoes=True):
    """Entrada: dict do projeto (JSON da interface). Saída: (resultado serializável, objetos Engrenamento, análises)."""
    proj = Projeto.model_validate(proj_dict)
    out = calcular_projeto(proj, com_tensoes)
    if isinstance(out, tuple):
        return out
    return out, [], []
