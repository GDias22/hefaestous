# -*- coding: utf-8 -*-
"""Traduz falhas numéricas do cálculo (math domain error, solver que não converge…) em mensagens por campo, em português,
com o valor-limite e a faixa viável. Só roda DEPOIS que o cálculo falhou, usando fórmulas geométricas elementares:

  • flanco evolvente existe só se o diâmetro de referência deslocado d + 2·x·m_n ≥ d_b  ⇒  x ≥ −(z/(2·cosβ))·(1 − cos α_t)
  • Σx = x₁ + x₂ sai da distância entre centros a (ângulo de pressão de trabalho α_wt)
  • a ≥ (z₁+z₂)·m_t·cos α_t / 2 (senão cos α_wt > 1)
  • espessura de cabeça s_a ≥ ~0,2·m_n (dente pontiagudo abaixo disso; só rodas externas)
Os números são aproximações de projeto (cabeça padrão h_aP* = 1); servem para orientar, não substituem o cálculo completo."""
import math

R = math.radians
inv = lambda a: math.tan(a) - a          # função involuta (rad)
S_MIN = 0.2                               # espessura de cabeça mínima aceitável / m_n
FERR = ("x_pinhao", "a", "alpha_n", "beta", "m_n", "Z_pinhao", "Z_coroa")


def _f(v, nd=2):
    return f"{v:.{nd}f}".replace(".", ",")


def _geom(kw):
    z1, z2, m_n = int(kw["Z_pinhao"]), int(kw["Z_coroa"]), float(kw["m_n"])
    beta, a_n = float(kw.get("beta") or 0.0), float(kw["alpha_n"])
    cb = math.cos(R(beta))
    a_t = math.atan(math.tan(R(a_n)) / cb)
    return z1, z2, m_n, beta, a_n, cb, a_t, m_n / cb


def _sum_x(kw):
    """Σx pedido pela distância entre centros (None se `a` for geometricamente impossível)."""
    z1, z2, m_n, beta, a_n, cb, a_t, m_t = _geom(kw)
    c = (z1 + z2) * m_t * math.cos(a_t) / (2.0 * float(kw["a"]))
    if not (-1.0 <= c <= 1.0):
        return None
    awt = math.acos(c)
    return (inv(awt) - inv(a_t)) / (2.0 * math.tan(R(a_n))) * (z1 + z2)


def _x_min_evolvente(z, cb, a_t):
    """Menor x (roda externa) para o círculo de referência deslocado não ficar abaixo do de base."""
    return -(abs(z) / (2.0 * cb)) * (1.0 - math.cos(a_t))


def _ta(z, x, m_n, beta, a_n):
    """Espessura de cabeça normalizada s_a/m_n (roda externa, cabeça padrão, sem chanfro)."""
    cb = math.cos(R(beta)); a_t = math.atan(math.tan(R(a_n)) / cb); m_t = m_n / cb
    d = m_t * z; db = d * math.cos(a_t); da = d + 2.0 * m_n * (1.0 + x)
    if da <= db:
        return -1.0
    s_t = m_t * (math.pi / 2.0 + 2.0 * x * math.tan(R(a_n)))
    a_a = math.acos(db / da)
    return da * (s_t / d + inv(a_t) - inv(a_a)) / m_n


def faixa_x1(kw, passo=0.01):
    """(x1_min, x1_max) viáveis para este par mantendo a distância entre centros dada (None se nenhum valor serve)."""
    z1, z2, m_n, beta, a_n, cb, a_t, m_t = _geom(kw)
    sx = _sum_x(kw)
    if sx is None:
        return None
    ok = []
    for k in range(-300, 301):
        x1 = k * passo; x2 = sx - x1
        if z1 > 0 and x1 < _x_min_evolvente(z1, cb, a_t):
            continue
        if z2 > 0:
            if x2 < _x_min_evolvente(z2, cb, a_t):
                continue
            if _ta(z2, x2, m_n, beta, a_n) < S_MIN:
                continue
        if _ta(z1, x1, m_n, beta, a_n) < S_MIN:
            continue
        ok.append(x1)
    return (min(ok), max(ok)) if ok else None


SX_MAX = 2.5       # |Σx| acima disso não existe engrenagem prática (dente pontiagudo ou sem recobrimento)


def a_max_viavel(kw, passo=0.25, limite=3.0):
    """Maior distância entre centros (a partir da padrão, em passos) para a qual ainda existe algum x₁ viável."""
    z1, z2, m_n, beta, a_n, cb, a_t, m_t = _geom(kw)
    a0 = abs(z1 + z2) * m_t * math.cos(a_t) / 2.0
    sgn = -1.0 if float(kw["a"]) < 0 else 1.0
    melhor = None; a = a0
    while a <= a0 * (1 + limite):
        k = dict(kw, a=sgn * a)
        if faixa_x1(k, 0.02) is None:
            break
        melhor = a; a += passo
    return a0, melhor


