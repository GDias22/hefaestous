# -*- coding: utf-8 -*-
"""Fonte única de metadados dos parâmetros de entrada.

Cada entrada de PARAMS descreve um campo da interface: rótulo, unidade, texto de ajuda (tooltip "?"),
valor padrão, tipo, limites, opções, grupo (card do formulário) e etapa do assistente.

    type   : "number" | "int" | "text" | "choice" | "bool"
    nullable: True quando None é um valor válido (o campo pode ficar vazio -> None)
    stage  : "cinematica" | "geometria" | "tensoes" | "material" | "ferramenta" | "lubrificante"
    fig    : nome de figura em Figuras/ exibida no tooltip (opcional)

As chaves da etapa "geometria" coincidem com os kwargs de Dimensionamento_geometrico.Engrenamento; as das
etapas "material", "ferramenta" e "lubrificante" com os kwargs de Materiais, Ferramentas e Lubrificante;
as de "tensoes" com Analise_de_tensao; as de "cinematica" com web.backend.services.cinematica.buscar.
"""

STAGES = {
    "cinematica": "A · Cinemática do planetário",
    "geometria": "B · Geometria da malha",
    "tensoes": "C · Tensões e seguranças (ISO 6336)",
    "material": "Material",
    "ferramenta": "Ferramenta de usinagem",
    "lubrificante": "Lubrificante",
}

# Ordem e título dos grupos (cards) por etapa
GROUPS = {
    "cinematica": [
        ("objetivo", "Objetivo da redução"),
        ("malhas", "Malhas externa e interna"),
        ("envelope", "Envelope e montagem"),
        ("perfil", "Proporções do dente"),
        ("busca", "Limites e filtros da busca"),
        ("carga", "Carga de entrada (para preencher a etapa B)"),
    ],
    "geometria": [
        ("identificacao", "Identificação"),
        ("basica", "Geometria básica"),
        ("planetario", "Transmissão e cinemática"),
        ("carga", "Carga"),
        ("deslocamento", "Deslocamento de perfil"),
        ("espessura", "Espessura do dente e tolerâncias (DIN 3967)"),
        ("modificacoes", "Modificações do dente"),
        ("acabamento", "Acabamento e qualidade"),
        ("seguranca", "Coeficientes de segurança requeridos"),
        ("corpo", "Corpo da engrenagem, eixos e mancais"),
        ("temperatura", "Temperaturas e dilatação"),
        ("controle", "Controle dimensional"),
        ("lubrificacao", "Lubrificação"),
        ("metodos", "Métodos de cálculo"),
    ],
    "tensoes": [
        ("conjunto", "Conjunto analisado"),
        ("fatores", "Fatores impostos"),
    ],
    "material": [("mat", "Propriedades")],
    "ferramenta": [("fer", "Ferramenta")],
    "lubrificante": [("lub", "Lubrificante")],
}

IRREG = ["Choque uniforme", "Choque leve", "Choque moderado", "Choque pesado"]
OP_ACAB = ["Retificação", "Rasqueteamento", "Fresamento"]
AFAST = ["a", "ab", "b", "bc", "c", "cd", "d", "e", "f", "g", "h"]

HELP_IRREG = ("Grau de irregularidade do carregamento segundo a ISO 6336-6 / Mazzo. Define o fator de aplicação K_A junto "
              "com a irregularidade da outra roda: uniforme (motor elétrico, turbina), choque leve (motor multicilindro, "
              "bombas), moderado (motor monocilindro, misturadores), pesado (prensas, britadores).")
HELP_ARRANJO = ("Arranjo físico da roda no eixo segundo a figura de Mazzo (1 a 7). 1 e 2: roda entre mancais simétrica; "
                "3 a 7: posições em balanço ou assimétricas que geram deflexão do eixo e entram em K_Hβ (método C). "
                "Use vazio e informe K' manualmente em 'Constante K' quando o arranjo não estiver na figura.")
HELP_AFAST = ("Grupo de afastamento DIN 3967 sobre a espessura do dente (letras a..h). Define o jogo mínimo A_sne: "
              "'a' é o maior afastamento, 'h' é zero. Para redutores de precisão costuma-se usar 'cd', 'd' ou 'e'.")
HELP_TOL = ("Série de tolerância DIN 3967 para a espessura do dente (21 a 30). Quanto maior o número, maior o campo de "
            "tolerância T_sn. Redutores industriais: 24 a 27; precisão: 21 a 23.")
HELP_CROWN = ("Abaulamento (crowning) do flanco em mm. Reduz a concentração de carga nas bordas quando há desalinhamento. "
              "Valores típicos 0,005 a 0,03 mm; 0 quando não há abaulamento.")


def P(label, type="number", default=None, unit=None, help="", group="basica", stage="geometria",
      min=None, max=None, choices=None, nullable=False, step=None, fig=None, advanced=False):
    d = dict(label=label, type=type, default=default, unit=unit, help=help, group=group, stage=stage,
             nullable=nullable, advanced=advanced)
    if min is not None: d["min"] = min
    if max is not None: d["max"] = max
    if choices is not None: d["choices"] = choices
    if step is not None: d["step"] = step
    if fig is not None: d["fig"] = fig
    return d


PARAMS = {}

