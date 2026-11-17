# -*- coding: utf-8 -*-
"""Textos didáticos extraídos do caderno (web/backend/docs/fatores.json, gerado por web/tools/extrair_docs.py)."""
import json
import os

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/docs", tags=["docs"])
_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "fatores.json")
_cache = {"mtime": None, "lista": [], "por_chave": {}}


def carregar():
    try:
        mt = os.path.getmtime(_PATH)
    except OSError:
        return _cache
    if _cache["mtime"] != mt:
        with open(_PATH, encoding="utf-8") as f:
            lista = json.load(f)
        _cache.update(mtime=mt, lista=lista, por_chave={d["chave"]: d for d in lista})
    return _cache


def doc(chave):
    return carregar()["por_chave"].get(chave)


@router.get("")
def indice():
    return [{"chave": d["chave"], "titulo": d["titulo"], "figuras": len(d.get("figuras") or [])} for d in carregar()["lista"]]


@router.get("/{chave}")
def obter(chave: str):
    d = doc(chave)
    if d is None:
        raise HTTPException(404, "tema não encontrado")
    return d
