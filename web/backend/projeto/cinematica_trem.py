# -*- coding: utf-8 -*-
"""Dimensionamento cinemático de trem de engrenagens: distribui a redução alvo em N estágios e sugere pares z₁/z₂.

Critérios (Mazzo / prática): redução por estágio decrescente ou equilibrada (i_k ≈ i_total^(1/N), com peso para o
primeiro estágio mais rápido), z₁ ≥ z_min sem undercut para α_n (com x = 0), z₁ e z₂ primos entre si (hunting),
z₂ ≤ z_max, erro da redução total dentro da tolerância. Devolve candidatos ordenados por erro e por soma de dentes
(menor tamanho)."""
import math
from itertools import product


def z_min(alpha_n, beta=0.0, h_aP=1.0):
    at = math.atan(math.tan(math.radians(alpha_n)) / math.cos(math.radians(beta)))
    return math.ceil(2 * h_aP * math.cos(math.radians(beta)) / math.sin(at) ** 2)


def buscar_trem(i_alvo, n_estagios, alpha_n=20.0, beta=0.0, z1_min=None, z1_max=30, z2_max=150, tol_rel=0.02, max_resultados=200,
                hunting=True, i_max_estagio=8.0, distribuicao="equilibrada"):
    """Devolve dict com candidatos: [{estagios:[{z1,z2,i}], i_total, erro_rel, soma_z}], e os limites usados."""
    if n_estagios < 1:
        raise ValueError("número de estágios deve ser ≥ 1")
    if i_alvo <= 0:
        raise ValueError("redução alvo deve ser positiva")
    zmin = max(z1_min or 0, z_min(alpha_n, beta))
    # razão por estágio de referência
    base = i_alvo ** (1.0 / n_estagios)
    if distribuicao == "decrescente" and n_estagios > 1:   # primeiro estágio (rápido) com relação ~20 % maior
        pesos = [1.2 - 0.4 * k / max(1, n_estagios - 1) for k in range(n_estagios)]
        s = sum(math.log(p) for p in pesos) / n_estagios
        refs = [base * p / math.exp(s) for p in pesos]
    else:
        refs = [base] * n_estagios
    if any(r > i_max_estagio for r in refs):
        raise ValueError(f"redução por estágio {max(refs):.2f} acima do máximo {i_max_estagio}; aumente o número de estágios")
    # pares candidatos por estágio: z1 em [zmin, z1_max], z2 arredondado a i_ref*z1 ± 1, com hunting
    def pares(i_ref):
        out = []
        for z1 in range(zmin, z1_max + 1):
            for z2 in (round(i_ref * z1) - 1, round(i_ref * z1), round(i_ref * z1) + 1):
                if z2 <= z1 or z2 > z2_max:
                    continue
                if hunting and math.gcd(z1, z2) != 1:
                    continue
                out.append((z1, z2, z2 / z1))
        # mantém os pares com relação mais próxima da referência (até 12 por estágio) para o produto cartesiano
        out.sort(key=lambda t: abs(t[2] - i_ref))
        return out[:12]
    listas = [pares(r) for r in refs]
    if any(not l for l in listas):
        raise ValueError("nenhum par z₁/z₂ viável com os limites informados")
    cands = []
    for combo in product(*listas):
        i_tot = math.prod(c[2] for c in combo)
        erro = (i_tot - i_alvo) / i_alvo
        if abs(erro) > tol_rel:
            continue
        cands.append({"estagios": [{"z1": c[0], "z2": c[1], "i": c[2]} for c in combo], "i_total": i_tot, "erro_rel": erro, "soma_z": sum(c[0] + c[1] for c in combo)})
    cands.sort(key=lambda c: (abs(c["erro_rel"]), c["soma_z"]))
    for k, c in enumerate(cands[:max_resultados]):
        c["idx"] = k
    return {"candidatos": cands[:max_resultados], "n": len(cands), "z_min": zmin, "refs": refs, "i_alvo": i_alvo, "n_estagios": n_estagios}