def _msg_faixa(kw):
    fx = faixa_x1(kw)
    if fx is None:
        return ""
    return f" Para esta distância entre centros, valores de x₁ entre {_f(fx[0])} e {_f(fx[1])} costumam funcionar."


def diagnosticar(kw, ex):
    """kw: kwargs do Engrenamento; ex: exceção do cálculo. Devolve {campo_kwarg: mensagem} (nunca vazio)."""
    try:
        return _diagnosticar(kw, ex) or _generico(kw, ex)
    except Exception:  # noqa: BLE001  (o diagnóstico nunca pode piorar o erro)
        return _generico(kw, ex)


def _generico(kw, ex):
    return {"x_pinhao": "Os valores atuais não geram um dente viável e o cálculo não pôde ser concluído. "
                        "Revise o deslocamento de perfil x₁, a distância entre centros a e o módulo (detalhe técnico: "
                        f"{type(ex).__name__}: {str(ex)[:80]})."}


def _diagnosticar(kw, ex):
    z1, z2, m_n, beta, a_n, cb, a_t, m_t = _geom(kw)
    x1 = kw.get("x_pinhao"); a = float(kw["a"])
    sx = _sum_x(kw)
    out = {}
    # 1) distância entre centros menor que a mínima geométrica
    a_min = abs(z1 + z2) * m_t * math.cos(a_t) / 2.0
    if sx is None or abs(a) < a_min - 1e-9:
        return {"a": f"A distância entre centros |a| = {_f(abs(a))} mm é menor que o mínimo geométrico {_f(a_min)} mm "
                     f"(m·(z₁+z₂)/2 com o ângulo de pressão α_n = {_f(a_n, 1)}°). Aumente a ou use a distância padrão (deixe o campo vazio)."}
    # 1b) distância entre centros que exige Σx absurdo: o culpado é a, não o x₁
    if abs(sx) > SX_MAX and z2 > 0:
        a0, amax = a_max_viavel(kw)
        return {"a": (f"A distância entre centros {_f(abs(a))} mm exige um somatório de deslocamentos Σx = {_f(sx)}, inviável (a distância padrão para este par é {_f(a0)} mm, "
                      f"com Σx = 0). Reduza a" + (f"; até cerca de {_f(amax)} mm ainda é possível." if amax else ".") + " Deixe o campo vazio para usar a distância padrão.")}
    # 2) deslocamento de perfil: flanco evolvente e dente pontiagudo (rodas externas)
    if x1 is not None:
        x2 = sx - x1
        if z1 > 0 and x1 < _x_min_evolvente(z1, cb, a_t):
            lim = _x_min_evolvente(z1, cb, a_t)
            out["x_pinhao"] = (f"x₁ = {_f(x1)} é menor que o mínimo {_f(lim)} para o pinhão (z₁ = {z1}, α_n = {_f(a_n, 1)}°): "
                               f"abaixo disso o círculo de referência deslocado cai dentro do círculo de base e o dente deixa de ter flanco evolvente."
                               + _msg_faixa(kw))
        elif z2 > 0 and x2 < _x_min_evolvente(z2, cb, a_t):
            lim = _x_min_evolvente(z2, cb, a_t)
            out["x_pinhao"] = (f"Com a distância entre centros dada, Σx = {_f(sx)} e a coroa fica com x₂ = Σx − x₁ = {_f(x2)}, menor que o mínimo "
                               f"{_f(lim)} para z₂ = {z2}: o dente da coroa perde o flanco evolvente. Diminua x₁ ou aumente a distância entre centros." + _msg_faixa(kw))
        else:
            for nome, z, x, campo in (("do pinhão", z1, x1, "x_pinhao"), ("da coroa", z2, x2, "x_pinhao" if z2 > 0 else "a")):
                if z > 0 and _ta(z, x, m_n, beta, a_n) < S_MIN:
                    sa = _ta(z, x, m_n, beta, a_n)
                    out[campo] = (f"O dente {nome} fica pontiagudo (espessura de cabeça ≈ {_f(max(sa, 0), 2)}·m_n; o mínimo usual é {_f(S_MIN, 1)}·m_n) "
                                  f"com x = {_f(x)}: o deslocamento de perfil é grande demais para z = {z}. Reduza x₁ ou a distância entre centros." + _msg_faixa(kw))
                    break
    return out or None
