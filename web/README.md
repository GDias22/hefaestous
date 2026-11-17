# HEFAESTOUS — Interface web de dimensionamento de engrenagens (FEM/Unicamp · LAMAR)

Aplicação local (FastAPI + navegador) para dimensionar **trens de engrenagens** (N estágios pinhão × coroa em série) e
**planetários** (simples ou compostos, por elementos: sol, planetas, anelar), com cálculo **ao vivo** enquanto se edita,
explicação didática de cada fator (fórmula com os valores do projeto, texto do caderno, gráfico de sensibilidade),
desenhos 2D, sólido 3D com medição (STEP/GLB), relatório HTML → PDF e planilhas.

## Executar

```bat
run.bat                      :: na pasta Dimensionamento_engrenagens (cria o venv 3.13 na 1ª vez)
```
ou `web\.venv313\Scripts\python.exe web\app.py`. Abre `http://127.0.0.1:8765/`.

## Como usar

O fluxo segue o dos cadernos (`Dim_cinematico` → `dados_engrenagens` → `Analise_de_Tensões`). Árvore à esquerda, em ordem:

1. **Arquitetura** — trem de engrenagens, planetário simples (A) ou composto (B); nº de planetas. No planetário, o cartão **Fluxo de
   torque**: ENTRADA (membro ▾) → SAÍDA (membro ▾) · terceiro membro FIXO/LIVRE, com n e T de cada um, a relação de velocidades da
   AGMA 6123 (ou Willis no diferencial) e o aviso do Ring; no trem, o fluxo de potência pelos estágios. Em ambos, a **redução alvo** com
   tolerância (alimenta a busca de dentes), já comparada com a redução atual (desvio em %). A figura da tabela AGMA saiu.
2. **Entrada** — n, T e irregularidades das máquinas (K_A).
3. **Busca de dentes** — busca de números de dentes como etapa (não é modal): parâmetros no inspetor, tabela de candidatos no centro
   (filtros do caderno: sem defasagem e faixa de redução; ordenação), **esboço do candidato** ao lado e "Usar este candidato".
   O estado da busca sobrevive a sair e voltar do passo.
4. **Rodas** — cada engrenagem é um item próprio, com cor fixa: trem = Pinhão/Coroa de cada estágio; planetário = Sol,
   **Planeta maior**, **Planeta menor** (só no composto), Anelar e Porta-planetas.
5. **Layout (eixos e mancais)** — desenho à escala de cada eixo (entrada, intermediários, saída; no planetário, eixo do sol e
   pino do porta-planetas): diâmetro `d_sh`, vão entre mancais `l`, por qual lado entra o torque e posição de cada roda (arraste
   no desenho). O programa **deduz s, o arranjo físico 1–7 e K′** (centrada, descentrada com torque do mesmo lado ou oposto, em
   balanço, duas rodas simétricas ou assimétricas) e o ramo do K′ (roda integrada/prensada ou com chaveta/estrias; "automática"
   segue d/d_sh ≥ 1,15 do código original). No pino do planeta: **rolamentos de agulhas** dentro do planeta (Ø do furo) ou
   **planeta solidário ao eixo** (eixo biapoiado). Com "usar o layout nos cálculos" ativo, esses valores substituem os campos
   "Corpo, eixo e mancais" das rodas (que ficam cinza). Avisa sobreposição axial, s/l acima do limite da figura e eixo ≥ diâmetro
   da roda. A anelar fica fora (é da carcaça).
6. **Operação e materiais** · 7. **Análise ISO 6336**.

- **Topo**: nome do projeto (e do arquivo `.fem` aberto), Livre/Guiado, Novo · Abrir · Salvar (Ctrl+S) · Salvar como… (Ctrl+Shift+S) · Relatório · Exportar.
- **Arquivo `.fem`**: Salvar grava o projeto completo (entradas, arquitetura, rodas, layout, operação, métodos) mais uma foto dos
  resultados; Abrir recarrega tudo para continuar editando (também arrastando o arquivo para a janela). É JSON legível
  (`formato: "FEM-Planetaria"`, `versao`, `nome`, `salvo_em`, `projeto`, `resumo`); arquivos de versões antigas do modelo são migrados
  ao abrir, arquivos inválidos ou de versão mais nova são recusados com mensagem e não alteram o projeto aberto. No Chrome/Edge,
  Salvar regrava o mesmo arquivo; em outros navegadores baixa o arquivo. "Salvar •" indica alterações não gravadas, e o navegador
  avisa ao fechar com alterações pendentes. Relatório e exportações xlsx/json não exigem salvar o `.fem`.
