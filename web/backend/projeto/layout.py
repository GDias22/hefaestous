# -*- coding: utf-8 -*-
"""Layout de eixos e mancais -> L, s, arranjo físico (1 a 7) e K' de cada roda (ISO 6336-1, método C; figura de Mazzo).

O usuário informa, por EIXO: diâmetro d_sh, vão entre mancais L e a distância do centro de cada roda ao mancal esquerdo
(a_e). O módulo deduz:
  - s (desalinhamento) e o arranjo 1..7 pela posição das rodas (centrada, descentrada com torque do mesmo lado ou do lado
    oposto, em balanço, duas rodas simétricas ou assimétricas);
  - o ramo de K' (roda integrada/prensada ou com chaveta/estrias): "auto" segue a regra d/d_sh >= 1,15 do código original.
Quando o layout está ATIVO, `overrides()` sobrescreve d_sh, L, sh, Arranjo/k_linha (e di nos planetas) das rodas cobertas.
Anelar não tem eixo (fica fora do layout)."""
import math

from .defaults import default_malha, default_roda

# arranjo -> (K' da roda integrada/prensada ou d/d_sh >= 1,15 ; K' da roda com chaveta/estrias ou d/d_sh < 1,15)
K_LINHA = {1: (0.0, 0.0), 2: (0.0, 0.0), 3: (0.48, 0.80), 4: (-0.48, -0.80), 5: (1.33, 1.33), 6: (-0.36, -0.60), 7: (-0.60, -1.00)}
LIMITE_SL = {3: 0.3, 4: 0.3, 5: 0.5, 6: 0.3, 7: 0.3}      # validade s/l da figura
TOL_CENTRO = 0.5       # mm: roda "centrada"
FOLGA = 4.0            # mm entre rodas vizinhas no layout padrão
RAZAO_D = 1.15
FIXACOES = ("auto", "integrada_prensada", "chaveta")


def _d_ref(m_n, z, beta):
    return abs(float(m_n) * float(z) / math.cos(math.radians(float(beta or 0.0))))


def _roda_dict(d):
    r = default_roda(); r.update(d or {})
    return r


def _f(v, padrao):
    try:
        return padrao if v is None else float(v)
    except (TypeError, ValueError):
        return padrao


def estrutura(proj):
    """Eixos e rodas do projeto (independe do cálculo): [{id, nome, tipo, torque0, rodas:[{key, nome, d_ref, b, wd}]}]."""
    eixos = []
    if proj.tipo == "trem":
        ests = proj.estagios
        n = len(ests)

        def r_trem(i, lado):
            e = ests[i]; m = default_malha(); m.update(e.malha or {})
            z = int(m["Z_pinhao"] if lado == "pinhao" else m["Z_coroa"])
            wd = _roda_dict(e.pinhao if lado == "pinhao" else e.coroa)
            nome = (e.nome or f"Estágio {i + 1}")
            return {"key": f"estagio:{i}:{lado}", "nome": f"{'Pinhão' if lado == 'pinhao' else ('Anelar' if z < 0 else 'Coroa')} {i + 1}", "estagio": nome,
                    "d_ref": _d_ref(m["m_n"], z, m.get("beta")), "b": _f(wd.get("b"), 25.0), "wd": wd, "interna": z < 0}
        for k in range(n + 1):
            rodas = []
            if k >= 1:
                c = r_trem(k - 1, "coroa")
                if not c["interna"]:          # a anelar é da carcaça: não tem eixo
                    rodas.append(c)
            if k < n:
                rodas.append(r_trem(k, "pinhao"))
            if not rodas:
                continue
            nome = "Eixo de entrada" if k == 0 else ("Eixo de saída" if k == n else f"Eixo intermediário {k}")
            eixos.append({"id": f"e{k}", "nome": nome, "tipo": "eixo", "torque0": "esq" if k == 0 else ("dir" if k == n else None), "rodas": rodas})
        return eixos
    pl = proj.planetario
    if pl is None:
        return []
    comp = pl.tipo == "Composto"
    me, mi = default_malha(), default_malha(); me.update(pl.malha_ext or {}); mi.update(pl.malha_int or {})
    sol, maior, menor = _roda_dict(pl.sol), _roda_dict(pl.planeta_maior), _roda_dict(pl.planeta_menor if comp else pl.planeta_maior)
    zs, zb = int(sol.get("z") or 15), int(maior.get("z") or 48)
    zm = int(menor.get("z") or zb) if comp else zb
    eixos.append({"id": "sol", "nome": "Eixo do sol", "tipo": "eixo", "torque0": "esq", "rodas": [
        {"key": "sol", "nome": "Sol", "estagio": None, "d_ref": _d_ref(me["m_n"], zs, me.get("beta")), "b": _f(sol.get("b"), 25.0), "wd": sol, "interna": False}]})
    rodas = [{"key": "planeta_maior", "nome": "Planeta maior" if comp else "Planeta", "estagio": None, "d_ref": _d_ref(me["m_n"], zb, me.get("beta")),
              "b": _f(maior.get("b"), 25.0), "wd": maior, "interna": False}]
    if comp:
        rodas.append({"key": "planeta_menor", "nome": "Planeta menor", "estagio": None, "d_ref": _d_ref(mi["m_n"], zm, mi.get("beta")),
                      "b": _f(menor.get("b"), 25.0), "wd": menor, "interna": False})
    eixos.append({"id": "pino", "nome": "Pino do planeta (porta-planetas)", "tipo": "pino", "torque0": None, "rodas": rodas})
    return eixos