# ======================================================================================================
# ETAPA B — GEOMETRIA (kwargs de Engrenamento)
# ======================================================================================================
G = "geometria"
PARAMS.update({
    # --- identificação
    "apelido": P("Apelido da malha", "text", "Malha 1", help="Nome livre usado nos relatórios e nos arquivos gerados.", group="identificacao", stage=G),
    "Proj": P("Engenheiro responsável", "text", "", help="Nome que aparece no cabeçalho do relatório.", group="identificacao", stage=G, nullable=True),
    "tipo": P("Modo de cálculo", "choice", "Otimização", choices=["Inicial", "Otimização"], group="identificacao", stage=G,
              help="'Inicial': o programa escolhe o deslocamento de perfil pelo método selecionado. 'Otimização': você impõe x do pinhão e o programa calcula x da coroa pela soma necessária para a distância entre centros."),

    # --- geometria básica
    "m_n": P("Módulo normal m_n", "number", 3.0, "mm", min=0.1, group="basica", stage=G,
             help="Módulo normal do dentado (DIN 780). Define o tamanho do dente: passo normal p_n = π·m_n. Para hélice, o módulo transversal é m_t = m_n/cos β."),
    "Z_pinhao": P("Dentes do pinhão z₁", "int", 15, min=4, group="basica", stage=G,
                  help="Número de dentes do pinhão (roda menor ou motora da malha). Sempre positivo."),
    "Z_coroa": P("Dentes da coroa z₂", "int", 66, group="basica", stage=G,
                 help="Número de dentes da coroa. Convenção DIN 3960: engrenagem INTERNA (anelar) com sinal NEGATIVO (ex.: −150). Externa positiva."),
    "a": P("Distância entre centros a", "number", 121.5, "mm", group="basica", stage=G,
           help="Distância entre centros de trabalho. Negativa para malha interna (planeta × anelar), seguindo o sinal de z₂. Se diferente de a_standard = m_t(z₁+z₂)/2 o programa calcula a soma de deslocamentos de perfil necessária."),
    "b_pinhao": P("Largura do pinhão b₁", "number", 30.0, "mm", min=0.1, group="basica", stage=G, nullable=True,
                  help="Largura de dente do pinhão. Deixe vazio para o programa estimar a largura mínima pela resistência à flexão (usa 'Fator de largura')."),
    "b_coroa": P("Largura da coroa b₂", "number", 30.0, "mm", min=0.1, group="basica", stage=G, nullable=True,
                 help="Largura de dente da coroa. A extensão de contato usada no cálculo é a menor das duas larguras."),
    "ISO": P("Classe ISO da distância entre centros", "int", 7, min=5, max=11, group="basica", stage=G,
             help="Classe de tolerância (IT) da distância entre centros, de 5 a 11 (DIN 3964). Afeta o jogo entre flancos e a folga no pé."),
    "alpha_n": P("Ângulo de pressão normal α_n", "number", 20.0, "°", min=10, max=30, group="basica", stage=G, fig="angulo_de_pressao.png",
                 help="Ângulo de pressão normal da cremalheira de referência. 20° é o padrão; 25° aumenta a resistência do pé e reduz o grau de recobrimento."),
    "beta": P("Ângulo de hélice β", "number", 0.0, "°", min=-45, max=45, group="basica", stage=G, fig="engrenagens_helicoidais.jpg",
              help="Ângulo de hélice no cilindro de referência. 0 para dentes retos. O sinal indica o sentido da hélice; o módulo é usado nos fatores."),

    # --- transmissão / planetário
    "trans": P("Tipo de transmissão", "choice", "Planetário", choices=["Simples", "Planetário"], group="planetario", stage=G,
               help="'Simples': par convencional de eixos fixos. 'Planetário': a malha faz parte de um trem epicicloidal; o torque é dividido entre N_cp planetas e as rotações passam a ser relativas ao porta-planetas."),
    "N_cp": P("Número de planetas N_cp", "int", 3, min=1, max=12, group="planetario", stage=G, nullable=True,
              help="Quantidade de planetas que dividem a carga. A força tangencial por malha é F_t = 2000·T·K_γ/(d·N_cp)."),
    "Ky": P("Fator de distribuição entre planetas K_γ", "number", 1.05, min=1.0, max=1.6, group="planetario", stage=G, nullable=True, fig="ky.png",
            help="Fator de carga não uniforme entre planetas (ISO 6336-1 §4.2 / AGMA 6123). 1,0 para sistemas flutuantes ideais; 1,05 para 3 planetas com boa precisão (nível 2 AGMA); 1,10 a 1,25 para 4 ou mais planetas."),
    "membro_pinhao": P("Membro do pinhão", "choice", None, choices=["sol", "planeta", "anelar"], group="planetario", stage=G, nullable=True,
                       help="Qual membro do planetário é o pinhão desta malha. Vazio: inferido (malha externa → sol; malha interna → planeta). Sol e anelar têm N_cp engrenamentos por volta relativa; planeta tem 1."),
    "membro_coroa": P("Membro da coroa", "choice", None, choices=["sol", "planeta", "anelar"], group="planetario", stage=G, nullable=True,
                      help="Qual membro do planetário é a coroa desta malha. Vazio: inferido (externa → planeta; interna → anelar)."),
    "Tipo_planetario": P("Tipo de planetário", "choice", "Composto", choices=["Simples", "Composto"], group="planetario", stage=G, nullable=True, fig="Compound_Epicyclic.png",
                         help="'Simples': um planeta engrena com sol e anelar (flexão alternada no planeta, Y_M = 0,7). 'Composto': planeta duplo (maior engrena com o sol, menor com a anelar), Y_M = 1."),
    "n_carrier": P("Rotação do porta-planetas n_c", "number", 0.0, "rpm", group="planetario", stage=G, nullable=True,
                   help="Rotação absoluta do porta-planetas. Vazio ou 0 para par convencional. Em planetário o programa usa a rotação RELATIVA |n_t − n_c| em v_t, K_v, Z_V e nos ciclos de carga."),

    # --- carga
    "n_t": P("Rotação do pinhão n₁", "number", 2000.0, "rpm", group="carga", stage=G,
             help="Rotação ABSOLUTA do pinhão da malha no ponto de maior torque, com sinal (sol: rotação do motor, positiva; planeta: rotação absoluta do planeta n_c + n_rel, normalmente NEGATIVA porque gira em sentido oposto ao sol). O programa usa |n₁ − n_c| nos cálculos."),
    "T": P("Torque na malha T", "number", 300.0, "N·m", min=0, group="carga", stage=G,
           help="Torque máximo no membro de entrada da malha (sobre o pinhão). Em planetário é o torque TOTAL da malha (sol: torque do sol; malha interna: soma dos torques dos planetas), dividido por N_cp no cálculo de F_t."),
    "irregularidade_motora": P("Irregularidade da máquina motora", "choice", "Choque uniforme", choices=IRREG, group="carga", stage=G, help=HELP_IRREG),
    "irregularidade_movida": P("Irregularidade da máquina movida", "choice", "Choque leve", choices=IRREG, group="carga", stage=G, help=HELP_IRREG),
    "Ka_imposto": P("K_A imposto", "number", None, min=1.0, max=3.0, group="carga", stage=G, nullable=True,
                    help="Força um valor do fator de aplicação K_A em vez da tabela ISO 6336-6 (irregularidades). Deixe vazio para usar a tabela."),
    "Vr": P("Vida requerida", "number", 10000.0, "h", min=1, group="carga", stage=G, fig="vida_util.jpg",
            help="Vida nominal requerida da malha em horas. Define o número de ciclos N_L = 60·n_rel·contatos·Vr usado em Z_NT e Y_NT."),

    # --- deslocamento de perfil
    "x_pinhao": P("Deslocamento de perfil do pinhão x₁", "number", 0.3, group="deslocamento", stage=G, fig="desloc_coef.jpg",
                  help="Coeficiente de deslocamento de perfil do pinhão (modo 'Otimização'). Positivo afasta a ferramenta e engrossa o pé; a coroa recebe x₂ = Σx − x₁."),
    "metodo_x": P("Método de repartição de Σx", "choice", "DIN", choices=["DIN", "BS", "ISO"], group="deslocamento", stage=G,
                  help="Regra para repartir a soma de deslocamentos entre as rodas no modo 'Inicial': DIN 3992 (gráfico), BS 436 (G/F/V) ou ISO/TR 4467 (λ)."),
    "M_BS": P("Critério BS 436", "choice", None, choices=["G", "F", "V"], group="deslocamento", stage=G, nullable=True,
              help="Só para método BS: G = aplicações gerais; F = igualdade de resistência à flexão; V = igualdade de velocidade de deslizamento."),
    "Lambda": P("λ (ISO/TR 4467)", "number", None, min=0.3, max=1.0, group="deslocamento", stage=G, nullable=True,
                help="Só para método ISO: fator de repartição, recomendado entre 0,5 e 0,75."),

    # --- espessura / tolerâncias
    "afastamento_pinhao": P("Afastamento do pinhão (DIN 3967)", "choice", "d", choices=AFAST, group="espessura", stage=G, help=HELP_AFAST),
    "afastamento_coroa": P("Afastamento da coroa (DIN 3967)", "choice", "d", choices=AFAST, group="espessura", stage=G, help=HELP_AFAST),
    "tol_pinhao": P("Série de tolerância do pinhão", "int", 25, min=21, max=30, group="espessura", stage=G, help=HELP_TOL),
    "tol_coroa": P("Série de tolerância da coroa", "int", 25, min=21, max=30, group="espessura", stage=G, help=HELP_TOL),
    "ASNE_min_pinhao": P("A_sne mínimo do pinhão (imposto)", "number", None, "mm", group="espessura", stage=G, nullable=True, advanced=True,
                         help="Afastamento mínimo imposto sobre a espessura do dente (negativo em externa). Vazio: calculado pelo grupo DIN 3967."),
    "ASNE_max_pinhao": P("A_sne máximo do pinhão (imposto)", "number", None, "mm", group="espessura", stage=G, nullable=True, advanced=True,
                         help="Afastamento máximo imposto. Vazio: calculado pela série de tolerância."),
    "ASNE_min_coroa": P("A_sne mínimo da coroa (imposto)", "number", None, "mm", group="espessura", stage=G, nullable=True, advanced=True, help="Idem ao pinhão, para a coroa."),
    "ASNE_max_coroa": P("A_sne máximo da coroa (imposto)", "number", None, "mm", group="espessura", stage=G, nullable=True, advanced=True, help="Idem ao pinhão, para a coroa."),

    # --- modificações do dente
    "f_chanfro_pinhao": P("Fator de chanfro de cabeça do pinhão", "number", 0.0, min=0, max=0.5, group="modificacoes", stage=G, fig="inicio_chanfro.png",
                          help="Comprimento relativo do chanfro na cabeça do dente (Mazzo: 0,125 ≤ f ≤ 0,5, ideal 0,15). 0 = sem chanfro. Reduz o diâmetro útil de cabeça."),
    "f_chanfro_coroa": P("Fator de chanfro de cabeça da coroa", "number", 0.0, min=0, max=0.5, group="modificacoes", stage=G, help="Idem ao pinhão, para a coroa."),
    "f_b_pinhao": P("Fator de largura do pinhão", "number", 1.6, min=1.0, max=3.0, group="modificacoes", stage=G, advanced=True,
                    help="Fator multiplicador da largura mínima estimada pela flexão quando 'Largura do pinhão' está vazia."),
    "f_b_coroa": P("Fator de largura da coroa", "number", 1.6, min=1.0, max=3.0, group="modificacoes", stage=G, advanced=True, help="Idem para a coroa."),
    "crwon_s_pinhao": P("Abaulamento superior do pinhão", "number", 0.0, "mm", min=0, group="modificacoes", stage=G, help=HELP_CROWN),
    "crwon_i_pinhao": P("Abaulamento inferior do pinhão", "number", 0.0, "mm", min=0, group="modificacoes", stage=G, help=HELP_CROWN),
    "crwon_s_coroa": P("Abaulamento superior da coroa", "number", 0.0, "mm", min=0, group="modificacoes", stage=G, help=HELP_CROWN),
    "crwon_i_coroa": P("Abaulamento inferior da coroa", "number", 0.0, "mm", min=0, group="modificacoes", stage=G, help=HELP_CROWN),

    # --- acabamento
    "op_acabamento_pinhao": P("Acabamento do pinhão", "choice", "Retificação", choices=OP_ACAB, group="acabamento", stage=G, fig="indice_qualidade_processo.png",
                              help="Operação de acabamento dos flancos. Retificação alcança IQ 1–5; rasqueteamento 6–9; fresamento 10–12. Define o sobremetal de acabamento quando não informado."),
    "op_acabamento_coroa": P("Acabamento da coroa", "choice", "Retificação", choices=OP_ACAB, group="acabamento", stage=G, help="Idem ao pinhão."),
    "IQ_pinhao": P("Qualidade ISO 1328 do pinhão", "int", 6, min=1, max=12, group="acabamento", stage=G,
                   help="Grau de qualidade do dentado (ISO 1328-1:1995). Menor = mais preciso. Define as tolerâncias f_pt, f_fα e f_Hβ (fórmulas do grau 5 × √2 por grau, médias geométricas das faixas de m, d e b) usadas em K_v, K_Hβ e K_Hα."),
    "IQ_coroa": P("Qualidade ISO 1328 da coroa", "int", 6, min=1, max=12, group="acabamento", stage=G, help="Idem ao pinhão."),
    "Ra_flanco_pinhao": P("Ra do flanco do pinhão", "number", 0.8, "µm", min=0.05, group="acabamento", stage=G, fig="rugosidade.png",
                          help="Rugosidade média aritmética dos flancos. Usa-se Rz ≈ 6·Ra em Z_R. Retificado: 0,4–0,8 µm; rasqueteado: 0,8–1,6; fresado: 1,6–6,3."),
    "Ra_flanco_coroa": P("Ra do flanco da coroa", "number", 0.8, "µm", min=0.05, group="acabamento", stage=G, help="Idem ao pinhão."),
    "Ra_pe_pinhao": P("Ra do pé do pinhão", "number", 3.0, "µm", min=0.05, group="acabamento", stage=G,
                      help="Rugosidade do raio de pé (não retificado normalmente). Entra em Y_RrelT. Fresado/gerado: 3–6 µm."),
    "Ra_pe_coroa": P("Ra do pé da coroa", "number", 3.0, "µm", min=0.05, group="acabamento", stage=G, help="Idem ao pinhão."),
    "S_M_pinhao": P("Sobremetal de acabamento do pinhão", "number", None, "mm", min=0, group="acabamento", stage=G, nullable=True,
                    help="Sobremetal por flanco deixado para a operação de acabamento. Vazio: estimado pela tabela de Mazzo (operação, número de entradas/lâminas do hob). Entra na protuberância efetiva S_pr = pr − SM."),
    "S_M_coroa": P("Sobremetal de acabamento da coroa", "number", None, "mm", min=0, group="acabamento", stage=G, nullable=True, help="Idem ao pinhão."),

    # --- seguranças
    "S_Hmin": P("S_H mínimo", "number", 1.0, min=0.5, group="seguranca", stage=G,
                help="Coeficiente de segurança mínimo requerido contra pitting (ISO 6336-2). Típico 1,0 a 1,2."),
    "S_Fmin": P("S_F mínimo", "number", 1.2, min=0.5, group="seguranca", stage=G,
                help="Coeficiente de segurança mínimo requerido contra fratura do pé (ISO 6336-3). Típico 1,2 a 1,5."),
    "S_Hmax": P("S_H máximo (alvo)", "number", 1.3, min=0.5, group="seguranca", stage=G, advanced=True,
                help="Limite superior desejado de S_H; acima dele o projeto está superdimensionado (aviso)."),
    "S_Fmax": P("S_F máximo (alvo)", "number", 1.6, min=0.5, group="seguranca", stage=G, advanced=True,
                help="Limite superior desejado de S_F; usado também na estimativa da largura mínima quando b está vazio."),

    # --- corpo / eixos / mancais
    "Arranjo_pinhao": P("Arranjo físico do pinhão", "choice", 1, choices=[1, 2, 3, 4, 5, 6, 7], group="corpo", stage=G, nullable=True, fig="arranjos.png", help=HELP_ARRANJO),
    "Arranjo_coroa": P("Arranjo físico da coroa", "choice", 1, choices=[1, 2, 3, 4, 5, 6, 7], group="corpo", stage=G, nullable=True, help=HELP_ARRANJO),
    "k_linha_pinhao": P("Constante K' do pinhão (manual)", "number", None, group="corpo", stage=G, nullable=True, advanced=True,
                        help="Constante de posição K' usada em f_sh (deflexão do eixo, ISO 6336-1 método C). Só é usada quando o arranjo está vazio."),
    "k_linha_coroa": P("Constante K' da coroa (manual)", "number", None, group="corpo", stage=G, nullable=True, advanced=True, help="Idem ao pinhão."),
    "di_pinhao": P("Diâmetro interno da alma do pinhão d_i", "number", 0.0, "mm", min=0, group="corpo", stage=G, fig="alma.jpg",
                   help="Diâmetro do furo/aro da roda (0 = roda maciça ou integrada ao eixo). Usado na espessura de aro s_R (Y_B) e na inércia para K_v. Para anelar, informe o diâmetro EXTERNO do aro com sinal negativo."),
    "di_coroa": P("Diâmetro interno da alma da coroa d_i", "number", 0.0, "mm", group="corpo", stage=G, help="Idem ao pinhão. Anelar: diâmetro externo do aro, negativo."),
    "bs_pinhao": P("Espessura da alma do pinhão b_s", "number", 30.0, "mm", min=0, group="corpo", stage=G,
                   help="Espessura axial da alma (disco) da roda. Entra no fator Y_B / C_R de rigidez de corpo. Roda maciça: igual à largura."),
    "bs_coroa": P("Espessura da alma da coroa b_s", "number", 30.0, "mm", min=0, group="corpo", stage=G, help="Idem ao pinhão."),
    "d_sh_pinhao": P("Diâmetro do eixo do pinhão d_sh", "number", 30.0, "mm", min=0, group="corpo", stage=G, fig="eixo.png",
                     help="Diâmetro do eixo onde o pinhão está montado. Usado na deflexão f_sh (K_Hβ) e na razão d/d_sh do arranjo físico."),
    "d_sh_coroa": P("Diâmetro do eixo da coroa d_sh", "number", 30.0, "mm", min=0, group="corpo", stage=G, help="Idem ao pinhão. Para o planeta, é o diâmetro do pino do porta-planetas."),
    "L_pinhao": P("Distância entre mancais do pinhão l", "number", 100.0, "mm", min=0, group="corpo", stage=G,
                  help="Vão entre os centros dos mancais que apoiam o eixo do pinhão (plano axial). Usado em f_sh."),
    "L_coroa": P("Distância entre mancais da coroa l", "number", 100.0, "mm", min=0, group="corpo", stage=G, help="Idem ao pinhão."),
    "sh_pinhao": P("Desalinhamento do pinhão s", "number", 0.0, "mm", min=0, group="corpo", stage=G,
                   help="Distância entre o meio da roda e o meio do vão entre mancais (0 = roda centrada). Entra em f_sh pelo arranjo."),
    "sh_coroa": P("Desalinhamento da coroa s", "number", 0.0, "mm", min=0, group="corpo", stage=G, help="Idem ao pinhão."),
    "F_B_rolamento": P("Excentricidade dos mancais", "number", 0.01, "mm", min=0, group="corpo", stage=G, advanced=True,
                       help="Excentricidade radial dos rolamentos usada no jogo entre flancos (valor sugerido 0,01 mm)."),

    # --- temperaturas
    "C_Cdil": P("Coef. de dilatação da carcaça", "number", 1e-05, "1/°C", min=0, group="temperatura", stage=G,
                help="Coeficiente de dilatação térmica linear da carcaça (alumínio ≈ 2,3e-5; ferro fundido ≈ 1,0e-5). Entra na variação do jogo com a temperatura."),
    "T_Rmd": P("Temperatura das rodas (máx. diferença)", "number", 60.0, "°C", group="temperatura", stage=G,
               help="Temperatura das engrenagens no instante de máxima diferença térmica entre rodas e carcaça."),
    "T_Cmd": P("Temperatura da carcaça (máx. diferença)", "number", 30.0, "°C", group="temperatura", stage=G,
               help="Temperatura da carcaça no mesmo instante."),
    "T_op": P("Temperatura de operação", "number", 60.0, "°C", group="temperatura", stage=G,
              help="Temperatura de regime do óleo/engrenagens. Usada na viscosidade de operação (Z_L)."),

    # --- controle dimensional
    "k_otimi_pinhao": P("Dentes medidos W_k do pinhão (imposto)", "int", None, min=2, group="controle", stage=G, nullable=True, fig="dimensao_w.jpg",
                        help="Número k de dentes abrangidos na medida Wildhaber W_k. Vazio: calculado pela DIN 3960 (medição no meio da altura útil)."),
    "k_otimi_coroa": P("Dentes medidos W_k da coroa (imposto)", "int", None, min=2, group="controle", stage=G, nullable=True, help="Idem ao pinhão."),
    "Dim_sobre_pinos_pinhao": P("Diâmetro de pino/esfera do pinhão (imposto)", "number", None, "mm", min=0, group="controle", stage=G, nullable=True, fig="dimensao_m.jpg",
                                help="Diâmetro D_M do rolete/esfera para a medida M. Vazio: escolhido pelo programa (≈1,7·m_n externa, 1,9·m_n interna)."),
    "Dim_sobre_pinos_coroa": P("Diâmetro de pino/esfera da coroa (imposto)", "number", None, "mm", min=0, group="controle", stage=G, nullable=True, help="Idem ao pinhão."),

    # --- lubrificação
    "imersao": P("Roda mais imersa em óleo", "choice", "pinhão", choices=["pinhão", "coroa", "nenhuma"], group="lubrificacao", stage=G,
                 help="Qual roda fica mais submersa no banho de óleo. Usada para estimar volume de óleo e profundidade de imersão."),

    # --- métodos
    "metodo_YF": P("Método do fator de forma Y_F", "choice", "B", choices=["B", "C"], group="metodos", stage=G,
                   help="ISO 6336-3 método B: carga no ponto exterior de engrenamento individual (padrão ISO). Método C: carga na ponta com Y_ε (DIN 3990 / KISSsoft)."),
    "metodo_YF_interno": P("Y_F de dentado interno", "choice", "cortador", choices=["cortador", "rack", "legado"], group="metodos", stage=G, advanced=True,
                           help="'cortador' (padrão, ISO 6336-3 §6.2.4/6.2.5): pé da anelar gerado pelo pinhão-cortador z₀ da ferramenta da coroa, seção crítica a 60°; exige 'Dentes do pinhão-cortador' na ferramenta da anelar (sem ele cai no 'rack' com aviso). 'rack': cremalheira equivalente ao vão (DIN 3990, validado com KISSsoft). 'legado': formulação anterior de Mazzo (só comparação)."),
    "curva_vida": P("Curva de vida longa", "choice", "ISO", choices=["ISO", "DIN"], group="metodos", stage=G,
                    help="ISO 6336: Z_NT e Y_NT decaem até 0,85 em 10¹⁰ ciclos (conservador). DIN 3990 / KISSsoft: 1,0 acima de 3·10⁶ (flexão) e 5·10⁷ (pitting)."),
})

