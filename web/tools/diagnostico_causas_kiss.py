# -*- coding: utf-8 -*-
"""Diagnostico das causas dos desvios interface x KISSsoft (secao C de _revisao/comparacao_interface_kisssoft.md).
Cada bloco alimenta funcoes do codigo original (Equacoes_dimensionamento) com insumos lidos do relatorio KISSsoft e imprime o
resultado ao lado do valor do KISSsoft. Uso (a partir da raiz do projeto):  web/.venv313/Scripts/python.exe web/tools/diagnostico_causas_kiss.py"""
import sys, os, math, types
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
import validacao_kiss as V
ns, kw = V.carrega_run_kiss()
G = V.G
from backend.bootstrap import Eq
KISS = ns["KISS"]

# ---------------------------------------------------------------- diag4
E = {n: {m: G.Engrenamento(**kw[n][m]) for m in ("ext", "int")} for n in ("reto_sem_prot", "reto_com_prot", "helic_20")}
ref = {"reto_sem_prot": "sem_prot", "reto_com_prot": "com_prot", "helic_20": "helicoidal"}
KB = {  # c'th e C_B do KISSsoft (txt)
 ("reto_sem_prot", "ext"): (19.153, 0.9, 10.284), ("reto_sem_prot", "int"): (21.021, 0.9, 11.287),
 ("reto_com_prot", "ext"): (19.153, 0.944, 10.785), ("reto_com_prot", "int"): (21.021, 0.922, 11.562),
 ("helic_20", "ext"): (19.594, 0.9, 9.290), ("helic_20", "int"): (21.002, 0.9, 9.958)}
print("### (a) c' do KISS = c'th*CM*CR*CB*cos(beta)*(w_cod/100)*(E/Est)  [w_cod = Ft*Ky*KA/b do codigo]")
for (n, m), (th, cb, ck) in KB.items():
    e = E[n][m]
    pred = th * 0.8 * 1.0 * cb * math.cos(math.radians(e.beta)) * (e.w / 100) * (206.843 / 206)
    code = Eq.rigidez(e)
    print(n, m, "w_cod=%.3f  KISS c'=%.3f  formula linear=%.3f (%.2f%%)  codigo c'th=%.3f CB=%.4f c'=%.3f" % (e.w, ck, pred, 100*(pred-ck)/ck, code[0], (1 + 0.5*(1.2 - e.ferramenta_pinhao.cp_dedendo))*(1 - 0.02*(20 - e.alpha_n)), code[1]))

print("\n### (b) n_e modelo de par do KISS: n_e = 30e3/(pi z1)*sqrt(c_g/m_red), m_red = (m1/N*m2)/(m1/N+m2) (ext) ou m2*m12/(m2+m12) (int)")
def mb(e, lado, com_eixo=True):
    rho = getattr(e, f"material_{lado}").rho
    rm = (getattr(e, f"d_a_{lado}") + getattr(e, f"d_f_{lado}")) / 4
    di = getattr(e, f"di_{lado}"); dsh = getattr(e, f"d_sh_{lado}")
    if lado == "pinhao":
        i = rho * math.pi / 2 * e.b_pinhao * (rm**4 - (di/2)**4 + ((dsh/2)**4 if com_eixo else 0))
    else:
        i = rho * math.pi / 2 * e.b_coroa * abs(rm**4 - (di/2)**4)
    return i / getattr(e, f"b_{lado}") / (getattr(e, f"db_{lado}")/2)**2
for n in E:
    e1, e2 = E[n]["ext"], E[n]["int"]
    N = 3
    for com_eixo in (True, False):
        m1 = mb(e1, "pinhao", com_eixo); m2 = mb(e1, "coroa"); m12 = mb(e2, "coroa")
        a1 = Eq.rigidez(e1); a2 = Eq.rigidez(e2)
        red1 = (m1/N*m2)/(m1/N+m2); red2 = m2*m12/(m2+m12)
        ne1 = 30e3/(math.pi*e1.Z_pinhao)*math.sqrt(a1[2]/red1); ne2 = 30e3/(math.pi*e2.Z_pinhao)*math.sqrt(a2[2]/red2)
        print(n, "sol com eixo(d_sh)" if com_eixo else "sol sem eixo (J do KISS)", "m_red ext=%.5f int=%.4f ; n_e ext=%.0f int=%.0f" % (red1, red2, ne1, ne2), " (KISS %s)" % {k: KISS[ref[n]][k]["n_e"] for k in ("ext", "int")})

