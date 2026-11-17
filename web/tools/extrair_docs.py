# -*- coding: utf-8 -*-
"""Extrai os textos didáticos (markdown com fórmulas LaTeX e figuras) de Dimensionamento.ipynb para
web/backend/docs/fatores.json: lista de {chave, titulo, markdown, figuras}. Re-execute quando o notebook mudar.

Uso: python web/tools/extrair_docs.py   (qualquer Python com nbformat)"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.dirname(HERE)
ROOT = os.path.dirname(WEB)
OUT = os.path.join(WEB, "backend", "docs", "fatores.json")

# título (regex, sem acento-sensibilidade) -> chave
MAPA = [
    (r"FATOR DIN[ÂA]MICO", "Kv"), (r"RIGIDEZ DO DENTADO", "rigidez"), (r"LONGITUDINAL DE CARGA DE PRESS", "K_Hbeta"), (r"LONGITUDINAL DE CARGA NA RAIZ", "K_Fbeta"),
    (r"TRANSVERSAL DE CARGA DE PRESS", "K_Halpha"), (r"TRANSVERSAL DE CARGA DE FLEX", "K_Falpha"), (r"FATOR DE ZONA", "Z_H"), (r"FATOR DE ELASTICIDADE", "Z_E"),
    (r"FATOR DE [ÂA]NGULO DE H[ÉE]LICE \(\$Z", "Z_beta"), (r"FATOR DE LUBRIFICANTE", "Z_L"), (r"FATOR DE VELOCIDADE", "Z_V"), (r"FATOR DE RUGOSIDADE", "Z_R"),
    (r"FATOR DE DUREZA DE TRABALHO", "Z_W"), (r"FATOR DE TAMANHO \(\$Z", "Z_X"), (r"ENGRENAMENTO INDIVIDUAL - PINH[ÃA]O \(\$Z_B", "Z_B"), (r"ENGRENAMENTO INDIVIDUAL.*Z_D", "Z_D"),
    (r"FATOR DE VIDA [ÚU]TIL \(\$Z", "Z_NT"), (r"FATOR DE FORMA DO DENTE", "Y_F"), (r"FATOR DE CORRE[ÇC][ÂA]O DE TENS", "Y_S"), (r"FATOR DE [ÂA]NGULO DE H[ÉE]LICE \(\$Y", "Y_beta"),
    (r"FATOR DE ESPESSURA DE ARO", "Y_B"), (r"SENSIBILIDADE RELATIVA", "Y_dRelT"), (r"CONDI[ÇC][ÃA]O SUPERFICIAL RELATIVA", "Y_RRelT"), (r"FATOR DE TAMANHO DO DENTE", "Y_X"),
    (r"FATOR DE VIDA [ÚU]TIL \(\$Y", "Y_NT"), (r"TENS[ÃA]O DE CONTATO|PRESS[ÃA]O DE CONTATO|TENS[ÕO]ES DE CONTATO", "sigma_H"), (r"TENS[ÃA]O DE FLEX|TENS[ÕO]ES DE FLEX", "sigma_F"),
    (r"APLICA[ÇC][ÃA]O E MOTORIZA", "aplicacao"), (r"QUALIDADE DO DENTADO", "qualidade"), (r"COEFICI[ÊE]NTES DE SEGURAN[ÇC]A M[ÁA]XIMOS E M[ÍI]NIMOS", "seguranca"),
    (r"CARACTER[ÍI]STICAS DA TRANSMISS", "transmissao"), (r"ARRANJO F[ÍI]SICO", "arranjo"), (r"N[ÚU]MERO DE DENTES", "numero_dentes"), (r"DIST[ÂA]NCIA ENTRE CENTROS$", "distancia_centros"),
    (r"[ÂA]NGULO DE PRESS[ÃA]O", "angulo_pressao"), (r"^M[ÓO]DULO", "modulo"), (r"[ÂA]NGULO DE H[ÉE]LICE$", "angulo_helice"), (r"DI[ÂA]METRO DE REFER[ÊE]NCIA E DI", "diametros"),
    (r"^PASSOS", "passos"), (r"DESLOCAMENTO DO PERFIL$", "desloc_perfil"), (r"CARACTER[ÍI]STICAS GEOM[ÉE]TRICAS COMPLEMENTARES|ESPESSURA  ?CIRCULAR NORMAL", "espessura"),
    (r"DI[ÂA]METRO DE CABE[ÇC]A", "diam_cabeca"), (r"DI[ÂA]METRO DE IN[ÍI]CIO DE CHANFRO", "chanfro"), (r"DI[ÂA]METRO DE P[ÉE]$", "diam_pe"), (r"FOLGA NO P[ÉE]", "folga_pe"),
    (r"CORRE[ÇC][ÃA]O DO BLANK", "blank"), (r"CIRCULOS [ÚU]TEIS", "circulos_uteis"), (r"INTERFER[ÊE]NCIA ENTRE AS CABE", "interferencia_interna"), (r"INTERFER[ÊE]NCIA POR UNDERCUT", "undercut"),
    (r"^GRAU DE RECOBRIMENTO$", "recobrimento"), (r"VELOCIDADE DE ESCORREGAMENTO", "escorregamento"), (r"RAIO DE CRISTA", "raio_crista"), (r"EXTEN[ÇC][ÃA]O DE CONTATO", "largura"),
    (r"DI[ÂA]METRO DO EIXO", "eixo"), (r"DI[ÂA]METRO INTERNO DO ARO", "aro"), (r"CARACTER[ÍI]STICAS DE AJUSTE|JOGO ENTRE FLANCOS$", "jogo"), (r"CONTROLE DE ESPESSURA DO DENTE", "controle_W_M"),
    (r"TOLER[ÂA]NCIA DO DENTADO", "tolerancias"), (r"CARACTER[ÍI]STICAS FUNCIONAIS", "vida"), (r"TEMPERATURA", "temperatura"), (r"VIDA [ÚU]TIL NOMINAL", "vida"),
    (r"MATERIAIS E TRATAMENTO T[ÉE]RMICO", "material"), (r"^LUBRIFICA[ÇC][ÃA]O$", "lubrificacao"), (r"ESFOR[ÇC]OS ATUANTES", "forcas"), (r"AN[ÁA]LISE DE TENS[ÕO]ES", "analise_tensoes"),
    (r"PLANET[ÁA]RI", "planetario"), (r"INTRODU[ÇC][ÃA]O", "introducao"), (r"COEFICIENTE DE RECOBRIMENTO NA FLEX|FATOR DE RECOBRIMENTO NA FLEX", "Y_eps"), (r"FATOR DE RECOBRIMENTO  ?\(\$Z", "Z_eps"),
]


PLANETARIO_MD = r"""
Um trem planetário (epicicloidal) tem três membros coaxiais: o **sol** (externo, central), a **anelar** (coroa interna) e o **porta-planetas**, que carrega $N$ **planetas** igualmente espaçados engrenando ao mesmo tempo com o sol e com a anelar. Fixando um dos três membros, os outros dois ficam em relação fixa de rotação.

