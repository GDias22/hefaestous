# -*- coding: utf-8 -*-
"""Conversão de objetos de cálculo em estruturas JSON."""
import math
import numbers


def num(v):
    """Converte escalares numpy/float em float JSON-seguro (NaN/inf -> None)."""
    try:
        import numpy as np
        if isinstance(v, np.generic):
            v = v.item()
    except Exception:
        pass
    if isinstance(v, bool):
        return v
    if isinstance(v, numbers.Integral):
        return int(v)
    if isinstance(v, numbers.Real):
        f = float(v)
        return None if (math.isnan(f) or math.isinf(f)) else f
    return v


def to_jsonable(obj, _depth=0):
    """Converte recursivamente dicts/listas/objetos simples em JSON. Objetos com __dict__ viram dict
    (até profundidade 2) para evitar ciclos; o resto vira str."""
    if obj is None or isinstance(obj, (str, bool)):
        return obj
    n = num(obj)
    if isinstance(n, (int, float)) or n is None:
        return n
    if isinstance(obj, dict):
        return {str(k): to_jsonable(v, _depth + 1) for k, v in obj.items()}
    if isinstance(obj, (list, tuple, set)):
        return [to_jsonable(v, _depth + 1) for v in obj]
    try:
        import numpy as np
        if isinstance(obj, np.ndarray):
            return [to_jsonable(v, _depth + 1) for v in obj.tolist()]
    except Exception:
        pass
    if hasattr(obj, "__dict__") and _depth < 2:
        return {k: to_jsonable(v, _depth + 1) for k, v in vars(obj).items() if not k.startswith("_")}
    return str(obj)


def vars_numericos(obj):
    """Todos os atributos escalares (número, str, bool, None) de um objeto."""
    out = {}
    for k, v in vars(obj).items():
        if k.startswith("_"):
            continue
        n = num(v)
        if n is None or isinstance(n, (int, float, str, bool)):
            out[k] = n
        elif isinstance(v, (list, tuple)) and all(isinstance(x, str) for x in v):
            out[k] = list(v)
    return out


def r(v, nd=4):
    v = num(v)
    if isinstance(v, float):
        return round(v, nd)
    return v
