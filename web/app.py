# -*- coding: utf-8 -*-
"""Interface web local do dimensionamento de engrenagens planetárias (FEM/Unicamp — LAMAR).

Uso:  python web/app.py [--port 8765] [--no-browser]
Requer o venv Python 3.13 em web/.venv313 (criado com web/requirements.txt). Se executado com outro
interpretador, relança a si mesmo com o venv quando ele existir.
"""
import argparse
import os
import sys
import threading
import webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
VENV_PY = os.path.join(HERE, ".venv313", "Scripts", "python.exe")


def _relaunch_in_venv():
    if os.path.exists(VENV_PY) and os.path.abspath(sys.executable).lower() != os.path.abspath(VENV_PY).lower():
        os.execv(VENV_PY, [VENV_PY] + sys.argv)


def create_app():
    from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles
    from fastapi.responses import FileResponse

    sys.path.insert(0, HERE)
    from backend.bootstrap import FRONTEND
    from backend.api import meta, geometria, tensoes
    app = FastAPI(title="HEFAESTOUS · Dimensionamento de engrenagens", version="0.2")
    from backend import logs as _logs
    _logs.instalar(app)          # logs\servidor.log + erros.txt (histórico de problemas) na pasta de instalação
    for r in (meta.router, geometria.router, tensoes.router):
        app.include_router(r)
    for nome in ("cinematica", "perfil", "export", "projeto", "docs", "fem", "atualizacao", "vida"):
        mod = __import__(f"backend.api.{nome}", fromlist=["router"])
        app.include_router(mod.router)

    # Identificador do build = instante da modificação mais recente no frontend (sem node_modules). Os arquivos são servidos em
    # /s/<build>/... e o index.html é reescrito para esse prefixo: a cada alteração + reinício a URL muda e o navegador NÃO pode
    # reaproveitar módulos antigos do cache (os `import './x.js'` relativos herdam o prefixo novo). /static continua para compat.
    build = _build_id(FRONTEND)
    app.state.build = build

    @app.get("/")
    def index():
        from fastapi.responses import HTMLResponse
        with open(os.path.join(FRONTEND, "index.html"), encoding="utf-8") as f:
            html = f.read().replace("/static/", f"/s/{build}/")
        return HTMLResponse(html, headers={"Cache-Control": "no-store"})

    @app.get("/s/{build_id}/{caminho:path}")
    def estatico_versionado(build_id: str, caminho: str):
        from fastapi import HTTPException
        base = os.path.realpath(FRONTEND)
        alvo = os.path.realpath(os.path.join(base, caminho))
        if not alvo.startswith(base + os.sep) or not os.path.isfile(alvo):
            raise HTTPException(404)
        cache = "public, max-age=31536000, immutable" if build_id == build else "no-store"
        return FileResponse(alvo, headers={"Cache-Control": cache})

    app.mount("/static", StaticFiles(directory=FRONTEND), name="static")

    @app.middleware("http")
    async def sem_cache_estatico(request, call_next):
        resp = await call_next(request)
        if request.url.path.startswith("/static/"):
            resp.headers["Cache-Control"] = "no-cache, must-revalidate"
        return resp
    return app


def _build_id(frontend):
    """mtime mais recente (segundos) entre os arquivos do frontend, ignorando node_modules e pastas ocultas."""
    m = 0
    for raiz, dirs, arqs in os.walk(frontend):
        dirs[:] = [d for d in dirs if d != "node_modules" and not d.startswith(".")]
        for a in arqs:
            try:
                m = max(m, int(os.path.getmtime(os.path.join(raiz, a))))
            except OSError:
                pass
    return str(m)


def _porta_em_uso(host, port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.3)
        return s.connect_ex((host, port)) == 0


def _e_nosso_app(url):
    """True se quem ocupa a porta já é esta interface (então basta abrir o navegador)."""
    try:
        import urllib.request
        with urllib.request.urlopen(url + "api/meta/params", timeout=2) as r:
            return r.status == 200 and b'"stages"' in r.read(200)
    except Exception:  # noqa: BLE001
        return False


def _abrir_navegador(url):
    """Abre a URL quando o servidor responder (até 20 s); usa o navegador padrão do Windows como fallback."""
    import time
    import urllib.request
    for _ in range(80):
        try:
            urllib.request.urlopen(url, timeout=1).read(10)
            break
        except Exception:  # noqa: BLE001
            time.sleep(0.25)
    try:
        if not webbrowser.open(url):
            raise RuntimeError("webbrowser.open devolveu False")
    except Exception:  # noqa: BLE001
        try:
            os.startfile(url)  # noqa: S606  (Windows: navegador padrão)
        except Exception as ex:  # noqa: BLE001
            print(f"Não consegui abrir o navegador automaticamente ({ex}). Abra manualmente: {url}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--no-browser", action="store_true")
    ap.add_argument("--reload", action="store_true")
    ap.add_argument("--auto-encerrar", action="store_true", help="encerra o servidor quando a última aba da interface fechar (usado pelo HEFAESTOUS.exe)")
    args = ap.parse_args()
    if not args.reload:
        _relaunch_in_venv()
    import uvicorn
    port = args.port
    url = f"http://{args.host}:{port}/"
    if _porta_em_uso(args.host, port):
        if _e_nosso_app(url):
            print(f"A interface já está rodando em {url} — abrindo o navegador.")
            if not args.no_browser:
                _abrir_navegador(url)
            return
        for cand in range(port + 1, port + 20):
            if not _porta_em_uso(args.host, cand):
                print(f"Porta {port} ocupada por outro programa; usando {cand}.")
                port = cand; url = f"http://{args.host}:{port}/"
                break
        else:
            print(f"Nenhuma porta livre entre {args.port} e {args.port + 19}."); sys.exit(1)
    if not args.no_browser:
        threading.Thread(target=_abrir_navegador, args=(url,), daemon=True).start()
    print("=" * 64)
    print(f"  Interface em  {url}")
    print("  Deixe esta janela aberta enquanto usa o programa (Ctrl+C encerra).")
    print("=" * 64, flush=True)
    try:
        if args.reload:
            uvicorn.run("app:create_app", factory=True, host=args.host, port=port, reload=True, app_dir=HERE)
        else:
            app = create_app()
            if args.auto_encerrar:
                from backend.api import vida
                vida.ativar()
            uvicorn.run(app, host=args.host, port=port, log_level="info")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