# ======================================================================================================
# MATERIAL (kwargs de Materiais)
# ======================================================================================================
M = "material"
CLASSES_MAT = {
    1: "Ferro fundido cinzento", 2: "Ferro fundido nodular perlítico", 3: "Ferro fundido nodular bainítico",
    4: "Ferro fundido nodular ferrítico", 5: "Ferro fundido nodular perlítico tratado", 6: "Ferro fundido nodular temperado por indução/chama",
    7: "Ferro fundido perlítico maleável", 8: "Aço fundido", 9: "Aço fundido tratado", 10: "Aço normalizado ou recozido (σ_B < 800 MPa)",
    11: "Aço temperado e revenido (σ_B ≥ 800 MPa)", 12: "Aço temperado por indução ou chama", 13: "Aço cementado, temperado e revenido",
    14: "Aço temperado, revenido e nitretado a gás", 15: "Aço temperado, revenido e nitretado em líquido",
    16: "Aço carbonitretado, camada < 0,3 mm", 17: "Aço carbonitretado, camada ≥ 0,3 mm",
}
PARAMS.update({
    "mat_apelido": P("Nome do material", "text", "Material", group="mat", stage=M, help="Identificação livre."),
    "mat_composicao": P("Designação / composição", "text", "20MnCr5", group="mat", stage=M, help="Liga (ex.: 20MnCr5, 18CrNiMo7-6, 8622H)."),
    "mat_classe": P("Classe de material (ISO 6336-5)", "choice", 13, choices=list(CLASSES_MAT.keys()), group="mat", stage=M,
                    help="Classe do material/tratamento segundo a ISO 6336-5. Define as curvas de Z_NT, Y_NT, Z_X, Y_X e Y_RrelT. 13 = aço cementado (mais comum em planetários)."),
    "mat_classe_KHbeta": P("Classe para K_Hβ (amaciamento)", "choice", 3, choices=[1, 2, 3], group="mat", stage=M,
                           help="Grupo de material para o amaciamento y_β e y_α (ISO 6336-1): 1 = aço não endurecido superficialmente (y ∝ 1/σ_Hlim); 2 = ferro fundido; 3 = aço endurecido (cementado, nitretado)."),
    "mat_classe_Y_Rel": P("Classe para Y_δrelT", "choice", 15, choices=[10, 11, 12, 13, 14, 15, 16], group="mat", stage=M,
                          help="Grupo para a sensibilidade relativa ao entalhe Y_δrelT (ISO 6336-3): 10 = aço recozido/normalizado; 11 = aço temperado e revenido; 12 = ferro fundido nodular; 13 = ferro fundido cinzento; 14 = aço de alta resistência; 15 = aço cementado/endurecido; 16 = nitretado."),
    "mat_tipo": P("Tipo", "text", "Aço", group="mat", stage=M, help="Família: aço, ferro fundido, bronze, polímero."),
    "mat_rho": P("Massa específica ρ", "number", 7.83e-06, "kg/mm³", min=0, group="mat", stage=M, help="Usada nas inércias de K_v (aço 7,83e-6 kg/mm³)."),
    "mat_Lim_pressao": P("σ_Hlim (pitting)", "number", 1500.0, "MPa", min=0, group="mat", stage=M,
                         help="Limite de resistência à pressão de contato de referência (ISO 6336-5, qualidade MQ/ME). Aço cementado MQ ≈ 1300–1500 MPa."),
    "mat_Lim_flexao": P("σ_Flim (flexão)", "number", 430.0, "MPa", min=0, group="mat", stage=M,
                        help="Tensão nominal limite de flexão no pé (ISO 6336-5). Aço cementado MQ ≈ 430–500 MPa (σ_FE = 2·σ_Flim ≈ 860–1000 MPa)."),
    "mat_Lim_escoa": P("Limite de escoamento", "number", 1200.0, "MPa", min=0, group="mat", stage=M, help="σ_y do núcleo; informativo e usado em verificações estáticas."),
    "mat_Lim_tracao": P("Limite de resistência à tração σ_B", "number", 1200.0, "MPa", min=0, group="mat", stage=M, help="Informativo; separa classes 10/11."),
    "mat_E": P("Módulo de elasticidade E", "number", 206.0, "GPa", min=1, group="mat", stage=M, help="Entra em Z_E e na rigidez do dente c'."),
    "mat_Possion": P("Coeficiente de Poisson ν", "number", 0.3, min=0, max=0.5, group="mat", stage=M, help="Entra em Z_E."),
    "mat_Qualidade": P("Qualidade do material (ISO 6336-5)", "choice", "MQ", choices=["ML", "MQ", "ME"], group="mat", stage=M, fig="MQ.jpg",
                       help="ML: requisitos modestos; MQ: qualidade industrial com controle (padrão); ME: alta qualidade com controle rigoroso."),
    "mat_tratamento_termico": P("Tratamento térmico", "text", "Cementação", group="mat", stage=M, help="Descrição do tratamento (cementação, têmpera por indução, nitretação...)."),
    "mat_profund_camada_tratamento": P("Profundidade de camada", "number", 0.6, "mm", min=0, group="mat", stage=M, nullable=True, fig="cementacao.jpg",
                                       help="Profundidade efetiva da camada endurecida (recomendação 0,15 a 0,2·m_n para cementação)."),
    "mat_dureza_nucleo": P("Dureza do núcleo", "number", 40.0, "HRC", min=0, max=70, group="mat", stage=M, help="Dureza do núcleo em HRC (recomendado > 30–40 HRC para choques)."),
    "mat_dureza_superficial": P("Dureza superficial", "number", 60.0, "HRC", min=0, max=70, group="mat", stage=M, help="Dureza dos flancos em HRC (cementado 58–63 HRC). Usada em Z_W quando a coroa é mais macia (convertida para HB)."),
    "mat_coef_dilatacao": P("Coef. de dilatação térmica", "number", 1.15e-05, "1/°C", min=0, group="mat", stage=M, help="Entra no jogo entre flancos com a temperatura."),
})

