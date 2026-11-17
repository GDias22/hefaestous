# -*- coding: utf-8 -*-
"""Relatório HTML (Jinja2) e exportações JSON/XLSX de uma sessão."""
import base64
import io
import json
import math
import os
from datetime import datetime

from jinja2 import Environment, FileSystemLoader, select_autoescape

from ..bootstrap import FRONTEND
from ..params.metadata import PARAMS
from ..services.serialize import to_jsonable

HERE = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(os.path.join(HERE, "templates")), autoescape=select_autoescape(["html"]))


def _fmt(v, nd=4):
    if v is None:
        return "—"
    if isinstance(v, bool):
        return "sim" if v else "não"
    if isinstance(v, (int,)) and not isinstance(v, bool):
        return str(v)
    if isinstance(v, float):
        if math.isnan(v) or math.isinf(v):
            return "—"
        a = abs(v)
        if a != 0 and (a < 1e-3 or a >= 1e7):
            return f"{v:.3e}"
        s = f"{v:.{2 if a >= 1000 else nd}f}".rstrip("0").rstrip(".")
        return s if s not in ("", "-0") else "0"
    return str(v)


env.filters["fmt"] = _fmt


def _logo_data_uri(nome):
    p = os.path.join(FRONTEND, "img", nome)
    if not os.path.exists(p):
        return ""
    mime = "image/svg+xml" if nome.endswith(".svg") else "image/png"
    with open(p, "rb") as f:
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"


def entradas_rotuladas(payload, stage_prefix=""):
    """Lista [(label, valor, unidade)] de um payload de malha, na ordem do metadata."""
    out = []
    for key, meta in PARAMS.items():
        if meta["stage"] != "geometria" or key not in payload:
            continue
        v = payload[key]
        if isinstance(v, dict):
            continue
        out.append((meta["label"], _fmt(v), meta.get("unit") or ""))
    return out


def subobjetos(payload):
    """Materiais/ferramentas/lubrificante: nome do preset ou campos personalizados."""
    res = []
    for key, titulo in (("material_pinhao", "Material do pinhão"), ("material_coroa", "Material da coroa"),
                        ("ferramenta_pinhao", "Ferramenta do pinhão"), ("ferramenta_coroa", "Ferramenta da coroa"), ("lubrificante", "Lubrificante")):
        v = payload.get(key)
        if isinstance(v, dict) and v.get("preset"):
            res.append((titulo, f"preset: {v['preset']}", []))
        elif isinstance(v, dict):
            campos = [(PARAMS[k]["label"], _fmt(val), PARAMS[k].get("unit") or "") for k, val in v.items() if k in PARAMS]
            res.append((titulo, "personalizado", campos))
    return res


def render_relatorio(sessao, session_id, svgs=None, extras=None):
    tpl = env.get_template("relatorio.html")
    geometria = sessao.get("geometria") or []
    entradas = sessao.get("entradas_geometria") or []
    proj = sessao.get("projeto") or {}
    if proj and not entradas:
        # projeto novo (v2): monta as entradas rotuladas a partir dos payloads de malha gerados pelo montador
        try:
            from ..projeto.modelo import Projeto
            from ..projeto.montar import montar
            mont = montar(Projeto.model_validate(proj))
            entradas = []
            for pl in mont["malhas"]:
                pl = {k: v for k, v in pl.items() if not k.startswith("_")}
                entradas.append(pl)
        except Exception:  # noqa: BLE001
            entradas = []
    ctx = dict(
        titulo=sessao.get("titulo") or session_id, session_id=session_id, data=datetime.now().strftime("%d/%m/%Y %H:%M"),
        transmissao=sessao.get("transmissao"), projeto=proj,
        logo_unicamp=_logo_data_uri("logo-unicamp.svg"), logo_fem=_logo_data_uri("logo-fem.png"), logo_app=_logo_data_uri("icon-mark.png"),
        cinematica=sessao.get("cinematica"), geometria=geometria,   # lista completa (None = malha não calculada), alinhada a entradas/sobremetal
        # pares (entradas, geometria) alinhados por índice; malhas com erro de cálculo ficam sem geometria
        entradas=[(entradas_rotuladas(e), subobjetos(e), (geometria[i] if i < len(geometria) else None)) for i, e in enumerate(entradas)],
        tensoes=sessao.get("tensoes"), entradas_tensoes=sessao.get("entradas_tensoes") or {},
        svgs=svgs or {}, extras=extras or {}, PARAMS=PARAMS,
        engenheiro=(entradas[0].get("Proj") if entradas and isinstance(entradas[0], dict) else None) or (proj.get("operacao") or {}).get("Proj"),
    )
    return tpl.render(**ctx)


