# coding: utf-8
import Dimensionamento_geometrico as Geo_dim
from fpdf import FPDF
import os
from datetime import datetime
import Equações_dimensionamento as Eq_tensao
class Analise_de_tensao:
    def __init__(self,apelido,Proj,Par_engrenado_1,Par_engrenado_2,k1,k2,Ck1,Ck2,Tipo_planetario,Ring,K_Hbeta_imposto1 = None,K_Hbeta_imposto2 = None) :
        self.apelido = apelido # Apelido do par engrenado
        self.Proj = Proj # Nome do projetista
        self.Par_engrenado_1 = Par_engrenado_1 # Conjunto de pinhão e coroa 1
        self.Par_engrenado_2 = Par_engrenado_2 # Conjunto de pinhão e coroa 2
        self.k1 = k1 # Número de engrenagens em um mesmo eixo
        self.k2 = k2 # Número de engrenagens em um mesmo eixo
        self.Ck1 = Ck1 # Recuo de cabeça ou de pé do par engrenado 2 (Caso não seja especificado = None )
        self.Ck2 = Ck2 # Recuo de cabeça ou de pé do par engrenado 1 (Caso não seja especificado = None )
        self.Tipo_planetario = Tipo_planetario # Informação se o planetário é simples ou compostos
        self.Ring = Ring # Informação se a engrenagem interna e fixa ou rotativa

        ##############################################################################################################################################################################################################

        self.c_linha_th1,self.c_linha1,self.c_gamma_alpha1,self.c_gamma_beta1 = Eq_tensao.rigidez (Par_engrenado_1)
        if self.Par_engrenado_2 != None :
            self.c_linha_th2,self.c_linha2,self.c_gamma_alpha2,self.c_gamma_beta2 = Eq_tensao.rigidez (Par_engrenado_2)
        else:
            self.c_linha_th2 = self.c_linha2 = self.c_gamma_alpha2 = self.c_gamma_beta2 = None

        self.n_e1,self.n_e2,self.zona1,self.zona2,self.Kv1,self.Kv2 = Eq_tensao.kv(Par_engrenado_1,Par_engrenado_2,self.c_linha1,self.c_linha2,self.c_gamma_alpha1,self.c_gamma_alpha2,self.Ck1,self.Ck2,self.Tipo_planetario,self.Ring)
        self.K_Hbeta1,self.b_cal1,self.Cond1 = Eq_tensao.K_Hbeta (self.Par_engrenado_1,self.Kv1,self.c_gamma_beta1,self.k1,K_Hbeta_imposto1)
        self.K_Fbeta1 = Eq_tensao.K_Fbeta(Par_engrenado_1,self.K_Hbeta1)
        self.Z_epsilon1 = Eq_tensao.Z_epsilon(self.Par_engrenado_1)
        self.K_Halpha1 = Eq_tensao.K_Halpha(self.Par_engrenado_1,self.Kv1,self.K_Hbeta1,self.c_gamma_alpha1,self.Z_epsilon1)
        self.K_Falpha1 = Eq_tensao.K_Falpha(self.Par_engrenado_1,self.K_Halpha1)
        self.Z_H1 = Eq_tensao.Z_H (self.Par_engrenado_1)
        self.Z_E1 = Eq_tensao.Z_E (self.Par_engrenado_1)
        self.Z_beta1 = Eq_tensao.Z_beta (self.Par_engrenado_1)
        self.Z_L1 = Eq_tensao.Z_L (self.Par_engrenado_1)
        self.Z_V1 = Eq_tensao.Z_V (self.Par_engrenado_1)
        self.Z_R1 = Eq_tensao.Z_R (self.Par_engrenado_1)
        self.Z_W1_pinhao,self.Z_W1_coroa = Eq_tensao.Z_W (self.Par_engrenado_1)
        self.Z_X_pinhao1,self.Z_X_coroa1 = Eq_tensao.Z_X (self.Par_engrenado_1)
        self.Z_B1 = Eq_tensao.Z_B (self.Par_engrenado_1)
        self.Z_D1 = Eq_tensao.Z_D (self.Par_engrenado_1)
        self.Z_NT_pinhao1,self.Z_NT_coroa1,self.Z_GT_pinhao1,self.Z_GT_coroa1 = Eq_tensao.Z_NT (self.Par_engrenado_1)
        self.Yf_pinhao1 = self.Par_engrenado_1.Yf_pinhao
        self.Yf_coroa1 = self.Par_engrenado_1.Yf_coroa
        self.Y_S_pinhao1,self.Y_S_coroa1,AVISO11,AVISO21 = Eq_tensao.Y_S (self.Par_engrenado_1)
        if AVISO11 != None :
            self.Par_engrenado_1.AVISOS.append(AVISO11)
        if AVISO21 != None :
            self.Par_engrenado_1.AVISOS.append(AVISO21)
        self.Y_beta1 = Eq_tensao.Y_beta(self.Par_engrenado_1)
        self.Y_B1_pinhao,self.Y_B1_coroa = Eq_tensao.Y_B(self.Par_engrenado_1)
        self.Y_delta_RefT_pinhao1,self.Y_delta_RefT_coroa1 = Eq_tensao.Y_delta_RefT(self.Par_engrenado_1,self.Y_S_pinhao1,self.Y_S_coroa1)
        self.Y_R_RefT_pinhao1,self.Y_R_RefT_coroa1 = Eq_tensao.Y_R_RefT(self.Par_engrenado_1)
        self.Y_X_pinhao1,self.Y_X_coroa1 = Eq_tensao.Y_X(self.Par_engrenado_1)
        self.Y_NT_pinhao1, self.Y_NT_coroa1 = Eq_tensao.Y_NT(self.Par_engrenado_1)
        self.sigma_H01,self.sigma_Hpinhao1,self.sigma_Hcoroa1,self.sigma_HP_pinhao1,self.sigma_HP_coroa1,self.sigma_GP_pinhao1,self.sigma_GP_coroa1,self.S_Hpinhao1,self.S_Hcoroa1,self.S_Gpinhao1,self.S_Gcoroa1,self.VH_pinhao1,self.VH_coroa1,self.VG_pinhao1,self.VG_coroa1,AVISO11,AVISO21,AVISO31,AVISO41 = Eq_tensao.Tensao_contato(self.Par_engrenado_1,self.Kv1,self.K_Hbeta1,self.K_Halpha1,self.Z_H1,self.Z_E1,self.Z_epsilon1,self.Z_beta1,self.Z_L1,self.Z_V1,self.Z_R1,self.Z_W1_pinhao,self.Z_W1_coroa,self.Z_X_pinhao1,self.Z_X_coroa1,self.Z_B1,self.Z_D1,self.Z_NT_pinhao1,self.Z_NT_coroa1,self.Z_GT_pinhao1,self.Z_GT_coroa1)
        if AVISO11 != None :
            self.Par_engrenado_1.AVISOS.append(AVISO11)
        if AVISO21 != None :
            self.Par_engrenado_1.AVISOS.append(AVISO21)
        if AVISO31 != None :
            self.Par_engrenado_1.AVISOS.append(AVISO31)
        if AVISO41 != None :
            self.Par_engrenado_1.AVISOS.append(AVISO41)
        self.sigma_F011,self.sigma_F021,self.sigma_Fpinhao1,self.sigma_Fcoroa1,self.sigma_FP_pinhao1,self.sigma_FP_coroa1,self.S_Fpinhao1,self.S_Fcoroa1,self.VF_pinhao1,self.VF_coroa1,AVISO11,AVISO21 = Eq_tensao.Tensao_flexao (self.Par_engrenado_1,self.Kv1,self.K_Fbeta1,self.K_Falpha1,self.Yf_pinhao1,self.Yf_coroa1,self.Y_S_pinhao1,self.Y_S_coroa1,self.Y_beta1,self.Y_delta_RefT_pinhao1,self.Y_delta_RefT_coroa1,self.Y_R_RefT_pinhao1,self.Y_R_RefT_coroa1,self.Y_X_pinhao1,self.Y_X_coroa1,self.Y_NT_pinhao1, self.Y_NT_coroa1,self.Y_B1_pinhao,self.Y_B1_coroa)
        if AVISO11 != None :
            self.Par_engrenado_1.AVISOS.append(AVISO11)
        if AVISO21 != None :
            self.Par_engrenado_1.AVISOS.append(AVISO21)

        self.P_21,self.eficencia1,self.T_HP11,self.P_HP11,self.T_HP21,self.P_HP21,self.T_GP11,self.P_GP11,self.T_GP21,self.P_GP21,self.T_FP11,self.P_FP11,self.T_FP21,self.P_FP21 = Eq_tensao.Capacidade_Carga(self.Par_engrenado_1,self.Kv1,self.K_Hbeta1,self.K_Fbeta1,self.K_Halpha1,self.K_Falpha1,self.Z_H1,self.Z_E1,self.Z_epsilon1,self.Z_beta1,self.Z_B1,self.Z_D1,self.Yf_pinhao1,self.Yf_coroa1,self.Y_S_pinhao1,self.Y_S_coroa1,self.Y_beta1,self.sigma_HP_pinhao1,self.sigma_HP_coroa1,self.sigma_GP_pinhao1,self.sigma_GP_coroa1,self.sigma_FP_pinhao1,self.sigma_FP_coroa1,self.Y_B1_pinhao,self.Y_B1_coroa)



        if self.Par_engrenado_2 != None :
            self.K_Hbeta2,self.b_cal2,self.Cond2 = Eq_tensao.K_Hbeta (self.Par_engrenado_2,self.Kv2,self.c_gamma_beta2,self.k2,K_Hbeta_imposto2)
            self.K_Fbeta2 = Eq_tensao.K_Fbeta(Par_engrenado_2,self.K_Hbeta2)
            self.Z_epsilon2 =Eq_tensao.Z_epsilon(self.Par_engrenado_2)
            self.K_Halpha2 = Eq_tensao.K_Halpha(self.Par_engrenado_2,self.Kv2,self.K_Hbeta2,self.c_gamma_alpha2,self.Z_epsilon2)
            self.K_Falpha2 = Eq_tensao.K_Falpha(self.Par_engrenado_2,self.K_Halpha2)
            self.Z_H2 = Eq_tensao.Z_H (self.Par_engrenado_2)
            self.Z_E2 = Eq_tensao.Z_E (self.Par_engrenado_2)
            self.Z_beta2 = Eq_tensao.Z_beta (self.Par_engrenado_2)
            self.Z_L2 = Eq_tensao.Z_L (self.Par_engrenado_2)
            self.Z_V2 = Eq_tensao.Z_V (self.Par_engrenado_2)
            self.Z_R2 = Eq_tensao.Z_R (self.Par_engrenado_2)
            self.Z_W2_pinhao,self.Z_W2_coroa = Eq_tensao.Z_W (self.Par_engrenado_2)
            self.Z_X_pinhao2,self.Z_X_coroa2 = Eq_tensao.Z_X (self.Par_engrenado_2)
            self.Z_B2 = Eq_tensao.Z_B (self.Par_engrenado_2)
            self.Z_D2 = Eq_tensao.Z_D (self.Par_engrenado_2)
            self.Z_NT_pinhao2,self.Z_NT_coroa2,self.Z_GT_pinhao2,self.Z_GT_coroa2 = Eq_tensao.Z_NT (self.Par_engrenado_2)
            self.Yf_pinhao2 = self.Par_engrenado_2.Yf_pinhao
            self.Yf_coroa2 = self.Par_engrenado_2.Yf_coroa
            self.Y_S_pinhao2,self.Y_S_coroa2,AVISO12,AVISO22 = Eq_tensao.Y_S (self.Par_engrenado_2)
            if AVISO12 != None :
                self.Par_engrenado_2.AVISOS.append(AVISO12)
            if AVISO22 != None :
                self.Par_engrenado_2.AVISOS.append(AVISO22)
            self.Y_beta2= Eq_tensao.Y_beta (self.Par_engrenado_2)
            self.Y_B2_pinhao,self.Y_B2_coroa = Eq_tensao.Y_B(self.Par_engrenado_2)
            self.Y_delta_RefT_pinhao2,self.Y_delta_RefT_coroa2 = Eq_tensao.Y_delta_RefT(self.Par_engrenado_2,self.Y_S_pinhao2,self.Y_S_coroa2)
            self.Y_R_RefT_pinhao2,self.Y_R_RefT_coroa2 = Eq_tensao.Y_R_RefT(self.Par_engrenado_2)
            self.Y_X_pinhao2,self.Y_X_coroa2 = Eq_tensao.Y_X(self.Par_engrenado_2)
            self.Y_NT_pinhao2, self.Y_NT_coroa2 = Eq_tensao.Y_NT(self.Par_engrenado_2)
            self.sigma_H02,self.sigma_Hpinhao2,self.sigma_Hcoroa2,self.sigma_HP_pinhao2,self.sigma_HP_coroa2,self.sigma_GP_pinhao2,self.sigma_GP_coroa2,self.S_Hpinhao2,self.S_Hcoroa2,self.S_Gpinhao2,self.S_Gcoroa2,self.VH_pinhao2,self.VH_coroa2,self.VG_pinhao2,self.VG_coroa2,AVISO12,AVISO22,AVISO32,AVISO42 = Eq_tensao.Tensao_contato(self.Par_engrenado_2,self.Kv2,self.K_Hbeta2,self.K_Halpha2,self.Z_H2,self.Z_E2,self.Z_epsilon2,self.Z_beta2,self.Z_L2,self.Z_V2,self.Z_R2,self.Z_W2_pinhao,self.Z_W2_coroa,self.Z_X_pinhao2,self.Z_X_coroa2,self.Z_B2,self.Z_D2,self.Z_NT_pinhao2,self.Z_NT_coroa2,self.Z_GT_pinhao2,self.Z_GT_coroa2)
            if AVISO12 != None :
                self.Par_engrenado_2.AVISOS.append(AVISO12)
            if AVISO22 != None :
                self.Par_engrenado_2.AVISOS.append(AVISO22)
            if AVISO32 != None :
                self.Par_engrenado_2.AVISOS.append(AVISO32)
            if AVISO42 != None :
                self.Par_engrenado_2.AVISOS.append(AVISO42)

            self.sigma_F012,self.sigma_F022,self.sigma_Fpinhao2,self.sigma_Fcoroa2,self.sigma_FP_pinhao2,self.sigma_FP_coroa2,self.S_Fpinhao2,self.S_Fcoroa2,self.VF_pinhao2,self.VF_coroa2,AVISO12,AVISO22 = Eq_tensao.Tensao_flexao (self.Par_engrenado_2,self.Kv2,self.K_Fbeta2,self.K_Falpha2,self.Yf_pinhao2,self.Yf_coroa2,self.Y_S_pinhao2,self.Y_S_coroa2,self.Y_beta2,self.Y_delta_RefT_pinhao2,self.Y_delta_RefT_coroa2,self.Y_R_RefT_pinhao2,self.Y_R_RefT_coroa2,self.Y_X_pinhao2,self.Y_X_coroa2,self.Y_NT_pinhao2, self.Y_NT_coroa2,self.Y_B2_pinhao,self.Y_B2_coroa)
            if AVISO12 != None :
                self.Par_engrenado_2.AVISOS.append(AVISO12)
            if AVISO22 != None :
                self.Par_engrenado_2.AVISOS.append(AVISO22)

            self.P_22,self.eficencia2,self.T_HP12,self.P_HP12,self.T_HP22,self.P_HP22,self.T_GP12,self.P_GP12,self.T_GP22,self.P_GP22,self.T_FP12,self.P_FP12,self.T_FP22,self.P_FP22 = Eq_tensao.Capacidade_Carga(self.Par_engrenado_2,self.Kv2,self.K_Hbeta2,self.K_Fbeta2,self.K_Halpha2,self.K_Falpha2,self.Z_H2,self.Z_E2,self.Z_epsilon2,self.Z_beta2,self.Z_B2,self.Z_D2,self.Yf_pinhao2,self.Yf_coroa2,self.Y_S_pinhao2,self.Y_S_coroa2,self.Y_beta2,self.sigma_HP_pinhao2,self.sigma_HP_coroa2,self.sigma_GP_pinhao2,self.sigma_GP_coroa2,self.sigma_FP_pinhao2,self.sigma_FP_coroa2,self.Y_B2_pinhao,self.Y_B2_coroa)



        if not os.environ.get("ENGR_SEM_PDF") :
            self.salvar_em_PDF()

    def __str__(self):
        if self.Par_engrenado_2 != None :
            return ("\n RELATÓRIO DE DIMENSIONAMENTO DE PAR ENGRENADO  \n \n"

                    f"Apelido do modelo --> Par 1 : {self.Par_engrenado_1.apelido} ; Par 2 : {self.Par_engrenado_2.apelido} \n"
                    f"Engenheiro --> {self.Proj} \n"
                    f"Tipo de interação --> Par 1 : {self.Par_engrenado_1.tipo} ; Par 2 : {self.Par_engrenado_2.tipo} \n"
                    f"Tipo de transmissão --> Par 1 : {self.Par_engrenado_1.trans} ; Par 2 : {self.Par_engrenado_2.trans}  \n"
                    f"Quantidade de planetas --> Par 1 : {self.Par_engrenado_1.N_cp} ; Par 2 : {self.Par_engrenado_2.N_cp}  \n"
                    f"Tipo de planetárila --> {self.Tipo_planetario} \n"
                    f"Tipo de ring --> {self.Ring} \n"
                    f"Vida útil nominal requerida pelo egrenamento [horas] --> Par 1 : {round(self.Par_engrenado_1.Vr,4)} ; Par 2 : {round(self.Par_engrenado_2.Vr,4)}\n"
                    f"Grau de irregularida --> Par 1 :  Pinhão : {self.Par_engrenado_1.irregularidade_motora} ; Coroa : {self.Par_engrenado_1.irregularidade_movida} , Par 2 :  Pinhão : {self.Par_engrenado_2.irregularidade_motora} ; Coroa : {self.Par_engrenado_2.irregularidade_movida}\n"
                    f"Temperatura dos engrenagens no instante de máxiam difernça de temperatura entre a caixa e as rodas [°C ] --> Par 1 : {round(self.Par_engrenado_1.T_Rmd,4)} ; Par 1 : {round(self.Par_engrenado_2.T_Rmd,4)} \n"
                    f"Temperatura da caixa no instante de máxiam difernça de temperatura entre a caixa e as rodas [°C]  -->  Par 1 : {round(self.Par_engrenado_1.T_Cmd,4)}; Par 2 : {round(self.Par_engrenado_2.T_Cmd,4)} \n"
                    f"Temperatura de operação [°C] --> Par 1 : {round(self.Par_engrenado_1.T_op,4)} ; Par 2 : {round(self.Par_engrenado_2.T_op,4)} \n"
                    f"Qualidade das engrenagens --> Par 1 : Pinhão : {self.Par_engrenado_1.IQ_pinhao} ; Coroa : {self.Par_engrenado_1.IQ_coroa} ; Par 2 : Pinhão : {self.Par_engrenado_2.IQ_pinhao} ; Coroa : {self.Par_engrenado_2.IQ_coroa} \n"
                    f"Número de dentes mínimo para prevenir Undercut -->  Par 1 : Pinhão : {self.Par_engrenado_1.Z_min_pinhao} ; Coroa : {self.Par_engrenado_1.Z_min_coroa} ;  Par 2 : Pinhão : {self.Par_engrenado_2.Z_min_pinhao} ; Coroa : {self.Par_engrenado_2.Z_min_coroa} \n"
                    f"Qualidade do par engrenado --> Par 1 : {self.Par_engrenado_1.IQ} ; Par 2 : {self.Par_engrenado_2.IQ} \n"
                    f"Rigidez máxima teórica --> Par 1 : {round(self.c_linha_th1,4)}; Par 2 : {round(self.c_linha_th2,4)} \n"
                    f"Rigidez máxima --> Par 1 : {round(self.c_linha1,4)}; Par 2 : {round(self.c_linha2,4)} \n"
                    f"Rigidez de malha alpha  --> Par 1 : {round(self.c_gamma_alpha1,4)}; Par 2 : {round(self.c_gamma_alpha2,4)} \n"
                    f"Rigidez de malha beta  --> Par 1 : {round(self.c_gamma_beta1,4)}; Par 2 : {round(self.c_gamma_beta2,4)} \n"
                    f"Rotação crítica de ressonância [Rpm] --> Par 1 : {round(self.n_e1)}; Par 2 : {round(self.n_e2)} \n"

                    "\n MATERIAIS \n \n"

                    f"Material do pinhão 1 \n \n {self.Par_engrenado_1.material_pinhao} \n"
                    f"Material da coroa 1 \n \n {self.Par_engrenado_1.material_coroa} \n"
                    f"Material do pinhão 2  \n \n {self.Par_engrenado_2.material_pinhao} \n"
                    f"Material da coroa 2 \n \n {self.Par_engrenado_2.material_coroa} \n"

                    "\n FERRAMENTAS \n \n"

                    f"Ferramenta de usinagem do pinhão 1 \n \n {self.Par_engrenado_1.ferramenta_pinhao} \n"
                    f"Ferramenta de usinagem da coroa 1 \n \n {self.Par_engrenado_1.ferramenta_coroa} \n"
                    f"Ferramenta de usinagem do pinhão 2 \n \n {self.Par_engrenado_2.ferramenta_pinhao} \n"
                    f"Ferramenta de usinagem da coroa 2 \n \n {self.Par_engrenado_2.ferramenta_coroa} \n"
                    f"Raio de crista da ferramenta máximo [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.rk_pinhao_max,4)} ; Coroa : {round(self.Par_engrenado_1.rk_coroa_max,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.rk_pinhao_max,4)} ; Coroa : {round(self.Par_engrenado_2.rk_coroa_max,4)} \n"
                    f"Raio de crista da ferramenta [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.rk_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.rk_coroa,4)} ;  Par 2 : Pinhão : {round(self.Par_engrenado_2.rk_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.rk_coroa,4)} \n"

                    "\n Lubrificantes 1  \n \n"

                    f"{self.Par_engrenado_1.lubrificante} \n"
                    f"Volume de óleo [L] --> Máximo: {round(self.Par_engrenado_1.V_ls,4)} ; Mínimo : {round(self.Par_engrenado_1.V_li,4)} \n"
                    f"Profundidade de submersão [mm] --> Máximo: {round(self.Par_engrenado_1.P_rs,5)} ; Mínimo : {round(self.Par_engrenado_1.P_ri,4)} \n"

                    "\n Lubrificantes 2  \n \n"

                    f"{self.Par_engrenado_2.lubrificante} \n"
                    f"Volume de óleo [L] --> Máximo: {round(self.Par_engrenado_2.V_ls,4)} ; Mínimo : {round(self.Par_engrenado_2.V_li,4)} \n"
                    f"Profundidade de submersão [mm] --> Máximo: {round(self.Par_engrenado_2.P_rs,5)} ; Mínimo : {round(self.Par_engrenado_2.P_ri,4)} \n"


                    "\n CARACTERÍSTICAS GEOMÉTRICAS BÁSICAS \n \n"

                    f"Modulo normal do par [mm] --> Par 1 : {round(self.Par_engrenado_1.m_n,4)} ; Par 2 : {round(self.Par_engrenado_2.m_n,4)} \n"
                    f"Modulo transversal do par [mm] --> Par 1 : {round(self.Par_engrenado_1.m_t,4)} ; Par 2 : {round(self.Par_engrenado_2.m_t,4)} \n"
                    f"Modulo transversal de trabalho [mm]--> Par 1 : {round(self.Par_engrenado_1.m_wn,4)} ; Par 2 : {round(self.Par_engrenado_2.m_wn,4)} \n"
                    f"Distância entre centros standart [mm] --> Par 1 : {round(self.Par_engrenado_1.a_standart,4)} ; Par 2 : {round(self.Par_engrenado_2.a_standart,4)} \n"
                    f"Distância entre centros de trabalho (Imposta) [mm] --> Par 1 : {round(self.Par_engrenado_1.a,4)} ; Par 2 : {round(self.Par_engrenado_2.a,4)} \n"
                    f"Distância entre centros de trabalho (Calculada) [mm] --> Par 1 : {round(self.Par_engrenado_1.a_conferencia,4)} ; Par 2 : {round(self.Par_engrenado_2.a_conferencia,4)} \n"
                    f"Tolerância da distância entre centros [mm] --> Par 1 : Superior : {round(self.Par_engrenado_1.Aa_s,4)} ; Inferior {round(self.Par_engrenado_1.Aa_i,4)} ; Par 2 : Superior : {round(self.Par_engrenado_2.Aa_s,4)} ; Inferior {round(self.Par_engrenado_2.Aa_i,4)} \n"
                    f"Número de dentes --> Par 1 : Pinhão :  {self.Par_engrenado_1.Z_pinhao} ; Coroa : {self.Par_engrenado_1.Z_coroa} ;  Par 2 : Pinhão :  {self.Par_engrenado_2.Z_pinhao} ; Coroa : {self.Par_engrenado_2.Z_coroa} \n"
                    f"Número de dentes virtuais --> Par 1 : Pinhão : {round(self.Par_engrenado_1.zn_pinhao,4)}; Coroa : {round(self.Par_engrenado_1.zn_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.zn_pinhao,4)}; Coroa : {round(self.Par_engrenado_2.zn_coroa,4)} \n"
                    f"Razão de engrenamento --> Par 1 : {round(self.Par_engrenado_1.u,4)} ; Par 2 : {round(self.Par_engrenado_2.u,4)} \n "
                    f"Comprimento dos dentes [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.b_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.b_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.b_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.b_coroa,4)} \n"
                    f"Extenção de contato (Comprimento do dente em contato) [mm] --> Par 1 : {round(self.Par_engrenado_1.b,4)} ;  Par 2 : {round(self.Par_engrenado_2.b,4)} \n"
                    f"Largura de calculo [mm] --> Par 1 : {round(self.b_cal1,4)} ; Par 2 : {round(self.b_cal2,4)} \n"
                    f"Ângulo de pressão normal [°] --> Par 1 : {round(self.Par_engrenado_1.alpha_n,4)} ; Par 2 : {round(self.Par_engrenado_2.alpha_n,4)} \n"
                    f"Ângulo de pressão transversal [°] --> Par 1 : {round(self.Par_engrenado_1.alpha_t,4)} ; Par 2 : {round(self.Par_engrenado_2.alpha_t,4)} \n"
                    f"Ângulo de pressão de trabalho normal [°] --> Par 1 : {round(self.Par_engrenado_1.alpha_wn,4)} ; Par 2 : {round(self.Par_engrenado_2.alpha_wn,4)} \n"
                    f"Ângulo de pressão de trabalho transversal [°] --> Par 1 : {round(self.Par_engrenado_1.alpha_wt,4)} ;  Par 2 : {round(self.Par_engrenado_2.alpha_wt,4)} \n"
                    f"Ângulo de pressão normal sobre o diâmetro de referência deslocado [°] --> Par 1 : Pinhão :{round(self.Par_engrenado_1.alpha_vn_pinhao,4)}  ; Coroa : {round(self.Par_engrenado_1.alpha_vn_coroa,4)} ;  Par 2 : Pinhão : {round(self.Par_engrenado_2.alpha_vn_pinhao,4)}  ; Coroa : {round(self.Par_engrenado_2.alpha_vn_coroa,4)}  \n"
                    f"Ângulo de pressão transversal sobre o diâmetro de referência deslocado [°] --> Par 1 : Pinhão :{round(self.Par_engrenado_1.alpha_vt_pinhao,4)}  ; Coroa : {round(self.Par_engrenado_1.alpha_vt_coroa,4)} ; Par 2 : Pinhão :{round(self.Par_engrenado_2.alpha_vt_pinhao,4)}  ; Coroa : {round(self.Par_engrenado_2.alpha_vt_coroa,4)}  \n"
                    f"Ângulo de hélice [°] --> Par 1 : {round(self.Par_engrenado_1.beta,4)} ; Par 2 : {round(self.Par_engrenado_2.beta,4)} \n"
                    f"Ângulo de hélice sobre o circulo base [°] --> Par 1 : {round(self.Par_engrenado_1.beta_b,4)} ;  Par 2 : {round(self.Par_engrenado_2.beta_b,4)} \n"
                    f"Ângulo de hélice sobre o diâmetro de referência deslocado [°] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.beta_v_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.beta_v_coroa,4)} ;  Par 2 : Pinhão : {round(self.Par_engrenado_2.beta_v_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.beta_v_coroa,4)} \n"
                    f"Ângulo de hélice sobre o diâmetro primitivo [°] --> Par 1 : {round(self.Par_engrenado_1.beta_w_pinhao,4)} ; Par 2 : {round(self.Par_engrenado_2.beta_w_pinhao,4)} \n"
                    f"Diâmetro de referência [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.d_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.d_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.d_coroa,4)} \n"
                    f"Diâmetro primitivo [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.dw_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.dw_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.dw_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.dw_coroa,4)} \n"
                    f"Diâmetro de referência deslocado [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.d_pinhao_deslocado,4)} ; Coroa : {round(self.Par_engrenado_1.d_coroa_deslocado,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.d_pinhao_deslocado,4)} ; Coroa : {round(self.Par_engrenado_2.d_coroa_deslocado,4)} \n"
                    f"Diâmetro base [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.db_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.db_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.db_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.db_coroa,4)} \n"
                    f"Relação auxiliar ((x1+x2/z1+z2)) --> Par 2 : {round(self.Par_engrenado_1.K,6)} ; Par 2 : {round(self.Par_engrenado_2.K,6)} \n"
                    f"Coeficiente de correção do blank --> Par 1 : {round(self.Par_engrenado_1.rel_aux,6)} ; Par 2 : {round(self.Par_engrenado_2.rel_aux,6)} \n"
                    f"Addendum real [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.h_a_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.h_a_coroa,4,)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.h_a_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.h_a_coroa,4,)} \n"
                    f"Dedendum real [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.h_f_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.h_f_coroa,4,)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.h_f_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.h_f_coroa,4,)} \n"
                    f"Altura do dente [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.h_dente_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.h_dente_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.h_dente_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.h_dente_coroa,4)} \n"
                    f"Diâmetro de cabeça [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.d_a_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_a_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.d_a_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.d_a_coroa,4)} \n"
                    f"Tolerância superior do diâmetro de cabeça [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.A_da_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.A_da_s_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.A_da_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.A_da_s_coroa,4)} \n"
                    f"Tolerância inferior do diâmetro de cabeça [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.A_da_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.A_da_i_coroa,4)} ;  Par 2 : Pinhão : {round(self.Par_engrenado_2.A_da_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.A_da_i_coroa,4)} \n"
                    f"Diâmetro de pé [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.d_f_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_f_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.d_f_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.d_f_coroa,4)} \n"
                    f"Tolerância superior do diâmetro de pé [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.A_df_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.A_df_s_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.A_df_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.A_df_s_coroa,4)} \n"
                    f"Tolerância inferior do diâmetro de pé [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.A_df_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.A_df_i_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.A_df_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.A_df_i_coroa,4)} \n"
                    f"Folga no pé do dente [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.Cs_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Cs_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.Cs_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Cs_coroa,4)} \n"
                    f"Folga superior no pé do dente [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.Css_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Css_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.Css_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Css_coroa,4)} \n"
                    f"Folga inferior no pé do dente [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.Csi_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Csi_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.Csi_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Csi_coroa,4)} \n"
                    f"Diâmetro de cabeça útil [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.d_na_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_na_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.d_na_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.d_na_coroa,4)} \n"
                    f"Diâmetro de pé útil [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.d_nf_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_nf_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.d_nf_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.d_nf_coroa,4)} \n"
                    f"Passo circular normal [mm] --> Par 1 : {round(self.Par_engrenado_1.pc_n,4)} ; Par 2 : {round(self.Par_engrenado_2.pc_n,4)} \n"
                    f"Passo circular transversal [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.pc_t_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.pc_t_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.pc_t_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.pc_t_coroa,4)} \n"
                    f"Passo circular transversal primitivo [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.pc_tw_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.pc_tw_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.pc_tw_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.pc_tw_coroa,4)} \n"
                    f"Passo axial [mm] --> Par 1 : {round(self.Par_engrenado_1.p_x,4)} ; Par 2 : {round(self.Par_engrenado_2.p_x,4)} \n"
                    f"Passo base [mm] --> Par 1 : {round(self.Par_engrenado_1.pb,4)} ; Par 2 : {round(self.Par_engrenado_2.pb,4)} \n"
                    f"Passo base axial [mm] --> Par 1 : {round(self.Par_engrenado_1.pb_x,4)} ; Par 2 : {round(self.Par_engrenado_2.pb_x,4)} \n"
                    f"Somatório do deslocameno de perfil do pinhão e da coroa --> Par 1 : {round(self.Par_engrenado_1.sum_x,6)} ; Par 2 : {round(self.Par_engrenado_2.sum_x,6)} \n"
                    f"Deslocamento de perfil --> Par 1 : Pinhão : {round(self.Par_engrenado_1.x_pinhao,6)} ; Coroa : {round(self.Par_engrenado_1.x_coroa,6)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.x_pinhao,6)} ; Coroa : {round(self.Par_engrenado_2.x_coroa,6)} \n"
                    f"Espessura do dente normal nominal [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.S_n_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_n_coroa,4)} ;  Par 2 : Pinhão : {round(self.Par_engrenado_2.S_n_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.S_n_coroa,4)} \n"
                    f"Espessura superior do dente normal [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.S_ns_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_ns_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.S_ns_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.S_ns_coroa,4)} \n"
                    f"Espessura  inferior do dente normal  [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.S_ni_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_ni_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.S_ni_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.S_ni_coroa,4)} \n"
                    f"Espessura do dente normal transversal [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.S_t_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_t_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.S_t_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.S_t_coroa,4)} \n"
                    f"Espessura superior transversal do dente [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.S_ts_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_ts_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.S_ts_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.S_ts_coroa,4)} \n"
                    f"Espessura inferior transversal do dente [mm]  [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.S_ti_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_ti_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.S_ti_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.S_ti_coroa,4)} \n"
                    f"Espessura da cabeça do dente sem o chanfro normal nominal [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.S_na_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_na_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.S_na_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.S_na_coroa,4)} \n"
                    f"Espessura da cabeça do dente sem o chanfro superior normal [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.S_na_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_na_s_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.S_na_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.S_na_s_coroa,4)} \n"
                    f"Espessura da cabeça do dente sem o chanfro inferior normal [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.S_na_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_na_i_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.S_na_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.S_na_i_coroa,4)} \n"
                    f"Espessura da cabeça do dente com o chanfro normal nominal [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.s_nk_pinhao,4)} ; Coroa {round(self.Par_engrenado_1.s_nk_coroa,4)} ;  Par 2 : Pinhão : {round(self.Par_engrenado_2.s_nk_pinhao,4)} ; Coroa {round(self.Par_engrenado_2.s_nk_coroa,4)} \n"
                    f"Espessura da cabeça do dente com o chanfro superior normal [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.s_nk_s_pinhao,4)} ; Coroa {round(self.Par_engrenado_1.s_nk_s_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.s_nk_s_pinhao,4)} ; Coroa {round(self.Par_engrenado_2.s_nk_s_coroa,4)} \n"
                    f"Espessura da cabeça do dente com o chanfro inferior normal [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.s_nk_i_pinhao,4)} ; Coroa {round(self.Par_engrenado_1.s_nk_i_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.s_nk_i_pinhao,4)} ; Coroa {round(self.Par_engrenado_2.s_nk_i_coroa,4)} \n"
                    f"Dimensão do vão normal [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.T_n_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.T_n_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.T_n_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.T_n_coroa,4)} \n"
                    f"Dimensão superior normal do vão [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.T_ns_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.T_ns_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.T_ns_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.T_ns_coroa,4)} \n"
                    f"Dimensão inferior normal do vão [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.T_ni_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.T_ni_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.T_ni_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.T_ni_coroa,4)} \n"
                    f"Dimensão do vão transversal [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.T_t_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.T_t_coroa,4)} ; Par 1 : Pinhão : {round(self.Par_engrenado_2.T_t_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.T_t_coroa,4)}  \n"
                    f"Dimensão superior transversal do vão  [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.T_ts_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.T_ts_coroa,4)} ; Par 1 : Pinhão : {round(self.Par_engrenado_2.T_ts_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.T_ts_coroa,4)} \n"
                    f"Dimensão inferior transversal do vão [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.T_ti_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.T_ti_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.T_ti_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.T_ti_coroa,4)} \n"
                    f"Ângulo de chanfro na seção normal [°] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.phi_na_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.phi_na_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.phi_na_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.phi_na_coroa,4)}  \n"
                    f"Ângulo de chanfro na seção transversal [°] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.phi_ta_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.phi_ta_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.phi_ta_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.phi_ta_coroa,4)} \n"
                    f"Comprimento de chanfro [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.C_a_pinhao,4)} ; Coroa {round(self.Par_engrenado_1.C_a_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.C_a_pinhao,4)} ; Coroa {round(self.Par_engrenado_2.C_a_coroa,4)} \n"
                    f"Diâmetro de início de chanfro [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.d_nk_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_nk_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.d_nk_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.d_nk_coroa,4)} \n"
                    f"Tolerância superior do diâmetro de início de chanfro [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.A_dnk_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.A_dnk_s_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.A_dnk_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.A_dnk_s_coroa,4)} \n"
                    f"Tolerância inferior do diâmetro de início de chanfro [mm] --> Par 1 : Pinhão : {round(self.Par_engrenado_1.A_dnk_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.A_dnk_i_coroa,4)} ; Par 2 : Pinhão : {round(self.Par_engrenado_2.A_dnk_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.A_dnk_i_coroa,4)} \n"
                    f"Grau de recobrimento de perfil --> Par 1 : {round(self.Par_engrenado_1.epsilon_alpha,4)} ; Par 2 : {round(self.Par_engrenado_2.epsilon_alpha,4)} \n"
                    f"Grau de recobrimento de hélice --> Par 1 : {round(self.Par_engrenado_1.epsilon_beta,4)} ; Par 2 : {round(self.Par_engrenado_2.epsilon_beta,4)} \n"
                    f"Grau de recobrimento de total --> Par 1 : {round(self.Par_engrenado_1.epsilon_total,4)} ; Par 2 : {round(self.Par_engrenado_2.epsilon_total,4)} \n"
                    f"Velocidade de escorregamento de recesso [m/s] --> Par 1 : {round(self.Par_engrenado_1.v_ga,4)} ;  Par 1 : {round(self.Par_engrenado_2.v_ga,4)} \n"
                    f"Velocidade de escorregamento de acesso [m/s] --> Par 1 : {round(self.Par_engrenado_1.v_gf,4)} ; Par 2 : {round(self.Par_engrenado_2.v_gf,4)}   \n"

                    "\n CARACTERÍSTICAS DO CORPO DA ENGRENAGEM E DOS MANCAIS 1 \n \n"

                    f"Diâmetro de alma [mm]  --> Pinhão : {round(self.Par_engrenado_1.di_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.di_coroa,4)} \n"
                    f"Espessura de alma [mm] -->  Pinhão : {round(self.Par_engrenado_1.bs_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.bs_coroa,4)} \n"
                    f"Diâmetro do eixo [mm] --> Pinhão : {round(self.Par_engrenado_1.d_sh_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_sh_coroa,4)} \n"
                    f"Espessura entre diâmetro de alma e do diâmetro de pé [mm] --> Pinhão : {round(self.Par_engrenado_1.s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.s_coroa,4)} \n"
                    f"Distância entre os mancais [mm] --> Pinhao : {round(self.Par_engrenado_1.L_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.L_coroa,4)} \n"
                    f"Distância do centro dos mancais ao dentro da roda dentada [mm] --> Pinhão : {round(self.Par_engrenado_1.sh_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.sh_coroa,4)} \n"
                    f"Constante para a posição --> Pinhão : {round(self.Par_engrenado_1.K_linha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.K_linha_coroa,4)}\n"

                    "\n CARACTERÍSTICAS DO CORPO DA ENGRENAGEM E DOS MANCAIS 2 \n \n"

                    f"Diâmetro de alma [mm]  --> Pinhão : {round(self.Par_engrenado_2.di_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.di_coroa,4)} \n"
                    f"Espessura de alma [mm] -->  Pinhão : {round(self.Par_engrenado_2.bs_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.bs_coroa,4)} \n"
                    f"Diâmetro do eixo [mm] --> Pinhão : {round(self.Par_engrenado_2.d_sh_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.d_sh_coroa,4)} \n"
                    f"Espessura entre diâmetro de alma e do diâmetro de pé [mm] --> Pinhão : {round(self.Par_engrenado_2.s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.s_coroa,4)} \n"
                    f"Distância entre os mancais [mm] --> Pinhao : {round(self.Par_engrenado_2.L_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.L_coroa,4)} \n"
                    f"Distância do centro dos mancais ao dentro da roda dentada [mm] --> Pinhão : {round(self.Par_engrenado_2.sh_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.sh_coroa,4)} \n"
                    f"Constante para a posição --> Pinhão : {round(self.Par_engrenado_2.K_linha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.K_linha_coroa,4)}\n"

                    "\n OPREÇÃO DE ACABAMENTO 1 \n \n"

                    f"Operação de acabamento --> Pinhão :{self.Par_engrenado_1.op_acabamento_pinhao} ; Coroa : {self.Par_engrenado_1.op_acabamento_coroa} \n"
                    f"Sobremetal para acabamento [mm] --> Pinhão : {round(self.Par_engrenado_1.SM_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.SM_coroa,4)} \n"
                    f"Rugosidade média no flanco do dente [micrometro] --> Pinhão : {round(self.Par_engrenado_1.Ra_flanco_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Ra_flanco_coroa,4)} \n"
                    f"Altura máxima do perfil de rugosidade nos flancos do dente [micrometro] --> Pinhão : {round(self.Par_engrenado_1.Rz_flanco_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Rz_flanco_coroa,4)} \n"
                    f"Rugosidade média no pé do dente [micrometro] --> Pinhão : {round(self.Par_engrenado_1.Ra_pe_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Ra_pe_coroa,4)} \n"
                    f"Altura máxima do perfil de rugosidade no pé do dente [micrometro] --> Pinhão : {round(self.Par_engrenado_1.Rz_pe_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Rz_pe_coroa,4)} \n"
                    f"Qualidade das engrenagens --> Pinhão : {round(self.Par_engrenado_1.IQ_pinhao,1)} ; Coroa : {round(self.Par_engrenado_1.IQ_coroa,1)} \n"

                    "\n OPREÇÃO DE ACABAMENTO 2 \n \n"

                    f"Operação de acabamento --> Pinhão :{self.Par_engrenado_2.op_acabamento_pinhao} ; Coroa : {self.Par_engrenado_2.op_acabamento_coroa} \n"
                    f"Sobremetal para acabamento [mm] --> Pinhão : {round(self.Par_engrenado_2.SM_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.SM_coroa,4)} \n"
                    f"Rugosidade média no flanco do dente [micrometro] --> Pinhão : {round(self.Par_engrenado_2.Ra_flanco_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Ra_flanco_coroa,4)} \n"
                    f"Altura máxima do perfil de rugosidade nos flancos do dente [micrometro] --> Pinhão : {round(self.Par_engrenado_2.Rz_flanco_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Rz_flanco_coroa,4)} \n"
                    f"Rugosidade média no pé do dente [micrometro] --> Pinhão : {round(self.Par_engrenado_2.Ra_pe_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Ra_pe_coroa,4)} \n"
                    f"Altura máxima do perfil de rugosidade no pé do dente [micrometro] --> Pinhão : {round(self.Par_engrenado_2.Rz_pe_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Rz_pe_coroa,4)} \n"
                    f"Qualidade das engrenagens --> Pinhão : {round(self.Par_engrenado_2.IQ_pinhao,1)} ; Coroa : {round(self.Par_engrenado_2.IQ_coroa,1)} \n"

                    "\n CONTROLE DE ESPESSURA DO DENTE 1 \n \n"

                    f"Números de dentes seguidos a se medir --> Pinhão : {self.Par_engrenado_1.k_pinhao} ; Coroa : {self.Par_engrenado_1.k_coroa} \n"
                    f"Dimensão W superior [mm] --> Pinhão : {round(self.Par_engrenado_1.Wk_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Wk_s_coroa,4)} \n"
                    f"Dimensão W inferior [mm] --> Pinhão : {round(self.Par_engrenado_1.Wk_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Wk_i_coroa,4)} \n"
                    f"Diâmetro da esfera/rolo [mm] --> Pinhão : {round(self.Par_engrenado_1.Dm_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Dm_coroa,4)} \n"
                    f"Entre pinos/esferas superior [mm] --> Pinhão : {round(self.Par_engrenado_1.Md_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Md_s_coroa,4)} \n"
                    f"Entre pinos/esferas inferior [mm] --> Pinhão : {round(self.Par_engrenado_1.Md_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Md_i_coroa,4)} \n"
                    f"Diâmetro de tangência da esfera/pino superior [mm] --> Pinhão : {round(self.Par_engrenado_1.d_m_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_m_s_coroa,4)} \n"
                    f"Diâmetro de tangência da esfera/pino inferior [mm] --> Pinhão : {round(self.Par_engrenado_1.d_m_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_m_i_coroa,4)} \n"
                    f"Abaulameto superior do dente (Crown)[mm] --> Pinhão : {round(self.Par_engrenado_1.crwon_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.crwon_s_coroa,4)} \n"
                    f"Abaulameto inferior do dente (Crown)[mm] --> Pinhão : {round(self.Par_engrenado_1.crwon_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.crwon_i_coroa,4)} \n"

                    "\n CONTROLE DE ESPESSURA DO DENTE 2 \n \n"

                    f"Números de dentes seguidos a se medir --> Pinhão : {self.Par_engrenado_2.k_pinhao} ; Coroa : {self.Par_engrenado_2.k_coroa} \n"
                    f"Dimensão W superior [mm] --> Pinhão : {round(self.Par_engrenado_2.Wk_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Wk_s_coroa,4)} \n"
                    f"Dimensão W inferior [mm] --> Pinhão : {round(self.Par_engrenado_2.Wk_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Wk_i_coroa,4)} \n"
                    f"Diâmetro da esfera/rolo [mm] --> Pinhão : {round(self.Par_engrenado_2.Dm_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Dm_coroa,4)} \n"
                    f"Entre pinos/esferas superior [mm] --> Pinhão : {round(self.Par_engrenado_2.Md_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Md_s_coroa,4)} \n"
                    f"Entre pinos/esferas inferior [mm] --> Pinhão : {round(self.Par_engrenado_2.Md_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Md_i_coroa,4)} \n"
                    f"Diâmetro de tangência da esfera/pino superior [mm] --> Pinhão : {round(self.Par_engrenado_2.d_m_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.d_m_s_coroa,4)} \n"
                    f"Diâmetro de tangência da esfera/pino inferior [mm] --> Pinhão : {round(self.Par_engrenado_2.d_m_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.d_m_i_coroa,4)} \n"
                    f"Abaulameto superior do dente (Crown)[mm] --> Pinhão : {round(self.Par_engrenado_2.crwon_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.crwon_s_coroa,4)} \n"
                    f"Abaulameto inferior do dente (Crown)[mm] --> Pinhão : {round(self.Par_engrenado_2.crwon_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.crwon_i_coroa,4)} \n"

                    "\n MICROGEOMETRIA 1 \n \n"

                    f"Desvio de concetricidade (Fr) [mm] --> Pinhão : {round(self.Par_engrenado_1.Fr_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Fr_coroa,4)} \n"
                    f"Flutuação nas espessuras dos dentes (Rs) [mm] --> Pinhão : {round(self.Par_engrenado_1.Rs_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Rs_coroa,4)} \n"
                    f"Desvio de passo individual (fp) [mm] --> Pinhão : {round(self.Par_engrenado_1.fp_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.fp_coroa,4)} \n"
                    f"Erro entre os passos consecutivos (fu) [mm] --> Pinhão : {round(self.Par_engrenado_1.fu_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.fu_coroa,4)} \n"
                    f"Erro total de passo (Fp) [mm] --> Pinhão : {round(self.Par_engrenado_1.Fp_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Fp_coroa,4)} \n"
                    f"Desvio de passo sobre k dentes consecutivos (Fpk) [mm] --> Pinhão : {round(self.Par_engrenado_1.Fpk_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Fpk_coroa,4)} \n"
                    f"Desvio de passo sobre uma fração de (z/8) dentes consecutivos (Fpk/8) [mm] --> Pinhão : {round(self.Par_engrenado_1.Fpk_8_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Fpk_8_coroa,4)} \n"
                    f"Desvio de passo base normal (fpe) [mm] --> Pinhão : {round(self.Par_engrenado_1.fpe_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.fpe_coroa,4)} \n"
                    f"Desvio total na linha dos flancos (F_beta) [mm] --> Pinhão : {round(self.Par_engrenado_1.F_beta_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.F_beta_coroa,4)} \n"
                    f"Desvio angular na linha dos flancos (f_Hbeta) [mm] --> Pinhão : {round(self.Par_engrenado_1.f_Hbeta_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.f_Hbeta_coroa,4)} \n"
                    f"Desvio de forma na linha dos flancos (f_betaf) [mm] --> Pinhão : {round(self.Par_engrenado_1.f_betaf_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.f_betaf_coroa,4)} \n"
                    f"Desvio total de perfil envolvente (Ff) [mm] --> Pinhão : {round(self.Par_engrenado_1.F_f_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.F_f_coroa,4)} \n"
                    f"Desvio angular de perfil envolvente (F_Halpha) [mm] --> Pinhão : {round(self.Par_engrenado_1.f_Halpha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.f_Halpha_coroa,4)} \n"
                    f"Desvio de forma de perfil envolvente (ff) [mm] --> Pinhão : {round(self.Par_engrenado_1.f_f_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.f_f_coroa,4)} \n"
                    f"Deslocamento composto radial (F''i) [mm] --> Pinhão : {round(self.Par_engrenado_1.F_i_llinha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.F_i_llinha_coroa,4)} \n"
                    f"Salto radial (f''i) [mm] --> Pinhão : {round(self.Par_engrenado_1.f_i_llinha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.f_i_llinha_coroa,4)} \n"
                    f"Deslocamento composto tangencial (F'i) [mm] --> Pinhão : {round(self.Par_engrenado_1.F_i_linha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.F_i_linha_coroa,4)} \n"
                    f"Salto tangencial (f'i) [mm] --> Pinhão : {round(self.Par_engrenado_1.f_i_linha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.f_i_linha_coroa,4)} \n"

                    "\n MICROGEOMETRIA 2 \n \n"

                    f"Desvio de concetricidade (Fr) [mm] --> Pinhão : {round(self.Par_engrenado_2.Fr_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Fr_coroa,4)} \n"
                    f"Flutuação nas espessuras dos dentes (Rs) [mm] --> Pinhão : {round(self.Par_engrenado_2.Rs_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Rs_coroa,4)} \n"
                    f"Desvio de passo individual (fp) [mm] --> Pinhão : {round(self.Par_engrenado_2.fp_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.fp_coroa,4)} \n"
                    f"Erro entre os passos consecutivos (fu) [mm] --> Pinhão : {round(self.Par_engrenado_2.fu_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.fu_coroa,4)} \n"
                    f"Erro total de passo (Fp) [mm] --> Pinhão : {round(self.Par_engrenado_2.Fp_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Fp_coroa,4)} \n"
                    f"Desvio de passo sobre k dentes consecutivos (Fpk) [mm] --> Pinhão : {round(self.Par_engrenado_2.Fpk_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Fpk_coroa,4)} \n"
                    f"Desvio de passo sobre uma fração de (z/8) dentes consecutivos (Fpk/8) [mm] --> Pinhão : {round(self.Par_engrenado_2.Fpk_8_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.Fpk_8_coroa,4)} \n"
                    f"Desvio de passo base normal (fpe) [mm] --> Pinhão : {round(self.Par_engrenado_2.fpe_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.fpe_coroa,4)} \n"
                    f"Desvio total na linha dos flancos (F_beta) [mm] --> Pinhão : {round(self.Par_engrenado_2.F_beta_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.F_beta_coroa,4)} \n"
                    f"Desvio angular na linha dos flancos (f_Hbeta) [mm] --> Pinhão : {round(self.Par_engrenado_2.f_Hbeta_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.f_Hbeta_coroa,4)} \n"
                    f"Desvio de forma na linha dos flancos (f_betaf) [mm] --> Pinhão : {round(self.Par_engrenado_2.f_betaf_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.f_betaf_coroa,4)} \n"
                    f"Desvio total de perfil envolvente (Ff) [mm] --> Pinhão : {round(self.Par_engrenado_2.F_f_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.F_f_coroa,4)} \n"
                    f"Desvio angular de perfil envolvente (F_Halpha) [mm] --> Pinhão : {round(self.Par_engrenado_2.f_Halpha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.f_Halpha_coroa,4)} \n"
                    f"Desvio de forma de perfil envolvente (ff) [mm] --> Pinhão : {round(self.Par_engrenado_2.f_f_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.f_f_coroa,4)} \n"
                    f"Deslocamento composto radial (F''i) [mm] --> Pinhão : {round(self.Par_engrenado_2.F_i_llinha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.F_i_llinha_coroa,4)} \n"
                    f"Salto radial (f''i) [mm] --> Pinhão : {round(self.Par_engrenado_2.f_i_llinha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.f_i_llinha_coroa,4)} \n"
                    f"Deslocamento composto tangencial (F'i) [mm] --> Pinhão : {round(self.Par_engrenado_2.F_i_linha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.F_i_linha_coroa,4)} \n"
                    f"Salto tangencial (f'i) [mm] --> Pinhão : {round(self.Par_engrenado_2.f_i_linha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_2.f_i_linha_coroa,4)} \n"


                    "\n JOGO ENTRE FLANCOS (BACKLASH) 1 \n \n"

                    f"Jogo entre flancos teórico [mm] --> Mínimo : {round(self.Par_engrenado_1.jn1_min,4)} ; Máximo : {round(self.Par_engrenado_1.jn1_max,4)} \n"
                    f"Jogo entre flancos pela influência da tolerância entre centros [mm] --> Mínimo : {round(self.Par_engrenado_1.jn2_min,4)} ; Máximo : {round(self.Par_engrenado_1.jn2_max,4)} \n"
                    f"Jogo entre flancos pela influência do erro de cruzamento de eixos [mm] --> Mínimo : {round(self.Par_engrenado_1.jn3_min,4)} ; Máximo : {round(self.Par_engrenado_1.jn3_max,4)} \n"
                    f"Jogo entre flancos pela influência dos erros individuais do dentado [mm] --> Mínimo : {round(self.Par_engrenado_1.jn4_min,4)} ; Máximo : {round(self.Par_engrenado_1.jn4_max,4)} \n"
                    f"Jogo entre flancos pela influência da excentricidade dos mancais [mm] --> Mínimo : {round(self.Par_engrenado_1.jn5_min,4)} ; Máximo : {round(self.Par_engrenado_1.jn5_max,4)} \n"
                    f"Jogo entre flancos pela  influência da elasticidade do conjunto [mm] --> Mínimo : {round(self.Par_engrenado_1.jn6_min,4)} ; Máximo : {round(self.Par_engrenado_1.jn6_max,4)} \n"
                    f"Jogo entre flancos pela influência da  temperatura [mm] (Final) --> Mínimo : {round(self.Par_engrenado_1.jn7_min,4)} ; Máximo : {round(self.Par_engrenado_1.jn7_max,4)} \n"

                    "\n JOGO ENTRE FLANCOS (BACKLASH) 2 \n \n"

                    f"Jogo entre flancos teórico [mm] --> Mínimo : {round(self.Par_engrenado_2.jn1_min,4)} ; Máximo : {round(self.Par_engrenado_2.jn1_max,4)} \n"
                    f"Jogo entre flancos pela influência da tolerância entre centros [mm] --> Mínimo : {round(self.Par_engrenado_2.jn2_min,4)} ; Máximo : {round(self.Par_engrenado_2.jn2_max,4)} \n"
                    f"Jogo entre flancos pela influência do erro de cruzamento de eixos [mm] --> Mínimo : {round(self.Par_engrenado_2.jn3_min,4)} ; Máximo : {round(self.Par_engrenado_2.jn3_max,4)} \n"
                    f"Jogo entre flancos pela influência dos erros individuais do dentado [mm] --> Mínimo : {round(self.Par_engrenado_2.jn4_min,4)} ; Máximo : {round(self.Par_engrenado_2.jn4_max,4)} \n"
                    f"Jogo entre flancos pela influência da excentricidade dos mancais [mm] --> Mínimo : {round(self.Par_engrenado_2.jn5_min,4)} ; Máximo : {round(self.Par_engrenado_2.jn5_max,4)} \n"
                    f"Jogo entre flancos pela  influência da elasticidade do conjunto [mm] --> Mínimo : {round(self.Par_engrenado_2.jn6_min,4)} ; Máximo : {round(self.Par_engrenado_2.jn6_max,4)} \n"
                    f"Jogo entre flancos pela influência da  temperatura [mm] (Final) --> Mínimo : {round(self.Par_engrenado_2.jn7_min,4)} ; Máximo : {round(self.Par_engrenado_2.jn7_max,4)} \n"

                    "\n FATORES DE INFLUÊNCIA \n \n"

                    f"Fator de aplicação Ka --> Par 1 : {round(self.Par_engrenado_1.Ka,4)} ; Par 2 : {round(self.Par_engrenado_2.Ka,4)} \n"
                    f"Fator de carregamento de malha Ky --> Par 1 : {self.Par_engrenado_1.Ky} ; Par 2 : {self.Par_engrenado_2.Ky} \n"
                    f"Fator dinâmico Kv --> Par 1 :{round(self.Kv1,4)} ; Par 2 :{round(self.Kv2,4)} \n"
                    f"Zona de operação --> Par 1 : {self.zona1}; Par 2 : {self.zona2} \n"
                    f"Condição de Fator de distribuição longitudinal de carga de pressão (K_Hbeta) --> Par 1 : {self.Cond1} ; Par 2 : {self.Cond2} \n"
                    f"Fator de distribuição longitudinal de carga de pressão(K_Hbeta) --> Par 1 : {round(self.K_Hbeta1,4)}; Par 2 : {round(self.K_Hbeta2,4)} \n"
                    f"Fator de distribuição longitudinal de carga de flexão (K_Fbeta) --> Par 1 : {round(self.K_Fbeta1,4)}; Par 2 : {round(self.K_Fbeta2,4)} \n"
                    f"Fator de distribuição transversal de carga de pressão (K_Halpha) --> Par 1 : {round(self.K_Halpha1,4)} ; Par 2 : {round(self.K_Halpha2,4)} \n"
                    f"Fator de distribuição transversal de carga de flexão (K_Falpha) --> Par 1 : {round(self.K_Falpha1,4)} ; Par 2 : {round(self.K_Falpha2,4)} \n"
                    f"Fator de zona (Z_H) --> Par 1 : {round(self.Z_H1,4)} ; Par 2 : {round(self.Z_H2,4)} \n"
                    f"Fator de elasticidade (Z_E) --> Par 1 : {round(self.Z_E1,4)} ; Par 2 : {round(self.Z_E2,4)} \n"
                    f"Fator de recobrimento (Z_epsilon) --> Par 1 : {round(self.Z_epsilon1,4)} ; Par 2 : {round(self.Z_epsilon2,4)} \n"
                    f"Fator de ângulo de hélice (Z_beta) --> Par 1 : {round(self.Z_beta1,4)} ; Par 2 : {round(self.Z_beta2,4)} \n"
                    f"Fator de lubrificante (Z_L) --> Par 1 : {round(self.Z_L1,4)} ; Par 2 : {round(self.Z_L2,4)} \n"
                    f"Fator de velocidade (Z_V) --> Par 1 : {round(self.Z_V1,4)} ; Par 2 : {round(self.Z_V2,4)} \n"
                    f"Fator de rugosidade (Z_R) --> Par 1 : {round(self.Z_R1,4)} ; Par 2 : {round(self.Z_R2,4)} \n"
                    f"Fator de dureza de trabalho (Z_W) --> Par 1 : Pinhão : {round(self.Z_W1_pinhao,4)} , Coroa : {round(self.Z_W1_coroa,4)}  ; Pinhão : {round(self.Z_W2_pinhao,4)} , Coroa : {round(self.Z_W2_coroa,4)} \n"
                    f"Fator de tamanho (Z_X) --> Par 1 : Pinhão : {round(self.Z_X_pinhao1,4)} , Coroa : {round(self.Z_X_coroa1,4)}  ; Par 2 : Pinhão : {round(self.Z_X_pinhao2,4)} , Coroa : {round(self.Z_X_coroa2,4)} \n"
                    f"Fator de engrenamento individual - Pinhão (Z_B) --> Par 1 : {round(self.Z_B1,4)} ; Par 2 : {round(self.Z_B2,4)} \n"
                    f"Fator de engrenamento individual - Coroa (Z_D) --> Par 1 : {round(self.Z_D1,4)} ; Par 2 : {round(self.Z_D2,4)} \n"
                    f"Fator de vida útil sem pites (Z_NT) --> Par 1 : Pinhão : {round(self.Z_NT_pinhao1,4)} , Coroa : {round(self.Z_NT_coroa1,4)}  ; Par 2 : Pinhão : {round(self.Z_NT_pinhao2,4)} , Coroa : {round(self.Z_NT_coroa2,4)} \n"
                    f"Fator de vida útil com pites (Z_GT) --> Par 1 : Pinhão : {round(self.Z_GT_pinhao1,4)} , Coroa : {round(self.Z_GT_coroa1,4)}  ; Par 2 : Pinhão : {round(self.Z_GT_pinhao2,4)} , Coroa : {round(self.Z_GT_coroa2,4)} \n"
                    f"Fator de forma (Y_F) --> Par 1 : Pinhão : {round(self.Yf_pinhao1,4)} , Coroa : {round(self.Yf_coroa1,4)}  ; Par 2 : Pinhão : {round(self.Yf_pinhao2,4)} , Coroa : {round(self.Yf_coroa2,4)} \n"
                    f"Fator de correção de tensão (Y_S) --> Par 1 : Pinhão : {round(self.Y_S_pinhao1,4)} , Coroa : {round(self.Y_S_coroa1,4)}  ; Par 2 : Pinhão : {round(self.Y_S_pinhao2,4)} , Coroa : {round(self.Y_S_coroa2,4)} \n"
                    f"Fator de ângulo de hélice(Y_beta) --> Par 1 : {round(self.Y_beta1,4)} ; Par 2 :{round(self.Y_beta2,4)} \n"
                    f"Fator de espessura de aro (Y_B) --> Par 1 : Pinhão : {round(self.Y_B1_pinhao,4)} , Coroa : {round(self.Y_B1_coroa,4)}  ; Par 2 : Pinhão : {round(self.Y_B2_pinhao,4)} , Coroa : {round(self.Y_B2_coroa,4)} \n"
                    f"Fator de sensibilidade relativa (Y_delta,RelT) --> Par 1 : Pinhão : {round(self.Y_delta_RefT_pinhao1,4)} , Coroa : {round(self.Y_delta_RefT_coroa1,4)}  ; Par 2 : Pinhão : {round(self.Y_delta_RefT_pinhao2,4)} , Coroa : {round(self.Y_delta_RefT_coroa2,4)} \n"
                    f"Fator de condição superficial relativa da raiz (Y_R,RelT) --> Par 1 : Pinhão : {round(self.Y_R_RefT_pinhao1,4)} , Coroa : {round(self.Y_R_RefT_coroa1,4)}  ; Par 2 : Pinhão : {round(self.Y_R_RefT_pinhao2,4)} , Coroa : {round(self.Y_R_RefT_coroa2,4)} \n"
                    f"Fator de tamanho do dente (Y_X) --> Par 1 : Pinhão : {round(self.Y_X_pinhao1,4)} , Coroa : {round(self.Y_X_coroa1,4)}  ; Par 2 : Pinhão : {round(self.Y_X_pinhao2,4)} , Coroa : {round(self.Y_X_coroa2,4)} \n"
                    f"Fator de vida útil (Y_NT) --> Par 1 : Pinhão : {round(self.Y_NT_pinhao1,4)} , Coroa : {round(self.Y_NT_coroa1,4)}  ; Par 2 : Pinhão : {round(self.Y_NT_pinhao2,4)} , Coroa : {round(self.Y_NT_coroa2,4)} \n"


                    "\n TENSÕES \n \n"

                    f"Pressão de Hertz (sigma_H0) [Mpa] --> Par 1 : {round(self.sigma_H01,4)} ; Par 2 : {round(self.sigma_H02,4)} \n"
                    f"Tensão nominal de flexão (sigma_F0)  [Mpa] --> Par 1 : Pinhão : {round(self.sigma_F011,4)}, Coroa : {round(self.sigma_F021,4)} ; Par 2 : {round(self.sigma_F012,4)}, Coroa : {round(self.sigma_F022,4)}  \n"
                    f"Tensão efetiva de contato (sigma_H) [Mpa] --> Par 1 : Pinhão : {round(self.sigma_Hpinhao1,4)} , Coroa : {round(self.sigma_Hcoroa1,4)}  ; Par 2 : Pinhão : {round(self.sigma_Hpinhao2,4)} , Coroa : {round(self.sigma_Hcoroa2,4)} \n"
                    f"Tensão fletora efetiva no pé do dente (sigma_F) [Mpa] --> Par 1 : Pinhão : {round(self.sigma_Fpinhao1,4)} , Coroa : {round(self.sigma_Fcoroa1,4)}  ; Par 2 : Pinhão : {round(self.sigma_Fpinhao2,4)} , Coroa : {round(self.sigma_Fcoroa2,4)} \n"
                    f"Tensão adimissível de contato sem pites (sigma_HP) [Mpa] --> Par 1 : Pinhão : {round(self.sigma_HP_pinhao1,4)} , Coroa : {round(self.sigma_HP_coroa1,4)}  ; Par 2 : Pinhão : {round(self.sigma_HP_pinhao2,4)} , Coroa : {round(self.sigma_HP_coroa2,4)} \n"
                    f"Tensão adimissível de contato com pites (sigma_GP) [Mpa] --> Par 1 : Pinhão : {round(self.sigma_GP_pinhao1,4)} , Coroa : {round(self.sigma_GP_coroa1,4)}  ; Par 2 : Pinhão : {round(self.sigma_GP_pinhao2,4)} , Coroa : {round(self.sigma_GP_coroa2,4)} \n"
                    f"Tensão fletora adimissível (sigma_FP) [Mpa] --> Par 1 : Pinhão : {round(self.sigma_FP_pinhao1,4)} , Coroa : {round(self.sigma_FP_coroa1,4)}  ; Par 2 : Pinhão : {round(self.sigma_FP_pinhao2,4)} , Coroa : {round(self.sigma_FP_coroa2,4)} \n"

                    "\n COEFICIÊNTES DE SEGURANÇA \n \n"

                    f"Coeficiênte de segurança de falha por fadiga superficial --> Par 1 : Máximo {round(self.Par_engrenado_1.S_Hmax,4)} ; Mínimo : {round(self.Par_engrenado_1.S_Hmin,4)} ; Par 2 : Máximo {round(self.Par_engrenado_2.S_Hmax,4)} ; Mínimo : {round(self.Par_engrenado_2.S_Hmin,4)} \n"
                    f"Coeficiênte de segurança de falha por flexão --> Par 1 : Máximo {round(self.Par_engrenado_1.S_Fmax,4)} ; Mínimo : {round(self.Par_engrenado_1.S_Fmin,4)} ; Par 2 : Máximo {round(self.Par_engrenado_2.S_Fmax,4)} ; Mínimo : {round(self.Par_engrenado_2.S_Fmin,4)} \n"
                    f"Coeficiente de segurança de contato calculado para o caso sem pites (S_H) --> Par 1 : Pinhão : {round(self.S_Hpinhao1,4)} , Coroa : {round(self.S_Hcoroa1,4)}  ; Par 2 : Pinhão : {round(self.S_Hpinhao2,4)} , Coroa : {round(self.S_Hcoroa2,4)} \n"
                    f"Coeficiente de segurança de contato calculado para o caso com pites (S_G) --> Par 1 : Pinhão : {round(self.S_Gpinhao1,4)} , Coroa : {round(self.S_Gcoroa1,4)}  ; Par 2 : Pinhão : {round(self.S_Gpinhao2,4)} , Coroa : {round(self.S_Gcoroa2,4)} \n"
                    f"Coeficiente de segurança à flexão (S_F) --> Par 1 : Pinhão : {round(self.S_Fpinhao1,4)} , Coroa : {round(self.S_Fcoroa1,4)}  ; Par 2 : Pinhão : {round(self.S_Fpinhao2,4)} , Coroa : {round(self.S_Fcoroa2,4)} \n"

                    "\n VIDAS ÚTEIS NOMINAIS \n \n"

                    f"Vida nominal útil de contato calculada para o caso sem pites (VH) [hrs * 1e-03] --> Par 1 : Pinhão : {round(self.VH_pinhao1/1e03,4)} , Coroa : {round(self.VH_coroa1/1e03,4)}  ; Par 2 : Pinhão : {round(self.VH_pinhao2/1e03,4)} , Coroa : {round(self.VH_coroa2/1e03,4)} \n"
                    f"Vida nominal útil de contato calculada para o caso com pites (VH) [hrs * 1e-03] --> Par 1 : Pinhão : {round(self.VG_pinhao1/1e03,4)} , Coroa : {round(self.VG_coroa1/1e03,4)}  ; Par 2 : Pinhão : {round(self.VG_pinhao2/1e03,4)} , Coroa : {round(self.VG_coroa2/1e03,4)} \n"
                    f"Vida nominal útil à flexão (VF) [hrs * 1e-06] --> Par 1 : Pinhão : {round(self.VF_pinhao1/1e06,4)} , Coroa : {round(self.VF_coroa1/1e06,4)}  ; Par 2 : Pinhão : {round(self.VF_pinhao2/1e06,4)} , Coroa : {round(self.VF_coroa2/1e06,4)} \n"

                    "\n FORÇAS, TORQUES, ROTAÇÕES E POTÊNCIAS \n \n"

                    f"Torque de entrada [Nm] --> Par 1 : {round(self.Par_engrenado_1.T,4)} ; Par 2 : {round(self.Par_engrenado_2.T,4)} \n"
                    f"Torque de saída [Nm] --> Par 1 : {round(self.Par_engrenado_1.T_out,4)} ; Par 2 : {round(self.Par_engrenado_2.T_out,4)} \n"
                    f"Velocidade de entrada [Rpm] --> Par 1 : {round(self.Par_engrenado_1.n_t,4)} ; Par 2 : {round(self.Par_engrenado_2.n_t,4)} \n"
                    f"Rotação do porta-planetas [Rpm] --> {round(self.Par_engrenado_1.n_carrier,4)} \n"
                    f"Rotação relativa ao porta-planetas [Rpm] --> Par 1 : {round(self.Par_engrenado_1.n_rel,4)} ; Par 2 : {round(self.Par_engrenado_2.n_rel,4)} \n"
                    f"Engrenamentos por volta relativa --> Par 1 : Pinhão {self.Par_engrenado_1.contatos_pinhao} , Coroa {self.Par_engrenado_1.contatos_coroa} ; Par 2 : Pinhão {self.Par_engrenado_2.contatos_pinhao} , Coroa {self.Par_engrenado_2.contatos_coroa} \n"
                    f"Fator de carga alternada (Y_M) --> Par 1 : Pinhão {self.Par_engrenado_1.Y_M_pinhao} , Coroa {self.Par_engrenado_1.Y_M_coroa} ; Par 2 : Pinhão {self.Par_engrenado_2.Y_M_pinhao} , Coroa {self.Par_engrenado_2.Y_M_coroa} \n"
                    f"Velocidade de saída [Rpm] --> Par 1 : {round(self.Par_engrenado_1.n_t_out,4)} ; Par 2 : {round(self.Par_engrenado_2.n_t_out,4)} \n"
                    f"Potência de entrada [kW] --> Par 1 : {round(self.Par_engrenado_1.potencia,4)} ; Par 2 : {round(self.Par_engrenado_2.potencia,4)}  \n"
                    f"Potência estimada de saída  [kW] --> Par 1 : {round(self.P_21,4)} ; Par 2 : {round(self.P_22,4)} \n"
                    f"Eficiência do par engrenado --> Par 1 : {round(self.eficencia1 * 100,4)} % ; Par 2 : {round(self.eficencia2 *100,4)} % \n"
                    f"Velocidade tangencial do par [m/s] --> Par 1 : {round(self.Par_engrenado_1.v_t,4)} ; Par 2 : {round(self.Par_engrenado_2.v_t,4)} \n"
                    f"Força tangência [N] --> Par 1 : {round(self.Par_engrenado_1.Ft,4)} ; Par 2 : {round(self.Par_engrenado_2.Ft,4)} \n"
                    f"Força tangência no plano normal [N] --> Par 1 : {round(self.Par_engrenado_1.F_b,4)} ; Par 2 : {round(self.Par_engrenado_2.F_b,4)} \n"
                    f"Força tangência no plano normal sobre a linha de ação [N] -->  Par 1 : {round(self.Par_engrenado_1.F,4)} ; Par 2 : {round(self.Par_engrenado_2.F,4)} \n"
                    f"Força radial [N] --> Par 1 : {round(self.Par_engrenado_1.F_rd,4)} ; Par 2 : {round(self.Par_engrenado_2.F_rd,4)} \n"
                    f"Força axial [N] --> Par 1 : {round(self.Par_engrenado_1.F_ax,4)} ; Par 2 : {round(self.Par_engrenado_2.F_ax,4)} \n"
                    f"Carregamento específico [N//mm] --> Par 1 : {round(self.Par_engrenado_1.w,4)} ; Par 2 : {round(self.Par_engrenado_2.w,4)}  \n"

                    "\n TORQUES E POTÊNCIAS MÁXIMAS ADIMISSÍVEIS\n \n"

                    f"Torque máximo admissível à pressão sem pites (T_HP) [Nm] --> Par 1 : Pinhão : {round(self.T_HP11,4)} , Coroa : {round(self.T_HP21,4)} ; Par 2 : Pinhão : {round(self.T_HP12,4)} , Coroa : {round(self.T_HP22,4)} \n"
                    f"Capacidade admissível à pressão sem pites (P_HP) [kW] --> Par 1 : Pinhão : {round(self.P_HP11/1e03,4)} , Coroa : {round(self.P_HP21/1e03,4)} ; Par 2 : Pinhão : {round(self.P_HP12/1e03,4)} , Coroa : {round(self.P_HP22/1e03,4)} \n"
                    f"Torque máximo admissível à pressão com pites (T_GP) [Nm] --> Par 1 : Pinhão : {round(self.T_GP11,4)} , Coroa : {round(self.T_GP21,4)} ; Par 2 : Pinhão : {round(self.T_GP12,4)} , Coroa : {round(self.T_GP22,4)} \n"
                    f"Capacidade admissível à pressão com pites (P_GP) [kW] --> Par 1 : Pinhão : {round(self.P_GP11/1e03,4)} , Coroa : {round(self.P_GP21/1e03,4)} ; Par 2 : Pinhão : {round(self.P_GP12/1e03,4)} , Coroa : {round(self.P_GP22/1e03,4)} \n"
                    f"Torque máximo admissível à flexão (T_FP) [Nm] --> Par 1 : Pinhão : {round(self.T_FP11,4)} , Coroa : {round(self.T_FP21,4)} ; Par 2 : Pinhão : {round(self.T_FP12,4)} , Coroa : {round(self.T_FP22,4)} \n"
                    f"Capacidade admissível à flexão (P_FP) [kW] --> Par 1 : Pinhão : {round(self.P_FP11/1e03,4)} , Coroa : {round(self.P_FP21/1e03,4)} ; Par 2 : Pinhão : {round(self.P_FP12/1e03,4)} , Coroa : {round(self.P_FP22/1e03,4)} \n"

                    "\n AVISOS 1 \n \n"

                    "\n".join(self.Par_engrenado_1.AVISOS) + "\n"

                    "\n AVISOS 2 \n \n"

                    "\n".join(self.Par_engrenado_2.AVISOS) + "\n")


        elif self.Par_engrenado_2 == None :
            return ("\n RELATÓRIO DE DIMENSIONAMENTO DE PAR ENGRENADO  \n \n"

                    f"Apelido do modelo --> {self.Par_engrenado_1.apelido} \n"
                    f"Engenheiro --> {self.Proj} \n"
                    f"Tipo de interação --> {self.Par_engrenado_1.tipo} \n"
                    f"Tipo de transmissão --> {self.Par_engrenado_1.trans} \n"
                    f"Quantidade de planetas --> {self.Par_engrenado_1.N_cp} \n"
                    f"Tipo de planetárila --> {self.Tipo_planetario} \n"
                    f"Tipo de ring --> {self.Ring} \n"
                    f"Vida útil nominal requerida pelo egrenamento [horas] --> {round(self.Par_engrenado_1.Vr,4)} \n"
                    f"Grau de irregularida -->  Pinhão : {self.Par_engrenado_1.irregularidade_motora} ; Coroa : {self.Par_engrenado_1.irregularidade_movida}\n"
                    f"Temperatura dos engrenagens no instante de máxiam difernça de temperatura entre a caixa e as rodas [°C ] --> {round(self.Par_engrenado_1.T_Rmd,4)} \n"
                    f"Temperatura da caixa no instante de máxiam difernça de temperatura entre a caixa e as rodas [°C]  --> {round(self.Par_engrenado_1.T_Cmd,4)} \n"
                    f"Temperatura de operação [°C] --> {round(self.Par_engrenado_1.T_op,4)} \n"
                    f"Qualidade das engrenagens --> Pinhão : {self.Par_engrenado_1.IQ_pinhao} ; Coroa : {self.Par_engrenado_1.IQ_coroa} \n"
                    f"Qualidade do par engrenado --> {self.Par_engrenado_1.IQ} \n"
                    f"Rigidez máxima teórica --> {round(self.c_linha_th1,4)} \n"
                    f"Rigidez máxima --> {round(self.c_linha1,4)} \n"
                    f"Rigidez de malha alpha  --> {round(self.c_gamma_alpha1,4)} \n"
                    f"Rigidez de malha beta  --> {round(self.c_gamma_beta1,4)} \n"
                    f"Rotação crítica de ressonância [Rpm] --> {round(self.n_e1)} \n"

                    "\n MATERIAIS \n \n"

                    f"Material do pinhão \n \n {self.Par_engrenado_1.material_pinhao} \n"
                    f"Material da coroa \n \n {self.Par_engrenado_1.material_coroa} \n"

                    "\n FERRAMENTAS \n \n"

                    f"Ferramenta de usinagem do pinhão \n \n {self.Par_engrenado_1.ferramenta_pinhao} \n"
                    f"Ferramenta de usinagem da coroa \n \n {self.Par_engrenado_1.ferramenta_coroa} \n"
                    f"Raio de crista da ferramenta máximo [mm] --> Pinhão : {round(self.Par_engrenado_1.rk_pinhao_max,4)} ; Coroa : {round(self.Par_engrenado_1.rk_coroa_max,4)} \n"
                    f"Raio de crista da ferramenta [mm] --> Pinhão : {round(self.Par_engrenado_1.rk_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.rk_coroa,4)} \n"

                    "\n Lubrificantes \n \n"

                    f"{self.Par_engrenado_1.lubrificante} \n"
                    f"Volume de óleo [L] --> Máximo: {round(self.Par_engrenado_1.V_ls,4)} ; Mínimo : {round(self.Par_engrenado_1.V_li,4)} \n"
                    f"Profundidade de submersão [mm] --> Máximo: {round(self.Par_engrenado_1.P_rs,5)} ; Mínimo : {round(self.Par_engrenado_1.P_ri,4)} \n"

                    "\n CARACTERÍSTICAS GEOMÉTRICAS BÁSICAS \n \n"

                    f"Modulo normal do par [mm] --> {round(self.Par_engrenado_1.m_n,4)} \n"
                    f"Modulo transversal do par [mm] --> {round(self.Par_engrenado_1.m_t,4)} \n"
                    f"Modulo transversal de trabalho [mm]--> {round(self.Par_engrenado_1.m_wn,4)} \n"
                    f"Distância entre centros standart [mm] --> {round(self.Par_engrenado_1.a_standart,4)} \n"
                    f"Distância entre centros de trabalho (Imposta) [mm] --> {round(self.Par_engrenado_1.a,4)} \n"
                    f"Distância entre centros de trabalho (Calculada) [mm] --> {round(self.Par_engrenado_1.a_conferencia,4)} \n"
                    f"Tolerância da distância entre centros [mm] --> Superior : {round(self.Par_engrenado_1.Aa_s,4)} ; Inferior {round(self.Par_engrenado_1.Aa_i,4)} \n"
                    f"Número de dentes --> Pinhão : {self.Par_engrenado_1.Z_pinhao} ; Coroa : {self.Par_engrenado_1.Z_coroa} \n"
                    f"Número de dentes virtuais --> Pinhão : {round(self.Par_engrenado_1.zn_pinhao,4)}; Coroa : {round(self.Par_engrenado_1.zn_coroa,4)} \n"
                    f"Razão de engrenamento --> {round(self.Par_engrenado_1.u,4)}\n "
                    f"Comprimento dos dentes [mm] --> Pinhão : {round(self.Par_engrenado_1.b_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.b_coroa,4)}  \n"
                    f"Extenção de contato (Comprimento do dente em contato) [mm] --> {round(self.Par_engrenado_1.b,4)} \n"
                    f"Largura de calculo [mm] --> {round(self.b_cal1,4)} \n"
                    f"Ângulo de pressão normal [°] --> {round(self.Par_engrenado_1.alpha_n,4)} \n"
                    f"Ângulo de pressão transversal [°] --> {round(self.Par_engrenado_1.alpha_t,4)} \n"
                    f"Ângulo de pressão de trabalho normal [°] --> {round(self.Par_engrenado_1.alpha_wn,4)} \n"
                    f"Ângulo de pressão de trabalho transversal [°] --> {round(self.Par_engrenado_1.alpha_wt,4)} \n"
                    f"Ângulo de pressão normal sobre o diâmetro de referência deslocado [°] --> Pinhão :{round(self.Par_engrenado_1.alpha_vn_pinhao,4)}  ; Coroa : {round(self.Par_engrenado_1.alpha_vn_coroa,4)}  \n"
                    f"Ângulo de pressão transversal sobre o diâmetro de referência deslocado [°] --> Pinhão :{round(self.Par_engrenado_1.alpha_vt_pinhao,4)}  ; Coroa : {round(self.Par_engrenado_1.alpha_vt_coroa,4)}  \n"
                    f"Ângulo de hélice [°] --> {round(self.Par_engrenado_1.beta,4)} \n"
                    f"Ângulo de hélice sobre o circulo base [°] --> {round(self.Par_engrenado_1.beta_b,4)} \n"
                    f"Ângulo de hélice sobre o diâmetro de referência deslocado [°] --> Pinhão : {round(self.Par_engrenado_1.beta_v_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.beta_v_coroa,4)} \n"
                    f"Ângulo de hélice sobre o diâmetro primitivo [°] --> {round(self.Par_engrenado_1.beta_w_pinhao,4)} \n"
                    f"Diâmetro de referência [mm] --> Pinhão : {round(self.Par_engrenado_1.d_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_coroa,4)} \n"
                    f"Diâmetro primitivo [mm] --> Pinhão : {round(self.Par_engrenado_1.dw_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.dw_coroa,4)} \n"
                    f"Diâmetro de referência deslocado [mm] --> Pinhão : {round(self.Par_engrenado_1.d_pinhao_deslocado,4)} ; Coroa : {round(self.Par_engrenado_1.d_coroa_deslocado,4)} \n"
                    f"Diâmetro base [mm] --> Pinhão : {round(self.Par_engrenado_1.db_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.db_coroa,4)} \n"
                    f"Relação auxiliar ((x1+x2/z1+z2)) -->  {round(self.Par_engrenado_1.K,6)} \n"
                    f"Coeficiente de correção do blank --> {round(self.Par_engrenado_1.rel_aux,6)} \n"
                    f"Addendum real [mm] --> Pinhão : {round(self.Par_engrenado_1.h_a_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.h_a_coroa,4,)} \n"
                    f"Dedendum real [mm] --> Pinhão : {round(self.Par_engrenado_1.h_f_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.h_f_coroa,4,)} \n"
                    f"Altura do dente [mm] --> Pinhão : {round(self.Par_engrenado_1.h_dente_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.h_dente_coroa,4)} \n"
                    f"Diâmetro de cabeça [mm] --> Pinhão : {round(self.Par_engrenado_1.d_a_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_a_coroa,4)} \n"
                    f"Tolerância superior do diâmetro de cabeça [mm] --> Pinhão : {round(self.Par_engrenado_1.A_da_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.A_da_s_coroa,4)} \n"
                    f"Tolerância inferior do diâmetro de cabeça [mm] --> Pinhão : {round(self.Par_engrenado_1.A_da_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.A_da_i_coroa,4)} \n"
                    f"Diâmetro de pé [mm] --> Pinhão : {round(self.Par_engrenado_1.d_f_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_f_coroa,4)} \n"
                    f"Tolerância superior do diâmetro de pé [mm] --> Pinhão : {round(self.Par_engrenado_1.A_df_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.A_df_s_coroa,4)} \n"
                    f"Tolerância inferior do diâmetro de pé [mm] --> Pinhão : {round(self.Par_engrenado_1.A_df_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.A_df_i_coroa,4)} \n"
                    f"Folga no pé do dente [mm] --> Pinhão : {round(self.Par_engrenado_1.Cs_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Cs_coroa,4)} \n"
                    f"Folga superior no pé do dente [mm] --> Pinhão : {round(self.Par_engrenado_1.Css_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Css_coroa,4)} \n"
                    f"Folga inferior no pé do dente [mm] --> Pinhão : {round(self.Par_engrenado_1.Csi_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Csi_coroa,4)} \n"
                    f"Diâmetro de cabeça útil [mm] --> Pinhão : {round(self.Par_engrenado_1.d_na_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_na_coroa,4)} \n"
                    f"Diâmetro de pé útil [mm] --> Pinhão : {round(self.Par_engrenado_1.d_nf_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_nf_coroa,4)} \n"
                    f"Passo circular normal [mm] --> {round(self.Par_engrenado_1.pc_n,4)} \n"
                    f"Passo circular transversal [mm] --> Pinhão : {round(self.Par_engrenado_1.pc_t_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.pc_t_coroa,4)} \n"
                    f"Passo circular transversal primitivo [mm] --> Pinhão : {round(self.Par_engrenado_1.pc_tw_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.pc_tw_coroa,4)} \n"
                    f"Passo axial [mm] --> {round(self.Par_engrenado_1.p_x,4)} \n"
                    f"Passo base [mm] --> {round(self.Par_engrenado_1.pb,4)} \n"
                    f"Passo base axial [mm] --> {round(self.Par_engrenado_1.pb_x,4)} \n"
                    f"Somatório do deslocameno de perfil do pinhão e da coroa --> {round(self.Par_engrenado_1.sum_x,6)} \n"
                    f"Deslocamento de perfil --> Pinhão : {round(self.Par_engrenado_1.x_pinhao,6)} ; Coroa : {round(self.Par_engrenado_1.x_coroa,6)} \n"
                    f"Espessura do dente normal nominal [mm] --> Pinhão : {round(self.Par_engrenado_1.S_n_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_n_coroa,4)} \n"
                    f"Espessura superior do dente normal [mm] --> Pinhão : {round(self.Par_engrenado_1.S_ns_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_ns_coroa,4)} \n"
                    f"Espessura  inferior do dente normal  [mm] --> Pinhão : {round(self.Par_engrenado_1.S_ni_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_ni_coroa,4)} \n"
                    f"Espessura do dente normal transversal [mm] --> Pinhão : {round(self.Par_engrenado_1.S_t_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_t_coroa,4)} \n"
                    f"Espessura superior transversal do dente [mm] --> Pinhão : {round(self.Par_engrenado_1.S_ts_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_ts_coroa,4)} \n"
                    f"Espessura inferior transversal do dente [mm]  [mm] --> Pinhão : {round(self.Par_engrenado_1.S_ti_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_ti_coroa,4)} \n"
                    f"Espessura da cabeça do dente sem o chanfro normal nominal [mm] --> Pinhão : {round(self.Par_engrenado_1.S_na_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_na_coroa,4)} \n"
                    f"Espessura da cabeça do dente sem o chanfro superior normal [mm] --> Pinhão : {round(self.Par_engrenado_1.S_na_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_na_s_coroa,4)} \n"
                    f"Espessura da cabeça do dente sem o chanfro inferior normal [mm] --> Pinhão : {round(self.Par_engrenado_1.S_na_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.S_na_i_coroa,4)} \n"
                    f"Espessura da cabeça do dente com o chanfro normal nominal [mm] --> Pinhão : {round(self.Par_engrenado_1.s_nk_pinhao,4)} ; Coroa {round(self.Par_engrenado_1.s_nk_coroa,4)} \n"
                    f"Espessura da cabeça do dente com o chanfro superior normal [mm] --> Pinhão : {round(self.Par_engrenado_1.s_nk_s_pinhao,4)} ; Coroa {round(self.Par_engrenado_1.s_nk_s_coroa,4)} \n"
                    f"Espessura da cabeça do dente com o chanfro inferior normal [mm] --> Pinhão : {round(self.Par_engrenado_1.s_nk_i_pinhao,4)} ; Coroa {round(self.Par_engrenado_1.s_nk_i_coroa,4)} \n"
                    f"Dimensão do vão normal [mm] --> Pinhão : {round(self.Par_engrenado_1.T_n_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.T_n_coroa,4)} \n"
                    f"Dimensão superior normal do vão [mm] --> Pinhão : {round(self.Par_engrenado_1.T_ns_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.T_ns_coroa,4)} \n"
                    f"Dimensão inferior normal do vão [mm] --> Pinhão : {round(self.Par_engrenado_1.T_ni_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.T_ni_coroa,4)} \n"
                    f"Dimensão do vão transversal [mm] --> Pinhão : {round(self.Par_engrenado_1.T_t_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.T_t_coroa,4)} \n"
                    f"Dimensão superior transversal do vão  [mm] --> Pinhão : {round(self.Par_engrenado_1.T_ts_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.T_ts_coroa,4)} \n"
                    f"Dimensão inferior transversal do vão [mm] --> Pinhão : {round(self.Par_engrenado_1.T_ti_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.T_ti_coroa,4)} \n"
                    f"Ângulo de chanfro na seção normal [°] --> Pinhão : {round(self.Par_engrenado_1.phi_na_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.phi_na_coroa,4)} \n"
                    f"Ângulo de chanfro na seção transversal [°] --> Pinhão : {round(self.Par_engrenado_1.phi_ta_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.phi_ta_coroa,4)} \n"
                    f"Comprimento de chanfro [mm] --> Pinhão : {round(self.Par_engrenado_1.C_a_pinhao,4)} ; Coroa {round(self.Par_engrenado_1.C_a_coroa,4)} \n"
                    f"Diâmetro de início de chanfro [mm] --> Pinhão : {round(self.Par_engrenado_1.d_nk_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_nk_coroa,4)} \n"
                    f"Tolerância superior do diâmetro de início de chanfro [mm] --> Pinhão : {round(self.Par_engrenado_1.A_dnk_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.A_dnk_s_coroa,4)} \n"
                    f"Tolerância inferior do diâmetro de início de chanfro [mm] --> Pinhão : {round(self.Par_engrenado_1.A_dnk_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.A_dnk_i_coroa,4)} \n"
                    f"Grau de recobrimento de perfil --> {round(self.Par_engrenado_1.epsilon_alpha,4)} \n"
                    f"Grau de recobrimento de hélice --> {round(self.Par_engrenado_1.epsilon_beta,4)} \n"
                    f"Grau de recobrimento de total --> {round(self.Par_engrenado_1.epsilon_total,4)} \n"
                    f"Velocidade de escorregamento de recesso [m/s] --> {round(self.Par_engrenado_1.v_ga,4)} \n"
                    f"Velocidade de escorregamento de acesso [m/s] --> {round(self.Par_engrenado_1.v_gf,4)}  \n"

                    "\n CARACTERÍSTICAS DO CORPO DA ENGRENAGEM E DOS MANCAIS \n \n"

                    f"Diâmetro de alma [mm]  --> Pinhão : {round(self.Par_engrenado_1.di_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.di_coroa,4)} \n"
                    f"Espessura de alma [mm] -->  Pinhão : {round(self.Par_engrenado_1.bs_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.bs_coroa,4)} \n"
                    f"Diâmetro do eixo [mm] --> Pinhão : {round(self.Par_engrenado_1.d_sh_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_sh_coroa,4)} \n"
                    f"Espessura entre diâmetro de alma e do diâmetro de pé [mm] --> Pinhão : {round(self.Par_engrenado_1.s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.s_coroa,4)} \n"
                    f"Distância entre os mancais [mm] --> Pinhao : {round(self.Par_engrenado_1.L_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.L_coroa,4)} \n"
                    f"Distância do centro dos mancais ao dentro da roda dentada [mm] --> Pinhão : {round(self.Par_engrenado_1.sh_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.sh_coroa,4)} \n"
                    f"Constante para a posição --> Pinhão : {round(self.Par_engrenado_1.K_linha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.K_linha_coroa,4)}\n"

                    "\n OPREÇÃO DE ACABAMENTO \n \n"

                    f"Operação de acabamento --> Pinhão :{self.Par_engrenado_1.op_acabamento_pinhao} ; Coroa : {self.Par_engrenado_1.op_acabamento_coroa} \n"
                    f"Sobremetal para acabamento [mm] --> Pinhão : {round(self.Par_engrenado_1.SM_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.SM_coroa,4)} \n"
                    f"Rugosidade média no flanco do dente [micrometro] --> Pinhão : {round(self.Par_engrenado_1.Ra_flanco_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Ra_flanco_coroa,4)} \n"
                    f"Altura máxima do perfil de rugosidade nos flancos do dente [micrometro] --> Pinhão : {round(self.Par_engrenado_1.Rz_flanco_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Rz_flanco_coroa,4)} \n"
                    f"Rugosidade média no pé do dente [micrometro] --> Pinhão : {round(self.Par_engrenado_1.Ra_pe_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Ra_pe_coroa,4)} \n"
                    f"Altura máxima do perfil de rugosidade no pé do dente [micrometro] --> Pinhão : {round(self.Par_engrenado_1.Rz_pe_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Rz_pe_coroa,4)} \n"
                    f"Qualidade das engrenagens --> Pinhão : {round(self.Par_engrenado_1.IQ_pinhao,1)} ; Coroa : {round(self.Par_engrenado_1.IQ_coroa,1)} \n"

                    "\n CONTROLE DE ESPESSURA DO DENTE \n \n"

                    f"Números de dentes seguidos a se medir --> Pinhão : {self.Par_engrenado_1.k_pinhao} ; Coroa : {self.Par_engrenado_1.k_coroa} \n"
                    f"Dimensão W superior [mm] --> Pinhão : {round(self.Par_engrenado_1.Wk_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Wk_s_coroa,4)} \n"
                    f"Dimensão W inferior [mm] --> Pinhão : {round(self.Par_engrenado_1.Wk_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Wk_i_coroa,4)} \n"
                    f"Diâmetro da esfera/rolo [mm] --> Pinhão : {round(self.Par_engrenado_1.Dm_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Dm_coroa,4)} \n"
                    f"Entre pinos/esferas superior [mm] --> Pinhão : {round(self.Par_engrenado_1.Md_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Md_s_coroa,4)} \n"
                    f"Entre pinos/esferas inferior [mm] --> Pinhão : {round(self.Par_engrenado_1.Md_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Md_i_coroa,4)} \n"
                    f"Diâmetro de tangência da esfera/pino superior [mm] --> Pinhão : {round(self.Par_engrenado_1.d_m_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_m_s_coroa,4)} \n"
                    f"Diâmetro de tangência da esfera/pino inferior [mm] --> Pinhão : {round(self.Par_engrenado_1.d_m_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.d_m_i_coroa,4)} \n"
                    f"Abaulameto superior do dente (Crown)[mm] --> Pinhão : {round(self.Par_engrenado_1.crwon_s_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.crwon_s_coroa,4)} \n"
                    f"Abaulameto inferior do dente (Crown)[mm] --> Pinhão : {round(self.Par_engrenado_1.crwon_i_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.crwon_i_coroa,4)} \n"

                    "\n MICROGEOMETRIA \n \n"

                    f"Desvio de concetricidade (Fr) [mm] --> Pinhão : {round(self.Par_engrenado_1.Fr_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Fr_coroa,4)} \n"
                    f"Flutuação nas espessuras dos dentes (Rs) [mm] --> Pinhão : {round(self.Par_engrenado_1.Rs_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Rs_coroa,4)} \n"
                    f"Desvio de passo individual (fp) [mm] --> Pinhão : {round(self.Par_engrenado_1.fp_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.fp_coroa,4)} \n"
                    f"Erro entre os passos consecutivos (fu) [mm] --> Pinhão : {round(self.Par_engrenado_1.fu_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.fu_coroa,4)} \n"
                    f"Erro total de passo (Fp) [mm] --> Pinhão : {round(self.Par_engrenado_1.Fp_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Fp_coroa,4)} \n"
                    f"Desvio de passo sobre k dentes consecutivos (Fpk) [mm] --> Pinhão : {round(self.Par_engrenado_1.Fpk_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Fpk_coroa,4)} \n"
                    f"Desvio de passo sobre uma fração de (z/8) dentes consecutivos (Fpk/8) [mm] --> Pinhão : {round(self.Par_engrenado_1.Fpk_8_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.Fpk_8_coroa,4)} \n"
                    f"Desvio de passo base normal (fpe) [mm] --> Pinhão : {round(self.Par_engrenado_1.fpe_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.fpe_coroa,4)} \n"
                    f"Desvio total na linha dos flancos (F_beta) [mm] --> Pinhão : {round(self.Par_engrenado_1.F_beta_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.F_beta_coroa,4)} \n"
                    f"Desvio angular na linha dos flancos (f_Hbeta) [mm] --> Pinhão : {round(self.Par_engrenado_1.f_Hbeta_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.f_Hbeta_coroa,4)} \n"
                    f"Desvio de forma na linha dos flancos (f_betaf) [mm] --> Pinhão : {round(self.Par_engrenado_1.f_betaf_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.f_betaf_coroa,4)} \n"
                    f"Desvio total de perfil envolvente (Ff) [mm] --> Pinhão : {round(self.Par_engrenado_1.F_f_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.F_f_coroa,4)} \n"
                    f"Desvio angular de perfil envolvente (F_Halpha) [mm] --> Pinhão : {round(self.Par_engrenado_1.f_Halpha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.f_Halpha_coroa,4)} \n"
                    f"Desvio de forma de perfil envolvente (ff) [mm] --> Pinhão : {round(self.Par_engrenado_1.f_f_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.f_f_coroa,4)} \n"
                    f"Deslocamento composto radial (F''i) [mm] --> Pinhão : {round(self.Par_engrenado_1.F_i_llinha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.F_i_llinha_coroa,4)} \n"
                    f"Salto radial (f''i) [mm] --> Pinhão : {round(self.Par_engrenado_1.f_i_llinha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.f_i_llinha_coroa,4)} \n"
                    f"Deslocamento composto tangencial (F'i) [mm] --> Pinhão : {round(self.Par_engrenado_1.F_i_linha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.F_i_linha_coroa,4)} \n"
                    f"Salto tangencial (f'i) [mm] --> Pinhão : {round(self.Par_engrenado_1.f_i_linha_pinhao,4)} ; Coroa : {round(self.Par_engrenado_1.f_i_linha_coroa,4)} \n"


                    "\n JOGO ENTRE FLANCOS (BACKLASH) \n \n"

                    f"Jogo entre flancos teórico [mm] --> Mínimo : {round(self.Par_engrenado_1.jn1_min,4)} ; Máximo : {round(self.Par_engrenado_1.jn1_max,4)} \n"
                    f"Jogo entre flancos pela influência da tolerância entre centros [mm] --> Mínimo : {round(self.Par_engrenado_1.jn2_min,4)} ; Máximo : {round(self.Par_engrenado_1.jn2_max,4)} \n"
                    f"Jogo entre flancos pela influência do erro de cruzamento de eixos [mm] --> Mínimo : {round(self.Par_engrenado_1.jn3_min,4)} ; Máximo : {round(self.Par_engrenado_1.jn3_max,4)} \n"
                    f"Jogo entre flancos pela influência dos erros individuais do dentado [mm] --> Mínimo : {round(self.Par_engrenado_1.jn4_min,4)} ; Máximo : {round(self.Par_engrenado_1.jn4_max,4)} \n"
                    f"Jogo entre flancos pela influência da excentricidade dos mancais [mm] --> Mínimo : {round(self.Par_engrenado_1.jn5_min,4)} ; Máximo : {round(self.Par_engrenado_1.jn5_max,4)} \n"
                    f"Jogo entre flancos pela  influência da elasticidade do conjunto [mm] --> Mínimo : {round(self.Par_engrenado_1.jn6_min,4)} ; Máximo : {round(self.Par_engrenado_1.jn6_max,4)} \n"
                    f"Jogo entre flancos pela influência da  temperatura [mm] (Final) --> Mínimo : {round(self.Par_engrenado_1.jn7_min,4)} ; Máximo : {round(self.Par_engrenado_1.jn7_max,4)} \n"

                    "\n FATORES DE INFLUÊNCIA \n \n"

                    f"Fator de aplicação Ka --> {round(self.Par_engrenado_1.Ka,4)} \n"
                    f"Fator de carregamento de malha Ky --> {self.Par_engrenado_1.Ky} \n"
                    f"Fator dinâmico Kv --> {round(self.Kv1,4)} \n"
                    f"Zona de operação --> {self.zona1} \n"
                    f"Fator de distribuição longitudinal de carga de pressão (K_Hbeta) --> {round(self.K_Hbeta1,4)} \n"
                    f"Fator de distribuição longitudinal de carga de flexão (K_Fbeta) --> {round(self.K_Fbeta1,4)} \n"
                    f"Fator de distribuição transversal de carga de pressão (K_Halpha) --> {round(self.K_Halpha1,4)} \n"
                    f"Fator de distribuição transversal de carga de flexão (K_Falpha) --> {round(self.K_Falpha1,4)} \n"
                    f"Fator de zona (Z_H) --> {round(self.Z_H1,4)} \n"
                    f"Fator de elasticidade (Z_E) --> {round(self.Z_E1,4)} \n"
                    f"Fator de recobrimento (Z_epsilon) --> {round(self.Z_epsilon1,4)} \n"
                    f"Fator de ângulo de hélice (Z_beta) --> {round(self.Z_beta1,4)} \n"
                    f"Fator de lubrificante (Z_L) --> {round(self.Z_L1,4)} \n"
                    f"Fator de velocidade (Z_V) --> {round(self.Z_V1,4)} \n"
                    f"Fator de rugosidade (Z_R) --> {round(self.Z_R1,4)} \n"
                    f"Fator de dureza de trabalho (Z_W) --> Pinhão : {round(self.Z_W1_pinhao,4)} , Coroa : {round(self.Z_W1_coroa,4)} \n"
                    f"Fator de tamanho (Z_X) --> Pinhão : {round(self.Z_X_pinhao1,4)} , Coroa : {round(self.Z_X_coroa1,4)} \n"
                    f"Fator de engrenamento individual - Pinhão (Z_B) --> {round(self.Z_B1,4)} \n"
                    f"Fator de engrenamento individual - Coroa (Z_D) --> {round(self.Z_D1,4)} \n"
                    f"Fator de vida útil sem pites (Z_NT) --> Pinhão : {round(self.Z_NT_pinhao1,4)} , Coroa : {round(self.Z_NT_coroa1,4)} \n"
                    f"Fator de vida útil com pites (Z_GT) --> Pinhão : {round(self.Z_GT_pinhao1,4)} , Coroa : {round(self.Z_GT_coroa1,4)} \n"
                    f"Fator de forma (Y_F) --> Pinhão : {round(self.Yf_pinhao1,4)} , Coroa : {round(self.Yf_coroa1,4)} \n"
                    f"Fator de correção de tensão (Y_S) --> Pinhão : {round(self.Y_S_pinhao1,4)} , Coroa : {round(self.Y_S_coroa1,4)} \n"
                    f"Fator de ângulo de hélice(Y_beta) --> {round(self.Y_beta1,4)} \n"
                    f"Fator de correção de tensão (Y_B) --> Pinhão : {round(self.Y_B1_pinhao,4)} , Coroa : {round(self.Y_B1_coroa,4)} \n"
                    f"Fator de sensibilidade relativa (Y_delta,RelT) --> Pinhão : {round(self.Y_delta_RefT_pinhao1,4)} , Coroa : {round(self.Y_delta_RefT_coroa1,4)} \n"
                    f"Fator de condição superficial relativa da raiz (Y_R,RelT) --> Pinhão : {round(self.Y_R_RefT_pinhao1,4)} , Coroa : {round(self.Y_R_RefT_coroa1,4)} \n"
                    f"Fator de tamanho do dente (Y_X) --> Pinhão : {round(self.Y_X_pinhao1,4)} , Coroa : {round(self.Y_X_coroa1,4)} \n"
                    f"Fator de vida útil (Y_NT) --> Pinhão : {round(self.Y_NT_pinhao1,4)} , Coroa : {round(self.Y_NT_coroa1,4)} \n"


                    "\n TENSÕES \n \n"

                    f"Pressão de Hertz (sigma_H0) [Mpa] --> {round(self.sigma_H01,4)} \n"
                    f"Tensão nominal de flexão (sigma_F0)  [Mpa] --> Pinhão : {round(self.sigma_F011,4)}, Coroa : {round(self.sigma_F021,4)} \n"
                    f"Tensão efetiva de contato (sigma_H) [Mpa] --> Pinhão : {round(self.sigma_Hpinhao1,4)} , Coroa : {round(self.sigma_Hcoroa1,4)} \n"
                    f"Tensão fletora efetiva no pé do dente (sigma_F) [Mpa] --> Pinhão : {round(self.sigma_Fpinhao1,4)} , Coroa : {round(self.sigma_Fcoroa1,4)} \n"
                    f"Tensão adimissível de contato sem pites (sigma_HP) [Mpa] -->  Pinhão : {round(self.sigma_HP_pinhao1,4)} , Coroa : {round(self.sigma_HP_coroa1,4)} \n"
                    f"Tensão adimissível de contato com pites (sigma_GP) [Mpa] -->  Pinhão : {round(self.sigma_GP_pinhao1,4)} , Coroa : {round(self.sigma_GP_coroa1,4)} \n"
                    f"Tensão fletora adimissível (sigma_FP) [Mpa] --> Pinhão : {round(self.sigma_FP_pinhao1,4)} , Coroa : {round(self.sigma_FP_coroa1,4)} \n"

                    "\n COEFICIÊNTES DE SEGURANÇA \n \n"

                    f"Coeficiênte de segurança de falha por fadiga superficial --> Máximo {round(self.Par_engrenado_1.S_Hmax,4)} ; Mínimo : {round(self.Par_engrenado_1.S_Hmin,4)} \n"
                    f"Coeficiênte de segurança de falha por flexão --> Máximo {round(self.Par_engrenado_1.S_Fmax,4)} ; Mínimo : {round(self.Par_engrenado_1.S_Fmin,4)} \n"
                    f"Coeficiente de segurança de contato calculado para o caso sem pites (S_H) -->  Pinhão : {round(self.S_Hpinhao1,4)} , Coroa : {round(self.S_Hcoroa1,4)} \n"
                    f"Coeficiente de segurança de contato calculado para o caso com pites (S_G) -->  Pinhão : {round(self.S_Gpinhao1,4)} , Coroa : {round(self.S_Gcoroa1,4)} \n"
                    f"Coeficiente de segurança à flexão (S_F) --> Pinhão : {round(self.S_Fpinhao1,4)} , Coroa : {round(self.S_Fcoroa1,4)} \n"

                    "\n VIDAS ÚTEIS NOMINAIS \n \n"

                    f"Vida nominal de contato calculada para o caso sem pites (VH) [hrs * 1e-03] -->  Pinhão : {round(self.VH_pinhao1/1e03)} , Coroa : {round(self.VH_coroa1/1e03)} \n"
                    f"Vida nominal de contato calculada para o caso com pites (VH) [hrs * 1e-03] -->  Pinhão : {round(self.VG_pinhao1/1e03)} , Coroa : {round(self.VG_coroa1/1e03)} \n"
                    f"Vida nominal útil à flexão (VF) [hrs * 1e-06] --> Pinhão : {round(self.VF_pinhao1/1e06)} , Coroa : {round(self.VF_coroa1/1e06)} \n"

                    "\n FORÇAS, TORQUES, ROTAÇÕES E POTÊNCIAS \n \n"

                    f"Torque de entrada [Nm] --> {round(self.Par_engrenado_1.T,4)} \n"
                    f"Torque de saída [Nm] --> {round(self.Par_engrenado_1.T_out,4)} \n"
                    f"Velocidade de entrada [Rpm] --> {round(self.Par_engrenado_1.n_t,4)} \n"
                    f"Rotação relativa ao porta-planetas [Rpm] --> {round(self.Par_engrenado_1.n_rel,4)} \n"
                    f"Engrenamentos por volta relativa --> Pinhão {self.Par_engrenado_1.contatos_pinhao} , Coroa {self.Par_engrenado_1.contatos_coroa} \n"
                    f"Velocidade de saída [Rpm] --> {round(self.Par_engrenado_1.n_t_out,4)} \n"
                    f"Potência de entrada [kW] --> {round(self.Par_engrenado_1.potencia,4)} \n"
                    f"Potência estimada de saída [kW] --> {round(self.P_21,4)} \n"
                    f"Eficiência do par engrenado --> {round(self.eficencia1 * 100,4)} % \n"
                    f"Velocidade tangencial do par [m/s] --> {round(self.Par_engrenado_1.v_t,4)} \n"
                    f"Força tangência [N] --> {round(self.Par_engrenado_1.Ft,4)} \n"
                    f"Força tangência no plano normal [N] --> {round(self.Par_engrenado_1.F_b,4)} \n"
                    f"Força tangência no plano normal sobre a linha de ação [N] --> {round(self.Par_engrenado_1.F,4)} \n"
                    f"Força radial [N] --> {round(self.Par_engrenado_1.F_rd,4)} \n"
                    f"Força axial [N] --> {round(self.Par_engrenado_1.F_ax,4)} \n"
                    f"Carregamento específico [N//mm] --> {round(self.Par_engrenado_1.w,4)} \n"

                    "\n TORQUES E POTÊNCIAS MÁXIMAS ADIMISSÍVEIS\n \n"

                    f"Torque máximo admissível à pressão sem pites (T_HP) [Nm] --> Pinhão : {round(self.T_HP11,4)} , Coroa : {round(self.T_HP21,4)} \n"
                    f"Capacidade admissível à pressão sem pites (P_HP) [kW] --> Pinhão : {round(self.P_HP11/1e03,4)} , Coroa : {round(self.P_HP21/1e03,4)} \n"
                    f"Torque máximo admissível à pressão com pites (T_GP) [Nm] --> Pinhão : {round(self.T_GP11,4)} , Coroa : {round(self.T_GP21,4)} \n"
                    f"Capacidade admissível à pressão com pites (P_GP) [kW] --> Pinhão : {round(self.P_GP11/1e03,4)} , Coroa : {round(self.P_GP21/1e03,4)} \n"
                    f"Torque máximo admissível à flexão (T_FP) [Nm] --> Pinhão : {round(self.T_FP11,4)} , Coroa : {round(self.T_FP21,4)} \n"
                    f"Capacidade admissível à flexão (P_FP) [kW] --> Par 1 : Pinhão : {round(self.P_FP11/1e03,4)} , Coroa : {round(self.P_FP21/1e03,4)} \n"

                    "\n AVISOS \n \n"

                    "\n".join(self.Par_engrenado_1.AVISOS) + "\n")

    def salvar_em_PDF(self):
        caminho_pasta = "Relatórios Dimensionais"
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
        pdf.cell(0, 10, f"Relatório Dimensional {self.apelido} ", ln=True, align="C")
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
        nome_arquivo = f"Relatorio_de_dimensionamento_{self.apelido}.pdf"
        caminho_completo = os.path.join(caminho_pasta, nome_arquivo)
        pdf.output(caminho_completo, dest='F')
