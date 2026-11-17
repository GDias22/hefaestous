# HEFAESTOUS

**Dimensionamento de engrenagens cilíndricas e planetárias** — DIN 3960/3967 · ISO 6336
FEM/Unicamp — Laboratório de Máquinas Rotativas (LAMAR) · Desenvolvido por Gabriel Dias

HEFAESTOUS (Hefesto, o ferreiro dos deuses) é um programa para Windows que projeta e verifica engrenagens de dentes retos e
helicoidais: **trens de engrenagens** (N estágios pinhão × coroa, externos ou internos) e **redutores planetários** (simples ou
compostos). Ele roda localmente no seu computador e abre no navegador; não envia dados para fora.

---

## Como baixar e instalar

Requisitos: Windows 10/11 de 64 bits e internet durante a instalação. Não precisa de administrador nem de Python instalado.

1. Baixe este repositório: botão **Code → Download ZIP** (ou `git clone`). Descompacte onde quiser.
2. Execute **`Instalar_HEFAESTOUS.exe`**. Escolha a pasta de instalação (o padrão é `%LOCALAPPDATA%\Programs\HEFAESTOUS`) e clique
   em **Instalar**. O instalador baixa o Python 3.13 oficial e as bibliotecas necessárias (~400 MB, inclui o kernel CAD) para dentro
   da própria pasta. Leva alguns minutos.
3. Abra pelo atalho **HEFAESTOUS** criado na Área de Trabalho (também há um no Menu Iniciar).

Se o Windows SmartScreen avisar "editor desconhecido", clique em *Mais informações → Executar assim mesmo*: os executáveis não são
assinados digitalmente. Para desinstalar: *Configurações › Aplicativos › HEFAESTOUS*.

**Atualizações.** Ao abrir, o programa verifica se há versão nova neste repositório. Se houver, aparece uma faixa no topo com
**Atualizar agora**: ele baixa, troca os arquivos e reabre sozinho, preservando o que você já tinha. Detalhes, instalação sem
internet e diagnóstico de problemas: [INSTALAR.md](INSTALAR.md).

---

## O que ele faz

**Arquitetura da transmissão.** Trem de engrenagens com quantos estágios quiser (pares externos ou pinhão × anelar), ou planetário
simples (sol, planetas, anelar, porta-planetas) e composto (dois planetas por pino, módulos independentes). No planetário você escolhe
quem é entrada, saída e membro fixo, ou impõe duas rotações (diferencial, equações de Willis).

**Busca de número de dentes.** Dada a redução desejada e a tolerância, lista as combinações de dentes possíveis com os filtros dos
cadernos de projeto (montagem, defasagem, faixa de redução), com esboço de cada candidato.

**Geometria DIN 3960 / 3967.** Módulo, ângulos de pressão e hélice, deslocamentos de perfil, diâmetros, recobrimentos, espessuras de
dente, dimensão sobre dentes e sobre pinos/esferas, jogo entre flancos com tolerâncias, verificações de interferência e de ponta
afiada. Ferramentas de corte (cremalheira com protuberância, pinhão-cortador para anelares) e sobremetal de retificação.

**Layout de eixos e mancais.** Desenho à escala de cada eixo com diâmetro, vão entre mancais, lado do torque e posição das rodas,
de onde saem automaticamente o arranjo físico e a constante K′ usados na distribuição de carga.

**Análise de resistência ISO 6336.** Fatores de aplicação, dinâmico, de distribuição de carga (K_Hβ, K_Hα), de forma e correção de
tensão, durabilidade à flexão e ao pitting, com os coeficientes de segurança S_H e S_F de cada roda. Materiais, lubrificantes e
acabamentos superficiais em presets editáveis. Cada valor tem um **"por quê?"** que mostra a fórmula com os números do projeto, o
texto didático e um gráfico de sensibilidade.

**Desenhos e CAD.** Perfil do dente e roda completa em 2D (com pré-usinagem e protuberância), sólido 3D de cada roda com furo do
eixo, e o **conjunto montado** com todas as rodas em fase. Exporta **STEP** (CAD), **STL** (impressão 3D), **GLB** e um ZIP com
tudo. O visualizador 3D tem corte, medição por dois cliques e controles de mouse no padrão SolidWorks.

**Relatório e planilhas.** Relatório HTML (imprimível em PDF) com todos os resultados, e exportação em XLSX/JSON. Projetos são
salvos em arquivos `.fem` (JSON legível) que você pode abrir, versionar e compartilhar.

**Aprender.** Textos didáticos dos cadernos (Mazzo, ISO 6336) ligados a cada parâmetro e resultado.

---

## Como funciona

A tela se organiza em três colunas:

- **Esquerda — fluxo do projeto.** As etapas em ordem: Arquitetura → Entrada (rotação e torque) → Busca de dentes → Rodas (uma por
  engrenagem, com cor própria) → Layout → Operação e materiais → Análise ISO 6336 → Saída. Clique numa etapa ou numa roda para editá-la.
- **Centro — vistas.** Esquema da transmissão, Dente, Roda 2D, 3D/STEP, Layout, Tabelas e Aprender. As vistas mostram sempre a roda
  selecionada na árvore.
- **Direita — inspetor e resultados.** Os parâmetros do item selecionado (essenciais à mostra, avançados em acordeões) e, embaixo, os
  medidores S_H e S_F da roda em foco, avisos e fatores. Tudo recalcula **ao vivo** enquanto você edita.

Modo **Guiado** percorre as etapas uma a uma com explicações; modo **Livre** deixa tudo acessível.

Por dentro, é um servidor local em Python (FastAPI) com os módulos de cálculo validados nos cadernos de projeto, e uma interface em
HTML/JavaScript que abre em `http://127.0.0.1:8765/`. O CAD usa o kernel OpenCascade (build123d). A janelinha que abre junto mostra o
endereço e encerra o servidor quando fechada. Problemas ficam registrados em `erros.txt` e `logs\servidor.log` na pasta de instalação.

---

## Conteúdo deste repositório

```
Instalar_HEFAESTOUS.exe   instalador
HEFAESTOUS.exe            lançador (alvo do atalho)
LEIA-ME.txt · INSTALAR.md
web\                      aplicação (servidor FastAPI, interface, ferramentas)
*.py                      módulos de cálculo (geometria DIN, equações, análise de tensões ISO 6336)
Figuras\                  figuras didáticas usadas nos tooltips e no Aprender
Exemplos_fem\             projetos de exemplo validados contra as referências (abra em Abrir)
instalador\               fontes do instalador e do lançador; versao.json
```

Este é o repositório de **produção**: só recebe versões prontas. Problemas e sugestões: abra uma *issue*.