![](/api/figuras/Simple_Epicyclic.png)

**Planetário simples**: um único planeta de $z_p$ dentes engrena com o sol ($z_s$) e com a anelar ($z_r$). Condição geométrica: $z_r = z_s + 2 z_p$ (mesmo módulo). O planeta sofre **flexão alternada** (os dois flancos trabalham), por isso $Y_M = 0{,}7$ na ISO 6336-3.

**Planetário composto**: o planeta é duplo — a roda maior ($z_{bp}$) engrena com o sol e a menor ($z_{sp}$), solidária, com a anelar. Permite reduções maiores e módulos diferentes nas duas malhas.

![](/api/figuras/Compound_Epicyclic.png)

**Relação básica** (porta-planetas parado, trem ordinário):

$$k = \frac{z_r\, z_{bp}}{z_s\, z_{sp}}$$

**Fórmula de Willis**: $\dfrac{n_s - n_c}{n_r - n_c} = -k$. Casos usuais:

| Entrada → saída | Fixo | Relação $i = n_{in}/n_{out}$ |
|---|---|---|
| sol → porta-planetas | anelar | $1 + k$ |
| porta-planetas → sol | anelar | $1/(1+k)$ |
| sol → anelar | porta-planetas | $-k$ |
| anelar → porta-planetas | sol | $(1+k)/k$ |

**Torques** independem da cinemática (equilíbrio estático): $T_r = k\,T_s$ e $T_c = -(1+k)\,T_s$. Cada malha recebe o torque do sol dividido pelos $N$ planetas, majorado pelo fator de repartição $K_\gamma$ (1,05 para 3 planetas bem fabricados).

