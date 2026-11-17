# HEFAESTOUS — instalação e distribuição

Dimensionamento de engrenagens cilíndricas e planetárias · DIN 3960/3967 · ISO 6336
FEM/Unicamp — Laboratório de Máquinas Rotativas (LAMAR) · Desenvolvido por Gabriel Dias

## Para quem vai USAR o programa (Windows 10/11, 64 bits)

1. Baixe a pasta do projeto (botão **Code → Download ZIP** no GitHub, ou `git clone`) e descompacte onde quiser.
2. Dê dois cliques em **`Instalar_HEFAESTOUS.exe`**.
   - Escolha a pasta de instalação (padrão: `%LOCALAPPDATA%\Programs\HEFAESTOUS`, não exige administrador).
   - O instalador copia a aplicação, baixa o **Python 3.13** oficial (python.org, ~11 MB) para dentro da instalação e instala as
     bibliotecas necessárias (~400 MB, inclui o kernel CAD para STEP/STL). Precisa de internet; leva alguns minutos.
   - Ao final cria o atalho **HEFAESTOUS** na Área de Trabalho e no Menu Iniciar e registra o programa em
     *Configurações › Aplicativos* (para desinstalar).
3. Abra pelo atalho. Aparece uma janelinha com o endereço local (`http://127.0.0.1:8765/`) e o navegador abre sozinho.
   Deixe a janelinha aberta enquanto usa; fechá-la encerra o servidor.

Nada do seu Python ou de outros programas é alterado: tudo fica dentro da pasta de instalação.

**Deu problema?** Não aparece nenhum terminal: o programa grava tudo em arquivo, na pasta de instalação.
- `erros.txt` — histórico legível dos problemas (data/hora, o que estava sendo feito, mensagem e detalhes). É o arquivo para enviar
  junto com um relato de erro.
- `logs\servidor.log` — log completo do servidor (requisições, avisos, tracebacks); rotaciona em 5 MB.
**Desinstalar**: *Configurações › Aplicativos › HEFAESTOUS* ou `Desinstalar.bat` na pasta de instalação.

Se o Windows SmartScreen avisar "editor desconhecido" (os executáveis não são assinados digitalmente), clique em
*Mais informações → Executar assim mesmo*.

### Sem internet na máquina de destino

Coloque, dentro de `instalador\`, antes de distribuir:
- `python-3.13.9-embed-amd64.zip` (de https://www.python.org/ftp/python/3.13.9/)
- `get-pip.py` (de https://bootstrap.pypa.io/get-pip.py)
- a pasta `wheels\` com as dependências: `web\.venv313\Scripts\python.exe -m pip download -r web\requirements.txt -d instalador\wheels`

O instalador detecta esses arquivos e não acessa a rede.

## Para quem vai DISTRIBUIR / desenvolver

- **Pasta de distribuição**: `web\.venv313\Scripts\python.exe instalador\montar_distribuicao.py --zip` monta (apagando a anterior) a pasta
  **`HEFAESTOUS\`** ao lado da pasta do projeto, só com o necessário (≈40 MB: os dois .exe, LEIA-ME.txt, INSTALAR.md, módulos .py,
  Figuras, Exemplos_fem, web sem venv/testes, instalador), e o `HEFAESTOUS.zip` correspondente. É essa pasta/zip que se compartilha ou
  se sobe no git — não a pasta de desenvolvimento.

- `instalador\build.bat` compila, com PyInstaller (no venv `web\.venv313`), os dois executáveis que ficam na raiz:
  `Instalar_HEFAESTOUS.exe` (instalador, `instalador\instalador.py`) e `HEFAESTOUS.exe` (lançador, `instalador\launcher.py`).
  Rode-o sempre que mudar esses dois scripts; o resto do app (`web\`, módulos `.py`, `Figuras\`) é copiado pelo instalador
  tal como está na pasta, então **mudanças no app não exigem recompilar nada**.
- A versão exibida vem de `instalador\versao.json`.
- O `.gitignore` já exclui o que não deve ir para o repositório: `web\.venv313`, `node_modules`, `sessions`, caches, wheels.
  O que precisa estar no repositório/ZIP: os `.py` da raiz, `Figuras\`, `Exemplos_fem\`, `web\` (sem venv) e os dois `.exe`.
- Desenvolvimento local continua igual: `run.bat` (usa `web\.venv313`). O `HEFAESTOUS.exe` também funciona na pasta de
  desenvolvimento: se não houver `runtime\`, ele usa `web\.venv313`.
- Teste automatizado do instalador (silencioso, sem atalhos):
  `Instalar_HEFAESTOUS.exe --silent --dest C:\Temp\hefa_test --sem-atalhos --log C:\Temp\hefa.log`

## Como funciona por dentro

```
<instalação>\
  HEFAESTOUS.exe        lançador: sobe runtime\python.exe web\app.py, espera responder, abre o navegador
  runtime\              Python 3.13 embeddable + Lib\site-packages (pip, fastapi, numpy, scipy, build123d/OCP…)
  web\                  aplicação (FastAPI + HTML/JS); web\sessions\ guarda CAD gerado e sessões
  erros.txt             histórico de problemas (lançador e servidor) — webackend\logs.py
  logs\servidor.log     log completo do servidor (rotativo)
  *.py, Figuras\, Exemplos_fem\
  Desinstalar.bat
```

O servidor é um processo filho do lançador dentro de um Job Object do Windows: encerrar o lançador (botão, X da janela,
Gerenciador de Tarefas ou logoff) encerra o servidor. Se já houver um HEFAESTOUS rodando na porta 8765, o lançador só abre o
navegador; se a porta estiver ocupada por outro programa, usa a próxima livre.