# ======================================================================================================
# FERRAMENTA (kwargs de Ferramentas)
# ======================================================================================================
F = "ferramenta"
PARAMS.update({
    "fer_apelido": P("Nome da ferramenta", "text", "Ferramenta", group="fer", stage=F, help="Identificação livre."),
    "fer_tipo": P("Tipo", "choice", "Hob", choices=["Hob", "Shaper"], group="fer", stage=F, nullable=True,
                  help="Hob (fresa caracol) gera dentado externo; shaper (pinhão-cortador) é necessário para dentado interno e rodas com ressalto."),
    "fer_Z0_hob": P("Entradas do hob", "int", 1, min=1, group="fer", stage=F, nullable=True, help="Número de entradas (filetes) da fresa caracol. Entra na estimativa do sobremetal."),
    "fer_i_hob": P("Lâminas (ranhuras) do hob", "int", 14, min=1, group="fer", stage=F, nullable=True, help="Número de ranhuras/lâminas do hob. Entra na estimativa do sobremetal."),
    "fer_Z_shaper": P("Dentes do pinhão-cortador z₀", "int", None, min=5, group="fer", stage=F, nullable=True,
                      help="Número de dentes do shaper. Necessário para dentado interno: Y_F e Y_S da anelar pela geometria do cortador (ISO 6336-3 §6.2.4) e o perfil 2D da anelar. Vazio na anelar: Y_F cai na cremalheira equivalente, com aviso."),
    "fer_k_a": P("Fator de adendo h_aP*", "number", 1.0, min=0.5, max=1.5, group="fer", stage=F, fig="cabeca.png",
                 help="Altura de cabeça do dente em múltiplos do módulo (1,0 = padrão; >1 adendo alongado; <1 encurtado)."),
    "fer_cp_dedendo": P("Fator de dedendo h_fP*", "number", 1.25, min=1.0, max=1.6, group="fer", stage=F, fig="pe.png",
                        help="Altura de pé do dente em múltiplos do módulo (1,25 = padrão com folga 0,25·m_n; 1,4 com protuberância/retífica)."),
    "fer_rk": P("Raio de ponta da ferramenta ρ_aP0", "number", None, "mm", min=0, group="fer", stage=F, nullable=True, fig="crista.jpg",
                help="Raio de arredondamento da ponta da cremalheira/cortador, que gera o raio de pé ρ_F. Vazio: o programa usa o raio máximo possível (pé pleno). Típico 0,25–0,38·m_n."),
    "fer_pr": P("Protuberância pr₀", "number", 0.0, "mm", min=0, group="fer", stage=F, fig="pretuberancia.jpg",
                help="Protuberância da ferramenta: alívio no pé do dente para que a retífica não deixe degrau. Efetiva S_pr = pr₀ − sobremetal. 0 = sem protuberância."),
})