def _sep_padrao(rodas):
    """Distância entre os centros de duas rodas vizinhas (sem sobreposição + folga)."""
    return (rodas[0]["b"] + rodas[1]["b"]) / 2.0 + FOLGA


def _posicoes_padrao(rodas, L):
    """Centros (a_e) das rodas sobre o vão L: uma roda no meio; duas simétricas em relação ao meio do vão (arranjo 6)."""
    c = L / 2.0
    if len(rodas) == 1:
        return [c]
    if len(rodas) == 2:
        s = _sep_padrao(rodas)
        return [c - s / 2.0, c + s / 2.0]
    total = sum(r["b"] for r in rodas) + FOLGA * (len(rodas) - 1)
    x = c - total / 2.0; out = []
    for r in rodas:
        out.append(x + r["b"] / 2.0); x += r["b"] + FOLGA
    return out


def _vao_minimo(rodas):
    """Vão que acomoda as rodas com folga para os mancais e mantém s/l < 0,3 quando há duas rodas (validade da figura)."""
    if len(rodas) == 1:
        return rodas[0]["b"] + 20.0
    return max(sum(r["b"] for r in rodas) + FOLGA * (len(rodas) - 1) + 24.0, _sep_padrao(rodas) / 0.28) if len(rodas) == 2 else sum(r["b"] for r in rodas) + FOLGA * len(rodas) + 24.0


def layout_padrao(proj, ativo=True):
    """Layout inicial: d_sh e L vêm dos campos atuais da 1ª roda do eixo; rodas centradas/lado a lado, arranjo automático."""
    out = {"ativo": bool(ativo), "eixos": {}}
    for e in estrutura(proj):
        w0 = e["rodas"][0]["wd"]
        L = max(_f(w0.get("L"), 100.0), _vao_minimo(e["rodas"]))
        cfg = {"d_sh": _f(w0.get("d_sh"), 30.0), "L": round(L, 3), "torque": e["torque0"] or "indef", "rodas": {}}
        if e["tipo"] == "pino":
            cfg["montagem"] = "agulhas"
        for r, a in zip(e["rodas"], _posicoes_padrao(e["rodas"], L)):
            rc = {"a": round(a, 3), "fixacao": "auto", "arranjo": None}
            if e["tipo"] == "pino":
                rc["d_furo"] = _f(r["wd"].get("di"), 0.0) or round(_f(w0.get("d_sh"), 30.0) * 1.0, 3)
            cfg["rodas"][r["key"]] = rc
        out["eixos"][e["id"]] = cfg
    return out


def _classificar(a, i, L, torque):
    """(arranjo, s, limite s/l) da roda i entre as rodas de centros `a` no vão L."""
    c = L / 2.0; me = a[i]
    if me < 0 or me > L:
        return 5, min(abs(me), abs(me - L)), LIMITE_SL[5]           # em balanço: s = distância ao mancal mais próximo
    outras = [x for j, x in enumerate(a) if j != i and 0 <= x <= L]
    if len(a) >= 3:
        return 2, 0.0, None                                          # várias rodas no vão
    if len(a) == 2 and outras:                                       # duas rodas dentro do vão
        sim = abs((a[0] + a[1]) / 2.0 - c) <= TOL_CENTRO
        return (6 if sim else 7), abs(me - outras[0]), LIMITE_SL[6]
    s = abs(me - c)                                                  # uma roda (ou a outra está em balanço)
    if s <= TOL_CENTRO:
        return 1, 0.0, None
    lado = "esq" if me < c else "dir"
    return (3 if torque in (None, lado) else 4), s, LIMITE_SL[3]


def _s_para(arr, a, i, L):
    c = L / 2.0; me = a[i]
    if arr in (1, 2):
        return 0.0
    if arr in (3, 4):
        return abs(me - c)
    if arr == 5:
        return min(abs(me), abs(me - L))
    outras = [x for j, x in enumerate(a) if j != i]
    return abs(me - outras[0]) if outras else abs(me - c)


