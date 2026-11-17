# coding: utf-8
import Equações_dimensionamento as Eq
import math
import os
from fpdf import FPDF
from datetime import datetime
class Materiais:
    def __init__(self,apelido,composicao,classe_KHbeta,classe,classe_Y_Rel,tipo,rho,Lim_pressao,Lim_flexao,Lim_escoa,Lim_tracao,E,Possion,Qualidade,tratamento_termico,profund_camada_tratamento,dureza_nucleo,dureza_superficial,coef_dilatacao):
        self.apelido = apelido # apelido do materail
        self.tipo = tipo # se é um aço, um ferro , plástico e etc
        self.classe_KHbeta = classe_KHbeta # Classe que o material que se encaixa para cálculo do K_Hbeta
        self.classe = classe # Classe que o material que se encaixa
        self.classe_Y_Rel = classe_Y_Rel # Classe que o material que se encaixa para o cálculo do Y_delta_RelT
        self.composicao = composicao # Elemntos químicos que compo~e o material
        self.rho = rho # Densidade do material [Kg/m^3]
        self.Lim_pressao = Lim_pressao # Limite de tensão de pressão
        self.Lim_flexao = Lim_flexao # Limite de tensão de flexão
        self.Lim_escoa = Lim_escoa # Limite de escoamento do material
        self.Lim_tracao = Lim_tracao # Limite de resistência a tração dom material
        self.E = E # módulo de elasticidade do material
        self.Possion = Possion # Coeficiente de Possion
        self.Qualidade=Qualidade # Padrão de qualidade do material
        self.tratamento_termico = tratamento_termico # Tratamento térmico do materail
        self.profund_camada_tratamento = profund_camada_tratamento # Profundidade da camada de tratamento térmico do material do material
        self.dureza_nucleo = dureza_nucleo # Dureza do núcleo da engrenagem (Dureza recomendada para choques violentos = 40 Rc)
        self.dureza_superficial = dureza_superficial # Dureza superficial dos dentes (Dureza recomendada para cementação de  58 a 63 Rc)
        self.coef_dilatacao = coef_dilatacao # Coeficiênte de dilatação térmica do material


        if self.classe == 2 or self.classe == 3 or self.classe == 5 or self.classe == 8 or self.classe == 9 or self.classe == 10 or self.classe == 11 or self.classe == 13 or self.classe == 17 or self.classe == 12 or self.classe == 6 or self.classe == 7 :
            self.classe_Z_NT = 1
        elif self.classe == 1 or self.classe == 4 or self.classe == 14 or self.classe == 15 :
            self.classe_Z_NT = 2
        elif self.classe == 16 :
            self.classe_Z_NT = 3

        if  self.classe == 1 or self.classe == 2 or self.classe == 3 or self.classe == 4 or self.classe == 5 or self.classe == 8 or self.classe == 9 or self.classe == 10 or self.classe == 11 or self.classe == 7 :
            self.classe_Z_X = 1
        elif self.classe == 13 or self.classe == 17 or self.classe == 12 or self.classe == 6 :
            self.classe_Z_X = 2
        elif self.classe == 14 or self.classe == 15 or self.classe == 16 :
             self.classe_Z_X = 3

        if self.classe == 10 or self.classe == 2 or self.classe == 3 or self.classe == 7 or self.classe == 11 or self.classe == 9 or self.classe == 8 or self.classe == 5 :
            self.classe_Y_X = 1
        elif self.classe == 13 or self.classe == 12 or self.classe == 6 or self.classe == 14 or self.classe == 15 or self.classe == 16 or self.classe ==17 :
            self.classe_Y_X = 2
        elif self.classe ==1 or self.classe == 4 :
            self.classe_Y_X = 3

        if self.classe == 11 or self.classe == 9 or self.classe == 2 or self.classe == 3 or self.classe == 13 or self.classe == 12 or self.classe == 6 or self.classe == 5 or self.classe == 7 or self.classe == 17 :
            self.classe_Y_R_RelT = 1
        elif self.classe == 10 or self.classe == 8 :
            self.classe_Y_R_RelT = 2
        elif self.classe == 1 or self.classe == 4 or self.classe == 14 or self.classe == 15 or self.classe == 16 :
            self.classe_Y_R_RelT = 3

        if self.classe == 2 or self.classe == 3 or self.classe == 5 or self.classe == 8 or self.classe == 9 or self.classe == 10 or self.classe == 11 or self.classe == 7 :
            self.classe_Y_NT = 1
        elif self.classe == 13 or self.classe == 17 or self.classe == 12 or self.classe == 6 :
            self.classe_Y_NT = 2
        elif self.classe == 1 or self.classe == 4 or self.classe == 15  or self.classe == 14 :
            self.classe_Y_NT = 3
        elif  self.classe == 16 :
            self.classe_Y_NT = 4


        if self.classe == 1 :
            self.a = f"Ferro fundido cinzento"
        elif self.classe == 2 :
            self.a = f"Ferro fundido nodular perlítico"
        elif self.classe == 3 :
            self.a = f"Ferro fundido nodular bainítico"
        elif self.classe == 4 :
            self.a = f"Ferro fundido nodular ferrítico"
        elif self.classe == 5 :
            self.a = f"Ferro fundido nodular perlítico tratado"
        elif self.classe == 6 :
            self.a = f"Ferro fundido nodular temperado por indução ou chama"
        elif self.classe == 7 :
            self.a = f"Ferro fundido perlítico maleável"
        elif self.classe == 8 :
            self.a = f"Aço fundido"
        elif self.classe == 9 :
            self.a = f"Aço fundido tratado"
        elif self.classe == 10 :
            self.a = f"Aço normalizado ou recozido (sigma_B < 800 N/mm^2)"
        elif self.classe == 11 :
            self.a = f"Aço temperado e revenido (sigma_B >= 800 N/mm^2)"
        elif self.classe == 12 :
            self.a = f"Aço temperado por indução ou chama"
        elif self.classe == 13 :
            self.a = f"Aço cementado, temperado e revenido"
        elif self.classe == 14 :
            self.a = f"Aço temperado, revenido e nitretado à gas "
        elif self.classe == 15 :
            self.a = f"Aço temperado, revenido e nitretado em líquido "
        elif self.classe == 16 :
            self.a = f"Aço carbonitretado cpm camada < 0.3 mm "
        elif self.classe == 17 :
            self.a = f"Aço carbonitretado cpm camada >= 0.3 mm "






    def __str__(self):
        return (f"Apelido do material --> {self.apelido} \n"
                f"Composição do material --> {self.composicao} \n"
                f"Densidade [kg/mm^3] --> {self.rho} \n"
                f"Classe --> {self.a} \n"
                f"Tipo de material --> {self.tipo} \n"
                f"Limite de resistência a pressão [MPa] --> {self.Lim_pressao} \n"
                f"Limite de resistência a flexão [MPa] --> {self.Lim_flexao} \n"
                f"Limite de escoamento  [MPa] --> {self.Lim_escoa} \n"
                f"Limite de resistência a tração [MPa] --> {self.Lim_tracao} \n"
                f"Módulo de elasticidade do material [GPa] --> {self.E} \n"
                f"Coeficiente de Possion --> {self.Possion} \n"
                f"Padrão de qualidade --> {self.Qualidade} \n"
                f"Tratamento térmico utilizado --> {self.tratamento_termico} \n"
                f"Profundidade do tratamento térmico utilizado [mm] --> {self.profund_camada_tratamento} \n"
                f"Dureza de núcleo [HRC] --> {self.dureza_nucleo} \n"
                f"Dureza superficial [HRC] --> {self.dureza_superficial} \n"
                f"Coeficiente de dilatação térmica [1/°C]  --> {self.coef_dilatacao}  \n")
Mazzo_material = Materiais(apelido = "Exemplo Mazzo", composicao ="20MnCr5",classe_KHbeta = 3,classe = 13,classe_Y_Rel = 15,tipo= "Aço",rho = 7.83e-06,Lim_pressao = 1500 ,Lim_flexao = 430,Lim_escoa = 1200,
                           Lim_tracao = 1200 , E = 206 ,Possion = 0.3,Qualidade = "MQ",tratamento_termico = "Cementação",profund_camada_tratamento = 0.6,dureza_nucleo = "> 40",dureza_superficial = 60,
                           coef_dilatacao = 11.5e-06)


Norma1_material = Materiais(apelido = "Exemplo 1 da norma ISO 6336-30", composicao ="Eh",classe_KHbeta =3,classe = 13,classe_Y_Rel = 15,tipo= "Aço", rho = 7.83e-06, Lim_pressao = 1500 ,Lim_flexao = 500,Lim_escoa = 1200,
                           Lim_tracao = 1200,E =206, Possion = 0.3,Qualidade = "MQ",tratamento_termico = "Cementação",profund_camada_tratamento = 0.6,dureza_nucleo = 30 ,dureza_superficial = 60,
                           coef_dilatacao = 11.5e-06)

Norma6_material_pinhao = Materiais(apelido = "Exemplo 6 da norma ISO 6336-30", composicao ="Aço forjado, temperado e revenido",classe_KHbeta =1,classe = 11,classe_Y_Rel = 10,tipo= "Aço", rho = 7.83e-06, Lim_pressao = 780 ,Lim_flexao = 319,Lim_escoa = 500,
                           Lim_tracao = 500,E =206, Possion = 0.3,Qualidade = "MQ",tratamento_termico = "Sem",profund_camada_tratamento = None,dureza_nucleo = 31 ,dureza_superficial = 31,
                           coef_dilatacao = 11.5e-06)

Norma6_material_coroa = Materiais(apelido = "Exemplo 6 da norma ISO 6336-30", composicao ="Aço forjado, temperado e revenido",classe_KHbeta =1,classe = 11,classe_Y_Rel = 10,tipo= "Aço", rho = 7.83e-06, Lim_pressao = 714 ,Lim_flexao = 298,Lim_escoa = 500,
                           Lim_tracao = 500,E =206, Possion = 0.3,Qualidade = "MQ",tratamento_termico = "Sem",profund_camada_tratamento = None,dureza_nucleo = 24 ,dureza_superficial = 24,
                           coef_dilatacao = 11.5e-06)

Material_base = Materiais(apelido = "Materaial base para dimensionamento", composicao ="20MnCr5",classe_KHbeta =3 ,classe = 13,classe_Y_Rel = 15,tipo= "Aço", rho = 7.83e-06, Lim_pressao = 1270 ,Lim_flexao = 430,Lim_escoa = 1200,
                           Lim_tracao = 1200,E =206, Possion = 0.3,Qualidade = "MQ",tratamento_termico = "Cementação",profund_camada_tratamento = 0.3,dureza_nucleo = 40 ,dureza_superficial = 62,
                           coef_dilatacao = 11.5e-06)

Material_plat_antiga = Materiais(apelido = "Materaial utilizado na planetária anterior", composicao ="8622H",classe_KHbeta =3 ,classe = 13,classe_Y_Rel = 15,tipo= "Aço", rho = 7.83e-06, Lim_pressao = 1420 ,Lim_flexao = 650,Lim_escoa = 1200,
                           Lim_tracao = 1200,E =206, Possion = 0.3,Qualidade = "MQ",tratamento_termico = "Cementação",profund_camada_tratamento = 0.3,dureza_nucleo = 40 ,dureza_superficial = 62,
                           coef_dilatacao = 11.5e-06)

Material_Ref = Materiais(apelido = "Materaial com melhores valores de limite de pressão e de flexão", composicao ="17NiCrMo6",classe_KHbeta =3 ,classe = 13,classe_Y_Rel = 15,tipo= "Aço", rho = 7.83e-06, Lim_pressao = 1500 ,Lim_flexao = 500,Lim_escoa = 1200,
                           Lim_tracao = 1200,E =206, Possion = 0.3,Qualidade = "MQ",tratamento_termico = "Cementação",profund_camada_tratamento = 0.3,dureza_nucleo = 40 ,dureza_superficial = 62,
                           coef_dilatacao = 11.5e-06)




class Ferramentas:
    def __init__(self,apelido,tipo,Z0_hob,i_hob,Z_shaper,k_a,cp_dedendo,rk,pr):
        self.apelido = apelido # Nome da ferramenta
        self.tipo =tipo #Tipo de ferramenta (Hob ou shaper)
        self.Z0_hob = Z0_hob # Número de entradas do hob de usiangem
        self.i_hob = i_hob # Número de lâminas do hob do pinhão
        self.Z_shaper = Z_shaper# Número de dentes do shaper do pinhão
        self.k_a = k_a # Fator de altura do dente de adendo
        self.cp_dedendo =cp_dedendo # Fator de altura do pé do dente
        self.rk = rk # Raio de crista da ferramenta
        self.pr = pr # Peturberância da ferramenta


    def __str__(self):
        return (f"Apelido da ferramenta --> {self.apelido} \n"
                f"Tipo de ferramenta --> {self.tipo} \n"
                f"Número de entradas do hob  --> {self.Z0_hob} \n"
                f"Número de lâminas do hob --> {self.i_hob} \n"
                f"Número de dentes do shaper --> {self.Z_shaper} \n"
                f"Fator de altura de adendo do dente --> {self.k_a} \n"
                f"Fator de altura do pé do dente  --> {self.cp_dedendo} \n"
                f"Raio de crista da ferramenta [mm] --> {self.rk} \n"
                f"Preturberância da ferramenta [mm] --> {self.pr} \n")