**Rotações relativas**: para $K_v$, $Z_V$ e os ciclos de carga usa-se a rotação **relativa ao porta-planetas** ($n - n_c$), pois é com ela que os dentes se engrenam. O sol e a anelar sofrem $N$ engrenamentos por volta relativa; o planeta, um por malha.

**Condições de montagem** com $N$ planetas igualmente espaçados: $(z_s + z_r)/N$ inteiro (simples) ou a condição generalizada do composto; **hunting**: $z$ das rodas em malha sem fator comum; **folga entre planetas vizinhos**: $2\,a\,\sin(\pi/N) > d_{a,p}$.

![](/api/figuras/Hunting_conditions.png)
"""


def dividir(src):
    """Divide o markdown de uma célula em seções por título **…** (nível ### ou ####). Devolve [(titulo, texto)]."""
    linhas = src.splitlines()
    secs = []; cur_t = None; cur = []
    for l in linhas:
        m = re.match(r"^\s*[-*]?\s*#{2,5}\s*\*\*(.+?)\*\*\s*#*\s*$", l)
        if m:
            if cur_t is not None or cur:
                secs.append((cur_t, "\n".join(cur)))
            cur_t = m.group(1).strip(); cur = [l]
        else:
            cur.append(l)
    if cur_t is not None or cur:
        secs.append((cur_t, "\n".join(cur)))
    return secs


def chave_para(titulo):
    if not titulo:
        return None
    t = re.sub(r"\s+", " ", titulo).strip()
    for pat, ch in MAPA:
        if re.search(pat, t, re.I):
            return ch
    return None


def limpar(md):
    # remove indentação comum (as células do notebook indentam o corpo das seções)
    linhas = md.splitlines()
    ind = [len(l) - len(l.lstrip()) for l in linhas if l.strip() and not l.lstrip().startswith("#")]
    k = min(ind) if ind else 0
    out = []
    for l in linhas:
        out.append(l[k:] if len(l) >= k and l[:k].strip() == "" else l.lstrip())
    md = "\n".join(out)
    md = re.sub(r'<img src="Figuras/([^"]+)"[^>]*>', r'![](/api/figuras/\1)', md)
    md = md.replace('<div align="center">', '<div class="center">')
    return md.strip()


def main():
    import nbformat
    nb = nbformat.read(os.path.join(ROOT, "Dimensionamento.ipynb"), as_version=4)
    docs = {}
    ordem = []
    atual = None
    for i, c in enumerate(nb.cells):
        if c.cell_type != "markdown":
            continue
        for titulo, texto in dividir(c.source):
            ch = chave_para(titulo)
            figs = re.findall(r"Figuras/([^\"')\s]+)", texto)
            if not ch:
                # subseção sem chave própria: pertence ao tema corrente (ex.: "RELAÇÃO DE VELOCIDADES" em transmissao)
                if atual and titulo:
                    docs[atual]["markdown"] += "\n\n" + limpar(texto); docs[atual]["figuras"] += figs
                continue
            if ch in docs:          # mesma chave em mais de uma seção (ex.: vida): concatena
                docs[ch]["markdown"] += "\n\n" + limpar(texto); docs[ch]["figuras"] += figs
            else:
                t = re.sub(r"\s+", " ", titulo).strip()
                t = re.sub(r"\s*\(\$.*?\$\s*\)", "", t)          # remove "($K_v$)" do título visível
                docs[ch] = {"chave": ch, "titulo": t.capitalize() if t.isupper() else t, "titulo_raw": titulo, "markdown": limpar(texto), "figuras": figs, "celula": i}
                ordem.append(ch)
            atual = ch
    # tema escrito à mão (não existe no caderno): planetário
    docs["planetario"] = {"chave": "planetario", "titulo": "Trens planetários (epicicloidais)", "titulo_raw": "PLANETÁRIO", "celula": -1, "figuras": ["Simple_Epicyclic.png", "Compound_Epicyclic.png", "Hunting_conditions.png", "Speed_ratio.png"], "markdown": PLANETARIO_MD}
    ordem.append("planetario")
    out = [docs[k] for k in ordem]
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"{len(out)} temas -> {OUT}")
    faltam = [ch for _, ch in MAPA if ch not in docs]
    if faltam:
        print("sem texto no notebook:", sorted(set(faltam)))


if __name__ == "__main__":
    sys.exit(main())