- **Esquema interativo**: cada roda tem rótulo (z, m), cor própria, tooltip ao passar o mouse (z, m_n, d_w, b, S_H/S_F mínimos) e
  clique que seleciona *aquela* roda; a selecionada fica em destaque e as demais atenuam. O selo **"Editando: …"** no topo do
  canvas e o cabeçalho do inspetor mostram qual roda está ativa; focar um campo de uma roda a seleciona no esquema.
- **Centro**: duas coisas independentes. A **árvore** à esquerda escolhe a **etapa** (o que se edita no inspetor); as **abas** acima do
  canvas escolhem a **vista** (Esquema, Dente, Roda 2D, 3D/STEP, Layout, Tabelas, Aprender). Arquitetura e Busca de dentes **não têm aba**:
  são painéis abertos só pela árvore (nenhuma aba fica acesa enquanto estão abertos). Trocar de aba não muda a etapa nem a seleção;
  escolher uma roda a partir de Arquitetura/Busca de dentes abre o Esquema. Não há mais a faixa "Passo/Editando" sobre o canvas: o
  cabeçalho do inspetor (direita) e a árvore dizem o que está selecionado.
- **Dente / Roda 2D / 3D**: a barra da vista só mostra a roda em foco (chip colorido + nome); a roda se escolhe **apenas na árvore** à
  esquerda (decisão do usuário, 2026-11-16: o seletor por chips dentro da vista foi retirado). Trocar de roda na árvore não sai da vista.
- **3D / STEP**: o sólido é gerado com o **furo do eixo de projeto** (Ø d_sh da roda; planeta sobre rolamentos de agulhas usa o Ø do furo d_i
  do Layout; anelar não tem furo; furo ≥ 90 % do pé é omitido com aviso). O backend verifica que o resultado é UM sólido fechado válido
  (BRepCheck) antes de exportar — o STEP é AP214 em mm com `MANIFOLD_SOLID_BREP`, não casca. **Baixar ▾** oferece STEP (CAD), GLB (viewer)
  e STL (impressão 3D). O viewer mostra uma **tríade XYZ** no canto inferior esquerdo (Z = eixo da roda) que gira com a câmera, e o
  **corte** pinta a seção com tampa (stencil), para o interior aparecer como material e não como casca oca.