def resolver(proj):
    """Layout resolvido: lista de eixos com valores calculados por roda (sempre calculado, ativo ou não)."""
    lay = proj.layout or {}
    cfgs = lay.get("eixos") or {}
    base = None
    out = []
    for e in estrutura(proj):
        c = cfgs.get(e["id"])
        if c is None:
            base = base or layout_padrao(proj)
            c = base["eixos"][e["id"]]
        d0 = _f(e["rodas"][0]["wd"].get("d_sh"), 30.0)
        d_sh, L = _f(c.get("d_sh"), d0), _f(c.get("L"), 100.0)
        torque = c.get("torque", e["torque0"])
        torque = None if torque in ("indef", "", None) else torque
        rc = c.get("rodas") or {}
        if set(rc) != {r["key"] for r in e["rodas"]}:      # o conjunto de rodas do eixo mudou (estágio adicionado/removido): reposiciona
            rc = {}; L = max(L, _vao_minimo(e["rodas"]))
        avisos = []
        invalido = d_sh <= 0 or L <= 0
        if invalido:
            avisos.append({"nivel": "erro", "texto": "Diâmetro do eixo e vão entre mancais devem ser positivos; o layout deste eixo foi ignorado."})
        pos = _posicoes_padrao(e["rodas"], max(L, 1e-6))
        a = [_f((rc.get(r["key"]) or {}).get("a"), pos[j]) for j, r in enumerate(e["rodas"])]
        montagem = c.get("montagem", "agulhas") if e["tipo"] == "pino" else None
        rodas_out = []
        for i, r in enumerate(e["rodas"]):
            cr = rc.get(r["key"]) or {}
            av = []
            arr_auto, s_auto, lim = _classificar(a, i, L, torque) if not invalido else (1, 0.0, None)
            man = cr.get("arranjo")
            arr = int(man) if man not in (None, "", "auto") else arr_auto
            s = _s_para(arr, a, i, L) if not invalido else 0.0
            fix = cr.get("fixacao") or "auto"
            razao = r["d_ref"] / d_sh if d_sh > 0 else 99.0
            sup_razao = razao >= RAZAO_D
            sup = sup_razao if fix == "auto" else (fix == "integrada_prensada")
            k_lin = K_LINHA[arr][0 if sup else 1]
            lim_arr = LIMITE_SL.get(arr)
            sl = s / L if L > 0 else 0.0
            if lim_arr is not None and sl > lim_arr:
                av.append({"nivel": "aviso", "texto": f"s/l = {sl:.2f} acima do limite {lim_arr:g} da figura do arranjo {arr}; o K' não é garantido."})
            if arr == 5 and not (a[i] < 0 or a[i] > L):
                av.append({"nivel": "aviso", "texto": "Arranjo 5 é para roda em balanço (fora do vão entre mancais)."})
            if man not in (None, "", "auto") and arr != arr_auto:
                av.append({"nivel": "info", "texto": f"Arranjo manual {arr}; pela posição o automático seria {arr_auto}."})
            if razao > 0 and e["tipo"] == "eixo" and r["d_ref"] <= d_sh:
                av.append({"nivel": "erro", "texto": f"Eixo (Ø {d_sh:g}) maior ou igual ao diâmetro de referência da roda (Ø {r['d_ref']:.1f}): use roda integrada ao eixo (pinhão-eixo) ou reduza o eixo."})
            ov = None
            if not invalido:
                ov = {"d_sh": d_sh, "L": L, "sh": s, "Arranjo": arr if sup == sup_razao else None, "k_linha": None if sup == sup_razao else k_lin}
                if e["tipo"] == "pino":
                    ov["di"] = _f(cr.get("d_furo"), 0.0) if montagem == "agulhas" else 0.0
            rodas_out.append({"key": r["key"], "nome": r["nome"], "estagio": r.get("estagio"), "d_ref": r["d_ref"], "b": r["b"], "a": a[i], "a_dir": L - a[i], "s": s, "s_l": sl,
                              "arranjo": arr, "arranjo_auto": arr_auto, "arranjo_manual": None if man in (None, "", "auto") else int(man), "k_linha": k_lin,
                              "ramo": "integrada/prensada" if sup else "chaveta/estrias", "fixacao": fix, "razao_d": razao, "avisos": av,
                              "d_furo": _f(cr.get("d_furo"), 0.0) if e["tipo"] == "pino" else None, "override": ov})
        # sobreposição axial de rodas vizinhas
        ordem = sorted(range(len(e["rodas"])), key=lambda j: a[j])
        for p, q in zip(ordem, ordem[1:]):
            folga = (a[q] - a[p]) - (e["rodas"][p]["b"] + e["rodas"][q]["b"]) / 2.0
            if folga < 0:
                avisos.append({"nivel": "erro", "texto": f"{e['rodas'][p]['nome']} e {e['rodas'][q]['nome']} se sobrepõem axialmente ({-folga:.1f} mm)."})
        out.append({"id": e["id"], "nome": e["nome"], "tipo": e["tipo"], "d_sh": d_sh, "L": L, "torque": torque, "montagem": montagem, "rodas": rodas_out, "avisos": avisos, "invalido": invalido})
    return {"ativo": bool(lay.get("ativo")), "eixos": out}


def overrides(proj):
    """{chave_da_roda: {d_sh, L, sh, Arranjo, k_linha[, di]}} — vazio quando o layout não está ativo."""
    if not (proj.layout or {}).get("ativo"):
        return {}
    ov = {}
    for e in resolver(proj)["eixos"]:
        for r in e["rodas"]:
            if r["override"]:
                ov[r["key"]] = r["override"]
    return ov