# ======================================================================================================
# LUBRIFICANTE
# ======================================================================================================
L = "lubrificante"
PARAMS.update({
    "lub_apelido": P("Nome", "text", "Lubrificante", group="lub", stage=L, help="Identificação livre."),
    "lub_tipo": P("Designação comercial", "text", "ISO VG 220", group="lub", stage=L, nullable=True, help="Nome técnico/comercial."),
    "lub_base_quimica": P("Base química", "text", None, group="lub", stage=L, nullable=True, help="Mineral, PAO, PAG..."),
    "lub_visc_40": P("Viscosidade cinemática a 40 °C", "number", 220.0, "mm²/s", min=1, group="lub", stage=L,
                     help="ν₄₀ do óleo (ISO VG). Entra no fator de lubrificação Z_L."),
})

# ======================================================================================================
# ETAPA C — TENSÕES (kwargs de Analise_de_tensao)
# ======================================================================================================
T_ = "tensoes"
PARAMS.update({
    "an_apelido": P("Apelido da análise", "text", "Planetário", group="conjunto", stage=T_, help="Nome usado no relatório de tensões."),
    "k1": P("Rodas no eixo do pinhão (malha 1) k₁", "int", 100, min=1, group="conjunto", stage=T_,
            help="Número de engrenagens no mesmo eixo do pinhão da malha 1, ou fator de proporção de deflexão. Afeta f_sh em K_Hβ método C. Use 100 quando o pinhão não é afetado por outras rodas no eixo."),
    "k2": P("Rodas no eixo do pinhão (malha 2) k₂", "int", 50, min=1, group="conjunto", stage=T_, nullable=True, help="Idem para a segunda malha (planeta menor × anelar)."),
    "Ck1": P("Recuo de cabeça C_a da malha 1", "number", None, "µm", min=0, group="fatores", stage=T_, nullable=True,
             help="Alívio de ponta (tip relief) especificado, em µm, usado em K_v. Vazio: o programa usa C_ay calculado pela ISO 6336-1 a partir de σ_Hlim."),
    "Ck2": P("Recuo de cabeça C_a da malha 2", "number", None, "µm", min=0, group="fatores", stage=T_, nullable=True, help="Idem para a malha 2."),
    "Tipo_planetario_an": P("Tipo de planetário", "choice", "Composto", choices=["Simples", "Composto"], group="conjunto", stage=T_,
                            help="Define o modelo de inércias para a rotação de ressonância de K_v: simples (um planeta) ou composto (planeta duplo em um corpo). Só usado com as duas malhas selecionadas."),
    "Ring": P("Anelar", "choice", "Fixo", choices=["Fixo", "Rotativo"], group="conjunto", stage=T_,
              help="Anelar fixa à carcaça ou rotativa (saída/entrada). Muda a inércia equivalente usada em K_v."),
    "K_Hbeta_imposto1": P("K_Hβ imposto na malha 1", "number", None, min=1.0, max=3.0, group="fatores", stage=T_, nullable=True,
                          help="Força o fator de distribuição longitudinal de carga da malha 1 (ex.: 1,20 do KISSsoft) em vez do método C da ISO 6336-1. Vazio: calculado."),
    "K_Hbeta_imposto2": P("K_Hβ imposto na malha 2", "number", None, min=1.0, max=3.0, group="fatores", stage=T_, nullable=True, help="Idem para a malha 2."),
})