- **Distribuição como aplicativo (2026-11-16)**: ver `INSTALAR.md` na raiz. `Instalar_HEFAESTOUS.exe` (GUI tkinter ou `--silent`) copia a
  aplicação para `%LOCALAPPDATA%\Programs\HEFAESTOUS`, baixa o Python 3.13 embeddable, instala `web/requirements.txt` num `runtime\`
  próprio, cria atalhos (Desktop/Menu Iniciar) e registra em Aplicativos; `HEFAESTOUS.exe` (lançador) sobe `runtime\python.exe webpp.py`
  num Job Object (morre junto), espera e abre o navegador. Fontes em `instalador\`; `instaladoruild.bat` recompila os dois com PyInstaller.
- **Logs sem terminal (2026-11-16, decisão do usuário)**: nenhum console aparece. `backend/logs.py` manda uvicorn/fastapi/backend para
  `<base>\logs\servidor.log` (rotativo 5 MB × 3) e grava um histórico legível em `<base>\erros.txt` (exceções não tratadas → 500 em JSON +
  entrada; 422 de negócio/validação e 501 em `/api/*` também entram, com rota e traceback). `<base>` = `HEFAESTOUS_HOME` (o lançador define
  = pasta de instalação) ou a raiz do projeto em desenvolvimento. O lançador grava em `erros.txt` falhas de arranque (servidor caiu / não respondeu, com as últimas linhas do log).
- **Anelar: correção do pinhão-cortador (2026-11-16).** Em `geom/perfil2d.cortador` a normal usada para posicionar o arredondamento
  de ponta ρ_a0 estava com o sinal trocado: o centro do arco caía fora do flanco, a ponta do cortador virava um "gancho" mais largo
  que o dente e a envoltória da anelar ganhava um "V" no fundo de cada vão (no 3D aparecia como um corte entre os dentes). Agora o
  arco fica do lado de dentro e o vão estreita monotonicamente da cabeça ao pé. Além disso, se os flancos do cortador se cruzam
  antes do adendo nominal (dente afiado, ex.: z₀ = 23 com h_aP0* = 1,4 e α = 25°) ou se ρ não cabe na ponta, a cabeça é truncada no
  maior raio possível e o perfil devolve `avisos` (mostrados na vista Dente / Roda 2D): o pé real d_f fica acima do nominal; use um
  cortador com mais dentes ou adendo menor. Teste de regressão em `tests/test_geom.py`.
- **Mouse no 3D** (padrão SolidWorks, 2026-11-16): botão do meio orbita; Ctrl+meio desloca; Shift+meio faz zoom arrastando; roda dá zoom
  no ponto sob o cursor (para frente AFASTA, como no SW — a caixa "roda como no SW" inverte, guardada em `localStorage.engr.zoomSW`);
  duplo clique do meio enquadra. Esquerdo também orbita e direito desloca (notebook sem botão do meio); "Medir" continua por clique esquerdo.
- **Gerar conjunto** (vista 3D): todas as rodas do projeto montadas e **em fase** (dente no vão) — `backend/services/conjunto.py`.
  Trem: estágios em série ao longo de +X (centro da coroa i = pinhão i + |a_i|), empilhados em Z com folga; planetário: sol na origem,
  N planetas a |a| em ψ_k = −90° + 360°·k/N, anelar em fase com o planeta 1 (aviso se (z_sol + z_anelar)/N não é inteiro: os demais
  planetas não casam); composto: planeta menor + anelar num 2º plano Z. Hélice: sentidos opostos na malha externa, iguais na interna.
  **Baixar conjunto ▾**: STEP (montagem, uma peça por roda com nome e cor), GLB (viewer mostra cada roda na sua cor), STL e **ZIP**
  (conjunto + `pecas/*.step|stl` separadas + `posicoes.json` com x, y, z e rotação de cada peça). Verificado por interseção booleana
  no OCC: malhas externas em fase com sobreposição ≈ 0; malhas internas podem acusar alguns mm³ quando o par tem interferência de
  involuta real (ex.: 24/−63 com h_a* = 1), o que é dado do projeto e não da montagem.
- **Saída** (fim da árvore): tabela de eixos/membros (n, T, P) e o bloco **Redução: desejada × obtida** com o desvio em % e se está dentro da
  tolerância; o subtítulo na árvore já mostra o desvio. No planetário, os membros de entrada/saída também podem ser trocados no inspetor da Arquitetura.
- **Direita**: inspetor do item (essenciais + acordeões "Avançado" por tema; erros aparecem no campo) e resultados
  (medidores S_H/S_F da roda em destaque, avisos, fatores K/Z/Y). Cada valor tem **"por quê?"** → fórmula, variáveis, texto e sensibilidade.
- **Modo Guiado**: 8 passos na mesma ordem, com conclusão automática pelos dados; tour na primeira abertura.
- Tudo recalcula ao digitar (debounce 160 ms; o cálculo leva ~1 ms). Uma cópia de trabalho fica em `localStorage` (recuperação ao reabrir a página); o arquivo do projeto é o `.fem`.
- Projetos antigos (um único `planeta` com `z_ext/z_int`) são migrados ao abrir para `planeta_maior` + `planeta_menor`.
- **Planetário: modo de operação** (Arquitetura). *Membro fixo* (padrão): o terceiro membro, nem entrada nem saída, é preso à carcaça
  e i é fixo. *Diferencial*: o terceiro membro gira com rotação imposta `n_livre` (2 graus de liberdade — diferencial/somador); a
  cinemática sai da equação de Willis, os torques da estática, e i passa a depender de `n_livre` (`n_livre = 0` coincide com o modo fixo).
  O **Ring** usado no K_v (anelar presa = "Fixo"; anelar girando = "Rotativo") é deduzido disso e mostrado na Arquitetura, no
  Porta-planetas e no relatório, com um aviso do que muda no cálculo. Em trens, o par interno usa sempre "Rotativo" (a anelar gira).
- **Erros de geometria em português**: entradas que não geram engrenagem (ex.: x₁ = −0,75 num par 20/61) não mostram mais
  "math domain error". `backend/services/diagnostico.py` roda só depois de uma falha e explica a causa com o limite real (x₁ mínimo para
  haver flanco evolvente, distância entre centros mínima, Σx inviável, dente pontiagudo, ε_α ≤ 1) e a faixa de x₁ viável; a mensagem aparece
  no campo, num cartão "Ajuste: …" com botão **Ir para o campo** e no centro, no lugar do esquema. `tests/test_diagnostico.py` varre uma
  grade de entradas e exige que nenhuma falha crua vaze.
- **"?" → Aprender**: todo "?" tem link "Ver no Aprender" para o tema do caderno que explica o conceito. O mapa parâmetro→tema fica em
  `DOC_PARAM` (fim de `backend/params/metadata.py`); campos livres (nome do estágio, engenheiro) não têm tema.
- **Exemplos de validação** (`Exemplos_fem/`, um `.fem` por caso: ISO 6336-30 Ex.1 e Ex.6, Mazzo, Galle e as 6 planetárias) e o relatório
  `Exemplos_fem/LEIAME_validacao.md`, gerados por `python tools/validacao_exemplos.py > ../Exemplos_fem/LEIAME_validacao.md` (compara 68/136 fatores com `_revisao/depois/resultados.json`).
- **Métodos conforme as normas (rodada 7, 2026-11-13)** — as mesmas fórmulas nos cadernos e na interface: tolerâncias do dentado pela **ISO 1328-1:1995**
  (grau 5 × √2 por grau, médias geométricas das faixas de m, d e b; reproduz os 48 valores dos 8 exemplos do ISO/TR 6336-30); **K_Hβ** com `f_ma = √(f_Hβ1² + f_Hβ2²)`
  (ISO 6336-1 Eq. 64) e f_Hβ do grau 5 na Eq. 53; **Y_F/Y_S da anelar** pela geometria do **pinhão-cortador** (ISO 6336-3 §6.2.4/6.2.5, tangente a 60°), método
  `cortador` padrão em "Análise ▸ Avançado"; exige "Dentes do pinhão-cortador z₀" na ferramenta da anelar, senão cai na cremalheira equivalente com aviso.
  Ex. 6 da ISO/TR 6336-30: K_v 1,123 (norma 1,12), K_Hβ 2,33 (2,28), Y_F anelar 1,12 (1,18), Y_S anelar 3,45 (3,14), S_F anelar 4,95 (5,37), S_H 1,12 (1,14).
  No método do cortador, ρ_F recebe o piso 0,1·m_n (convenção KISSsoft) e o app avisa quando o piso atua (rodada 8). Os relatórios KISSsoft usados em
  `_revisao/comparacao_interface_kisssoft.md` são DIN 3990/3961: a malha interna diverge mais agora por diferença de norma (K_v 1,42 × 1,29; Y_F anelar 1,71 × 1,58),
  não por defeito — ver a seção C.8 daquele arquivo. Decisão de projeto: a nota 12 da ISO 6336-1 §8.3.1 (f_fα no lugar de f_pb em K_Hα) NÃO é aplicada.
- **Rodapé**: "Desenvolvido por Gabriel Dias" na barra lateral e no relatório.
- **Ícone do app** (identidade visual, 2026-11-16): engrenagem anelar com sol e três planetas e, no centro, bigorna e chama de Hefesto, em azul
  com acento cobre. Arte original em `frontend/img/fonte/hefaestous_icone_original.jpg`; `python tools/gerar_icones.py <imagem>` regenera
  `icon*.png` e `hefaestous.ico` (fundo grafite: favicon / Windows) e as marcas de tema claro com fundo removido: `icon-mark.png` (emblema
  completo — barra superior e cabeçalho do relatório), `icon-mark-small.png` (só a engrenagem central) e, a partir dela, `favicon.ico` /
  `favicon.png` / `favicon-32.png` para a aba do navegador. `hefaestous.ico` (atalho da Área de Trabalho, .exe, Aplicativos) também é
  **modo claro** desde 2026-11-17 (pedido do usuário): emblema completo nos tamanhos ≥ 48 px e só a engrenagem central abaixo disso
  (`_ico_misto` monta o .ico com imagens diferentes por tamanho); a versão escura fica guardada em `hefaestous-escuro.ico`, sem uso.
  `criar_atalho.bat` (na raiz) cria o atalho "HEFAESTOUS" na Área de Trabalho apontando para `run.bat` com esse ícone.

## Estrutura

```
web/
  app.py                        servidor (uvicorn) + abre o navegador
  backend/bootstrap.py          ENGR_SEM_PDF=1, sys.path, importa Eq / G / A
  backend/params/metadata.py    FONTE ÚNICA dos parâmetros: rótulo, unidade, ajuda ("?"), padrão, limites, figura
  backend/projeto/              modelo.py (Pydantic), defaults.py, montar.py (projeto -> malhas, encadeamento n/T, cinemática
                                do planetário pelo membro fixo), calcular.py (geometria + tensões + resumo + erros por campo),
                                explicar.py (fórmulas/variáveis por fator), sensibilidade.py
  backend/docs/fatores.json     textos didáticos extraídos de Dimensionamento.ipynb por web/tools/extrair_docs.py
  backend/services/             geometria.py, tensoes.py, cinematica.py (busca de dentes + cinematica_membro_fixo), perfil.py
  backend/geom/                 sobremetal.py, perfil2d.py (envoltória: hob c/ protuberância, shaper), cad3d.py (build123d)
  backend/report/               render.py + templates/relatorio.html (seção Transmissão, geometria, tensões; CSS A4)
  backend/api/                  projeto, docs, meta, geometria, tensoes, cinematica (jobs), perfil, export
  frontend/                     index.html, css/app.css, js/app.js (estado, debounce, undo, migração), js/model/rodas.js (rodas: cor,
                                malha/lado, seleção), js/ui/* (arquitetura, busca, sidebar, inspector, canvas...), js/draw/* (train2d,
                                planetary2d, tip), vendor/{three,katex,marked}
  tests/                        pytest (test_projeto.py: igualdade com resultados.json, migração, planeta maior/menor, erros por campo, API)
                                + ui_v3.mjs + ui_migracao.mjs
  _legado_v1/                   interface v1 (assistente de 4 etapas), não servida; contém o antigo ui_edge.mjs
```

## Testes

```bat
web\.venv313\Scripts\python.exe -m pytest web\tests -q      :: ~1 min com CAD
node tests\ui_v3.mjs                                        :: a partir de web\, servidor rodando; screenshots em tests\_ui\v3_*.png
node tests\ui_layout.mjs                                    :: layout de eixos e mancais (desenho, arraste, ativação, agulhas)
node tests\ui_ajuda_erro.mjs                                :: erro guiado, "?" com link ao Aprender (todos os campos), ilustração
node tests\ui_diferencial.mjs                               :: modo diferencial do planetário e aviso do Ring (anelar fixa/girando)
node tests\ui_fem.mjs                                       :: .fem (salvar/abrir de verdade, inválidos, formato antigo), abas, cotas editáveis
node tests\ui_migracao.mjs                                  :: projeto no formato antigo abre e migra; modo Guiado
```

Validações: projeto planetário dos exemplos reproduz `_revisao/depois/resultados.json` (Pla56_ref) exatamente; trem com
ISO 6336-30 Ex.1 como estágio 1 reproduz Ex.1 e encadeia n/T/P; cinemática do planetário conferida por Willis e balanço
de potência nos três membros fixos; sobremetal conferido com KISSsoft.

## Notas

- Convenção DIN: engrenagem interna com z e a negativos; a interface aceita "Engrenagem interna" (checkbox) e cuida dos sinais.
- Dois pares "Simples" não podem compartilhar uma `Analise_de_tensao` (`Eq.kv` só acopla malhas de planetário): cada estágio do
  trem tem sua própria análise; o planetário usa as duas malhas acopladas (externa = malha 1).
- `a` vazio = distância entre centros padrão (Σx = 0). `x₁` vazio = repartição automática (método DIN/BS/ISO).
- Textos didáticos: edite o caderno `Dimensionamento.ipynb` e rode `python web/tools/extrair_docs.py`.
- Fórmulas: os cadernos são a fonte; alterações de método são feitas por scripts idempotentes em `_revisao/aplicar_N.py` (rodadas 7–9 = normas ISO lidas em
  2026-11-13), que também reexportam os `.py`. Depois: `_revisao/run_casos.py depois`, `_revisao/comparar.py`, `tools/validacao_exemplos.py`, `tools/validacao_kiss.py`, `extrair_docs.py`.
