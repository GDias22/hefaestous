# -*- coding: utf-8 -*-
"""Formato de arquivo do app: `.fem` (JSON UTF-8, legível e editável à mão).

Estrutura:
  formato   "FEM-Planetaria"         identifica o arquivo (rejeita JSON qualquer)
  versao    1                        versão do formato; o app abre versões <= à sua e recusa as mais novas
  app       texto                    quem gravou
  salvo_em  ISO-8601
  nome      nome do projeto
  projeto   o projeto COMPLETO (entradas, arquitetura, rodas, layout, operação, métodos) — é o que se recarrega e edita
  resumo    foto dos resultados no momento de salvar (informativo; o app recalcula ao abrir)

Projetos gravados em versões anteriores do modelo (ex.: um único `planeta` com z_ext/z_int) são migrados em `ler()`
pelo próprio modelo Pydantic (`Projeto`)."""
from datetime import datetime

from .projeto.calcular import calcular_json
from .projeto.modelo import Projeto

FORMATO = "FEM-Planetaria"
VERSAO = 1
EXTENSAO = ".fem"
APP = "HEFAESTOUS · Dimensionamento de engrenagens"   # FORMATO permanece "FEM-Planetaria" para abrir os .fem já salvos


class ErroFem(ValueError):
    """Arquivo .fem inválido (mensagem em português, mostrada ao usuário)."""


def resumir(res):
    """Foto compacta dos resultados (serializável) para guardar no arquivo."""
    if not res:
        return None
    t = res.get("transmissao") or {}
    r = res.get("resumo") or {}
    seg = []
    for m in res.get("malhas") or []:
        for c in m.get("cards") or []:
            seg.append({"malha": m.get("apelido"), "fator": c.get("fator"), "roda": c.get("roda"), "valor": c.get("valor"), "minimo": c.get("minimo"), "status": c.get("status")})
    return {"tipo": t.get("tipo"), "i_total": t.get("i_total"), "eta_total": t.get("eta_total"), "calculo_ok": bool(res.get("ok")),
            "todos_atendem": r.get("todos_atendem"), "pior": r.get("pior"), "problemas": sorted((res.get("erros") or {}).keys()), "seguranca": seg}


def empacotar(projeto, com_resumo=True):
    """projeto (dict da interface) -> dict do arquivo .fem. Valida o projeto; levanta ErroFem se não for um projeto."""
    try:
        proj = Projeto.model_validate(projeto)
    except Exception as ex:  # noqa: BLE001
        raise ErroFem(f"Projeto inválido: {ex}") from ex
    dados = proj.model_dump()
    resumo = None
    if com_resumo:
        try:
            res, _, _ = calcular_json(dados, True)
            resumo = resumir(res)
        except Exception:  # noqa: BLE001  (o arquivo vale mesmo que o cálculo falhe: o projeto é o que importa)
            resumo = None
    return {"formato": FORMATO, "versao": VERSAO, "app": APP, "salvo_em": datetime.now().isoformat(timespec="seconds"),
            "nome": dados.get("nome") or "Projeto", "projeto": dados, "resumo": resumo}


def ler(conteudo):
    """dict (JSON já lido do arquivo) -> {projeto, nome, salvo_em, versao, resumo, migrado}. Levanta ErroFem com mensagem clara."""
    if not isinstance(conteudo, dict):
        raise ErroFem("O arquivo não é um projeto .fem (o conteúdo não é um objeto JSON).")
    if conteudo.get("formato") != FORMATO:
        raise ErroFem("O arquivo não é um projeto .fem deste aplicativo (campo \"formato\" ausente ou diferente).")
    v = conteudo.get("versao")
    if not isinstance(v, int) or v < 1:
        raise ErroFem("O arquivo .fem não informa uma versão válida do formato.")
    if v > VERSAO:
        raise ErroFem(f"O arquivo foi gravado por uma versão mais nova do aplicativo (formato {v}; esta versão abre até o {VERSAO}). Atualize o aplicativo.")
    bruto = conteudo.get("projeto")
    if not isinstance(bruto, dict):
        raise ErroFem("O arquivo .fem não contém o campo \"projeto\".")
    planeta_antigo = isinstance(bruto.get("planetario"), dict) and "planeta" in bruto["planetario"]
    try:
        proj = Projeto.model_validate(bruto)
    except Exception as ex:  # noqa: BLE001
        raise ErroFem(f"O projeto dentro do arquivo é inválido: {ex}") from ex
    return {"projeto": proj.model_dump(), "nome": conteudo.get("nome") or proj.nome, "salvo_em": conteudo.get("salvo_em"), "versao": v,
            "resumo": conteudo.get("resumo"), "migrado": planeta_antigo}
