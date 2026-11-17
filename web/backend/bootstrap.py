# -*- coding: utf-8 -*-
"""Prepara o ambiente e importa os módulos de cálculo existentes (sem gerar PDFs).

    from backend.bootstrap import G, A, Eq, ROOT, FIGURAS, SESSIONS
"""
import os
import sys

os.environ.setdefault("ENGR_SEM_PDF", "1")

WEB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(WEB)
REV = os.path.join(ROOT, "_revisao")
FIGURAS = os.path.join(ROOT, "Figuras")
SESSIONS = os.path.join(WEB, "sessions")
FRONTEND = os.path.join(WEB, "frontend")
os.makedirs(SESSIONS, exist_ok=True)

for p in (REV, ROOT):
    if p not in sys.path:
        sys.path.insert(0, p)

import Equações_dimensionamento as Eq      # noqa: E402
import Dimensionamento_geometrico as G     # noqa: E402  (classes, funções e presets; exemplos ficam em exemplos_geometria)
import Analise_tensoes as A                # noqa: E402  (classe Analise_de_tensao; exemplos em exemplos_tensoes)

__all__ = ["G", "A", "Eq", "ROOT", "REV", "FIGURAS", "SESSIONS", "FRONTEND", "WEB"]