# ======================================================================================================
# ETAPA A — CINEMÁTICA (busca de dentes; inputs da célula 6 do Dim_cinematico + limites da busca)
# ======================================================================================================
C = "cinematica"
HELP_KA_CIN = "Fator de adendo h_aP* desta roda (1 = padrão; >1 alongado; <1 encurtado)."
HELP_CP_CIN = "Fator de dedendo h_fP* desta roda (1,25 padrão, folga 0,25·m_n)."
PARAMS.update({
    "reduction": P("Redução alvo i", "number", 11.5, min=1.01, group="objetivo", stage=C, fig="Speed_ratio.png",
                   help="Razão de redução desejada entre entrada e saída (n_in/n_out). Para sol→porta-planetas com anelar fixa: i = 1 + z_r·z_bp/(z_s·z_sp)."),
    "tol_reduction": P("Tolerância da redução", "number", 0.5, min=0, group="objetivo", stage=C, help="Faixa aceitável em torno da redução alvo (±)."),
    "Planetary_Type": P("Tipo de planetário", "choice", 1, choices=[0, 1], group="objetivo", stage=C, fig="Compound_Epicyclic.png",
                        help="0 = simples (um planeta engrena com sol e anelar, mesmo módulo); 1 = composto (planeta maior com o sol, planeta menor com a anelar, módulos independentes)."),
    "torq_Input": P("Membro de entrada", "choice", 0, choices=[0, 1, 2], group="objetivo", stage=C, help="0 = sol; 1 = porta-planetas; 2 = anelar."),
    "torq_Output": P("Membro de saída", "choice", 1, choices=[0, 1, 2], group="objetivo", stage=C, help="0 = sol; 1 = porta-planetas; 2 = anelar. O terceiro membro fica fixo."),
    "N_Cp": P("Número de planetas", "int", 3, min=1, max=8, group="objetivo", stage=C, fig="Hunting_conditions.png",
              help="Planetas igualmente espaçados. A busca verifica a condição de montagem (z_s + z_r)/N múltiplo inteiro ou com defasagem, a condição de hunting e a folga entre planetas vizinhos."),

    "alpha_n_ext": P("α_n da malha externa", "number", 20.0, "°", min=10, max=30, group="malhas", stage=C, help="Ângulo de pressão normal sol × planeta."),
    "alpha_n_int": P("α_n da malha interna", "number", 25.0, "°", min=10, max=30, group="malhas", stage=C, help="Ângulo de pressão normal planeta × anelar (só composto; simples usa o externo)."),
    "m_n_ext": P("m_n da malha externa", "number", 0.7, "mm", min=0.1, group="malhas", stage=C, help="Módulo normal sol × planeta maior."),
    "tol_m_n_ext": P("Variação de m_n externa", "number", 0.0, "mm", min=0, group="malhas", stage=C, help="Se > 0, a busca varre 5 valores de módulo em ±tolerância."),
    "m_n_int": P("m_n da malha interna", "number", 1.3, "mm", min=0.1, group="malhas", stage=C, help="Módulo normal planeta menor × anelar (só composto)."),
    "tol_m_n_int": P("Variação de m_n interna", "number", 0.0, "mm", min=0, group="malhas", stage=C, help="Se > 0, varre 5 valores em ±tolerância."),
    "beta_ext": P("β da malha externa", "number", 0.0, "°", min=0, max=45, group="malhas", stage=C, help="Ângulo de hélice sol × planeta."),
    "tol_beta_ext": P("Variação de β externa", "number", 0.0, "°", min=0, group="malhas", stage=C, help="Se > 0, varre 5 valores."),
    "beta_int": P("β da malha interna", "number", 0.0, "°", min=0, max=45, group="malhas", stage=C, help="Ângulo de hélice planeta × anelar (só composto)."),
    "tol_beta_int": P("Variação de β interna", "number", 0.0, "°", min=0, group="malhas", stage=C, help="Se > 0, varre 5 valores."),

    "Upright_Diameter": P("Diâmetro interno máximo da manga", "number", 115.0, "mm", min=1, group="envelope", stage=C,
                          help="Envelope radial disponível: a anelar (diâmetro externo) e o círculo que envolve os planetas devem caber dentro deste diâmetro."),
    "Sr_ring": P("Espessura do aro da anelar", "number", 10.0, "mm", min=0, group="envelope", stage=C,
                 help="Espessura radial do aro da anelar do pé do dente até o diâmetro externo. Diâmetro externo = |d_f| + 2·S_r."),
    "tol_dist_centros": P("Variação da distância entre centros", "number", 3.0, "mm", min=0, group="envelope", stage=C,
                          help="A busca testa 10 distâncias entre centros em ±este valor em torno do padrão, gerando deslocamentos de perfil diferentes."),

    "k_a_sun": P("h_aP* do sol", "number", 1.0, min=0.5, max=1.5, group="perfil", stage=C, help=HELP_KA_CIN),
    "k_a_bp": P("h_aP* do planeta maior", "number", 1.0, min=0.5, max=1.5, group="perfil", stage=C, help=HELP_KA_CIN),
    "k_a_sp": P("h_aP* do planeta menor", "number", 1.0, min=0.5, max=1.5, group="perfil", stage=C, help=HELP_KA_CIN),
    "k_a_r": P("h_aP* da anelar", "number", 1.0, min=0.5, max=1.5, group="perfil", stage=C, help=HELP_KA_CIN),
    "cp_dedendo_sun": P("h_fP* do sol", "number", 1.25, min=1.0, max=1.6, group="perfil", stage=C, help=HELP_CP_CIN),
    "cp_dedendo_bp": P("h_fP* do planeta maior", "number", 1.25, min=1.0, max=1.6, group="perfil", stage=C, help=HELP_CP_CIN),
    "cp_dedendo_sp": P("h_fP* do planeta menor", "number", 1.25, min=1.0, max=1.6, group="perfil", stage=C, help=HELP_CP_CIN),
    "cp_dedendo_r": P("h_fP* da anelar", "number", 1.25, min=1.0, max=1.6, group="perfil", stage=C, help=HELP_CP_CIN),

    "Z_max_sun": P("z máximo do sol", "int", 50, min=6, max=200, group="busca", stage=C, help="Limite superior da varredura do sol (o mínimo é o z sem undercut)."),
    "Z_max_big": P("z máximo do planeta maior", "int", 100, min=6, max=300, group="busca", stage=C, help="Limite superior da varredura do planeta maior."),
    "Z_max_small": P("z máximo do planeta menor", "int", 100, min=6, max=300, group="busca", stage=C, help="Limite superior do planeta menor (composto)."),
    "Z_max_ring": P("z máximo da anelar", "int", 150, min=10, max=400, group="busca", stage=C, help="Limite superior da varredura da anelar."),
    "eps_alpha_min": P("ε_α mínimo", "number", 1.4, min=1.0, max=2.5, group="busca", stage=C, help="Grau de recobrimento de perfil mínimo aceito em cada malha."),
    "sum_x_max": P("|Σx| máximo", "number", 0.5, min=0, max=2, group="busca", stage=C, help="Soma máxima (em módulo) dos deslocamentos de perfil de cada malha."),
    "d_alpha_wt": P("Desvio máximo de α_wt", "number", 5.0, "°", min=0, max=15, group="busca", stage=C,
                    help="Diferença máxima admitida entre o ângulo de pressão de trabalho e α_n (limita o afastamento da distância entre centros padrão)."),
    "max_resultados": P("Máximo de resultados", "int", 500, min=10, max=5000, group="busca", stage=C, help="Interrompe a busca ao atingir este número de candidatos."),

    "n_sol": P("Rotação do sol", "number", 13000.0, "rpm", min=0, group="carga", stage=C, help="Rotação do sol usada para calcular as rotações de planetas e porta-planetas do candidato escolhido (preenche a etapa B)."),
    "T_sol": P("Torque no sol", "number", 31.0, "N·m", min=0, group="carga", stage=C, help="Torque total no sol; a função de cinemática deriva os torques de cada malha."),
})


