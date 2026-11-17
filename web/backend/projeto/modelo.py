# -*- coding: utf-8 -*-
"""Modelo de projeto (Pydantic). Os dicionários de roda/malha são validados campo a campo pelo metadata no montador,
por isso aqui ficam como Dict[str, Any] (a interface pode guardar só o que o usuário alterou)."""
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field, model_validator


class Entrada(BaseModel):
    n: float = 1450.0
    T: float = 100.0
    irregularidade_motora: str = "Choque uniforme"
    irregularidade_movida: str = "Choque leve"
    Ka_imposto: Optional[float] = None
    i_alvo: Optional[float] = None     # redução desejada (alimenta a busca de dentes)
    tol_i: Optional[float] = None      # tolerância absoluta da redução na busca


class Analise(BaseModel):
    k: Optional[float] = 100
    Ck: Optional[float] = None
    K_Hbeta_imposto: Optional[float] = None


class Estagio(BaseModel):
    nome: str = "Estágio"
    eta: float = Field(0.98, gt=0, le=1.0)
    malha: Dict[str, Any] = {}
    pinhao: Dict[str, Any] = {}
    coroa: Dict[str, Any] = {}
    analise: Analise = Analise()


def migrar_planeta(d):
    """Formato antigo (um único `planeta` com z_ext/z_int e overrides ext/int) -> `planeta_maior` e `planeta_menor`."""
    if not isinstance(d, dict) or "planeta" not in d:
        return d
    d = dict(d)
    pla = dict(d.pop("planeta") or {})
    ext, inte = pla.pop("ext", None) or {}, pla.pop("int", None) or {}
    z_ext, z_int = pla.pop("z_ext", None), pla.pop("z_int", None)
    if "planeta_maior" not in d:
        d["planeta_maior"] = {**pla, **ext, "z": z_ext}
    if "planeta_menor" not in d:
        d["planeta_menor"] = {**pla, **inte, "z": z_int if z_int is not None else z_ext}
    return d


class Planetario(BaseModel):
    tipo: Literal["Simples", "Composto"] = "Composto"
    N_cp: int = Field(3, ge=1, le=12)
    Ky: float = Field(1.05, ge=1.0, le=1.6)
    entrada: Literal["sol", "porta-planetas", "anelar"] = "sol"
    saida: Literal["sol", "porta-planetas", "anelar"] = "porta-planetas"
    modo: Literal["fixo", "diferencial"] = "fixo"   # fixo: o 3º membro é preso à carcaça. diferencial: o 3º membro gira a n_livre (2 graus de liberdade)
    n_livre: float = 0.0                              # rotação imposta ao 3º membro no modo diferencial [rpm, com sinal; sol positivo]
    sol: Dict[str, Any] = {}
    planeta_maior: Dict[str, Any] = {}   # z + campos de roda; engrena com o sol (malha externa)
    planeta_menor: Dict[str, Any] = {}   # z + campos de roda; engrena com a anelar (malha interna). Ignorado no Simples
    anelar: Dict[str, Any] = {}          # z (positivo), D_ext (diâmetro externo do aro), campos de roda
    malha_ext: Dict[str, Any] = {}
    malha_int: Dict[str, Any] = {}       # a é derivado (= -a_ext)
    analise_ext: Analise = Analise(k=100)
    analise_int: Analise = Analise(k=50)

    @model_validator(mode="before")
    @classmethod
    def _migrar(cls, d):
        return migrar_planeta(d)


class Projeto(BaseModel):
    model_config = {"extra": "ignore"}
    nome: str = "Novo projeto"
    tipo: Literal["trem", "planetario"] = "trem"
    entrada: Entrada = Entrada()
    operacao: Dict[str, Any] = {}
    metodos: Dict[str, Any] = {}
    estagios: List[Estagio] = []
    planetario: Optional[Planetario] = None
    layout: Dict[str, Any] = {}        # eixos e mancais (layout.py): {ativo, eixos:{id:{d_sh, L, torque, rodas:{key:{a, fixacao, arranjo}}}}}
