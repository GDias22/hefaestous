# -*- coding: utf-8 -*-
"""Valida a CAMADA DE SERVICO da interface web contra o codigo original e contra o KISSsoft (3 casos 'alef').

Os kwargs das malhas NAO sao redigitados: o trecho de `_revisao/run_kiss.py` anterior a `res = {}` (dados comuns, funcao par(),
make(), dict KISS e extrai()) e executado de forma controlada, com `G.Engrenamento` temporariamente trocado por um gravador de kwargs.
Cada kwargs gravado vira um payload de interface (materiais/ferramentas/lubrificante como dict de campos mat_*/fer_*/lub_*),
passa por json.dumps/loads (como na API) e e calculado por `calcular_malha` + `calcular_tensoes`.

Comparacoes:
  (A) interface x `_revisao/kiss_out/kiss_resultados.json` (resultado gravado do codigo original) e
      interface x codigo original reexecutado agora neste processo (mesmos kwargs/objetos de run_kiss.py);
  (B) interface x KISSsoft (dict KISS de run_kiss.py), fatores com |delta| > 3 %.

Uso:  web\\.venv313\\Scripts\\python.exe web\\tools\\validacao_kiss.py   (grava _revisao/comparacao_interface_kisssoft.md e
      _revisao/kiss_out/interface_resultados.json)
"""
import ast
import json
import math
import os
import sys
import types

WEB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(WEB)
REV = os.path.join(ROOT, "_revisao")
sys.path.insert(0, WEB)
os.environ["ENGR_SEM_PDF"] = "1"

from backend.bootstrap import G, A  # noqa: E402
from backend.services.geometria import calcular_malha  # noqa: E402
from backend.services.tensoes import calcular_tensoes  # noqa: E402

PREF = {"material": "mat_", "ferramenta": "fer_", "lubrificante": "lub_"}
SUBOBJ = {"material_pinhao": ("material", G.Materiais), "material_coroa": ("material", G.Materiais),
          "ferramenta_pinhao": ("ferramenta", G.Ferramentas), "ferramenta_coroa": ("ferramenta", G.Ferramentas),
          "lubrificante": ("lubrificante", G.Lubrificante)}


