# -*- coding: utf-8 -*-
"""Gera o conjunto de ícones do HEFAESTOUS a partir da arte original (PNG/JPG quadrado).

Saída em web/frontend/img/:
  icon.png            1024×1024 (fundo transparente fora do quadrado arredondado)
  icon-512.png, icon-256.png, icon-192.png, icon-64.png, icon-32.png
  icon-mark.png       512×512 só o emblema em MODO CLARO (fundo grafite/navy removido → transparente), para o relatório
  icon-mark-small.png 256×256 só a engrenagem central (bigorna + chama) em modo claro, legível em 40–60 px: barra do app
  hefaestous.ico      ícone de app do Windows (atalho, .exe) em MODO CLARO: emblema completo ≥ 48 px, engrenagem central < 48 px
  hefaestous-escuro.ico  a versão com fundo grafite (não usada; guardada)
  favicon.ico/.png    aba do navegador (engrenagem central, modo claro)

O app usa tema claro (fundo branco): a arte original é escura, então as marcas de topbar/relatório removem o fundo
(pixels escuros viram transparentes via rampa de alfa pelo canal máximo RGB) e recortam só a engrenagem central
com máscara circular no raio de cabeça, para os planetas não entrarem.

Uso: web\\.venv313\\Scripts\\python.exe web\\tools\\gerar_icones.py <caminho_da_imagem>
"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(os.path.dirname(HERE), "frontend", "img")


def arredondar(im, raio_frac=0.2):
    """Aplica máscara de quadrado arredondado (como ícone de app)."""
    im = im.convert("RGBA")
    w, h = im.size
    r = int(min(w, h) * raio_frac)
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=r, fill=255)
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    return out


def emblema(im, margem_frac=0.11):
    """Recorta o emblema circular (sem o fundo grafite): círculo inscrito com margem, fundo transparente."""
    im = im.convert("RGBA")
    w, h = im.size
    m = int(min(w, h) * margem_frac)
    box = [m, m, w - m, h - m]
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).ellipse(box, fill=255)
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    return out.crop(box)


def modo_claro(im, escuro=55, rampa=45):
    """Remove o fundo escuro da arte (grafite/navy): alfa = rampa linear no máximo RGB entre `escuro` e `escuro+rampa`.
    As engrenagens (azul B≈150) e a bigorna/chama (laranja) ficam opacas; grafite (≈32,41,50) e navy (≈19,28,37) somem."""
    a = np.asarray(im.convert("RGB")).astype(float)
    alpha = np.clip((a.max(axis=2) - escuro) / rampa, 0, 1) * 255
    return Image.fromarray(np.dstack([a, alpha]).astype(np.uint8), "RGBA")


def marca_central(im_claro, raio_frac=0.19, semente_frac=0.14):
    """Só a engrenagem central (bigorna + chama) em modo claro.
    Os dentes dos planetas engrenam com a central (não há folga radial para um simples recorte circular), então:
    disco de raio `raio_frac` do lado → componentes conexos do alfa → fica o componente que contém o corpo da engrenagem
    central (semente a `semente_frac` do lado, à direita do centro) + tudo dentro do raio interno (bigorna, chama, anel)."""
    from scipy import ndimage

    w, h = im_claro.size
    cx, cy, r = w / 2, h / 2, min(w, h) * raio_frac
    a = np.asarray(im_claro).copy()
    yy, xx = np.ogrid[:h, :w]
    dist = np.hypot(xx - cx, yy - cy)
    alpha = a[..., 3].astype(float) * (dist <= r)
    lab, n = ndimage.label(alpha > 100)
    seed = lab[int(cy), int(cx + min(w, h) * semente_frac)]
    keep = (lab == seed) | (dist <= min(w, h) * semente_frac)
    a[..., 3] = (alpha * keep).astype(np.uint8)
    out = Image.fromarray(a, "RGBA")
    return out.crop((int(cx - r), int(cy - r), int(cx + r), int(cy + r)))


def _ico_misto(caminho, grande, pequeno, limite=48, tamanhos=(16, 24, 32, 48, 64, 128, 256)):
    """Grava um .ico com imagens DIFERENTES por tamanho: `pequeno` abaixo de `limite`, `grande` a partir dele.
    (Pillow só gera .ico a partir de uma imagem; aqui o container é montado à mão com PNGs embutidos.)"""
    import io
    import struct
    entradas = []
    for n in tamanhos:
        im = (pequeno if n < limite else grande).resize((n, n), Image.LANCZOS)
        buf = io.BytesIO(); im.save(buf, "PNG"); entradas.append((n, buf.getvalue()))
    with open(caminho, "wb") as f:
        f.write(struct.pack("<HHH", 0, 1, len(entradas)))
        off = 6 + 16 * len(entradas)
        for n, dados in entradas:
            f.write(struct.pack("<BBBBHHII", n % 256, n % 256, 0, 0, 1, 32, len(dados), off)); off += len(dados)
        for _, dados in entradas:
            f.write(dados)


def main(src):
    os.makedirs(IMG, exist_ok=True)
    base = Image.open(src).convert("RGBA")
    if base.size[0] != base.size[1]:
        s = min(base.size)
        base = base.crop(((base.size[0] - s) // 2, (base.size[1] - s) // 2, (base.size[0] + s) // 2, (base.size[1] + s) // 2))
    base = base.resize((1024, 1024), Image.LANCZOS)
    icon = arredondar(base)
    icon.save(os.path.join(IMG, "icon.png"))
    for n in (512, 256, 192, 64, 32):
        icon.resize((n, n), Image.LANCZOS).save(os.path.join(IMG, f"icon-{n}.png"))
    # marcas para o tema claro do app/relatório: fundo escuro removido (transparente)
    claro = modo_claro(base)
    emblema(claro).resize((512, 512), Image.LANCZOS).save(os.path.join(IMG, "icon-mark.png"))
    # marca compacta para tamanhos pequenos (barra do app): só a engrenagem central com bigorna e chama — o emblema completo
    # (anelar + 3 planetas) vira uma mancha azul abaixo de ~60 px
    marca_central(claro).resize((256, 256), Image.LANCZOS).save(os.path.join(IMG, "icon-mark-small.png"))
    # Ícone de app do Windows (atalho da Área de Trabalho, .exe, Aplicativos) em MODO CLARO — decisão do usuário 2026-11-17: fundo
    # escuro removido. Tamanhos grandes (48–256) levam o emblema completo; pequenos (16–32) só a engrenagem central, que lê melhor.
    emb = emblema(claro)
    grande = Image.new("RGBA", (256, 256), (0, 0, 0, 0)); grande.alpha_composite(emb.resize((244, 244), Image.LANCZOS), (6, 6))
    marca = marca_central(claro)
    pequeno = Image.new("RGBA", (256, 256), (0, 0, 0, 0)); pequeno.alpha_composite(marca.resize((232, 232), Image.LANCZOS), (12, 12))
    _ico_misto(os.path.join(IMG, "hefaestous.ico"), grande, pequeno, limite=48)
    icon.save(os.path.join(IMG, "hefaestous-escuro.ico"), sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    # favicon da aba do navegador: só a engrenagem central (bigorna + chama) em modo claro, com margem; PNG + ICO multi-tamanho.
    pequeno.save(os.path.join(IMG, "favicon.png"))
    pequeno.resize((32, 32), Image.LANCZOS).save(os.path.join(IMG, "favicon-32.png"))
    pequeno.save(os.path.join(IMG, "favicon.ico"), sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64)])
    print("ícones gerados em", IMG)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1])