print("\n### (c) Y_F/h_Fe com os diametros uteis do KISSsoft")
def yf(e, lado, d_nk=None, d_na=None):
    g = lambda a: getattr(e, f"{a}_{lado}")
    ferr = g("ferramenta")
    return Eq.Yf(e.m_n, e.alpha_n, g("d"), g("d_f"), g("S_ns"), g("pr"), g("SM"), g("rk"), g("x"), g("Z"), e.beta, e.epsilon_alpha,
                 d_nk if d_nk else g("d_nk"), g("d_nf"), g("T_ns"), d_na if d_na else g("d_na"), ferr.cp_dedendo, "C", ferr.Z_shaper, 0.0, "rack")
e = E["reto_com_prot"]["int"]
print("anelar com_prot int  d_na codigo=%.3f -> Y_F=%.4f hFe=%.3f sFn=%.3f" % (e.d_na_coroa, *[yf(e, "coroa")[i] for i in (0, 2, 3)]), "| com d_na=-447.702 (KISS):", ["%.4f" % x for x in (yf(e, "coroa", d_na=-447.702)[0], yf(e, "coroa", d_na=-447.702)[2])], "(KISS Y_F 1.41 hFe 5.87)")
e = E["reto_sem_prot"]["int"]
print("planeta sem_prot int d_na codigo=%.3f -> Y_F=%.4f hFe=%.3f" % (e.d_na_pinhao, yf(e, "pinhao")[0], yf(e, "pinhao")[2]), "| com d_nk=207.737 (KISS):", ["%.4f" % x for x in (yf(e, "pinhao", d_nk=207.737)[0], yf(e, "pinhao", d_nk=207.737)[2])], "(KISS Y_F 1.90 hFe 5.83)")
e = E["helic_20"]["int"]
print("planeta helic int  d_nk codigo=%.3f -> Y_F=%.4f hFe=%.3f" % (e.d_nk_pinhao, yf(e, "pinhao")[0], yf(e, "pinhao")[2]), "| com d_nk=220.935 (planeta malha ext/KISS):", ["%.4f" % x for x in (yf(e, "pinhao", d_nk=220.935)[0], yf(e, "pinhao", d_nk=220.935)[2])], "(KISS Y_F 1.88 hFe 5.83)")
e = E["reto_com_prot"]["ext"]
print("sol com_prot ext: Y_F=%.4f hFe=%.3f sFn=%.3f rhoF=%.3f  d_f=%.3f d_nf=%.3f (KISS: Y_F 2.25 hFe 5.84 sFn 6.32 rho 1.32 d_f 40.434 d_nf 44.097)" % (e.Yf_pinhao, e.h_fe_pinhao, e.S_fn_pinhao, e.p_f_pinhao, e.d_f_pinhao, e.d_nf_pinhao))

print("\n### (d) Z_beta e sqrt(Ky): sigma_H0 helicoidal ext")
e = E["helic_20"]["ext"]
print("Z_beta ISO 1/sqrt(cosb)=%.4f  DIN sqrt(cosb)=%.4f ; razao=%.4f ; sqrt(Ky)=%.4f ; produto=%.4f ; sigma_H0 cod/KISS=%.4f" % (1/math.sqrt(math.cos(math.radians(20))), math.sqrt(math.cos(math.radians(20))), 1/math.cos(math.radians(20)), math.sqrt(1.05), math.sqrt(1.05)/math.cos(math.radians(20)), 509.3266/467.14))
print("\n### (e) T e Ft")
print("KISS Ft = 2000*143.24/45/3 = %.3f ; codigo sem Ky = 2000*143.2/45/3 = %.3f ; com Ky = %.3f" % (2000*143.24/45/3, 2000*143.2/45/3, 2000*143.2/45/3*1.05))