def params_for(stage):
    return {k: v for k, v in PARAMS.items() if v["stage"] == stage}


def defaults_for(stage):
    return {k: v["default"] for k, v in PARAMS.items() if v["stage"] == stage}


def strip_prefix(stage, d):
    """Remove o prefixo mat_/fer_/lub_ das chaves para montar os kwargs das classes."""
    pref = {"material": "mat_", "ferramenta": "fer_", "lubrificante": "lub_"}.get(stage)
    if not pref:
        return dict(d)
    return {(k[len(pref):] if k.startswith(pref) else k): v for k, v in d.items()}


# ---------------------------------------------------------------------------------------------------------------------
# Tema do "Aprender" (chave de backend/docs/fatores.json) que explica cada parâmetro. O "?" do campo leva direto a ele.
# Chaves sem sufixo valem para _pinhao/_coroa; prefixos mat_/fer_/lub_ e "cinematica" têm regras abaixo.
DOC_PARAM = {
    "m_n": "modulo", "Z": "numero_dentes", "a": "distancia_centros", "ISO": "jogo", "b": "largura", "alpha_n": "angulo_pressao", "beta": "angulo_helice",
    "tipo": "desloc_perfil", "trans": "planetario", "N_cp": "planetario", "Ky": "planetario", "membro": "planetario", "Tipo_planetario": "planetario", "n_carrier": "planetario",
    "n_t": "forcas", "T": "forcas", "irregularidade": "aplicacao", "Ka_imposto": "aplicacao", "Vr": "vida",
    "x_pinhao": "desloc_perfil", "metodo_x": "desloc_perfil", "M_BS": "desloc_perfil", "Lambda": "desloc_perfil",
    "afastamento": "jogo", "tol": "tolerancias", "ASNE": "jogo", "f_chanfro": "chanfro", "f_b": "largura", "crwon": "K_Hbeta",
    "op_acabamento": "qualidade", "IQ": "qualidade", "Ra_": "qualidade", "S_M": "qualidade", "S_H": "seguranca", "S_F": "seguranca",
    "Arranjo": "arranjo", "k_linha": "arranjo", "di": "aro", "bs": "aro", "d_sh": "eixo", "L": "arranjo", "sh": "arranjo", "F_B_rolamento": "jogo",
    "C_Cdil": "temperatura", "T_Rmd": "temperatura", "T_Cmd": "temperatura", "T_op": "temperatura", "k_otimi": "controle_W_M", "Dim_sobre_pinos": "controle_W_M",
    "imersao": "lubrificacao", "metodo_YF": "Y_F", "curva_vida": "vida", "k1": "K_Hbeta", "k2": "K_Hbeta", "Ck": "K_Halpha", "K_Hbeta_imposto": "K_Hbeta", "Ring": "planetario",
    "mat_": "material", "lub_": "lubrificacao", "fer_k_a": "diam_cabeca", "fer_cp_dedendo": "diam_pe", "fer_": "raio_crista",
    "reduction": "planetario", "tol_reduction": "planetario", "Planetary_Type": "planetario", "torq_": "planetario", "N_Cp": "planetario",
    "alpha_n_": "angulo_pressao", "m_n_": "modulo", "beta_": "angulo_helice", "tol_m_n_": "modulo", "tol_beta_": "angulo_helice",
    "Upright_Diameter": "aro", "Sr_ring": "aro", "tol_dist_centros": "distancia_centros", "d_alpha_wt": "distancia_centros",
    "k_a_": "diam_cabeca", "cp_dedendo_": "diam_pe", "Z_max_": "numero_dentes", "eps_alpha_min": "recobrimento", "sum_x_max": "desloc_perfil", "n_sol": "forcas", "T_sol": "forcas",
}


