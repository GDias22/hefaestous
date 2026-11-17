# -*- coding: utf-8 -*-
"""Logs do HEFAESTOUS — tudo em arquivo, nada em terminal.

Pasta base = HEFAESTOUS_HOME (definida pelo lançador = pasta de instalação) ou, em desenvolvimento, a raiz do projeto.
  <base>\\logs\\servidor.log   log completo (uvicorn, requisições, tracebacks); rotaciona em 5 MB × 3 arquivos
  <base>\\erros.txt            HISTÓRICO LEGÍVEL só dos problemas: data/hora, o que o usuário estava fazendo (rota),
                              mensagem e traceback. É o arquivo para mandar junto com um relato de bug.

`instalar(app)` registra: logging de arquivo para uvicorn/fastapi/backend, handler global de exceções não tratadas
(responde 500 em JSON e grava em erros.txt), e um middleware que anota respostas 5xx/erros de validação em erros.txt.
"""
import logging
import logging.handlers
import os
import sys
import time
import traceback

WEB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.environ.get("HEFAESTOUS_HOME") or os.path.dirname(WEB)
LOGS = os.path.join(BASE, "logs")
ERROS = os.path.join(BASE, "erros.txt")
_LOG = logging.getLogger("hefaestous")
_pronto = False


def preparar_logging():
    """Logging de arquivo para o processo inteiro (idempotente)."""
    global _pronto
    if _pronto:
        return
    _pronto = True
    os.makedirs(LOGS, exist_ok=True)
    fmt = logging.Formatter("%(asctime)s %(levelname)-7s %(name)s: %(message)s", "%Y-%m-%d %H:%M:%S")
    fh = logging.handlers.RotatingFileHandler(os.path.join(LOGS, "servidor.log"), maxBytes=5_000_000, backupCount=3, encoding="utf-8")
    fh.setFormatter(fmt)
    raiz = logging.getLogger()
    raiz.setLevel(logging.INFO)
    raiz.addHandler(fh)
    for nome in ("uvicorn", "uvicorn.error", "uvicorn.access", "fastapi"):
        lg = logging.getLogger(nome); lg.handlers = [fh]; lg.propagate = False; lg.setLevel(logging.INFO)
    # exceções fora do FastAPI (threads, startup)
    def _excepthook(tipo, val, tb):
        registrar_erro("exceção não tratada no processo", "".join(traceback.format_exception(tipo, val, tb)))
    sys.excepthook = _excepthook
    try:
        import threading
        threading.excepthook = lambda a: registrar_erro(f"exceção na thread {a.thread.name if a.thread else '?'}", "".join(traceback.format_exception(a.exc_type, a.exc_value, a.exc_traceback)))
    except Exception:  # noqa: BLE001
        pass


def registrar_erro(titulo, detalhe="", contexto=""):
    """Acrescenta uma entrada em erros.txt (e no log). Nunca lança."""
    try:
        os.makedirs(BASE, exist_ok=True)
        with open(ERROS, "a", encoding="utf-8") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {titulo}\n")
            if contexto:
                f.write(f"    onde: {contexto}\n")
            if detalhe:
                f.write("".join("    " + l + "\n" for l in str(detalhe).rstrip().splitlines()))
            f.write("\n")
        _LOG.error("%s | %s", titulo, contexto)
    except Exception:  # noqa: BLE001
        pass


def instalar(app):
    """Liga o logging de arquivo e os handlers de erro no FastAPI."""
    from fastapi import Request
    from fastapi.responses import JSONResponse
    from fastapi.exceptions import RequestValidationError
    from starlette.exceptions import HTTPException as StarletteHTTPException

    preparar_logging()
    _LOG.info("HEFAESTOUS iniciando — python %s — base %s", sys.version.split()[0], BASE)

    @app.exception_handler(Exception)
    async def _nao_tratada(request: Request, exc: Exception):
        registrar_erro(f"erro interno: {type(exc).__name__}: {exc}", traceback.format_exc(), f"{request.method} {request.url.path}")
        return JSONResponse(status_code=500, content={"detail": {"mensagem": f"Erro interno: {type(exc).__name__}: {exc}",
                                                                 "dica": "Detalhes gravados em erros.txt na pasta do programa."}})

    @app.exception_handler(RequestValidationError)
    async def _validacao(request: Request, exc: RequestValidationError):
        registrar_erro("entrada inválida (422)", str(exc)[:4000], f"{request.method} {request.url.path}")
        return JSONResponse(status_code=422, content={"detail": exc.errors()})

    @app.exception_handler(StarletteHTTPException)
    async def _http(request: Request, exc: StarletteHTTPException):
        # 4xx de negócio (ex.: perfil inválido) viram histórico também — ajudam a entender o que o usuário tentou; 404 de arquivo não.
        if exc.status_code >= 500 or (exc.status_code in (400, 422, 501) and request.url.path.startswith("/api/")):
            d = exc.detail if isinstance(exc.detail, str) else (exc.detail.get("mensagem") if isinstance(exc.detail, dict) else str(exc.detail))
            tr = exc.detail.get("trace", "") if isinstance(exc.detail, dict) else ""
            registrar_erro(f"HTTP {exc.status_code}: {d}", tr, f"{request.method} {request.url.path}")
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

    return app