# ---------------------------------------------------------------- diag5
E = {n: {m: G.Engrenamento(**kw[n][m]) for m in ("ext", "int")} for n in ("reto_sem_prot", "reto_com_prot", "helic_20")}

print("### (i) K_Halpha / K_Falpha do codigo alimentados com os insumos do KISSsoft (eps, c_g, Kv, KHbeta, Z_eps, Ft)")
cases = [("reto_sem_prot", "int", dict(eps_a=1.657, eps_b=0.0, cg=16.850, Kv=1.29, KHb=1.10, Zeps=0.884, Ft=2122.07), (1.28, 1.42)),
         ("reto_com_prot", "int", dict(eps_a=1.439, eps_b=0.0, cg=15.371, Kv=1.31, KHb=1.10, Zeps=0.924, Ft=2122.07), (1.17, 1.30)),
         ("helic_20", "ext", dict(eps_a=1.241, eps_b=1.089, cg=10.971, Kv=1.02, KHb=1.20, Zeps=0.898, Ft=1994.09), (1.31, 1.31)),
         ("helic_20", "int", dict(eps_a=1.492, eps_b=1.089, cg=13.630, Kv=1.25, KHb=1.10, Zeps=0.819, Ft=1994.09), (2.28, 2.28))]
for n, m, k, kiss in cases:
    e = E[n][m]
    for lab, Ft in (("Ft com Ky (como o codigo)", k["Ft"] * 1.05), ("Ft sem Ky", k["Ft"])):
        p = types.SimpleNamespace(**vars(e))
        p.epsilon_alpha = k["eps_a"]; p.epsilon_beta = k["eps_b"]; p.epsilon_total = k["eps_a"] + k["eps_b"]; p.Ft = Ft
        Kha = Eq.K_Halpha(p, k["Kv"], k["KHb"], k["cg"], k["Zeps"]); Kfa = Eq.K_Falpha(p, Kha)
        print(n, m, lab, "-> K_Halpha=%.3f K_Falpha=%.3f   (KISS %.2f / %.2f)" % (Kha, Kfa, *kiss))
    p = types.SimpleNamespace(**vars(e))
    print("    codigo: eps_total=%.4f c_g=%.3f (modelo completo) -> K_Halpha 'como o codigo calculou' (ver tabela)" % (e.epsilon_total, Eq.rigidez(e)[2]))

print("\n### (ii) n_e: modelo acoplado de 3 massas do codigo com c_g do KISS; conversao para rpm do proprio pinhao da malha")
def mb(e, lado, eixo=True):
    rho = getattr(e, f"material_{lado}").rho
    rm = (getattr(e, f"d_a_{lado}") + getattr(e, f"d_f_{lado}")) / 4
    di = getattr(e, f"di_{lado}"); dsh = getattr(e, f"d_sh_{lado}")
    if lado == "pinhao":
        i = rho * math.pi / 2 * e.b_pinhao * (rm**4 - (di/2)**4 + ((dsh/2)**4 if eixo else 0))
    else:
        i = rho * math.pi / 2 * e.b_coroa * abs(rm**4 - (di/2)**4)
    return i / getattr(e, f"b_{lado}") / (getattr(e, f"db_{lado}")/2)**2
KC = {"reto_sem_prot": (12.868, 16.850), "reto_com_prot": (12.069, 15.371), "helic_20": (10.971, 13.630)}
KN = {"reto_sem_prot": (43995, 1735), "reto_com_prot": (42139, 1654), "helic_20": (38247, 1575)}
for n in E:
    e1, e2 = E[n]["ext"], E[n]["int"]
    m1, m2, m12 = mb(e1, "pinhao"), mb(e1, "coroa"), mb(e2, "coroa")
    for lab, cg in (("c_g do codigo", (Eq.rigidez(e1)[2], Eq.rigidez(e2)[2])), ("c_g do KISS", KC[n])):
        B = cg[0]*(1/m1+1/m2) + cg[1]*(1/m12+1/m2); C = cg[0]*cg[1]*((m1+m2+m12)/(m1*m2*m12))
        l1 = 0.5*(B+math.sqrt(B*B-4*C)); l2 = 0.5*(B-math.sqrt(B*B-4*C))
        f = 30e3/(math.pi*e1.Z_pinhao)
        ne1, ne2 = f*math.sqrt(l1), f*math.sqrt(l2)
        print(n, lab, "acoplado: n_e1=%.0f (ref. sol)  n_e2=%.0f (ref. sol) = %.0f rpm do planeta (z=66 vs 15)" % (ne1, ne2, ne2*e1.Z_pinhao/e2.Z_pinhao), "| KISS:", KN[n])