def _doc_de(chave):
    base = chave
    for suf in ("_pinhao", "_coroa"):
        if base.endswith(suf):
            base = base[: -len(suf)]
    if base in DOC_PARAM:
        return DOC_PARAM[base]
    if chave in DOC_PARAM:
        return DOC_PARAM[chave]
    # prefixos (mais longos primeiro): Z_pinhao -> "Z", S_Hmin -> "S_H", Ra_flanco -> "Ra_", torq_Input -> "torq_"
    for pref in sorted((k for k in DOC_PARAM if k.endswith("_") or k in ("Z", "S_H", "S_F", "Ra_", "irregularidade", "membro", "afastamento", "tol", "ASNE", "crwon", "f_chanfro", "f_b", "k_otimi", "Dim_sobre_pinos")), key=len, reverse=True):
        if base.startswith(pref):
            return DOC_PARAM[pref]
    return None


DOC_EXTRA = {"metodo_YF_interno": "Y_F", "Ck1": "K_Halpha", "Ck2": "K_Halpha", "K_Hbeta_imposto1": "K_Hbeta", "K_Hbeta_imposto2": "K_Hbeta", "Tipo_planetario_an": "planetario"}
DOC_PARAM.update(DOC_EXTRA)
for _k, _p in PARAMS.items():
    _d = DOC_EXTRA.get(_k) or _doc_de(_k)
    if _d and not _p.get("doc"):
        _p["doc"] = _d