# ------------------------------------------------------------------------------------------------ carrega run_kiss.py (sem editar)
def carrega_run_kiss():
    """Executa run_kiss.py ate `res = {}`; devolve (namespace, kwargs gravados por caso e malha)."""
    src = open(os.path.join(REV, "run_kiss.py"), encoding="utf-8").read()
    tree = ast.parse(src)
    # corta antes da atribuicao `res = {}` de nivel superior
    idx = next(i for i, n in enumerate(tree.body) if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", None) == "res")
    tree.body = tree.body[:idx]
    code = compile(tree, os.path.join(REV, "run_kiss.py"), "exec")
    tmp = os.path.join(REV, "kiss_out", "_tmp_validacao")
    os.makedirs(tmp, exist_ok=True)
    cwd, argv = os.getcwd(), sys.argv
    sys.argv = ["run_kiss.py", tmp]
    ns = {"__file__": os.path.join(REV, "run_kiss.py"), "__name__": "run_kiss_ctrl"}
    try:
        exec(code, ns)
    finally:
        os.chdir(cwd)
        sys.argv = argv
    # grava kwargs
    orig = G.Engrenamento
    gravados = []

    def rec(**kw):
        gravados.append(kw)
        return types.SimpleNamespace(**kw)
    G.Engrenamento = rec
    try:
        kw_casos = {}
        for nome, c in ns["casos"].items():
            gravados.clear()
            c["mk"]()
            kw_casos[nome] = dict(ext=dict(gravados[0]), int=dict(gravados[1]), ref=c["ref"])
    finally:
        G.Engrenamento = orig
    return ns, kw_casos


def obj_para_campos(stage, obj):
    import inspect
    cls = {"material": G.Materiais, "ferramenta": G.Ferramentas, "lubrificante": G.Lubrificante}[stage]
    campos = {}
    for nome in inspect.signature(cls.__init__).parameters:
        if nome == "self":
            continue
        campos[PREF[stage] + nome] = getattr(obj, nome)
    return campos


def kwargs_para_payload(kw):
    p = {}
    for k, v in kw.items():
        if k in SUBOBJ:
            p[k] = obj_para_campos(SUBOBJ[k][0], v)
        else:
            p[k] = v
    return json.loads(json.dumps(p))   # como na API (JSON)


def projeto_alef(kw):
    """Monta o alef como PROJETO do app (planetario Simples, modo diferencial: entrada sol, saida anelar, porta-planetas a 1000 rpm).
    Os campos de roda/malha vem dos MESMOS kwargs de run_kiss.py (sol = pinhao da malha ext; planeta = coroa da malha ext; anelar = coroa da malha int)."""
    from backend.projeto.defaults import RODA, default_roda, default_entrada, default_operacao, default_metodos, default_analise, OPERACAO, METODOS
    ext, inn = kw["ext"], kw["int"]

    def roda(k, lado):
        d = default_roda()
        for base, (kp, kc) in RODA.items():
            key = kp if lado == "pinhao" else kc
            if key in k:
                v = k[key]
                d[base] = obj_para_campos(SUBOBJ[key][0], v) if key in SUBOBJ else v
        return d
    sol = roda(ext, "pinhao"); sol["z"] = ext["Z_pinhao"]
    pla = roda(ext, "coroa"); pla["z"] = ext["Z_coroa"]
    an = roda(inn, "coroa"); an["z"] = abs(inn["Z_coroa"]); an["D_ext"] = abs(inn["di_coroa"])
    an.pop("di", None)
    oper = default_operacao()
    for k in OPERACAO:
        if k in ext:
            oper[k] = ext[k]
    oper["lubrificante"] = obj_para_campos("lubrificante", ext["lubrificante"])
    met = default_metodos()
    for k in METODOS:
        if k in ext and ext[k] is not None:
            met[k] = ext[k]
    ent = default_entrada(n=2000.0, T=143.2)
    ent.update(irregularidade_motora=ext["irregularidade_motora"], irregularidade_movida=ext["irregularidade_movida"], Ka_imposto=ext["Ka_imposto"])
    mal = lambda k, a: dict(m_n=k["m_n"], alpha_n=k["alpha_n"], beta=k["beta"], x_pinhao=k["x_pinhao"], tipo=k["tipo"], a=a)
    return {"nome": "alef", "tipo": "planetario", "entrada": ent, "operacao": oper, "metodos": met, "estagios": [],
            "planetario": {"tipo": "Simples", "N_cp": ext["N_cp"], "Ky": ext["Ky"], "entrada": "sol", "saida": "anelar", "modo": "diferencial", "n_livre": 1000.0,
                           "sol": sol, "planeta_maior": pla, "planeta_menor": dict(pla), "anelar": an,
                           "malha_ext": mal(ext, ext["a"]), "malha_int": mal(inn, None),
                           "analise_ext": default_analise(100) | {"K_Hbeta_imposto": 1.20}, "analise_int": default_analise(100) | {"K_Hbeta_imposto": 1.10}}}


def rel(a, b):
    if a is None or b is None or isinstance(a, (str, list)) or isinstance(b, (str, list)):
        return None
    if b == 0:
        return 0.0 if a == 0 else float("inf")
    return (a - b) / abs(b)


def main():
    ns, kw_casos = carrega_run_kiss()
    extrai, KISS, num = ns["extrai"], ns["KISS"], ns["num"]
    ref_json = json.load(open(os.path.join(REV, "kiss_out", "kiss_resultados.json"), encoding="utf-8"))

    # chaves de kwargs que o metadata da interface nao conhece (seriam descartadas por kwargs_malha)
    from backend.params.metadata import params_for
    meta_keys = set(params_for("geometria"))
    nao_meta = sorted(set(kw_casos["reto_sem_prot"]["ext"]) - meta_keys - set(SUBOBJ))

    iface, orig_now, payloads = {}, {}, {}
    for nome, c in kw_casos.items():
        pl = {m: kwargs_para_payload(c[m]) for m in ("ext", "int")}
        payloads[nome] = pl
        # interface (camada de servico)
        e1 = calcular_malha(pl["ext"]); e2 = calcular_malha(pl["int"])
        an = calcular_tensoes(e1, e2, dict(an_apelido=f"KISS_{nome}", k1=100, k2=100, Ck1=None, Ck2=None, Tipo_planetario_an="Simples",
                                           Ring="Rotativo", K_Hbeta_imposto1=1.20, K_Hbeta_imposto2=1.10))
        iface[nome] = dict(ext=extrai(an, 1, e1), int=extrai(an, 2, e2), ref=c["ref"])
        # codigo original reexecutado agora (objetos originais compartilhados, como em run_kiss.py)
        o1 = G.Engrenamento(**c["ext"]); o2 = G.Engrenamento(**c["int"])
        ao = A.Analise_de_tensao(apelido=f"KISS_{nome}", Proj=None, Par_engrenado_1=o1, Par_engrenado_2=o2, k1=100, k2=100, Ck1=None, Ck2=None,
                                 Tipo_planetario="Simples", Ring="Rotativo", K_Hbeta_imposto1=1.20, K_Hbeta_imposto2=1.10)
        orig_now[nome] = dict(ext=extrai(ao, 1, o1), int=extrai(ao, 2, o2), ref=c["ref"])

    # (A3) mesmo caso pelo MODELO DE PROJETO do app (planetario Simples em modo diferencial) -> calcular_json
    from backend.projeto.calcular import calcular_json
    proj_res = {}
    for nome, c in kw_casos.items():
        pj = json.loads(json.dumps(projeto_alef(c)))
        r, objs, ans = calcular_json(pj)
        if not r.get("ok") or not objs or objs[0] is None:
            proj_res[nome] = {"erro": r.get("erros")}
            continue
        proj_res[nome] = dict(ext=extrai(ans[0], 1, objs[0]), int=extrai(ans[0], 2, objs[1]), cin=r["transmissao"]["cinematica"].get("n_membros"),
                              ring=r["transmissao"]["cinematica"].get("ring"))
    json.dump(iface, open(os.path.join(REV, "kiss_out", "interface_resultados.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False, default=str)

    L = []
    w = L.append
    w("# Camada de servico da interface web x codigo original x KISSsoft (casos 'alef')\n")
    w("Gerado por `web/tools/validacao_kiss.py` (kwargs lidos de `_revisao/run_kiss.py`, sem redigitar). Fonte da interface: `calcular_malha` + `calcular_tensoes` "
      "(payload JSON com materiais/ferramentas/lubrificante como dict de campos `mat_*`/`fer_*`/`lub_*`; `Tipo_planetario_an=\"Simples\"`, `Ring=\"Rotativo\"`, k1=k2=100, K_Hbeta_imposto1=1,20 / 2=1,10).\n")
    w(f"Chaves de kwargs de `run_kiss.par()` fora do metadata da interface (seriam descartadas): {nao_meta if nao_meta else 'nenhuma'}.\n")

    # ---------------- (A)
    w("\n## A. Interface x codigo original\n")
    tot_fat = 0
    pior = (0.0, None)
    desvios = []
    for fonte, base, rot in (("kiss_resultados.json (gravado)", ref_json, "A1"), ("codigo original reexecutado agora", orig_now, "A2")):
        n = 0; maxd = 0.0; ruins = []; maxk = None
        for nome in iface:
            for m in ("ext", "int"):
                a = iface[nome][m]; b = base[nome][m]
                for k, v in a.items():
                    if k == "avisos":
                        continue
                    bv = b.get(k)
                    if isinstance(v, (int, float)) and isinstance(bv, (int, float)):
                        n += 1
                        d = abs(v - bv) / max(abs(bv), 1e-300) if bv != 0 else abs(v)
                        if d > maxd:
                            maxd = d; maxk = (nome, m, k, v, bv)
                        if d > 1e-6:
                            ruins.append((nome, m, k, v, bv, d))
                    elif (v is None) != (bv is None) or (isinstance(v, str) and v != bv):
                        ruins.append((nome, m, k, v, bv, float("nan")))
        w(f"- **{rot}** interface x {fonte}: {n} fatores numericos comparados; maior desvio relativo = {maxd:.3e}"
          + (f" ({maxk[0]}/{maxk[1]}/{maxk[2]}: interface {maxk[3]!r} x ref {maxk[4]!r})" if maxk and maxd > 0 else "") + f"; fatores com desvio > 1e-6: {len(ruins)}.")
        for r in ruins[:40]:
            w(f"    - {r[0]} / {r[1]} / {r[2]}: interface {r[3]!r} x ref {r[4]!r} (desvio {r[5]})")
        desvios.append((rot, n, maxd, len(ruins)))
    # A3: modelo de projeto
    for nome in iface:
        pr = proj_res[nome]
        if "erro" in pr:
            w(f"- **A3** {nome}: projeto (modo diferencial) nao calculou: {pr['erro']}")
            continue
        n = 0; maxd = 0.0; maxk = None; ruins = []
        for m in ("ext", "int"):
            for k, v in iface[nome][m].items():
                bv = pr[m].get(k)
                if k != "avisos" and isinstance(v, (int, float)) and isinstance(bv, (int, float)):
                    n += 1
                    d = abs(v - bv) / max(abs(v), 1e-300) if v != 0 else abs(bv)
                    if d > maxd: maxd = d; maxk = (m, k, v, bv)
                    if d > 1e-6: ruins.append((m, k, v, bv, d))
        w(f"- **A3** {nome}: modelo de projeto (planetario Simples, modo diferencial, entrada sol 2000 rpm, livre=porta-planetas 1000 rpm, saida anelar; ring={pr['ring']}; n_membros={pr['cin']}) x servico direto: {n} fatores; maior desvio relativo = {maxd:.3e}; > 1e-6: {len(ruins)}")
        for r in sorted(ruins, key=lambda x: -x[4])[:12]:
            w(f"    - {nome}/{r[0]}/{r[1]}: servico {r[2]!r} x projeto {r[3]!r} ({r[4]:.2e})")
    # avisos
    w("")
    for nome in iface:
        for m in ("ext", "int"):
            if sorted(iface[nome][m]["avisos"]) != sorted(orig_now[nome][m]["avisos"]):
                w(f"- Avisos diferem em {nome}/{m}: interface {len(iface[nome][m]['avisos'])} x original {len(orig_now[nome][m]['avisos'])}")
    # ---------------- (B)
    w("\n## B. Interface x KISSsoft (somente fatores com |delta| > 3 %, ordenados por |delta| decrescente)\n")
    w("Delta% = (interface - KISSsoft) / |KISSsoft|. Fatores sem valor no relatorio KISSsoft do caso nao aparecem. "
      "Y_F, Y_S etc.: p = pinhao (1a roda da malha), c = coroa.\n")
    tabelas = {}
    for nome in iface:
        ref = iface[nome]["ref"]
        for m in ("ext", "int"):
            kiss = KISS[ref][m]; cur = iface[nome][m]
            lin = []; ntot = 0
            for k, kv in kiss.items():
                cv = cur.get(k)
                if not isinstance(cv, (int, float)) or not isinstance(kv, (int, float)):
                    continue
                if kv == 0:
                    continue
                ntot += 1
                d = 100 * (cv - kv) / abs(kv)
                if abs(d) > 3:
                    lin.append((k, kv, cv, d))
            lin.sort(key=lambda x: -abs(x[3]))
            tabelas[(nome, m)] = (lin, ntot)
            w(f"\n### {nome} - malha {'externa (sol x planeta)' if m == 'ext' else 'interna (planeta x anelar)'}  ({len(lin)} de {ntot} fatores com |delta| > 3 %)\n")
            w("| # | Fator | KISSsoft | Interface | Delta % |\n|---|---|---|---|---|")
            for i, (k, kv, cv, d) in enumerate(lin, 1):
                w(f"| {i} | {k} | {kv:.5g} | {cv:.5g} | {d:+.1f} |")
    md = os.path.join(REV, "comparacao_interface_kisssoft.md")
    resto = ""      # secoes C e D (causas e conclusoes) sao escritas a mao: preservadas ao regenerar A e B
    if os.path.exists(md):
        antigo = open(md, encoding="utf-8").read()
        i = antigo.find("\n## C. ")
        if i >= 0:
            resto = antigo[i:]
    open(md, "w", encoding="utf-8").write("\n".join(L) + "\n" + resto)
    print("\n".join(L))
    print("\nRESUMO_A:", desvios)


if __name__ == "__main__":
    main()