print("\n### (iii) eps_a com os diametros uteis do KISS")
for n, ext_d, int_d in (("reto_com_prot", (53.657, 206.367), (207.737, -447.702)), ("reto_sem_prot", (53.657, 207.737), (207.737, -446.449))):
    e1, e2 = E[n]["ext"], E[n]["int"]
    ee1 = Eq.grau_recob_perfil(e1.Z_coroa, e1.m_n, e1.alpha_n, e1.db_pinhao, e1.db_coroa, ext_d[0], ext_d[1], e1.alpha_wt, e1.alpha_t)
    ee2 = Eq.grau_recob_perfil(e2.Z_coroa, e2.m_n, e2.alpha_n, e2.db_pinhao, e2.db_coroa, int_d[0], int_d[1], e2.alpha_wt, e2.alpha_t)
    print(n, "eps_a ext(d_Na KISS)=%.4f (codigo %.4f)  int(d_Na KISS)=%.4f (codigo %.4f)" % (ee1, e1.epsilon_alpha, ee2, e2.epsilon_alpha))
    print("   d_na codigo ext:", e1.d_na_pinhao, e1.d_na_coroa, " int:", e2.d_na_pinhao, e2.d_na_coroa, "| d_nf codigo ext:", e1.d_nf_pinhao, e1.d_nf_coroa)

print("\n### (iv) Y_F do planeta na malha interna (com_prot) com d_Na KISS = 207.737")
e = E["reto_com_prot"]["int"]; g = lambda a: getattr(e, f"{a}_pinhao")
r = Eq.Yf(e.m_n, e.alpha_n, g("d"), g("d_f"), g("S_ns"), g("pr"), g("SM"), g("rk"), g("x"), g("Z"), e.beta, e.epsilon_alpha, 207.737, g("d_nf"), g("T_ns"), 207.737, e.ferramenta_pinhao.cp_dedendo, "C", e.ferramenta_pinhao.Z_shaper, 0.0, "rack")
print("Y_F=%.4f p_f=%.3f h_fe=%.3f S_fn=%.3f   (KISS 2.04 / 1.19 / 5.56 / 6.85; codigo 2.1946 / %.3f / %.3f)" % (*r, e.p_f_pinhao, e.h_fe_pinhao))
print("pr=%s SM=%s ferr.pr=%s" % (g("pr"), g("SM"), e.ferramenta_pinhao.pr))

print("\n### (v) Wk: pb e diferenca de k")
e = E["reto_sem_prot"]["ext"]
print("pb=%.3f ; Wk(k=4)=%.3f (KISS 32.759)" % (e.pb, Eq.dimensao_W(e.alpha_n, e.m_n, e.Z_pinhao, e.x_pinhao, e.S_ns_pinhao, e.S_ni_pinhao, e.beta, e.alpha_t, 4)[1]))
e = E["helic_20"]["ext"]
print("helic sol k_codigo=%d  Wk=%.3f ; k=4: %.3f (KISS 32.836 com k=?)" % (e.k_pinhao, e.Wk_s_pinhao, Eq.dimensao_W(e.alpha_n, e.m_n, e.Z_pinhao, e.x_pinhao, e.S_ns_pinhao, e.S_ni_pinhao, e.beta, e.alpha_t, 4)[1]))