Mazzo_ferramenta_pinhao=Ferramentas(apelido = "Exemplo Mazzo pinhão",tipo ="Hob" ,Z0_hob= 1,i_hob= 14,Z_shaper= None,k_a = 1.198102,cp_dedendo = 1.806972,rk =None, pr= 0.11)
Mazzo_ferramenta_coroa=Ferramentas(apelido = "Exemplo Mazzo coroa",tipo ="Hob" ,Z0_hob= 3,i_hob= 14,Z_shaper= None,k_a = 1.556972,cp_dedendo = 1.448102,rk =None, pr= 0.11)

Norma1_ferramenta_pinhao=Ferramentas(apelido = "Exemplo 1 da norma ISO 6336-30 pinhão",tipo ="Hob" ,Z0_hob= 1,i_hob= 14,Z_shaper= None,k_a = 1,cp_dedendo = 1.4,rk = 3.12, pr= 0)
Norma1_ferramenta_coroa=Ferramentas(apelido = "Exemplo 1 da norma ISO 6336-30 coroa",tipo ="Hob" ,Z0_hob= 3,i_hob= 14,Z_shaper= None,k_a = 1,cp_dedendo = 1.4,rk =3.12, pr= 0)

Norma6_ferramenta_pinhao=Ferramentas(apelido = "Exemplo 6 da norma ISO 6336-30 pinhão",tipo =None ,Z0_hob= None,i_hob= None,Z_shaper= None,k_a = 1,cp_dedendo = 1.25,rk = 4.68, pr= 0)
Norma6_ferramenta_coroa=Ferramentas(apelido = "Exemplo 6 da norma ISO 6336-30 coroa",tipo ="Shaper" ,Z0_hob= None,i_hob= None,Z_shaper= 20,k_a = 1,cp_dedendo = 1.25,rk =0, pr= 0)   # pinhão-cortador z0 = 20, x0 = 0 (ISO/TR 6336-30, Tabela 12)

base_ferramenta_pinhao=Ferramentas(apelido = "Ferramenta base para dimensionamento",tipo =None ,Z0_hob= None,i_hob= None,Z_shaper= None,k_a = 1,cp_dedendo = 1.4,rk = None , pr= 0)
base_ferramenta_coroa=Ferramentas(apelido = "Exemplo 6 da norma ISO 6336-30 coroa",tipo =None ,Z0_hob= None,i_hob= None,Z_shaper= None,k_a = 1,cp_dedendo = 1.4,rk = None, pr= 0)

Sun_ferramenta_pinhao=Ferramentas(apelido = "Ferramenta base para dimensionamento",tipo =None ,Z0_hob= None,i_hob= None,Z_shaper= None,k_a = 1.15,cp_dedendo = 1.4,rk = None , pr= 0)
Bp_ferramenta_coroa=Ferramentas(apelido = "Exemplo 6 da norma ISO 6336-30 coroa",tipo =None ,Z0_hob= None,i_hob= None,Z_shaper= None,k_a = 1.15,cp_dedendo = 1.4,rk = None, pr= 0)
class Lubrificante:
    def __init__(self,apelido,tipo,base_quimica,visc_40):
        self.apelido = apelido # Apelido do lubrificante
        self.tipo =tipo #Nome técnico do lubrificante
        self.base_quimica = base_quimica # Base química do lubrificante
        self.visc_40 = visc_40 # Viscosidade do lubrificante à 40°C

    def __str__(self):
        return (f"Apelido do material --> {self.apelido} \n"
                f"Nome do material --> {self.tipo} \n"
                f"Base qúimica do lubrificante --> {self.base_quimica} \n"
                f"Viscosidade do lubrificante à 40°C [mm2/s] --> {self.visc_40} \n")
