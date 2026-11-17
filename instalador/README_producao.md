# HEFAESTOUS

**Dimensionamento de engrenagens cilíndricas e planetárias** — DIN 3960/3967 · ISO 6336
FEM/Unicamp — Laboratório de Máquinas Rotativas (LAMAR) · Desenvolvido por Gabriel Dias

Interface local (abre no navegador) com fluxo por etapas: arquitetura da transmissão (trem de engrenagens ou planetário simples/composto),
busca de número de dentes, geometria DIN 3960, layout de eixos e mancais, análise de tensões ISO 6336, desenhos 2D, sólido 3D (STEP/STL/GLB,
inclusive o conjunto montado), relatório e planilhas.

## Instalação (Windows 10/11, 64 bits)

1. Baixe este repositório: botão **Code → zip** (ou `git clone`), e descompacte.
2. Execute **`Instalar_HEFAESTOUS.exe`**. Escolha a pasta (o padrão não exige administrador) e clique em **Instalar**.
   O instalador baixa o Python 3.13 oficial e as bibliotecas necessárias (~400 MB; precisa de internet) — leva alguns minutos.
3. Abra pelo atalho **HEFAESTOUS** criado na Área de Trabalho.

Se o Windows SmartScreen avisar "editor desconhecido": *Mais informações → Executar assim mesmo* (os executáveis não são assinados).
Desinstalar: *Configurações › Aplicativos › HEFAESTOUS*. Detalhes, instalação sem internet e diagnóstico (`erros.txt`): **INSTALAR.md**.

## Conteúdo

```
Instalar_HEFAESTOUS.exe   instalador
HEFAESTOUS.exe            lançador (o atalho aponta para ele)
LEIA-ME.txt · INSTALAR.md
web\                      aplicação (FastAPI + HTML/JS)
*.py · Figuras\ · Exemplos_fem\   módulos de cálculo, figuras didáticas e projetos de exemplo (.fem)
instalador\               fontes do instalador/lançador
```

Este é o repositório de **produção**: recebe apenas versões prontas, publicadas a partir do repositório de desenvolvimento.
Problemas e sugestões: abra uma *issue* aqui.