# ---------------------------------------------------------------- diag6
E = {n: {m: G.Engrenamento(**kw[n][m]) for m in ("ext", "int")} for n in ("reto_sem_prot", "helic_20")}
print("### Z_R / Z_L / Z_V variando sigma_Hlim usado e Rz")
for n, KZ in (("reto_sem_prot", {"ext": (1.182, 1.072, 0.967), "int": (1.040, 1.072, 0.967)}), ("helic_20", {"ext": (1.184, 1.072, 0.968), "int": (1.042, 1.072, 0.968)})):
    for m in ("ext", "int"):
        e = E[n][m]
        rz = {"ext": (0.40, 0.40), "int": (0.40, 5.00)}[m]
        for lab, lim in (("min(sigmaHlim)=codigo", None), ("sigmaHlim=1500 p/ todas", 1500.0)):
            p = types.SimpleNamespace(**vars(e))
            p.material_pinhao = types.SimpleNamespace(**vars(e.material_pinhao)); p.material_coroa = types.SimpleNamespace(**vars(e.material_coroa))
            if lim:
                p.material_pinhao.Lim_pressao = lim; p.material_coroa.Lim_pressao = lim
            r0 = (Eq.Z_R(p), Eq.Z_L(p), Eq.Z_V(p))
            p.Rz_flanco_pinhao, p.Rz_flanco_coroa = rz
            r1 = Eq.Z_R(p)
            print(n, m, lab, "Z_R(Rz=6Ra)=%.4f Z_L=%.4f Z_V=%.4f | Z_R(Rz KISS)=%.4f" % (*r0, r1), "| KISS Z_R/Z_L/Z_V =", KZ[m])

# ---------------------------------------------------------------- diag8
e1 = G.Engrenamento(**kw["reto_sem_prot"]["ext"]); e2 = G.Engrenamento(**kw["reto_sem_prot"]["int"])
def mb(e, lado, eixo=True):
    rho = getattr(e, f"material_{lado}").rho
    rm = (getattr(e, f"d_a_{lado}") + getattr(e, f"d_f_{lado}")) / 4
    di = getattr(e, f"di_{lado}"); dsh = getattr(e, f"d_sh_{lado}")
    if lado == "pinhao":
        i = rho * math.pi / 2 * e.b_pinhao * (rm**4 - (di/2)**4 + ((dsh/2)**4 if eixo else 0))
    else:
        i = rho * math.pi / 2 * e.b_coroa * abs(rm**4 - (di/2)**4)
    return i / getattr(e, f"b_{lado}") / (getattr(e, f"db_{lado}")/2)**2
for eixo in (True, False):
    m1 = mb(e1, "pinhao", eixo); m2 = mb(e1, "coroa")
    print("sol com eixo" if eixo else "sol sem eixo", "m1_b=%.5f" % m1, "m_red sem N=%.5f  com N=3 =%.5f" % (m1*m2/(m1+m2), m1*m2/(m1+3*m2)), "(KISS 0.0027)")
J = 0.0001105  # kg m2 (KISS sol)
print("J_sol KISS = 0.0001105 kg m2 ; J_sol codigo (sem eixo) =", mb(e1, "pinhao", False) * (e1.db_pinhao/2)**2 * 30 * 1e-6, "kg m2 (b=30, dim. kg m2)")
c1, c2 = Eq.rigidez(e1)[2], Eq.rigidez(e2)[2]
print("c_g codigo", c1, c2)
for lab, m_red in (("sem N, com eixo", 0.00901), ("KISS 0.0027", 0.0027)):
    print(lab, "n_e par = %.0f" % (30e3/(math.pi*15)*math.sqrt(c1/m_red)))
print("KISS ext n_e conferencia: %.0f (c_g KISS 12.868, m_red 0.0027)" % (30e3/(math.pi*15)*math.sqrt(12.868/0.0027)))
print("KISS int n_e conferencia: %.0f (c_g KISS 16.850, m_red 0.1171, z=66)" % (30e3/(math.pi*66)*math.sqrt(16.850/0.1171)))
print("N KISS: ext n_rel/n_e=1000/43995=%.3f ; int 227.27/1735=%.3f ; N codigo ext (Kv zona)=%.3f int=%.3f" % (1000/43995, 227.27/1735, 1000/26838, 1000/8484))