Mazzo_lubrificante = Lubrificante(apelido = "Exemplo MAzzo",tipo = "Exemplo",base_quimica = None,visc_40 = 320)
Norma1_lubrificante = Lubrificante(apelido = "Exemplo 1 da norma ISO 6336-30",tipo = "Exemplo",base_quimica = None,visc_40 = 320)
Norma6_lubrificante = Lubrificante(apelido = "Exemplo 5 da norma ISO 6336-30",tipo = "Exemplo",base_quimica = None,visc_40 = 320)
base_lubrificante = Lubrificante(apelido = "Lubrificante base de cálculo",tipo = "GEM/MEG",base_quimica = None,visc_40 = 220)
class Engrenamento:
    def __init__(self,apelido,Proj,tipo,material_pinhao,material_coroa,ferramenta_pinhao,ferramenta_coroa,lubrificante, m_n, Z_pinhao, Z_coroa,a,b_pinhao,b_coroa,ISO, alpha_n,beta,x_pinhao,
                 metodo_x,M_BS,Lambda,afastamento_pinhao,afastamento_coroa,tol_pinhao,tol_coroa,ASNE_min_pinhao,ASNE_max_pinhao,ASNE_min_coroa,ASNE_max_coroa,
                 f_chanfro_pinhao,f_chanfro_coroa,f_b_pinhao,f_b_coroa,crwon_s_pinhao,crwon_i_pinhao,crwon_s_coroa,crwon_i_coroa,irregularidade_movida,
                 irregularidade_motora,op_acabamento_pinhao,op_acabamento_coroa,IQ_pinhao,IQ_coroa,Ra_flanco_pinhao,Ra_flanco_coroa,Ra_pe_pinhao,Ra_pe_coroa,S_Hmin,S_Fmin,
                 S_Hmax,S_Fmax,Arranjo_pinhao,Arranjo_coroa,k_linha_pinhao,k_linha_coroa,n_t,T,di_pinhao, di_coroa,bs_pinhao,bs_coroa,d_sh_pinhao,d_sh_coroa,L_pinhao,L_coroa,
                 sh_pinhao,sh_coroa,C_Cdil,T_Rmd,T_Cmd,T_op,Vr,k_otimi_pinhao,k_otimi_coroa,Dim_sobre_pinos_pinhao,Dim_sobre_pinos_coroa,trans,N_cp,Ky,F_B_rolamento,imersao,
                 S_M_pinhao,S_M_coroa,membro_pinhao = None,membro_coroa = None,n_carrier = None,Tipo_planetario = None,Ka_imposto = None,metodo_YF = "B",metodo_YF_interno = "cortador",curva_vida = "ISO"):

        ##########################################################################################################################################################################################
        self.AVISOS = [] # Vetor armazenador dos avisos
        self.apelido=apelido # Apelido do par engrenado
        self.Proj = Proj # Nome do Engenheiro responsável
        self.tipo = tipo # Interção inicial ou para otimização
        self.material_pinhao=material_pinhao# Material do pinhão
        self.material_coroa=material_coroa # Material da coroa
        self.ferramenta_pinhao = ferramenta_pinhao # Ferramenta de usinagem do pinhão
        self.ferramenta_coroa = ferramenta_coroa # Ferramenta de usinagem da coroa
        self.lubrificante = lubrificante # Lubrificante utilizado no prjeto
        self.m_n = m_n  # Módulo da engrenagem (m)
        self.Z_pinhao = Z_pinhao  # Número de dentes do pinhão
        self.Z_coroa = Z_coroa  # Número de dentes da coroa
        self.a =a # Distância entre centros das engrenagens
        self.ISO = ISO # Classe de tolerância da distância entre centros (variando de  5 a 11)
        self.u = self.Z_coroa/self.Z_pinhao # Razão de engrenamento
        self.alpha_n = alpha_n  # Ângulo de pressão (em graus)
        self.beta = beta # Ângulo de hélice (em graus)
        self.afastamento_pinhao = afastamento_pinhao # Afastamento para a espessura do dente ou sobre a dimensão do vão do pinhao
        self.afastamento_coroa = afastamento_coroa # Afastamento para a espessura do dente ou sobre a dimensão do vão da coroa
        self.tol_pinhao=tol_pinhao # Tolerância para espessura do dente ou para dimensão do vão do pinhão
        self.tol_coroa=tol_coroa # Tolerância para espessura do dente ou para dimensão do vão da coroa
        self.f_chanfro_pinhao=f_chanfro_pinhao # Correção de comprimento do chanfro na cabeça do dente do pinhão (Segundo mazzo 0.125 <=f <= 0.5 , sendo um valor ideal de 0.15)
        self.f_chanfro_coroa = f_chanfro_coroa # Correção de comprimento do chanfro na cabeça do dente da coroa (Segundo mazzo 0.125 <=f <= 0.5 , sendo um valor ideal de 0.15)
        self.f_b_pinhao=f_b_pinhao # Fator de correção no comprimento de dente sem otimização do pinhão
        self.f_b_coroa=f_b_coroa # Fator de correção no comprimento de dente sem otimização do pinhão
        self.ASNE_min_pinhao = ASNE_min_pinhao # Backlash mínimo sobre a espessura do dente ou dimensão do vão do pinhão
        self.ASNE_max_pinhao = ASNE_max_pinhao # Backlash máximo sobre a espessura do dente ou dimensão do vão do pinhão
        self.ASNE_min_coroa = ASNE_min_coroa # Backlash mínimo sobre a espessura do dente ou dimensão do vão da coroa
        self.ASNE_max_coroa = ASNE_max_coroa # Backlash máximo sobre a espessura do dente ou dimensão do vão da coroa
        self.crwon_s_pinhao = crwon_s_pinhao # Abaulamento superior do pinhao
        self.crwon_i_pinhao = crwon_i_pinhao # Abaulamento inferior do pinhao
        self.crwon_s_coroa = crwon_s_coroa # Abaulamento superior da coroa
        self.crwon_i_coroa = crwon_i_coroa # Abaulamento inferior da coroa
        self.irregularidade_movida = irregularidade_movida # Grau de irregularidade da roda movida
        self.irregularidade_motora = irregularidade_motora # Grau de irregularidade da roda motora
        self.op_acabamento_pinhao = op_acabamento_pinhao # Operação de acabamento dos dentes (Retífica, Resqueteamento ou Fresa)
        self.op_acabamento_coroa = op_acabamento_coroa # Operação de acabamento dos dentes (Retífica, Resqueteamento ou Fresa)
        self.IQ_pinhao = IQ_pinhao # Índice de qualidade do pinhão
        self.IQ_coroa = IQ_coroa # Índice de qualidade da coroa
        self.IQ = round((self.IQ_pinhao + self.IQ_coroa  )/2) # ìndice de qualidade média do conjunto
        self.Ra_flanco_pinhao = Ra_flanco_pinhao # Rugosidade média do flanco do dente do pinhão (valores de referência na figura  da documentação)
        self.Ra_flanco_coroa = Ra_flanco_coroa # Rugosidade média do flanco do dente da coroa (valores de referência na figura  da documentação)
        self.Rz_flanco_pinhao = self.Ra_flanco_pinhao * 6# Altura máxima do perfil de rugosidade dos flancos do dente do pinhão
        self.Rz_flanco_coroa = self.Ra_flanco_coroa * 6  # Altura máxima do perfil de rugosidade dos flancos do dente da coroa
        self.Ra_pe_pinhao = Ra_pe_pinhao # Rugosidade média do flanco do dente do pinhão (valores de referência na figura  da documentação)
        self.Ra_pe_coroa = Ra_pe_coroa # Rugosidade média do flanco do dente da coroa (valores de referência na figura  da documentação)
        self.Rz_pe_pinhao = self.Ra_pe_pinhao * 6# Altura máxima do perfil de rugosidade dos flancos do dente do pinhão
        self.Rz_pe_coroa = self.Ra_pe_coroa * 6  # Altura máxima do perfil de rugosidade dos flancos do dente da coroa
        self.S_Hmin = S_Hmin # Coeficiênte de segurança de falha por fadiga superficial mínimo
        self.S_Fmin = S_Fmin # Coeficiênte de segurança de falha por flexão mínimo
        self.S_Hmax = S_Hmax # Coeficiênte de segurança de falha por fadiga superficial máximo
        self.S_Fmax = S_Fmax # Coeficiênte de segurança de falha por flexão máximo
        self.n_t=n_t # rotação na região de maior torque
        self.T = T # Torque máximo
        self.di_pinhao = di_pinhao # Diâmetro de alma do pinhão [mm]
        self.di_coroa = di_coroa# Diâmetro de alma do pinhão [mm]
        self.bs_pinhao = bs_pinhao # Espessura de alma do pinhão [mm]
        self.bs_coroa = bs_coroa  # Espessura de alma da coroa [mm]
        self.Arranjo_pinhao = Arranjo_pinhao # tipo de arranjo físico do pinhão
        self.Arranjo_coroa = Arranjo_coroa # tipo de arranjo físico da coroa
        self.d_sh_pinhao=d_sh_pinhao # Diâmetro do eixo em que o pinhão está acentado [mm]
        self.d_sh_coroa=d_sh_coroa # Diâmetro do eixo em que o pinhão está acentado [mm]
        self.L_pinhao = L_pinhao # Distância entre os mancais do pinhão
        self.L_coroa = L_coroa # Distância entre os mancais do pinhão
        self.sh_pinhao = sh_pinhao # Distância entre o centro dos mancais até o centro do pinhão
        self.sh_coroa = sh_coroa # Distância entre o centro dos mancais até o centro do pinhão
        self.C_Cdil = C_Cdil # Coeficiênte de dilatação da caixa de engrenagens
        self.T_Rmd = T_Rmd # Temperatura dos engrenagens no instante de máxiam difernça de temperatura entre a caixa e as rodas
        self.T_Cmd = T_Cmd # Temperatura da caixa no instante de máxiam difernça de temperatura entre a caixa e as rodas
        self.T_op = T_op # Temperatura de operação
        self.Vr = Vr # Vida nominal requisitada do par
        self.k_otimi_pinhao = k_otimi_pinhao # Números de dentes consecutivos a se medir para otimização para o pinhao
        self.k_otimi_coroa = k_otimi_coroa # Números de dentes consecutivos a se medir para otimização para a coroa
        self.Dim_sobre_pinos_pinhao = Dim_sobre_pinos_pinhao # Diâmetro de pinos/roletes para otimização para o pinhão
        self.Dim_sobre_pinos_coroa =  Dim_sobre_pinos_coroa # Diâmetro de pinos/roletes para otimização para a coroa
        self.Ky = Ky #Fator de carregamento de malha
        self.trans = trans # tipo de Transmissão (Simples ou Planetário)
        self.N_cp = N_cp # Número de planetas na malha
        self.f_B_rolamento = F_B_rolamento # Excentricidade dos rolamento (Valor sugerido de 0.01)
        self.imersao =imersao # Qual das rodas que está mais abaixo (Mais imergida em óleo)
        self.S_M_pinhao = S_M_pinhao # Sobremetal indicado para o pinhão
        self.S_M_coroa = S_M_coroa # Sobremetal indicado para a caroa
        ##########################################################################################################################################################################################
        # CINEMÁTICA DA PLANETÁRIA (ISO 6336-1 §4.2 / AGMA 6123) -------------------------------------------------------------------------
        # membro_pinhao / membro_coroa : "sol", "planeta" ou "anelar" (None -> inferido: externa = sol/planeta ; interna = planeta/anelar)
        # n_t   : rotação ABSOLUTA do pinhão da malha [rpm]  (sol -> rotação do motor ; planeta -> rotação absoluta do planeta)
        # n_carrier : rotação absoluta do porta-planetas [rpm] (None -> 0, porta-planetas parado / par convencional)
        # n_rel : rotação do pinhão RELATIVA ao porta-planetas, usada em v_t, K_v, Z_V, ciclos de carga e escorregamento
        # contatos_* : nº de engrenamentos por volta relativa (sol e anelar = N_cp ; planeta = 1)
        # Y_M  : fator de carga alternada (ISO 6336-3/-5): 0.7 para planeta de planetário simples (engrena dos dois lados), 1 caso contrário
        self.Tipo_planetario = Tipo_planetario # "Simples" ou "Composto" (só informativo para Y_M)
        self.metodo_YF = metodo_YF # "B" (ISO método B) ou "C" (carga na ponta)
        self.metodo_YF_interno = metodo_YF_interno # "cortador" (pé gerado pelo pinhão-cortador z0, ISO 6336-3 §6.2.4; padrão), "rack" (cremalheira equivalente) ou "legado"
        self.curva_vida = curva_vida # "ISO" (Z_NT/Y_NT decaem até 0.85 em 1e10) ou "DIN" (= 1 acima de 3e6 / 5e7, como DIN 3990 / KISSsoft)
        self.n_carrier = n_carrier if n_carrier != None else 0
        if self.trans == "Planetário" :
            if membro_pinhao == None :
                membro_pinhao = "sol" if Z_coroa > 0 else "planeta"
            if membro_coroa == None :
                membro_coroa = "planeta" if Z_coroa > 0 else "anelar"
            if self.N_cp == None :
                self.N_cp = 1
            if self.Ky == None :
                self.Ky = 1
        self.membro_pinhao = membro_pinhao
        self.membro_coroa = membro_coroa
        self.n_rel = abs(self.n_t - self.n_carrier) # módulo da rotação relativa ao porta-planetas (o planeta gira em sentido oposto ao sol)
        if self.n_rel == 0 :
            raise ValueError("Rotação relativa ao porta-planetas nula: verifique n_t e n_carrier")
        self.contatos_pinhao = self.N_cp if (self.trans == "Planetário" and membro_pinhao in ("sol","anelar")) else 1
        self.contatos_coroa = self.N_cp if (self.trans == "Planetário" and membro_coroa in ("sol","anelar")) else 1
        alternada = (self.trans == "Planetário" and Tipo_planetario == "Simples")
        self.Y_M_pinhao = 0.7 if (alternada and membro_pinhao == "planeta") else 1.0
        self.Y_M_coroa = 0.7 if (alternada and membro_coroa == "planeta") else 1.0
        if Z_coroa > 0 and self.di_coroa != 0:
            if self.di_coroa < self.d_sh_coroa :
                self.di_coroa = self.d_sh_coroa
        if Z_pinhao > 0 and self.di_pinhao != 0 :
            if self.di_pinhao < self.d_sh_pinhao :
                self.di_pinhao = self.d_sh_pinhao
        #################################################################################################################################################################################
        self.Ka= Eq.KA(self.u,self.irregularidade_motora,self.irregularidade_movida) if Ka_imposto == None else Ka_imposto # Fator de aplicação (tabela ISO 6336-6 ou valor imposto)
        if self.ferramenta_pinhao.Z_shaper != None :
            self.u_shaper_pinhao = self.ferramenta_pinhao.Z_shaper/self.Z_pinhao  # Relação de transmissão de usinagem com shaper do pinhão
        else :
            self.u_shaper_pinhao = None # Relação de transmissão de usinagem com shaper do pinhão
        if self.ferramenta_coroa.Z_shaper != None :
            self.u_shaper_coroa = self.ferramenta_coroa.Z_shaper/self.Z_coroa  # Relação de transmissão de usinagem com shaper do pinhão
        else :
            self.u_shaper_coroa = None # Relação de transmissão de usinagem com shaper do pinhão
        self.SM_pinhao,self.SM_coroa =Eq.SM_acabamento(self.m_n,self.op_acabamento_pinhao,self.ferramenta_pinhao.i_hob,self.ferramenta_pinhao.Z0_hob,self.u_shaper_pinhao,self.op_acabamento_coroa,self.ferramenta_coroa.i_hob,self.ferramenta_coroa.Z0_hob,self.u_shaper_coroa,self.S_M_pinhao,self.S_M_coroa) # sobremetal para acabamento
        self.pr_pinhao = self.ferramenta_pinhao.pr # Pretuberância da ferramenta do pinhao
        self.pr_coroa = self.ferramenta_coroa.pr # Pretuberância da ferramenta  da coroa
        self.beta_b=Eq.beta_b(alpha_n,beta) # Ângulo de hélice sobre o circulo base (em graus)
        self.zn_pinhao = Eq.z_virt(self.Z_pinhao,self.beta_b,self.beta) # Número de dentes virtuais do pinhão
        self.zn_coroa = Eq.z_virt(self.Z_coroa,self.beta_b,beta) # Número de dentes virtuais da coroa
        self.Aa_s,self.Aa_i = Eq.Tol_dist_centros(self.a,ISO) # Tolerância da distância entre centros superior e inferior
        self.m_t = Eq.m_t(self.m_n,self.beta) # Modulo transversal do par
        self.alpha_t = Eq.alpha_t(self.alpha_n,self.beta) # Ângulo de presão transversal
        self.alpha_wt = Eq.alpha_wt(self.Z_pinhao,self.Z_coroa,self.m_t,self.a,self.alpha_t) # Ângulo de pressão transversal de trabalho
        self.alpha_wn = Eq.alpha_wn(self.alpha_wt,self.beta) #Ângulo de pressão normal de trabalho
        self.d_pinhao = Eq.diametro_ref(self.Z_pinhao,self.m_n,self.beta) # Diâmetro de referência do pinhão
        self.d_coroa = Eq.diametro_ref(self.Z_coroa,self.m_n,self.beta) # Diâmetro de referência da coroa
        self.dw_pinhao,self.dw_coroa = Eq.diametro_primi(self.Z_pinhao,self.Z_coroa,self.a) # Diâmetro primitivo do pinhão e da coroa
        self.pc_n = Eq.passo_circ_n(self.m_n) # Passo circular normal
        self.pc_t_pinhao = Eq.passo_circ_t(self.Z_pinhao,self.d_pinhao) # Passo circular transversal do pinhão
        self.pc_t_coroa = Eq.passo_circ_t(self.Z_coroa,self.d_coroa) # Passo circular transversal da coroa
        self.pc_tw_pinhao = Eq.passo_circ_tw(self.Z_pinhao,self.dw_pinhao) # Passo circular transversal de trabalho do pinhão
        self.pc_tw_coroa = Eq.passo_circ_tw(self.Z_coroa,self.dw_coroa) # Passo circular transversal de trabalho da coroa
        self.p_x = Eq.passo_axial(self.m_n,self.beta) # Passo axial
        self.pb = Eq.passo_base(self.m_n,self.alpha_n) #Passo base
        self.pb_x = Eq.passo_base_x(self.m_n,self.alpha_n,self.beta) # Passo base axial
        self.db_pinhao = Eq.diametro_base(self.d_pinhao,self.alpha_t) # Diâmetro base do pinhão
        self.db_coroa = Eq.diametro_base(self.d_coroa,self.alpha_t) # Diâmetro base da coroa
        self.metodo_x = metodo_x # Método de determinas o deslocamento de perfis iniciais das engrenagens (DIN,BS ou ISO)
        self.M_BS = M_BS # G = Aplicações gerais ; F = Igualdade de resistência a flexão ; V = Igualdade de velocidade de deslizamento
        self.Lambda = Lambda # Fator de redução (entre 0.5 e 0.75)
        self.sum_x, self.x_pinhao_rec, self.x_coroa_rec, aviso= Eq.desloc_perfil(self.Z_pinhao,self.Z_coroa,self.alpha_n,self.metodo_x,M_BS,Lambda,self.zn_pinhao,self.zn_coroa,self.alpha_t,self.alpha_wt,self.u) # determinação inicial dos deslocamentos de perfis
        if self.tipo == "Inicial":
            self.x_pinhao = self.x_pinhao_rec # deslocamento de perfil do pinhão
            self.x_coroa = self.x_coroa_rec # deslocamento de perfil da coroa
            if aviso != None :
                 self.AVISOS.append(aviso)
        elif self.tipo == "Otimização":
            self.x_pinhao = x_pinhao # deslocamento de perfil do pinhão
            self.x_coroa = self.sum_x - self.x_pinhao  # deslocamento de perfil da coroa
        self.beta_v_pinhao = Eq.beta_v(self.Z_pinhao,self.x_pinhao,self.beta) # Ângulo de hélice sobre o diâmetro de referência deslocado do pinhão
        self.beta_v_coroa = Eq.beta_v(self.Z_coroa,self.x_coroa,self.beta) # Ângulo de hélice sobre o diâmetro de referência deslocado da coroa
        self.beta_w_pinhao = Eq.beta_w(self.beta,self.dw_pinhao,self.d_pinhao) # Ângulo de hélice sobre o diâmetro primitivo do pinhão
        self.beta_w_coroa = Eq.beta_w(self.beta,self.dw_coroa,self.d_coroa)# Ângulo de hélice sobre o diâmetro primitivo da coroa
        self.alpha_vn_pinhao = Eq.alpha_vn(self.Z_pinhao,self.x_pinhao,self.alpha_n,self.beta,self.beta_v_pinhao) # Ângulo de pressão normal sobre o diâmetro de referência deslocado do pinhão
        self.alpha_vn_coroa = Eq.alpha_vn(self.Z_coroa,self.x_coroa,self.alpha_n,self.beta,self.beta_v_coroa) # Ângulo de pressão normal sobre o diâmetro de referência deslocado da coroa
        self.alpha_vt_pinhao = Eq.alpha_vt(self.Z_pinhao,self.alpha_t,self.x_pinhao,self.beta) # Ângulo de pressão transversal sobre o diâmetro de referência deslocado do pinhão
        self.alpha_vt_coroa = Eq.alpha_vt(self.Z_coroa,self.alpha_t,self.x_coroa,self.beta) # Ângulo de pressão transversal sobre o diâmetro de referência deslocado da coroa
        self.d_pinhao_deslocado = Eq.diametro_re_deloc(self.m_n,self.d_pinhao,self.x_pinhao) # Diâmetro de referência deslocado do pinhão
        self.d_coroa_deslocado = Eq.diametro_re_deloc(self.m_n,self.d_coroa,self.x_coroa) # Diâmetro de referência deslocado do pinhão
        self.S_n_pinhao,self.S_ns_pinhao,self.S_ni_pinhao,self.T_n_pinhao,self.T_ns_pinhao,self.T_ni_pinhao,self.A_sne_pinhao,self.T_sn_pinhao,self.S_t_pinhao,self.S_ts_pinhao,self.T_ti_pinhao,self.T_t_pinhao,self.S_ti_pinhao,self.T_ts_pinhao = Eq.espessura_dente(self.m_n,self.alpha_n,self.x_pinhao,self.d_pinhao,self.afastamento_pinhao,tol_pinhao,self.ASNE_min_pinhao,self.ASNE_max_pinhao,self.beta) # Dimensão circular normal teórica, superior e inferior do dente, e dimensão circular teórica, inferiror e superior do vão do pinhão
        self.S_n_coroa,self.S_ns_coroa,self.S_ni_coroa,self.T_n_coroa,self.T_ns_coroa,self.T_ni_coroa,self.A_sne_coroa,self.T_sn_coroa,self.S_t_coroa,self.S_ts_coroa,self.T_ti_coroa,self.T_t_coroa,self.S_ti_coroa,self.T_ts_coroa = Eq.espessura_dente(self.m_n,self.alpha_n,self.x_coroa,self.d_coroa,self.afastamento_coroa,tol_coroa,self.ASNE_min_coroa,self.ASNE_max_coroa,self.beta) # Dimensão circular normal teórica, superior e inferior do dente, e dimensão circular teórica, inferiror e superior do vão da coroa
        self.K,self.rel_aux = Eq.corre_blank(self.Z_pinhao,self.Z_coroa,self.x_pinhao,self.x_coroa,beta,self.alpha_t,self.alpha_wt)
        self.h_a_pinhao,self.d_a_pinhao,self.A_da_i_pinhao,self.A_da_s_pinhao = Eq.diam_cabeca2(self.m_n,self.d_pinhao,self.x_pinhao,self.ferramenta_pinhao.k_a,self.IQ,self.K) # Diâmetro de adendo, fator de altura do dente, Tolerância superior e inferior do adendo do pinhão
        self.h_a_coroa,self.d_a_coroa,self.A_da_i_coroa,self.A_da_s_coroa = Eq.diam_cabeca2(self.m_n,self.d_coroa,self.x_coroa,self.ferramenta_coroa.k_a,self.IQ,self.K)  # Diâmetro de adendo, fator de altura do dente, Tolerância superior e inferior do adendo da coroa

        self.S_na_pinhao,self.S_na_s_pinhao,self.S_na_i_pinhao,self.phi_na_pinhao,self.phi_ta_pinhao,self.C_a_pinhao,self.d_nk_pinhao,self.A_dnk_i_pinhao,self.A_dnk_s_pinhao,aviso = Eq.d_nk (self.m_n,self.Z_pinhao,self.alpha_n,self.db_pinhao,self.d_a_pinhao,self.alpha_t,self.S_n_pinhao,self.S_ns_pinhao,self.S_ni_pinhao,self.T_n_pinhao,self.T_ns_pinhao,self.T_ni_pinhao,self.beta,self.f_chanfro_pinhao,self.x_pinhao,"pinhão") # Cálculo da espessura de cabeça sem chanfro, do ângulo do chanfro na seção normal, do ângulo do chanfro na seção transversal, do comprimento do chanfro, di diâmetro do chanfro e das tolerâncias para o pinhão
        if aviso != None :
            self.AVISOS.append(aviso)
        self.S_na_coroa,self.S_na_s_coroa,self.S_na_i_coroa,self.phi_na_coroa,self.phi_ta_coroa,self.C_a_coroa,self.d_nk_coroa,self.A_dnk_i_coroa,self.A_dnk_s_coroa,aviso = Eq.d_nk (self.m_n,self.Z_coroa,self.alpha_n,self.db_coroa,self.d_a_coroa,self.alpha_t,self.S_n_coroa,self.S_ns_coroa,self.S_ni_coroa,self.T_n_coroa,self.T_ns_coroa,self.T_ni_coroa,self.beta,self.f_chanfro_coroa,self.x_coroa,"coroa") # Cálculo da espessura de cabeça sem chanfro, do ângulo do chanfro na seção normal, do ângulo do chanfro na seção transversal, do comprimento do chanfro, di diâmetro do chanfro e das tolerâncias para a coroa
        if aviso != None :
            self.AVISOS.append(aviso)
        self.s_nk_pinhao,self.s_nk_s_pinhao,self.s_nk_i_pinhao,aviso = Eq.S_nk(self.m_n,self.Z_pinhao,self.db_pinhao,self.d_nk_pinhao,self.d_a_pinhao,self.phi_ta_pinhao,self.alpha_t,self.beta,self.S_n_pinhao,self.S_ns_pinhao,self.S_ni_pinhao,"pinhão") # Espessura da cabeça do dente do pinhão com chanfro
        if aviso != None :
            self.AVISOS.append(aviso)
        self.s_nk_coroa,self.s_nk_s_coroa,self.s_nk_i_coroa,aviso = Eq.S_nk(self.m_n,self.Z_coroa,self.db_coroa,self.d_nk_coroa,self.d_a_coroa,self.phi_ta_coroa,self.alpha_t,self.beta,self.S_n_coroa,self.S_ns_coroa,self.S_ni_coroa,"coroa") # Espessura da cabeça do dente do pinhão com chanfro
        if aviso != None :
            self.AVISOS.append(aviso)
        self.h_f_pinhao,self.d_f_pinhao,self.A_df_i_pinhao,self.A_df_s_pinhao = Eq.diam_pe(self.m_n,self.alpha_n,self.x_pinhao,self.d_pinhao,self.ferramenta_pinhao.cp_dedendo,self.T_sn_pinhao,"pinhao") # Diâmetro de pé e suas tolerâncias para o pinhão
        self.h_f_coroa,self.d_f_coroa,self.A_df_i_coroa,self.A_df_s_coroa = Eq.diam_pe(self.m_n,self.alpha_n,self.x_coroa,self.d_coroa,self.ferramenta_coroa.cp_dedendo,self.T_sn_coroa,"coroa") # Diâmetro de pé e suas tolerâncias para a coroa
        self.Cs_pinhao,self.Csi_pinhao,self.Css_pinhao,self.Cs_coroa,self.Csi_coroa,self.Css_coroa,aviso = Eq.folga_pe_dente(self.d_a_pinhao,self.A_da_i_pinhao,self.A_da_s_pinhao,self.d_f_pinhao,self.A_df_i_pinhao,self.A_df_s_pinhao,self.d_a_coroa,self.A_da_i_coroa,self.A_da_s_coroa,self.d_f_coroa,self.A_df_i_coroa,self.A_df_s_coroa,self.a,self.Aa_i,self.Aa_s) # Calculo do afastamento entre addendo e dedendum superior e inferior do pinhão e da coroa
        if aviso != None :
            self.AVISOS.append(aviso)
        self.d_nf_pinhao,self.d_nf_coroa = Eq.diam_util_pe(self.Z_coroa,self.a,self.alpha_wt,self.d_nk_coroa,self.d_nk_pinhao,self.db_coroa,self.db_pinhao) # Diâmetro útil de pé da coroa e do pinhão
        self.d_na_pinhao,self.d_na_coroa = Eq.diam_util_cabeca(self.Z_coroa,self.db_pinhao,self.db_coroa,self.dw_pinhao,self.dw_coroa,self.d_nf_pinhao,self.d_nf_coroa) #Diâmetro útil de cabeça da coroa e do pinhão
        self.F_engrenamento_pinhao =Eq.falso_engrenamento(self.d_na_pinhao,self.d_nk_pinhao,"pinhao") # Falso engrenamento do pinhão
        if self.F_engrenamento_pinhao != None :
            self.AVISOS.append(self.F_engrenamento_pinhao)
        self.F_engrenamento_coroa =Eq.falso_engrenamento(self.d_na_coroa,self.d_nk_coroa,"coroa") # Falso engrenamento da coroa
        if self.F_engrenamento_coroa != None :
            self.AVISOS.append(self.F_engrenamento_coroa)
        self.rk_pinhao_max = Eq.raio_crista_max(self.m_n,self.alpha_n,self.S_ns_pinhao,self.d_pinhao,self.d_f_pinhao) # Raio de crista máximo da ferramenta para o pinhão
        self.rk_coroa_max = Eq.raio_crista_max(m_n,alpha_n,self.S_ns_coroa,self.d_coroa,self.d_f_coroa) # Raio de crista máximo da ferramenta para a coroa
        if self.ferramenta_pinhao.rk == None:
           self.rk_pinhao = self.rk_pinhao_max  # Raio da ferramenta para o pinhão
        elif self.ferramenta_pinhao.rk != None:
            self.rk_pinhao = self.ferramenta_pinhao.rk  # Raio da ferramenta para o pinhão
            if self.rk_pinhao > self.rk_pinhao_max  :
                self.AVISOS.append("AVISO : Está sendo utilizado para o pinhão o raio de crista de ferramenta maior do que o máximo permitido \n")

        if self.ferramenta_coroa.rk == None:
            self.rk_coroa = self.rk_coroa_max  # Raio de crista da ferramenta para a coroa
        elif self.ferramenta_coroa.rk != None:
            self.rk_coroa = self.ferramenta_coroa.rk   # Raio de crista da ferramenta para a coroa
            if self.rk_coroa > self.rk_coroa_max :
                self.AVISOS.append("AVISO : Está sendo utilizado para a coroa o raio de crista de ferramenta maior do que o máximo permitido \n")

        self.epsilon_alpha = Eq.grau_recob_perfil (self.Z_coroa,self.m_n,alpha_n,self.db_pinhao,self.db_coroa,self.d_na_pinhao,self.d_na_coroa,self.alpha_wt,self.alpha_t) # Grau de recobrimento de perfil
        self.Yf_pinhao,self.p_f_pinhao,self.h_fe_pinhao,self.S_fn_pinhao = Eq.Yf(self.m_n,self.alpha_n,self.d_pinhao,self.d_f_pinhao,self.S_ns_pinhao,self.pr_pinhao,self.SM_pinhao,self.rk_pinhao,self.x_pinhao,self.Z_pinhao,self.beta,self.epsilon_alpha,self.d_nk_pinhao,self.d_nf_pinhao,self.T_ns_pinhao,self.d_na_pinhao,self.ferramenta_pinhao.cp_dedendo,metodo_YF,self.ferramenta_pinhao.Z_shaper,0.0,metodo_YF_interno) # Cálculo do fator de formado dente do pinhão, do braço do momento fletor e o raio de curvatura do filete trocoidal no ponto de que se define a espessura crítica do dente do pinhão
        self.Yf_coroa,self.p_f_coroa,self.h_fe_coroa,self.S_fn_coroa = Eq.Yf(self.m_n,self.alpha_n,self.d_coroa,self.d_f_coroa,self.S_ns_coroa,self.pr_coroa,self.SM_coroa,self.rk_coroa,self.x_coroa,self.Z_coroa,self.beta,self.epsilon_alpha,self.d_nk_coroa,self.d_nf_coroa,self.T_ns_coroa,self.d_na_coroa,self.ferramenta_coroa.cp_dedendo,metodo_YF,self.ferramenta_coroa.Z_shaper,0.0,metodo_YF_interno)  # Cálculo do fator de formado dente da coroa, do braço do momento fletor e o raio de curvatura do filete trocoidal no ponto de que se define a espessura crítica do dente da coroa
        if self.Z_coroa < 0 and metodo_YF_interno == "cortador" and self.ferramenta_coroa.Z_shaper not in (None, 0) and abs(self.p_f_coroa - 0.1*self.m_n) < 1e-9 :
            self.AVISOS.append("AVISO : O raio de pé da anelar gerado pelo pinhão-cortador ficou abaixo de 0,1·m_n (canto de cortador quase vivo); rho_F foi limitado a 0,1·m_n para manter q_s na faixa de validade do Y_S, como faz o KISSsoft. Informe o raio de ponta do cortador (rk) para um valor realista \n")
        if self.Z_coroa < 0 and metodo_YF_interno == "cortador" and self.ferramenta_coroa.Z_shaper in (None, 0) :
            self.AVISOS.append("AVISO : A ferramenta da coroa interna não informa o número de dentes do pinhão-cortador (Z_shaper); Y_F e Y_S da anelar foram calculados pela cremalheira equivalente (método 'rack'), não pela geometria do cortador da ISO 6336-3 §6.2.4 \n")
        self.Ft = Eq.Ft(self.T,self.d_pinhao,self.Ky,self.N_cp,self.trans) # Força tangencial
        self.F_rd,self.F_ax,self.F_b,self.F = Eq.forças (self.Ft,self.alpha_wt,beta,self.beta_w_pinhao) # Força radial, Força axial, Força tangencial no plano normal, Força tangencial no plano normal sobre a linha de ação
        if b_pinhao == None or b_coroa == None :
               self.b_pinhao = Eq.b_i(self.m_n,self.alpha_n,self.S_Fmax,f_b_pinhao,self.Ft,self.h_fe_pinhao,self.Yf_pinhao,self.material_pinhao.Lim_flexao) # Caculo da extenção de contato mínima para o pinhão
               self.b_coroa = Eq.b_i(self.m_n,self.alpha_n,self.S_Fmax,f_b_coroa,self.Ft,self.h_fe_coroa,self.Yf_coroa,self.material_coroa.Lim_flexao) # Caculo da extenção de contato mínima para a coroa
        elif b_pinhao != None or b_coroa != None :
            self.b_pinhao = b_pinhao # Largura do pinhao
            self.b_coroa = b_coroa # Largura do pinhao
        self.b= min([self.b_pinhao,self.b_coroa]) # Caculo da extenção de contato para o par
        self.w,aviso = Eq.carreg_específico(self.Ft,self.Ka,self.b) #Carregamento específico no dente
        if aviso != None :
            self.AVISOS.append(aviso)
        if Z_pinhao < 0 or Z_coroa < 0 :
            self.av1,self.av2 = Eq.interf_montagem_int(self.db_pinhao,self.db_coroa,self.d_a_pinhao,self.d_a_coroa,self.a,self.alpha_wt,self.u) # Interferência de montagem para engrenagens internas
            self.AVISOS.append(self.av1)
            self.AVISOS.append(self.av2)
        else :
            self.av1,self.av2 = None,None
        self.epsilon_beta = Eq.grau_recob_helice(self.m_n,self.b,self.beta) # Grau de recobrimento de hélice
        self.epsilon_total = Eq.grau_recob_total(self.epsilon_alpha,self.epsilon_beta) # Grau de recobrimento total
        self.v_ga,self.v_gf = Eq.vel_escorregamento(self.Z_coroa,self.d_na_pinhao,self.db_pinhao,self.d_na_coroa,self.db_coroa,self.alpha_wt,self.u,self.n_rel)#Velocidade de deslizamento de acesso e de recesso
        self.di_pinhao,self.s_min_pinhao,self.s_pinhao,aviso = Eq.S_min(self.d_a_pinhao,self.d_f_pinhao,self.di_pinhao,"pinhao",self.m_n) # Espessura de Aro e espessura de aro mínima para o pinhão
        if aviso != None :
            self.AVISOS.append(aviso)
        self.di_coroa,self.s_min_coroa,self.s_coroa,aviso = Eq.S_min(self.d_a_coroa,self.d_f_coroa,self.di_coroa,"coroa",self.m_n) # Espessura de Aro e espessura de aro mínima para a coroa
        if aviso != None :
            self.AVISOS.append(aviso)
        self.k_pinhao,self.Wk_s_pinhao,self.Wk_i_pinhao = Eq.dimensao_W(self.alpha_n,self.m_n,self.Z_pinhao,self.x_pinhao,self.S_ns_pinhao,self.S_ni_pinhao,self.beta,self.alpha_t,self.k_otimi_pinhao) # Cálculo da dimensão W máximo e mínima e o número de dentes consecutivos a se medir no pinhão
        self.k_coroa,self.Wk_s_coroa,self.Wk_i_coroa = Eq.dimensao_W(self.alpha_n,self.m_n,self.Z_coroa,self.x_coroa,self.S_ns_coroa,self.S_ni_coroa,self.beta,self.alpha_t,self.k_otimi_coroa)# Cálculo da dimensão W máximo e mínima e o número de dentes consecutivos a se medir na coroa
        self.Dm_pinhao,self.Md_s_pinhao,self.Md_i_pinhao,self.d_m_s_pinhao,self.d_m_i_pinhao = Eq.dimensao_M(self.alpha_n,self.m_n,self.Z_pinhao,self.alpha_t,self.x_pinhao,self.beta,self.S_ns_pinhao,self.S_ni_pinhao,self.T_ns_pinhao,self.T_ni_pinhao,self.d_pinhao,self.db_pinhao,self.Dim_sobre_pinos_pinhao)# Cálculo da dimensão M (Sobre esferas/pinos), imensão da esfera, e diâmetro de tangência no pinhão
        self.Dm_coroa,self.Md_s_coroa,self.Md_i_coroa,self.d_m_s_coroa,self.d_m_i_coroa = Eq.dimensao_M(self.alpha_n,self.m_n,self.Z_coroa,self.alpha_t,self.x_coroa,self.beta,self.S_ns_coroa,self.S_ni_coroa,self.T_ns_coroa,self.T_ni_coroa,self.d_coroa,self.db_coroa,self.Dim_sobre_pinos_coroa) # Cálculo da dimensão M (Sobre esferas/pinos), imensão da esfera, e diâmetro de tangência na coroa
        self.Fr_pinhao,self.Rs_pinhao,self.fp_pinhao,self.fu_pinhao,self.Fp_pinhao,self.Fpk_pinhao,self.Fpk_8_pinhao,self.fpe_pinhao,self.F_beta_pinhao,self.f_Hbeta_pinhao,self.f_betaf_pinhao,self.f_Halpha_pinhao,self.f_f_pinhao,self.F_f_pinhao,self.F_i_llinha_pinhao,self.f_i_llinha_pinhao,self.F_i_linha_pinhao,self.f_i_linha_pinhao,self.f_Hbeta_6 = Eq.micro_geometria(self.m_n,self.d_pinhao,self.b,self.IQ_pinhao,self.Z_pinhao,self.k_pinhao) # Microgeometria do pinhão
        self.Fr_coroa,self.Rs_coroa,self.fp_coroa,self.fu_coroa,self.Fp_coroa,self.Fpk_coroa,self.Fpk_8_coroa,self.fpe_coroa,self.F_beta_coroa,self.f_Hbeta_coroa,self.f_betaf_coroa,self.f_Halpha_coroa,self.f_f_coroa,self.F_f_coroa,self.F_i_llinha_coroa,self.f_i_llinha_coroa,self.F_i_linha_coroa,self.f_i_linha_coroa,self.f_Hbeta_6 = Eq.micro_geometria(self.m_n,self.d_coroa,self.b,self.IQ_coroa,self.Z_coroa,self.k_coroa) # Microgeometria da coroa
        self.VT_Aa_min,self.VT_Aa_max,self.VT_Ce_min,self.VT_Ce_max,self.VT_Ei1_min,self.VT_Ei1_max,self.VT_Ei2_min,self.VT_Ei2_max,self.VT_Ex_min,self.VT_Ex_max,self.VT_El_min,self.VT_El_max,self.VT_Aq_min,self.VT_Aq_max = Eq.fatores_modificadores_flancos(self.alpha_n,self.L_pinhao,self.Z_pinhao,self.Z_coroa,self.T_Rmd,self.T_Cmd,self.d_sh_pinhao,self.a,self.Aa_i,self.Aa_s,self.beta,self.alpha_wt,self.b,self.F_beta_pinhao,self.F_f_pinhao,self.fp_pinhao,self.F_beta_coroa,self.F_f_coroa,self.fp_coroa,self.f_B_rolamento,self.F_rd,self.material_pinhao.coef_dilatacao,self.material_coroa.coef_dilatacao,self.C_Cdil) # Cálculo dos fatores modificadores do jogo entre flacos do par engrenado (Backlash)
        self.jn1_min,self.jn1_max,self.jn2_min,self.jn2_max,self.jn3_min,self.jn3_max,self.jn4_min,self.jn4_max,self.jn5_min,self.jn5_max,self.jn6_min,self.jn6_max,self.jn7_min,self.jn7_max= Eq.jogo_flancos(self.beta,self.A_sne_pinhao,self.A_sne_coroa,self.T_sn_pinhao ,self.T_sn_coroa,self.VT_Aa_min,self.VT_Aa_max,self.VT_Ce_min,self.VT_Ce_max,self.VT_Ei1_min,self.VT_Ei1_max,self.VT_Ei2_min,self.VT_Ei2_max,self.VT_Ex_min,self.VT_Ex_max,self.VT_El_min,self.VT_El_max,self.VT_Aq_min,self.VT_Aq_max)#  Jogo entre flacos do par engrenado (Backlash)
        self.potencia = (self.n_t *2*math.pi*T)/(60*1000) # Potência transmitida pelo membro de entrada da malha [kW]
        self.potencia_malha = (self.n_rel *2*math.pi*T)/(60*1000) # Potência de engrenamento (rotação relativa ao porta-planetas) [kW]
        self.v_t = (abs(self.n_rel) * 2*math.pi)/60 * (abs(self.dw_pinhao)/2000) # Velocidade períférica no ponto primitivo (relativa ao porta-planetas)
        if imersao == "pinhão":
            self.V_li,self.V_ls,self.P_ri,self.P_rs = Eq.lubrificante(self.m_n,self.Z_pinhao,self.beta,self.v_t,self.potencia_malha) # Volume máximo e mínimo de óleo e prundidade de imersão superior e inferior
        elif imersao == "coroa":
            self.V_li,self.V_ls,self.P_ri,self.P_rs = Eq.lubrificante(self.m_n,self.Z_coroa,self.beta,self.v_t,self.potencia_malha) # Volume máximo e mínimo de óleo e prundidade de imersão superior e inferior
        else :
            self.V_li = self.V_ls = self.P_ri = self.P_rs = 0

        self.a_conferencia =Eq.dist_centros (self.Z_pinhao,self.Z_coroa,self.m_n,self.beta,self.alpha_t,self.alpha_wt)
        if abs(self.a - self.a_conferencia) >= 1e-03 :
            aviso = f"AVISO : A distância entre centros imposta ({round(self.a,4)}) está diferente da distância entre centros calculada ({round(self.a_conferencia,4)}), sendo o erro de {round(abs(self.a - self.a_conferencia),4)} \n"
            self.AVISOS.append(aviso)
        self.m_wn = (2*self.a)/(self.Z_pinhao + self.Z_coroa) # Módulo TRANSVERSAL de trabalho (m_wt); nome mantido por compatibilidade
        self.a_standart = (self.d_pinhao + self.d_coroa)/2 # Distância entre centros padrão
        self.n_t_out = self.n_t/self.u # Rotação de saída
        self.T_out = self.T*self.u # Torque de saída
        self.K_linha_pinhao = Eq.arranjo_fisico(self.d_pinhao,self.d_sh_pinhao,Arranjo_pinhao,k_linha_pinhao) # Arranjo físico do pinhão
        self.K_linha_coroa = Eq.arranjo_fisico(self.d_coroa,self.d_sh_coroa,Arranjo_coroa,k_linha_coroa) # Arranjo físico da coroa
        self.h_dente_pinhao = self.h_a_pinhao +self.h_f_pinhao # Altura do dente do pinhão
        self.h_dente_coroa = self.h_a_coroa +self.h_f_coroa # Altura do dente do pinhão
        self.Z_min_pinhao = Eq.Z_min(self.m_n,self.alpha_n,self.alpha_t,self.beta,self.ferramenta_pinhao.cp_dedendo,self.rk_pinhao,self.x_pinhao,self.K)
        if abs(Z_pinhao) < abs(self.Z_min_pinhao) :
            aviso = f"AVISO :O número de dentes do pinhão ({self.Z_pinhao}) é menor que o número de dentes mínimo ({self.Z_min_pinhao}) para prevenir undercut \n"
            self.AVISOS.append(aviso)
        self.Z_min_coroa = Eq.Z_min (self.m_n,self.alpha_n,self.alpha_t,self.beta,self.ferramenta_coroa.cp_dedendo,self.rk_coroa,self.x_coroa,self.K)
        if Z_coroa > 0 and abs(Z_coroa) < abs(self.Z_min_coroa) :
            aviso = f"AVISO :O número de dentes da coroa ({self.Z_coroa}) é menor que o número de dentes mínimo ({self.Z_min_coroa}) para prevenir undercut \n"
            self.AVISOS.append(aviso)

        if Z_coroa > 0 and self.di_coroa != 0  :
            if self.di_coroa < self.d_sh_coroa :
                d_coroa = self.d_sh_coroa
                self.d_sh_coroa = self.di_coroa
                aviso = f"AVISO : O diâmetro de eixo da coroa {round(d_coroa,3)} mm teve que ser alterado para respeitar o diâmetro de aro máximo da engrenagem, com isso o novo valor é de {round(self.d_sh_coroa,3)} mm \n"
                self.AVISOS.append(aviso)
        if Z_pinhao > 0 and self.di_pinhao != 0 :
            if self.di_pinhao < self.d_sh_pinhao :
                d_pinhao = self.d_sh_pinhao
                self.d_sh_pinhao = self.di_pinhao
                aviso = f"AVISO : O diâmetro de eixo do pinhão {round(d_pinhao,3)} mm teve que ser alteradopara respeitar o diâmetro de aro máximo da engrenagem, com isso o novo valor é de {round(self.d_sh_pinhao,3)} mm \n"
                self.AVISOS.append(aviso)


        if op_acabamento_pinhao == "Rasqueteamento" :
            if IQ_pinhao == 6 :
                aviso = "AVISO : Dificuldade alta de alcançar o índice de qualidade do pinhão com a operação de acabamento escolhida, recomenda-se utilização de retífica \n"
                self.AVISOS.append(aviso)
            elif IQ_pinhao ==5 or IQ_pinhao == 4 :
                aviso = "AVISO : Dificuldade muito alta de alcançar o índice de qualidade do pinhão  com a operação de acabamento escolhida, recomenda-se utilização de retífica \n"
                self.AVISOS.append(aviso)
            elif IQ_pinhao <= 3 :
                aviso = "AVISO : Não é possível alcançar o índice de qualidade do pinhão  com a operação de acabamento escolhida, recomenda-se utilização de retífica \n"
                self.AVISOS.append(aviso)
            elif IQ_pinhao >= 9 :
                aviso = "AVISO : Recomeda-se o uso de fresamento para baratear o custo de operação do pinhão \n"
                self.AVISOS.append(aviso)
        elif op_acabamento_pinhao == "Retificação" :
            if IQ_pinhao > 8 :
                aviso = "AVISO : Recomeda-se o uso de fresamento para baratear o custo de operação do pinhão \n"
                self.AVISOS.append(aviso)
            elif IQ_pinhao == 7 or IQ_pinhao == 8   :
                aviso = "AVISO : Recomeda-se o uso de rasqueteamento para baratear o custo de operação do pinhão \n"
                self.AVISOS.append(aviso)
            elif IQ_pinhao <=3 :
                aviso = "AVISO : Dificuldade muito alta de alcançar o índice de qualidade do pinhão \n"
                self.AVISOS.append(aviso)
        elif op_acabamento_pinhao == "Fresamento" :
            if IQ_pinhao ==7 or IQ_pinhao ==6 :
                aviso = "AVISO : Dificuldade muito alta de alcançar o índice de qualidade do pinhão  com a operação de acabamento escolhida, recomenda-se utilização de rasqueteamento \n"
                self.AVISOS.append(aviso)
            elif IQ_pinhao <= 5:
                aviso = "AVISO : Não é possível alcançar o índice de qualidad do pinhão e com a operação de acabamento escolhida, recomenda-se utilização de retífica \n"
                self.AVISOS.append(aviso)
            elif IQ_pinhao == 8 :
                aviso = "AVISO : Dificuldade alta de alcançar o índice de qualidade do pinhão  com a operação de acabamento escolhida, recomenda-se utilização de rasquetemento \n"
                self.AVISOS.append(aviso)


        if op_acabamento_coroa == "Rasqueteamento" :
            if IQ_coroa == 6 :
                aviso = "AVISO : Dificuldade alta de alcançar o índice de qualidade da coroa com a operação de acabamento escolhida, recomenda-se utilização de retífica \n"
                self.AVISOS.append(aviso)
            elif IQ_coroa ==5 or IQ_coroa == 4 :
                aviso = "AVISO : Dificuldade muito alta de alcançar o índice de qualidade da coroa com a operação de acabamento escolhida, recomenda-se utilização de retífica \n"
                self.AVISOS.append(aviso)
            elif IQ_coroa <= 3 :
                aviso = "AVISO : Não é possível alcançar o índice de qualidade da coroa com a operação de acabamento escolhida, recomenda-se utilização de retífica \n"
                self.AVISOS.append(aviso)
            elif IQ_coroa >= 9 :
                aviso = "AVISO : Recomeda-se o uso de fresamento para baratear o custo de operação da coroa \n"
                self.AVISOS.append(aviso)
        elif op_acabamento_coroa == "Retificação" :
            if IQ_coroa > 8 :
                aviso = "AVISO : Recomeda-se o uso de fresamento para baratear o custo de operação da coroa \n"
                self.AVISOS.append(aviso)
            elif IQ_coroa== 7 or IQ_coroa== 8   :
                aviso = "AVISO : Recomeda-se o uso de rasqueteamento para baratear o custo de operação da coroa \n"
                self.AVISOS.append(aviso)
            elif IQ_coroa <=3 :
                aviso = "AVISO : Dificuldade muito alta de alcançar o índice de qualidade da coroa \n"
                self.AVISOS.append(aviso)
        elif op_acabamento_coroa == "Fresamento" :
            if IQ_coroa ==7 or IQ_coroa ==6 :
                aviso = "AVISO : Dificuldade muito alta de alcançar o índice de qualidade da coroa com a operação de acabamento escolhida, recomenda-se utilização de rasqueteamento \n"
                self.AVISOS.append(aviso)
            elif IQ_coroa <= 5:
                aviso = "AVISO : Não é possível alcançar o índice de qualidade da coroa com a operação de acabamento escolhida, recomenda-se utilização de retífica \n"
                self.AVISOS.append(aviso)
            elif IQ_coroa == 8 :
                aviso = "AVISO : Dificuldade alta de alcançar o índice de qualidade da coroa com a operação de acabamento escolhida, recomenda-se utilização de rasquetemento \n"
                self.AVISOS.append(aviso)

        if not os.environ.get("ENGR_SEM_PDF") :
            self.salvar_em_PDF()

    def __str__(self):
        return ("\n RELATÓRIO GEOMÉTRICO\n \n"

                f"Apelido do modelo --> {self.apelido} \n"
                f"Engenheiro responsável --> {self.Proj} \n"
                f"Tipo de interação --> {self.tipo} \n"
                f"Tipo de transmissão --> {self.trans} \n"
                f"Quantidade de planetas --> {self.N_cp} \n"
                f"Membros da malha --> Pinhão : {self.membro_pinhao} ; Coroa : {self.membro_coroa} \n"
                f"Vida útil nominal requerida pelo egrenamento [horas] --> {round(self.Vr,4)} \n"
                f"Temperatura dos engrenagens no instante de máxiam difernça de temperatura entre a caixa e as rodas [°C ] --> {round(self.T_Rmd,4)} \n"
                f"Temperatura da caixa no instante de máxiam difernça de temperatura entre a caixa e as rodas [°C]  --> {round(self.T_Cmd,4)} \n"
                f"Temperatura de operação [°C] --> {round(self.T_op,4)} \n"
                f"Qualidade das engrenagens --> Pinhão : {self.IQ_pinhao} ; Coroa : {self.IQ_coroa} \n"
                f"Qualidade do par engrenado --> {self.IQ} \n"
                f"Número de dentes mínimo para prevenir Undercut --> Pinhão : {self.Z_min_pinhao} ; Coroa : {self.Z_min_coroa} \n"

                "\n MATERIAIS \n \n"

                f"Material do pinhão \n \n {self.material_pinhao} \n"
                f"Material da coroa \n \n {self.material_coroa} \n"

                "\n FERRAMENTAS \n \n"

                f"Ferramenta de usinagem do pinhão \n \n {self.ferramenta_pinhao} \n"
                f"Ferramenta de usinagem da coroa \n \n {self.ferramenta_coroa} \n"
                f"Raio de crista da ferramenta máximo [mm] --> Pinhão : {round(self.rk_pinhao_max,4)} ; Coroa : {round(self.rk_coroa_max,4)} \n"
                f"Raio de crista da ferramenta [mm] --> Pinhão : {round(self.rk_pinhao,4)} ; Coroa : {round(self.rk_coroa,4)} \n"

                "\n Lubrificantes \n \n"

                f"{self.lubrificante}"
                f"Volume de óleo [L] --> Máximo: {round(self.V_ls,4)} ; Mínimo : {round(self.V_li,4)} \n"
                f"Profundidade de submersão [mm] --> Máximo: {round(self.P_rs,5)} ; Mínimo : {round(self.P_ri,4)} \n"

                "\n COEFICINETES DE SEGURAÇA \n \n"

                f"Coeficiênte de segurança de falha por fadiga superficial --> Máximo {round(self.S_Hmax,4)} ; Mínimo : {round(self.S_Hmin,4)} \n"
                f"Coeficiênte de segurança de falha por flexão --> Máximo {round(self.S_Fmax,4)} ; Mínimo : {round(self.S_Fmin,4)} \n"

                "\n CARACTERÍSTICAS GEOMÉTRICAS BÁSICAS \n \n"

                f"Modulo normal do par [mm] --> {round(self.m_n,4)} \n"
                f"Modulo transversal do par [mm] --> {round(self.m_t,4)} \n"
                f"Modulo transversal de trabalho [mm] --> {round(self.m_wn,4)} \n"
                f"Distância entre centros standart [mm] --> {round(self.a_standart,4)} \n"
                f"Distância entre centros de trabalho (Imposta) [mm] --> {round(self.a,4)} \n"
                f"Distância entre centros de trabalho (Calculada) [mm] --> {round(self.a_conferencia,4)} \n"
                f"Tolerância da distância entre centros [mm] --> Superior : {round(self.Aa_s,4)} ; Inferior {round(self.Aa_i,4)} \n"
                f"Número de dentes --> Pinhão : {self.Z_pinhao} ; Coroa : {self.Z_coroa} \n"
                f"Número de dentes virtuais --> Pinhão : {round(self.zn_pinhao,4)}; Coroa : {round(self.zn_coroa,4)} \n "
                f"Razão de engrenamento --> {round(self.u,4)}\n "
                f"Comprimento dos dentes [mm] --> Pinhão : {round(self.b_pinhao,4)} ; Coroa : {round(self.b_coroa,4)}  \n"
                f"Extenção de contato (Comprimento do dente em contato) [mm] --> {round(self.b,4)} \n"
                f"Ângulo de pressão normal [°] --> {round(self.alpha_n,4)} \n"
                f"Ângulo de pressão transversal [°] --> {round(self.alpha_t,4)} \n"
                f"Ângulo de pressão de trabalho normal [°] --> {round(self.alpha_wn,4)} \n"
                f"Ângulo de pressão de trabalho transversal [°] --> {round(self.alpha_wt,4)} \n"
                f"Ângulo de pressão normal sobre o diâmetro de referência deslocado [°] --> Pinhão :{round(self.alpha_vn_pinhao,4)}  ; Coroa : {round(self.alpha_vn_coroa,4)}  \n"
                f"Ângulo de pressão transversal sobre o diâmetro de referência deslocado [°] --> Pinhão :{round(self.alpha_vt_pinhao,4)}  ; Coroa : {round(self.alpha_vt_coroa,4)}  \n"
                f"Ângulo de hélice [°] --> {round(self.beta,4)} \n"
                f"Ângulo de hélice sobre o circulo base [°] --> {round(self.beta_b,4)} \n"
                f"Ângulo de hélice sobre o diâmetro de referência deslocado [°] --> Pinhão : {round(self.beta_v_pinhao,4)} ; Coroa : {round(self.beta_v_coroa,4)} \n"
                f"Ângulo de hélice sobre o diâmetro primitivo [°] --> {round(self.beta_w_pinhao,4)} \n"
                f"Diâmetro de referência [mm] --> Pinhão : {round(self.d_pinhao,4)} ; Coroa : {round(self.d_coroa,4)} \n"
                f"Diâmetro primitivo [mm] --> Pinhão : {round(self.dw_pinhao,4)} ; Coroa : {round(self.dw_coroa,4)} \n"
                f"Diâmetro de referência deslocado [mm] --> Pinhão : {round(self.d_pinhao_deslocado,4)} ; Coroa : {round(self.d_coroa_deslocado,4)} \n"
                f"Diâmetro base [mm] --> Pinhão : {round(self.db_pinhao,4)} ; Coroa : {round(self.db_coroa,4)} \n"
                f"Relação auxiliar ((x1+x2/z1+z2)) -->  {round(self.rel_aux,6)} \n"
                f"Coeficiente de correção do blank --> {round(self.K,6)} \n"
                f"Addendum real [mm] --> Pinhão : {round(self.h_a_pinhao,4)} ; Coroa : {round(self.h_a_coroa,4,)} \n"
                f"Dedendum real [mm] --> Pinhão : {round(self.h_f_pinhao,4)} ; Coroa : {round(self.h_f_coroa,4,)} \n"
                f"Altura do dente [mm] --> Pinhão : {round(self.h_dente_pinhao,4)} ; Coroa : {round(self.h_dente_coroa,4)} \n"
                f"Diâmetro de cabeça [mm] --> Pinhão : {round(self.d_a_pinhao,4)} ; Coroa : {round(self.d_a_coroa,4)} \n"
                f"Tolerância superior do diâmetro de cabeça [mm] --> Pinhão : {round(self.A_da_s_pinhao,4)} ; Coroa : {round(self.A_da_s_coroa,4)} \n"
                f"Tolerância inferior do diâmetro de cabeça [mm] --> Pinhão : {round(self.A_da_i_pinhao,4)} ; Coroa : {round(self.A_da_i_coroa,4)} \n"
                f"Diâmetro de pé [mm] --> Pinhão : {round(self.d_f_pinhao,4)} ; Coroa : {round(self.d_f_coroa,4)} \n"
                f"Tolerância superior do diâmetro de pé [mm] --> Pinhão : {round(self.A_df_s_pinhao,4)} ; Coroa : {round(self.A_df_s_coroa,4)} \n"
                f"Tolerância inferior do diâmetro de pé [mm] --> Pinhão : {round(self.A_df_i_pinhao,4)} ; Coroa : {round(self.A_df_i_coroa,4)} \n"
                f"Folga no pé do dente [mm] --> Pinhão : {round(self.Cs_pinhao,4)} ; Coroa : {round(self.Cs_coroa,4)} \n"
                f"Folga superior no pé do dente [mm] --> Pinhão : {round(self.Css_pinhao,4)} ; Coroa : {round(self.Css_coroa,4)} \n"
                f"Folga inferior no pé do dente [mm] --> Pinhão : {round(self.Csi_pinhao,4)} ; Coroa : {round(self.Csi_coroa,4)} \n"
                f"Diâmetro de cabeça útil [mm] --> Pinhão : {round(self.d_na_pinhao,4)} ; Coroa : {round(self.d_na_coroa,4)} \n"
                f"Diâmetro de pé útil [mm] --> Pinhão : {round(self.d_nf_pinhao,4)} ; Coroa : {round(self.d_nf_coroa,4)} \n"
                f"Passo circular normal [mm] --> {round(self.pc_n,4)} \n"
                f"Passo circular transversal [mm] --> Pinhão : {round(self.pc_t_pinhao,4)} ; Coroa : {round(self.pc_t_coroa,4)} \n"
                f"Passo circular transversal primitivo [mm] --> Pinhão : {round(self.pc_tw_pinhao,4)} ; Coroa : {round(self.pc_tw_coroa,4)} \n"
                f"Passo axial [mm] --> {round(self.p_x,4)} \n"
                f"Passo base [mm] --> {round(self.pb,4)} \n"
                f"Passo base axial [mm] --> {round(self.pb_x,4)} \n"
                f"Somatório do deslocameno de perfil do pinhão e da coroa --> {round(self.sum_x,6)} \n"
                f"Deslocamento de perfil --> Pinhão : {round(self.x_pinhao,6)} ; Coroa : {round(self.x_coroa,6)} \n"
                f"Espessura do dente normal nominal [mm] --> Pinhão : {round(self.S_n_pinhao,4)} ; Coroa : {round(self.S_n_coroa,4)} \n"
                f"Espessura superior do dente normal [mm] --> Pinhão : {round(self.S_ns_pinhao,4)} ; Coroa : {round(self.S_ns_coroa,4)} \n"
                f"Espessura  inferior do dente normal  [mm] --> Pinhão : {round(self.S_ni_pinhao,4)} ; Coroa : {round(self.S_ni_coroa,4)} \n"
                f"Espessura do dente normal transversal [mm] --> Pinhão : {round(self.S_t_pinhao,4)} ; Coroa : {round(self.S_t_coroa,4)} \n"
                f"Espessura superior transversal do dente [mm] --> Pinhão : {round(self.S_ts_pinhao,4)} ; Coroa : {round(self.S_ts_coroa,4)} \n"
                f"Espessura inferior transversal do dente [mm]  [mm] --> Pinhão : {round(self.S_ti_pinhao,4)} ; Coroa : {round(self.S_ti_coroa,4)} \n"
                f"Espessura da cabeça do dente sem o chanfro normal nominal [mm] --> Pinhão : {round(self.S_na_pinhao,4)} ; Coroa : {round(self.S_na_coroa,4)} \n"
                f"Espessura da cabeça do dente sem o chanfro superior normal [mm] --> Pinhão : {round(self.S_na_s_pinhao,4)} ; Coroa : {round(self.S_na_s_coroa,4)} \n"
                f"Espessura da cabeça do dente sem o chanfro inferior normal [mm] --> Pinhão : {round(self.S_na_i_pinhao,4)} ; Coroa : {round(self.S_na_i_coroa,4)} \n"
                f"Espessura da cabeça do dente com o chanfro normal nominal [mm] --> Pinhão : {round(self.s_nk_pinhao,4)} ; Coroa {round(self.s_nk_coroa,4)} \n"
                f"Espessura da cabeça do dente com o chanfro superior normal [mm] --> Pinhão : {round(self.s_nk_s_pinhao,4)} ; Coroa {round(self.s_nk_s_coroa,4)} \n"
                f"Espessura da cabeça do dente com o chanfro inferior normal [mm] --> Pinhão : {round(self.s_nk_i_pinhao,4)} ; Coroa {round(self.s_nk_i_coroa,4)} \n"
                f"Dimensão do vão normal [mm] --> Pinhão : {round(self.T_n_pinhao,4)} ; Coroa : {round(self.T_n_coroa,4)} \n"
                f"Dimensão superior normal do vão [mm] --> Pinhão : {round(self.T_ns_pinhao,4)} ; Coroa : {round(self.T_ns_coroa,4)} \n"
                f"Dimensão inferior normal do vão [mm] --> Pinhão : {round(self.T_ni_pinhao,4)} ; Coroa : {round(self.T_ni_coroa,4)} \n"
                f"Dimensão do vão transversal [mm] --> Pinhão : {round(self.T_t_pinhao,4)} ; Coroa : {round(self.T_t_coroa,4)} \n"
                f"Dimensão superior transversal do vão  [mm] --> Pinhão : {round(self.T_ts_pinhao,4)} ; Coroa : {round(self.T_ts_coroa,4)} \n"
                f"Dimensão inferior transversal do vão [mm] --> Pinhão : {round(self.T_ti_pinhao,4)} ; Coroa : {round(self.T_ti_coroa,4)} \n"
                f"Ângulo de chanfro na seção normal [°] --> Pinhão : {round(self.phi_na_pinhao,4)} ; Coroa : {round(self.phi_na_coroa,4)} \n"
                f"Ângulo de chanfro na seção transversal [°] --> Pinhão : {round(self.phi_ta_pinhao,4)} ; Coroa : {round(self.phi_ta_coroa,4)} \n"
                f"Comprimento de chanfro [mm] --> Pinhão : {round(self.C_a_pinhao,4)} ; Coroa {round(self.C_a_coroa,4)} \n"
                f"Diâmetro de início de chanfro [mm] --> Pinhão : {round(self.d_nk_pinhao,4)} ; Coroa : {round(self.d_nk_coroa,4)} \n"
                f"Tolerância superior do diâmetro de início de chanfro [mm] --> Pinhão : {round(self.A_dnk_s_pinhao,4)} ; Coroa : {round(self.A_dnk_s_coroa,4)} \n"
                f"Tolerância inferior do diâmetro de início de chanfro [mm] --> Pinhão : {round(self.A_dnk_i_pinhao,4)} ; Coroa : {round(self.A_dnk_i_coroa,4)} \n"
                f"Grau de recobrimento de perfil --> {round(self.epsilon_alpha,4)} \n"
                f"Grau de recobrimento de hélice --> {round(self.epsilon_beta,4)} \n"
                f"Grau de recobrimento de total --> {round(self.epsilon_total,4)} \n"
                f"Velocidade de escorregamento de recesso [m/s] --> {round(self.v_ga,4)} \n"
                f"Velocidade de escorregamento de acesso [m/s] --> {round(self.v_gf,4)}  \n"

                "\n CARACTERÍSTICAS DO CORPO DA ENGRENAGEM E DOS MANCAIS \n \n"

                f"Diâmetro de alma [mm]  --> Pinhão : {round(self.di_pinhao,4)} ; Coroa : {round(self.di_coroa,4)} \n"
                f"Espessura de alma [mm] -->  Pinhão : {round(self.bs_pinhao,4)} ; Coroa : {round(self.bs_coroa,4)} \n"
                f"Diâmetro do eixo [mm] --> Pinhão : {round(self.d_sh_pinhao,4)} ; Coroa : {round(self.d_sh_coroa,4)} \n"
                f"Espessura entre diâmetro de alma e do diâmetro de pé [mm] --> Pinhão : {round(self.s_pinhao,4)} ; Coroa : {round(self.s_coroa,4)} \n"
                f"Distância entre os mancais [mm] --> Pinhao : {round(self.L_pinhao,4)} ; Coroa : {round(self.L_coroa,4)} \n"
                f"Distância do centro dos mancais ao dentro da roda dentada [mm] --> Pinhão : {round(self.sh_pinhao,4)} ; Coroa : {round(self.sh_coroa,4)} \n"
                f"Constante para a posição --> Pinhão : {round(self.K_linha_pinhao,4)} ; Coroa : {round(self.K_linha_coroa,4)}\n"

                "\n APLICAÇÃO\n \n"

                f"Grau de irregularida -->  Pinhão : {self.irregularidade_motora} ; Coroa : {self.irregularidade_movida}\n"
                f"Fator de aplicação Ka --> {round(self.Ka,4)} \n"
                f"Fator de carregamento de malha Ky --> {self.Ky} \n"

                "\n OPREÇÃO DE ACABAMENTO \n \n"

                f"Operação de acabamento --> Pinhão :{self.op_acabamento_pinhao} ; Coroa : {self.op_acabamento_coroa} \n"
                f"Sobremetal para acabamento [mm] --> Pinhão : {round(self.SM_pinhao,4)} ; Coroa : {round(self.SM_coroa,4)} \n"
                f"Rugosidade média no flanco do dente [micrometro] --> Pinhão : {round(self.Ra_flanco_pinhao,4)} ; Coroa : {round(self.Ra_flanco_coroa,4)} \n"
                f"Altura máxima do perfil de rugosidade nos flancos do dente [micrometro] --> Pinhão : {round(self.Rz_flanco_pinhao,4)} ; Coroa : {round(self.Rz_flanco_coroa,4)} \n"
                f"Rugosidade média no pé do dente [micrometro] --> Pinhão : {round(self.Ra_pe_pinhao,4)} ; Coroa : {round(self.Ra_pe_coroa,4)} \n"
                f"Altura máxima do perfil de rugosidade no pé do dente [micrometro] --> Pinhão : {round(self.Rz_pe_pinhao,4)} ; Coroa : {round(self.Rz_pe_coroa,4)} \n"
                f"Qualidade das engrenagens --> Pinhão : {round(self.IQ_pinhao,1)} ; Coroa : {round(self.IQ_coroa,1)} \n"

                "\n CONTROLE DE ESPESSURA DO DENTE \n \n"

                f"Números de dentes seguidos a se medir --> Pinhão : {self.k_pinhao} ; Coroa : {self.k_coroa} \n"
                f"Dimensão W superior [mm] --> Pinhão : {round(self.Wk_s_pinhao,4)} ; Coroa : {round(self.Wk_s_coroa,4)} \n"
                f"Dimensão W inferior [mm] --> Pinhão : {round(self.Wk_i_pinhao,4)} ; Coroa : {round(self.Wk_i_coroa,4)} \n"
                f"Diâmetro da esfera/rolo [mm] --> Pinhão : {round(self.Dm_pinhao,4)} ; Coroa : {round(self.Dm_coroa,4)} \n"
                f"Entre pinos/esferas superior [mm] --> Pinhão : {round(self.Md_s_pinhao,4)} ; Coroa : {round(self.Md_s_coroa,4)} \n"
                f"Entre pinos/esferas inferior [mm] --> Pinhão : {round(self.Md_i_pinhao,4)} ; Coroa : {round(self.Md_i_coroa,4)} \n"
                f"Diâmetro de tangência da esfera/pino superior [mm] --> Pinhão : {round(self.d_m_s_pinhao,4)} ; Coroa : {round(self.d_m_s_coroa,4)} \n"
                f"Diâmetro de tangência da esfera/pino inferior [mm] --> Pinhão : {round(self.d_m_i_pinhao,4)} ; Coroa : {round(self.d_m_i_coroa,4)} \n"
                f"Abaulameto superior do dente (Crown)[mm] --> Pinhão : {round(self.crwon_s_pinhao,4)} ; Coroa : {round(self.crwon_s_coroa,4)} \n"
                f"Abaulameto inferior do dente (Crown)[mm] --> Pinhão : {round(self.crwon_i_pinhao,4)} ; Coroa : {round(self.crwon_i_coroa,4)} \n"

                "\n MICROGEOMETRIA \n \n"

                f"Desvio de concetricidade (Fr) [mm] --> Pinhão : {round(self.Fr_pinhao,4)} ; Coroa : {round(self.Fr_coroa,4)} \n"
                f"Flutuação nas espessuras dos dentes (Rs) [mm] --> Pinhão : {round(self.Rs_pinhao,4)} ; Coroa : {round(self.Rs_coroa,4)} \n"
                f"Desvio de passo individual (fp) [mm] --> Pinhão : {round(self.fp_pinhao,4)} ; Coroa : {round(self.fp_coroa,4)} \n"
                f"Erro entre os passos consecutivos (fu) [mm] --> Pinhão : {round(self.fu_pinhao,4)} ; Coroa : {round(self.fu_coroa,4)} \n"
                f"Erro total de passo (Fp) [mm] --> Pinhão : {round(self.Fp_pinhao,4)} ; Coroa : {round(self.Fp_coroa,4)} \n"
                f"Desvio de passo sobre k dentes consecutivos (Fpk) [mm] --> Pinhão : {round(self.Fpk_pinhao,4)} ; Coroa : {round(self.Fpk_coroa,4)} \n"
                f"Desvio de passo sobre uma fração de (z/8) dentes consecutivos (Fpk/8) [mm] --> Pinhão : {round(self.Fpk_8_pinhao,4)} ; Coroa : {round(self.Fpk_8_coroa,4)} \n"
                f"Desvio de passo base normal (fpe) [mm] --> Pinhão : {round(self.fpe_pinhao,4)} ; Coroa : {round(self.fpe_coroa,4)} \n"
                f"Desvio total na linha dos flancos (F_beta) [mm] --> Pinhão : {round(self.F_beta_pinhao,4)} ; Coroa : {round(self.F_beta_coroa,4)} \n"
                f"Desvio angular na linha dos flancos (f_Hbeta) [mm] --> Pinhão : {round(self.f_Hbeta_pinhao,4)} ; Coroa : {round(self.f_Hbeta_coroa,4)} \n"
                f"Desvio de forma na linha dos flancos (f_betaf) [mm] --> Pinhão : {round(self.f_betaf_pinhao,4)} ; Coroa : {round(self.f_betaf_coroa,4)} \n"
                f"Desvio total de perfil envolvente (Ff) [mm] --> Pinhão : {round(self.F_f_pinhao,4)} ; Coroa : {round(self.F_f_coroa,4)} \n"
                f"Desvio angular de perfil envolvente (F_Halpha) [mm] --> Pinhão : {round(self.f_Halpha_pinhao,4)} ; Coroa : {round(self.f_Halpha_coroa,4)} \n"
                f"Desvio de forma de perfil envolvente (ff) [mm] --> Pinhão : {round(self.f_f_pinhao,4)} ; Coroa : {round(self.f_f_coroa,4)} \n"
                f"Deslocamento composto radial (F''i) [mm] --> Pinhão : {round(self.F_i_llinha_pinhao,4)} ; Coroa : {round(self.F_i_llinha_coroa,4)} \n"
                f"Salto radial (f''i) [mm] --> Pinhão : {round(self.f_i_llinha_pinhao,4)} ; Coroa : {round(self.f_i_llinha_coroa,4)} \n"
                f"Deslocamento composto tangencial (F'i) [mm] --> Pinhão : {round(self.F_i_linha_pinhao,4)} ; Coroa : {round(self.F_i_linha_coroa,4)} \n"
                f"Salto tangencial (f'i) [mm] --> Pinhão : {round(self.f_i_linha_pinhao,4)} ; Coroa : {round(self.f_i_linha_coroa,4)} \n"


                "\n JOGO ENTRE FLANCOS (BACKLASH) \n \n"

                f"Backlash [mm] --> Mínimo {round((self.A_sne_coroa + self.A_sne_pinhao),4)}; Máximo {round((self.A_sne_coroa + self.A_sne_pinhao) + (self.T_sn_coroa + self.T_sn_pinhao),4)} \n"
                f"Jogo entre flancos teórico [mm] --> Mínimo : {round(self.jn1_min,4)} ; Máximo : {round(self.jn1_max,4)} \n"
                f"Jogo entre flancos pela influência da tolerância entre centros [mm] --> Mínimo : {round(self.jn2_min,4)} ; Máximo : {round(self.jn2_max,4)} \n"
                f"Jogo entre flancos pela influência do erro de cruzamento de eixos [mm] --> Mínimo : {round(self.jn3_min,4)} ; Máximo : {round(self.jn3_max,4)} \n"
                f"Jogo entre flancos pela influência dos erros individuais do dentado [mm] --> Mínimo : {round(self.jn4_min,4)} ; Máximo : {round(self.jn4_max,4)} \n"
                f"Jogo entre flancos pela influência da excentricidade dos mancais [mm] --> Mínimo : {round(self.jn5_min,4)} ; Máximo : {round(self.jn5_max,4)} \n"
                f"Jogo entre flancos pela  influência da elasticidade do conjunto [mm] --> Mínimo : {round(self.jn6_min,4)} ; Máximo : {round(self.jn6_max,4)} \n"
                f"Jogo entre flancos pela influência da  temperatura [mm] (Final) --> Mínimo : {round(self.jn7_min,4)} ; Máximo : {round(self.jn7_max,4)} \n"


                "\n FORÇAS, TORQUES, ROTAÇÕES E POTÊNCIAS \n \n"


                f"Torque de entrada [Nm] --> {round(self.T,4)} \n"
                f"Velocidade de entrada [Rpm] --> {round(self.n_t,4)} \n"
                f"Rotação do porta-planetas [Rpm] --> {round(self.n_carrier,4)} \n"
                f"Rotação relativa ao porta-planetas [Rpm] --> {round(self.n_rel,4)} \n"
                f"Engrenamentos por volta relativa --> Pinhão : {self.contatos_pinhao} ; Coroa : {self.contatos_coroa} \n"
                f"Fator de carga alternada (Y_M) --> Pinhão : {self.Y_M_pinhao} ; Coroa : {self.Y_M_coroa} \n"
                f"Torque de saída [Nm] --> {round(self.T_out,4)} \n"
                f"Velocidade de saída [Rpm] --> {round(self.n_t_out,4)} \n"
                f"Potência de entrada [kW] --> {round(self.potencia,4)} \n"
                f"Potência de engrenamento (rotação relativa) [kW] --> {round(self.potencia_malha,4)} \n"
                f"Velocidade tangencial do par [m/s] --> {round(self.v_t,4)} \n"
                f"Força tangência [N] --> {round(self.Ft,4)} \n"
                f"Força tangência no plano normal [N] --> {round(self.F_b,4)} \n"
                f"Força tangência no plano normal sobre a linha de ação [N] --> {round(self.F,4)} \n"
                f"Força radial [N] --> {round(self.F_rd,4)} \n"
                f"Força axial [N] --> {round(self.F_ax,4)} \n"
                f"Carregamento específico [N//mm] --> {round(self.w,4)} \n"

                "\n AVISOS \n \n"


                 "\n".join(self.AVISOS) + "\n" )


    def salvar_em_PDF(self):
        caminho_pasta = "Relatórios Gemoétricos"
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)
        data_atual = datetime.now().strftime("%d/%m/%Y")
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)

        # Adicionar a primeira página
        pdf.add_page()

        # Configurar margens
        pdf.set_left_margin(15)
        pdf.set_right_margin(15)
        pdf.set_top_margin(20)
        pdf.set_auto_page_break(auto=True, margin=20)

        # Adicionar cabeçalho na primeira página
        pdf.set_font("Times", "B", 16)
        pdf.cell(0, 10, f"Relatório Geométrico {self.apelido} ", ln=True, align="C")
        pdf.ln(10)  # Espaço após o cabeçalho

        # Configurar fonte do conteúdo
        pdf.set_font("Times", size=11)

        conteudo = str(self)  # Representação do conteúdo do objeto
        largura_celula = 190  # Largura disponível com margens
        altura_linha = 5  # Altura de cada linha no PDF



        # Adicionar conteúdo com numeração automática de páginas
        for linha in conteudo.split('\n'):
            pdf.multi_cell(w=largura_celula, h=altura_linha, txt=linha, border=0, align="L")

        pdf.cell(0, 10, f"Data: {data_atual} ", align="C", ln=1)
        # Salvar o PDF
        nome_arquivo = f"Relatorio_geometrico_{self.apelido}.pdf"
        caminho_completo = os.path.join(caminho_pasta, nome_arquivo)
        pdf.output(caminho_completo, dest='F')


