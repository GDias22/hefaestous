# -*- coding: utf-8 -*-
"""Sessões de cálculo: guarda em memória os objetos (Engrenamento, Analise) e em disco o JSON de entradas/resultados.

Toda leitura para serialização/relatório usa `snapshot()` (cópia feita sob o lock), para que um `salvar` concorrente
não altere o dict durante a iteração."""
import copy
import json
import os
import re
import threading
import uuid
from datetime import datetime

from fastapi import HTTPException

from .bootstrap import SESSIONS
from .services.serialize import to_jsonable

_lock = threading.RLock()
_mem = {}   # session_id -> {"malhas": [Engrenamento,...], "analise": Analise|None, ...}
_ID_RE = re.compile(r"^[A-Za-z0-9_-]{1,64}$")
NAO_SERIALIZAVEIS = ("malhas", "analise")


def validar_id(session_id):
    if not session_id or not _ID_RE.match(session_id):
        raise HTTPException(400, "session_id inválido")
    return session_id


def nova_sessao():
    return datetime.now().strftime("%Y%m%d-%H%M%S-") + uuid.uuid4().hex[:6]


def caminho(session_id, ext="json"):
    validar_id(session_id)
    return os.path.join(SESSIONS, f"{session_id}.{ext}")


def salvar(session_id, dados):
    with _lock:
        _mem.setdefault(session_id, {}).update(dados)
        disco = to_jsonable({k: v for k, v in _mem[session_id].items() if k not in NAO_SERIALIZAVEIS})
    tmp = caminho(session_id) + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(disco, f, ensure_ascii=False, indent=1)
    os.replace(tmp, caminho(session_id))
    return session_id


def obter(session_id):
    """Dict vivo da sessão (uso interno). Para serializar use snapshot()."""
    validar_id(session_id)
    with _lock:
        s = _mem.get(session_id)
        if s is not None:
            return s
    p = caminho(session_id)
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            s = json.load(f)
        with _lock:
            _mem.setdefault(session_id, {}).update(s)
            return _mem[session_id]
    return None


def snapshot(session_id):
    """Cópia JSON-segura (sem objetos de cálculo) feita sob o lock."""
    s = obter(session_id)
    if s is None:
        return None
    with _lock:
        return copy.deepcopy(to_jsonable({k: v for k, v in s.items() if k not in NAO_SERIALIZAVEIS}))


def malhas(session_id):
    """Objetos Engrenamento da sessão (lista alinhada às entradas; None = malha que falhou).
    Se a sessão veio do disco (servidor reiniciado), reconstrói a partir das entradas."""
    s = obter(session_id)
    if s is None:
        return None
    with _lock:
        objs = s.get("malhas")
    if objs is None and s.get("projeto"):
        from .projeto.calcular import calcular_json
        try:
            _, objs, analises = calcular_json(s["projeto"], True)
        except Exception:  # noqa: BLE001
            objs = []
        with _lock:
            s["malhas"] = objs
            s["analise"] = analises[0] if analises else None
    elif objs is None and s.get("entradas_geometria"):
        from .services.geometria import calcular_malha
        objs = []
        for payload in s["entradas_geometria"]:
            try:
                objs.append(calcular_malha(payload))
            except Exception:  # noqa: BLE001
                objs.append(None)
        with _lock:
            s["malhas"] = objs
    return objs


def listar(limit=50):
    arqs = sorted((f for f in os.listdir(SESSIONS) if f.endswith(".json")), reverse=True)[:limit]
    out = []
    for a in arqs:
        try:
            with open(os.path.join(SESSIONS, a), encoding="utf-8") as f:
                d = json.load(f)
            out.append({"session_id": a[:-5], "titulo": d.get("titulo"), "criado": d.get("criado"),
                        "etapas": [k for k in ("cinematica", "geometria", "tensoes") if d.get(k)]})
        except Exception:
            continue
    return out