def exportar_json(sessao, session_id):
    d = {k: v for k, v in sessao.items() if k not in ("malhas", "analise")}
    d["session_id"] = session_id
    return json.dumps(to_jsonable(d), ensure_ascii=False, indent=1)


def exportar_xlsx(sessao, session_id):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter

    wb = Workbook()
    head_font = Font(bold=True, color="FFFFFF"); head_fill = PatternFill("solid", fgColor="003882")
    sec_font = Font(bold=True, color="B8282C")

    def cab(ws, cols):
        ws.append(cols)
        for c in ws[ws.max_row]:
            c.font = head_font; c.fill = head_fill; c.alignment = Alignment(horizontal="center")

    def largura(ws):
        for i, col in enumerate(ws.columns, start=1):
            m = max((len(str(c.value)) if c.value is not None else 0) for c in col)
            ws.column_dimensions[get_column_letter(i)].width = min(60, max(10, m + 2))

    ws = wb.active; ws.title = "Entradas"
    cab(ws, ["Malha", "Parâmetro", "Valor", "Unidade"])
    for i, e in enumerate(sessao.get("entradas_geometria") or [], start=1):
        for label, v, u in entradas_rotuladas(e):
            ws.append([i, label, v, u])
        for titulo, modo, campos in subobjetos(e):
            ws.append([i, titulo, modo, ""])
            for label, v, u in campos:
                ws.append([i, f"   {label}", v, u])
    largura(ws)

    if sessao.get("cinematica"):
        ws = wb.create_sheet("Cinemática")
        cab(ws, ["Grandeza", "Valor"])
        cin = sessao["cinematica"]
        for bloco in ("entradas", "cinematica", "candidato"):
            d = cin.get(bloco) if isinstance(cin, dict) else None
            if isinstance(d, dict):
                ws.append([bloco.upper(), ""]); ws[ws.max_row][0].font = sec_font
                for k, v in d.items():
                    if not isinstance(v, (dict, list)):
                        ws.append([k, v])
        largura(ws)

    for i, g in enumerate(sessao.get("geometria") or [], start=1):
        if not g:
            ws = wb.create_sheet(f"Geometria_{i}"[:31]); ws.append(["Malha não calculada (erro de entrada na etapa B)"]); continue
        ws = wb.create_sheet(f"Geometria_{i}"[:31])
        cab(ws, ["Seção", "Grandeza", "Unidade", "Pinhão / Valor", "Coroa"])
        for sec in g["secoes"]:
            for l in sec["linhas"]:
                if "pc" in l:
                    ws.append([sec["titulo"], l["label"], l.get("unit") or "", l["pc"][0], l["pc"][1]])
                else:
                    ws.append([sec["titulo"], l["label"], l.get("unit") or "", l["v"], None])
        largura(ws)

    t = sessao.get("tensoes")
    if t:
        ws = wb.create_sheet("Tensões")
        cab(ws, ["Malha", "Seção", "Grandeza", "Unidade", "Pinhão / Valor", "Coroa"])
        for m in t["malhas"]:
            for sec in m["secoes"]:
                for l in sec["linhas"]:
                    if "pc" in l:
                        ws.append([m["indice"], sec["titulo"], l["label"], l.get("unit") or "", l["pc"][0], l["pc"][1]])
                    else:
                        ws.append([m["indice"], sec["titulo"], l["label"], l.get("unit") or "", l["v"], None])
        largura(ws)

    ws = wb.create_sheet("Avisos")
    cab(ws, ["Origem", "Nível", "Aviso"])
    for i, g in enumerate(sessao.get("geometria") or [], start=1):
        for a in (g or {}).get("avisos", []):
            ws.append([f"Geometria malha {i}", a["nivel"], a["texto"]])
    if t:
        for m in t["malhas"]:
            for a in m.get("avisos", []):
                ws.append([f"Tensões malha {m['indice']}", a["nivel"], a["texto"]])
    largura(ws)

    bio = io.BytesIO(); wb.save(bio); return bio.getvalue()