def cinematica_planetaria(Z_sol, Z_pla_ext, Z_pla_int, Z_anel, n_sol, T_sol, N_cp, Tipo = "Composto", Ring = "Fixo", Ky = 1, n_carrier = None, n_anel = None):
    """Cinemática de planetário (AGMA 6123 / ISO 6336-1 §4.2), saída no porta-planetas.
    Tipo "Composto": sol -> planeta maior (Z_pla_ext) ; planeta menor (Z_pla_int) -> anelar.  "Simples": Z_pla_int = Z_pla_ext.
    Ring = "Fixo": n_anel = 0.  Ring = "Rotativo": informe n_carrier OU n_anel (rpm, com sinal; sol positivo).
    Retorna dict: i (= n_sol/n_c, só p/ anel fixo), n_c, n_anel, n_pla (absoluta), n_sol_rel, n_pla_rel, n_anel_rel (módulos),
    T_malha_ext (torque total no sol), T_malha_int (torque total transmitido pelos planetas à anelar = soma dos N_cp),
    T_anel (reação), T_carrier (saída). Os torques independem da cinemática (estática), as rotações relativas não.
    A função Ft divide o torque de malha por N_cp e multiplica por Ky."""
    Z_anel = abs(Z_anel)
    if Tipo == "Simples":
        Z_pla_int = Z_pla_ext
    k = (Z_anel * Z_pla_ext) / (Z_sol * Z_pla_int)       # razão básica: (n_sol - n_c) = -k (n_anel - n_c) ... sinal: n_sol_rel = k*(n_c - n_anel)
    if Ring == "Fixo":
        n_anel = 0.0
        n_c = n_sol / (1 + k)
    else:
        if n_carrier is not None:
            n_c = n_carrier
            n_anel = n_c - (n_sol - n_c) / k
        elif n_anel is not None:
            n_c = (n_sol + k * n_anel) / (1 + k)
        else:
            raise ValueError("Ring rotativo: informe n_carrier ou n_anel")
    n_sol_rel = n_sol - n_c
    n_pla_rel = -n_sol_rel * Z_sol / Z_pla_ext              # relativa ao porta-planetas (sentido oposto ao sol)
    n_pla = n_c + n_pla_rel
    n_anel_rel = n_anel - n_c
    T_malha_ext = T_sol
    T_malha_int = T_sol * Z_pla_ext / Z_sol                 # equilíbrio de momento no corpo do planeta (soma dos N_cp planetas)
    T_anel = T_malha_int * Z_anel / Z_pla_int
    T_carrier = T_sol * (1 + k)
    return dict(i=1 + k, n_c=n_c, n_anel=n_anel, n_pla=n_pla, n_sol_rel=abs(n_sol_rel), n_pla_rel=abs(n_pla_rel), n_anel_rel=abs(n_anel_rel),
                T_malha_ext=T_malha_ext, T_malha_int=T_malha_int, T_anel=T_anel, T_carrier=T_carrier)
