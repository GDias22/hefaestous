# coding: utf-8
import numpy as np
import math
from scipy.optimize import newton
def KA(u,irregularidade_motora,irregularidade_movida):

    if irregularidade_motora == "Choque uniforme" :
        if irregularidade_movida =="Choque uniforme" :
            ka = 1.00
        elif irregularidade_movida =="Choque leve":
            ka = 1.25
        elif irregularidade_movida =="Choque moderado":
            ka = 1.50
        elif irregularidade_movida =="Choque pesado":
            ka = 1.75

    elif irregularidade_motora == "Choque leve" :
        if irregularidade_movida =="Choque uniforme" :
            ka = 1.10
        elif irregularidade_movida =="Choque leve":
            ka = 1.35
        elif irregularidade_movida =="Choque moderado":
            ka = 1.60
        elif irregularidade_movida =="Choque pesado":
            ka = 1.85

    elif irregularidade_motora == "Choque moderado" :
        if irregularidade_movida =="Choque uniforme" :
            ka = 1.25
        elif irregularidade_movida =="Choque leve":
            ka = 1.50
        elif irregularidade_movida =="Choque moderado":
            ka = 1.75
        elif irregularidade_movida =="Choque pesado":
            ka = 2.00

    elif irregularidade_motora == "Choque pesado" :
        if irregularidade_movida =="Choque uniforme" :
            ka = 1.50
        elif irregularidade_movida =="Choque leve":
            ka = 1.75
        elif irregularidade_movida =="Choque moderado":
            ka = 2.00
        elif irregularidade_movida =="Choque pesado":
            ka = 2.25

    if abs(u) < 1 :
        ka = ka*1.1

    return ka
def SM_acabamento(m_n,op_acabamento_pinhao,i_hob_pinhao,Z0_hob_pinhao,u_shaper_pinhao,op_acabamento_coroa,i_hob_coroa,Z0_hob_coroa,u_shaper_coroa,S_M_pinhao,S_M_coroa):

    if S_M_pinhao == None or S_M_coroa == None:
        if op_acabamento_pinhao == "Retificação":
            if i_hob_pinhao != None :
                if (i_hob_pinhao <= 15 and Z0_hob_pinhao <= 2) :
                    SM_pinhao = 0.069 * (m_n)**(1/3)
                elif (i_hob_pinhao > 15 and Z0_hob_pinhao <= 2) :
                    SM_pinhao = 0.060 * (m_n)**(1/3)
                elif  Z0_hob_pinhao >= 3:
                    SM_pinhao = 0.075 * (m_n)**(1/3)

            elif u_shaper_pinhao != None :
                if (u_shaper_pinhao < 2 and u_shaper_pinhao > 0)   :
                    SM_pinhao = 0.069 * (m_n)**(1/3)
                elif (u_shaper_pinhao >= 2 and u_shaper_pinhao < 2.3) :
                    SM_pinhao = 0.060 * (m_n)**(1/3)
                elif u_shaper_pinhao >= 2.3 :
                    SM_pinhao = 0.054 * (m_n)**(1/3)


        elif op_acabamento_pinhao == "Rasqueteamento":
            if i_hob_pinhao != None :
                if (i_hob_pinhao <= 15 and Z0_hob_pinhao <= 2) :
                    SM_pinhao = 0.023 * (m_n)**(1/3)
                elif (i_hob_pinhao > 15 and Z0_hob_pinhao <= 2) :
                    SM_pinhao = 0.020 * (m_n)**(1/3)
                elif  Z0_hob_pinhao >= 3:
                    SM_pinhao = 0.025 * (m_n)**(1/3)

            elif u_shaper_pinhao != None :
                if (u_shaper_pinhao < 2 and u_shaper_pinhao > 0)  :
                    SM_pinhao = 0.023 * (m_n)**(1/3)
                elif (u_shaper_pinhao >= 2 and u_shaper_pinhao < 2.3) :
                    SM_pinhao = 0.020 * (m_n)**(1/3)
                elif u_shaper_pinhao >= 2.3 :
                    SM_pinhao = 0.018 * (m_n)**(1/3)

        else :
            SM_pinhao = 0

        if op_acabamento_coroa == "Retificação":
            if i_hob_coroa != None :
                if (i_hob_coroa <= 15 and Z0_hob_coroa <= 2) :
                    SM_coroa = 0.069 * (m_n)**(1/3)
                elif (i_hob_coroa > 15 and Z0_hob_coroa <= 2):
                    SM_coroa = 0.060 * (m_n)**(1/3)
                elif  Z0_hob_coroa >= 3:
                    SM_coroa = 0.075 * (m_n)**(1/3)
            elif u_shaper_coroa != None :
                if (u_shaper_coroa < 2 and u_shaper_coroa > 0)  :
                    SM_coroa = 0.069 * (m_n)**(1/3)
                elif (u_shaper_coroa >= 2 and u_shaper_coroa < 2.3) :
                    SM_coroa = 0.060 * (m_n)**(1/3)
                elif u_shaper_coroa >= 2.3 :
                    SM_coroa = 0.054 * (m_n)**(1/3)

        elif op_acabamento_coroa == "Rasqueteamento":
            if i_hob_coroa != None :
                if (i_hob_coroa <= 15 and Z0_hob_coroa <= 2) :
                    SM_coroa = 0.023 * (m_n)**(1/3)
                elif (i_hob_coroa > 15 and Z0_hob_coroa <= 2)  :
                    SM_coroa = 0.020 * (m_n)**(1/3)
                elif  Z0_hob_coroa >= 3:
                    SM_coroa = 0.025 * (m_n)**(1/3)

            elif u_shaper_coroa != None :
                if  (u_shaper_coroa < 2 and u_shaper_coroa > 0)   :
                    SM_coroa = 0.023 * (m_n)**(1/3)
                elif (u_shaper_coroa >= 2 and u_shaper_coroa < 2.3) :
                    SM_coroa = 0.020 * (m_n)**(1/3)
                elif u_shaper_coroa >= 2.3 :
                    SM_coroa = 0.018 * (m_n)**(1/3)

        else :
            SM_coroa = 0


        if S_M_pinhao != None :
            SM_pinhao = S_M_pinhao
        if S_M_coroa != None :
            SM_coroa = S_M_coroa
    else :
        SM_pinhao = S_M_pinhao
        SM_coroa = S_M_coroa
    if 'SM_pinhao' not in locals() :
        SM_pinhao = 0
    if 'SM_coroa' not in locals() :
        SM_coroa = 0
    return SM_pinhao,SM_coroa

def pretuberancia_ferramenta(op_acabamento_pinhao,op_acabamento_coroa,SM_pinhao,SM_coroa):

    if op_acabamento_pinhao == "Retificação" or op_acabamento_pinhao =="Rasqueteamento" :
        pr_pinhao = 0.01 + SM_pinhao

    else :
        pr_pinhao = 0

    if op_acabamento_coroa == "Retificação" or op_acabamento_coroa =="Rasqueteamento" :
        pr_coroa = 0.01 + SM_coroa

    else :
        pr_coroa = 0
    return pr_pinhao,pr_coroa
def arranjo_fisico(d,d_sh,tipo,escolha):
    if tipo == 1 or tipo == 2:
        K_linha = 0
    elif tipo == 3 :
        if d/d_sh >= 1.15 :
            K_linha = 0.48
        elif d/d_sh < 1.15 :
            K_linha = 0.8
    elif tipo == 4 :
        if d/d_sh >= 1.15 :
            K_linha = -0.48
        elif d/d_sh < 1.15 :
            K_linha = -0.8
    elif tipo == 5 :
        if d/d_sh >= 1.15 :
            K_linha = 1.33
        elif d/d_sh < 1.15 :
            K_linha = 1.33
    elif tipo == 6 :
        if d/d_sh >= 1.15 :
            K_linha = -0.36
        elif d/d_sh < 1.15 :
            K_linha = -0.60
    elif tipo == 7 :
        if d/d_sh >= 1.15 :
            K_linha = -0.6
        elif d/d_sh < 1.15 :
            K_linha = -1.0
    elif tipo == None :
        K_linha = escolha


    return(K_linha)
def z_virt(Z_i,beta_b,beta):
    zn = Z_i/(math.cos(math.radians(beta_b))**2 * math.cos(math.radians(beta)))
    return zn
def dist_centros (Z_pinhao,Z_coroa,m_n,beta,alpha_t,alpha_tw) :
    a = ((m_n *(Z_pinhao + Z_coroa))/(2*math.cos(math.radians(beta))))*(math.cos(math.radians(alpha_t)))/(math.cos(math.radians(alpha_tw)))
    return a
def Tol_dist_centros(a,ISO):
    if abs(a) < 18:
        ai = 13.416
    elif abs(a) >= 18 and abs(a) < 30:
        ai = 23.238
    elif abs(a) >= 30 and abs(a) < 50:
        ai = 38.730
    elif abs(a) >= 50 and abs(a) < 80:
        ai = 63.246
    elif abs(a) >= 80 and abs(a) < 120:
        ai = 97.980
    elif abs(a) >= 120 and abs(a) < 180:
        ai = 146.969
    elif abs(a) >= 180 and abs(a) < 250:
        ai = 212.132
    elif abs(a) >= 250 and abs(a) < 315:
        ai = 280.624
    elif abs(a) >= 315 and abs(a) < 400:
        ai = 354.965
    elif abs(a) >= 400 and abs(a) < 500:
        ai = 447.214
    elif abs(a) >= 500 and abs(a) < 630:
        ai = 561.249
    elif abs(a) >= 630 and abs(a) < 800:
        ai = 709.930
    elif abs(a) >= 800 and abs(a) < 1000 :
        ai = 894.427
    elif abs(a) >= 1000 and abs(a) < 1250:
        ai = 1118.034
    elif abs(a) >= 1250 and abs(a) < 1600:
        ai = 1414.214
    elif abs(a) >= 1600 and abs(a) < 2000:
        ai = 1788.854
    elif abs(a) >= 2000 and abs(a) < 2500:
        ai = 2236.068
    elif abs(a) >= 2500 :
        ai = 2806.243

    if ISO == 5 :
        aj = 7
    elif ISO == 6 :
        aj = 10
    elif ISO == 7 :
        aj = 16
    elif ISO == 8 :
        aj = 25
    elif ISO == 9 :
        aj = 40
    elif ISO == 10 :
        aj = 64
    elif ISO == 11 :
        aj = 100

    A = 0.45*(ai)**(1/3)+(ai/1000)
    Aa = (aj*A)/2000
    Aa_s = Aa
    Aa_i = -Aa

    return Aa_s,Aa_i

def alpha_wt(Z_pinhao,Z_coroa,m_t,a,alpha_t):
    alpha_wt = math.acos((((Z_pinhao + Z_coroa)*m_t)/(2*a))* math.cos(math.radians(alpha_t)))
    return(math.degrees(alpha_wt))
def alpha_wn(alpha_wt,beta):
    alpha_wn = math.atan(math.tan(math.radians(alpha_wt)) * math.cos(math.radians(beta)))
    return math.degrees(alpha_wn)
def alpha_t(alpha_n,beta):
    alpha_t = math.atan(math.tan(math.radians(alpha_n))/math.cos(math.radians(beta)))
    return math.degrees(alpha_t)
def alpha_vn(Z_i,x,alpha_n,beta,beta_v):
    alpha_vn = math.acos((math.cos(math.radians(alpha_n)) * math.cos(math.radians(beta)))/(math.cos(math.radians(beta_v)) * (1+2*(x/Z_i)*math.cos(math.radians(beta)))))
    return(math.degrees(alpha_vn))
def alpha_vt(Z_i,alpha_t,x,beta):
    alpha_vt = math.acos((Z_i * math.cos(math.radians(alpha_t)))/(Z_i+2*x*math.cos(math.radians(beta))))
    return (math.degrees(alpha_vt))
def m_t(m_n,beta):
    m_t = m_n/math.cos(math.radians(beta))
    return(m_t)
def beta (m_n,n_t):
    beta = math.atan(((m_n*n_t)/50000)**0.555)
    return math.degrees(beta)
def beta_y(beta,dy,d):
    beta_y = math.atan(math.tan(math.radians(beta))* (dy/d))
    return(math.degrees(beta_y))
def beta_v(Z_i,x,beta):
    beta_v = math.atan(((Z_i + 2*x*math.cos(math.radians(beta)))/(Z_i))*math.tan(math.radians(beta)))
    return(math.degrees(beta_v))
def beta_b(alpha_n,beta):
    beta_b = math.asin(math.sin(math.radians(beta)) * math.cos(math.radians(alpha_n)))
    return(math.degrees(beta_b))
def beta_w(beta,dw,d):
    beta_w = math.atan(math.tan(math.radians(beta))* (dw/d))
    return(math.degrees(beta_w))
def diametro_ref(Z_i,m_n,beta):
    d = (m_n * Z_i)/math.cos(math.radians(beta))
    return d

def diametro_re_deloc(m_n,d,x):
    dv = d + 2*x*m_n
    return dv
def diametro_primi(Z_pinhao,Z_coroa,a):
    dw1 = (2*a)/(1+(Z_coroa/Z_pinhao))
    dw2 = dw1 *(Z_coroa/Z_pinhao)
    return dw1,dw2
def passo_circ_n(m_n):
    p_cn = m_n * math.pi
    return p_cn
def passo_circ_t(Z_i,d):
    p_ct = (d*math.pi)/Z_i
    return p_ct
def passo_circ_tw(Z_i,d_w):
    p_ctw = (d_w*math.pi)/Z_i
    return p_ctw
def passo_axial(m_n,beta):
    if beta == 0:
        p_x = 0
    else :
        p_x = (m_n * math.pi)/math.sin(math.radians(beta))
    return p_x
def passo_base(m_n,alpha_n):
    pb = m_n*math.pi*math.cos(math.radians(alpha_n))
    return pb
def passo_base_x(m_n,alpha_n,beta):
    if beta == 0:
        pbx = 0
    else :
        pbx = (m_n*math.pi*math.cos(math.radians(alpha_n)))/math.sin(math.radians(beta))
    return pbx
def diametro_base(d,alpha_t):
    db = d *math.cos(math.radians(alpha_t))
    return db
def desloc_perfil(Z_pinhao,Z_coroa,alpha_n,metodo,M_BS,Lambda,zn_1,zn_2,alpha_t,alpha_wt,u):
    if Z_coroa > 0 :
        inv_alpha_t = math.tan(math.radians(alpha_t)) - math.radians(alpha_t)
        inv_alpha_wt = math.tan(math.radians(alpha_wt)) - math.radians(alpha_wt)
        sum_x = (inv_alpha_wt-inv_alpha_t)/(2*math.tan(math.radians(alpha_n))) * (Z_pinhao +Z_coroa)
        if metodo == "DIN":
            z_nmed = (zn_1+zn_2)/2
            C = (z_nmed-20)/130
            A = [-0.196,-0.160,-0.120,-0.079,-0.036,0.008,0.054,0.102,0.153,0.210,0.272,0.341,0.417,0.500,0.590,0.685,0.784]
            B = [-4.632,-4.187,-3.735,-3.279,-2.823,-2.372,-1.932,-1.509,-1.109,-0.734,-0.387,-0.069,0.225,0.500,0.767,1.039,1.338]
            D = []
            for i in range(len(A)):
                D_i = A[i] - (A[i] - B[i])*C
                D.append(D_i)
                if D_i > (sum_x/2):
                    break
            if i == 0 :
                i = 1
                D.append(A[1] - (A[1] - B[1])*C)
            E = (((sum_x/2) - D[i-1])/(D[i]-D[i-1]))*(A[i] - A[i-1]) + A[i-1]
            F = (((sum_x/2) - D[i-1])/(D[i]-D[i-1]))*(B[i] - B[i-1]) + B[i-1]

            x_1 = (sum_x/2)-((F-E)/130) *(z_nmed - zn_1)
            x_2 = sum_x - x_1
            AVISO = None
        elif metodo == "BS" :
            if M_BS == "G":
                x_1 = (1/3) * (1-(1/u)) + sum_x/(1+u)
            elif M_BS == "F":
                x_1 = (1/2) * (1-(1/u)) + sum_x/(1+u)
            elif M_BS == "V":
                x_1 = (1/math.sqrt(zn_1)) * (1-(1/u)) + sum_x/(1+u)
            x_2 = sum_x - x_1
            AVISO = None
        elif metodo == "ISO" :
            x_1 = Lambda * ((u-1)/(u+1)) + sum_x/(u+1)
            x_2 = sum_x - x_1
            if Lambda < 0.5 or Lambda > 0.75 :
                AVISO = f"AVISO : O valor de lambada ({round(Lambda,3)}) está fora do intervalo recomedado ( 0.5 <= lambda <= 0.75) \n"
            else:
                AVISO = None
    elif Z_coroa < 0 :
        inv_alpha_t = math.tan(math.radians(alpha_t)) - math.radians(alpha_t)
        inv_alpha_wt = math.tan(math.radians(alpha_wt)) - math.radians(alpha_wt)
        sum_x = (inv_alpha_wt-inv_alpha_t)/(2*math.tan(math.radians(alpha_n))) * (Z_pinhao +Z_coroa)
        Z_coroa_abs = abs(Z_coroa)
        if Z_coroa_abs <= 40 :
            A = 0.0189
            B = 0.4369
            C = -0.0080
            D = 0.0750
        elif Z_coroa_abs > 40 and Z_coroa_abs <= 50 :
            A = 0.0159
            B = 0.5561
            C = -0.0061
            D = -0.0010
        elif Z_coroa_abs > 50 and Z_coroa_abs <= 55 :
            A = 0.0151
            B = 0.5956
            C = -0.0048
            D = -0.0660
        elif Z_coroa_abs > 55 and Z_coroa_abs <= 60 :
            A = 0.0175
            B = 0.4603
            C = -0.0050
            D = -0.0550
        elif Z_coroa_abs > 60 and Z_coroa_abs <= 65 :
            A = 0.0183
            B = 0.4147
            C = -0.0050
            D = -0.0550
        elif Z_coroa_abs > 65 and Z_coroa_abs <= 70 :
            A = 0.0087
            B = 1.0400
            C = -0.0014
            D = -0.2890
        elif Z_coroa_abs > 70 and Z_coroa_abs <= 75 :
            A = 0.0116
            B = 0.8084
            C = -0.0030
            D = -0.1770
        elif Z_coroa_abs > 75 and Z_coroa_abs <= 80 :
            A = 0.0021
            B = 1.5149
            C = -0.0014
            D = -0.2970
        elif Z_coroa_abs > 80 and Z_coroa_abs <= 90 :
            A = 0.0098
            B = 0.9037
            C = -0.0023
            D = -0.2250
        elif Z_coroa_abs > 90 and Z_coroa_abs <= 100 :
            A = 0.0109
            B = 0.8020
            C = -0.0025
            D = -0.2070
        elif Z_coroa_abs > 100 and Z_coroa_abs <= 110 :
            A = 0.0069
            B = 1.2080
            C = -0.0016
            D = -0.2970
        elif Z_coroa_abs > 110 and Z_coroa_abs <= 120 :
            A = 0.0043
            B = 1.4907
            C = -0.0011
            D = -0.3220
        elif Z_coroa_abs > 120 and Z_coroa_abs <= 140 :
            A = 0.0116
            B = 0.6147
            C = -0.0020
            D = -0.2440
        elif Z_coroa_abs > 140 and Z_coroa_abs <= 160 :
            A = 0.0086
            B = 1.0256
            C = -0.0015
            D = -0.3210
        elif Z_coroa_abs > 160 and Z_coroa_abs <= 200 :
            A = 0.0064
            B = 1.3788
            C = -0.0010
            D = -0.3970
        elif Z_coroa_abs > 200 and Z_coroa_abs <= 250 :
            A = 0.0046
            B = 1.7451
            C = -0.0007
            D = -0.4560
        elif Z_coroa_abs > 250 and Z_coroa_abs <= 400 :
            A = 0.0034
            B = 2.0371
            C = -0.0004
            D = -0.5293
        elif Z_coroa_abs > 400 and Z_coroa_abs <= 1000 :
            A = 0.0009
            B = 3.0454
            C = -0.0001
            D = -0.6460
        elif Z_coroa_abs > 1000 :
            A = 0.0000
            B = 4.8400
            C = 0.0000
            D = -0.8150
        E = C*abs(zn_2) + D
        x_1 = (A*abs(zn_2)+B)*zn_1**E
        x_2 = sum_x - x_1
        AVISO = None
    return sum_x,x_1,x_2,AVISO

def espessura_dente(m_n,alpha_n,x,d,afastamento,tol,A_Sne_min,A_Sne_max,beta):
    if A_Sne_min == None or A_Sne_max == None:
        d= abs(d)
        if d <=10 :
            Nb = 0
            Na = 0.242
        elif 10 < d and d <= 50 :
            Nb = 0.3
            Na = 0.484
        elif 50 < d and d <= 125 :
            Nb = 0.6
            Na = 0.726
        elif 125 < d and d <= 280 :
            Nb = 0.9
            Na = 0.968
        elif 280 < d and d <= 560 :
            Nb = 1.2
            Na = 1.210
        elif 560 < d and d <= 1000 :
            Nb = 1.5
            Na = 1.452
        elif 1000 < d and d <= 1600 :
            Nb = 1.8
            Na = 1.694
        elif 1600 < d and d <= 2500 :
            Nb = 2.1
            Na = 1.936
        elif 2500 < d and d <= 4000 :
            Nb = 2.4
            Na = 2.178
        elif 4000 < d and d <= 6300 :
            Nb = 2.7
            Na = 2.420
        elif 6300 < d and d <= 10000 :
            Nb = 3
            Na = 2.662

        if afastamento =="a":
            A_sne = 0.1*math.exp(Nb)
        elif afastamento == "ab" :
            A_sne = 0.083*math.exp(Nb)
        elif afastamento == "b" :
            A_sne = 0.07*math.exp(Nb)
        elif afastamento == "bc" :
            A_sne = 0.057*math.exp(Nb)
        elif afastamento == "c" :
            A_sne = 0.048*math.exp(Nb)
        elif afastamento == "cd" :
            A_sne = 0.04*math.exp(Nb)
        elif afastamento == "d" :
            A_sne = 0.033*math.exp(Nb)
        elif afastamento == "e" :
            A_sne = 0.022*math.exp(Nb)
        elif afastamento == "f" :
            A_sne = 0.010*math.exp(Nb)
        elif afastamento == "g" :
            A_sne = 0.005*math.exp(Nb)
        elif afastamento == "h" :
            A_sne = 0


        if tol == 21:
            T_sn = 1.77 * 1e-07 * math.exp(9.6894+Na)
        elif tol == 22:
            T_sn = 1.77 * 1e-07 * math.exp(10.1508+Na)
        elif tol == 23:
            T_sn = 1.77 * 1e-07 * math.exp(10.6122+Na)
        elif tol == 24:
            T_sn = 1.77 * 1e-07 * math.exp(11.0736+Na)
        elif tol == 25:
            T_sn = 1.77 * 1e-07 * math.exp(11.5350+Na)
        elif tol == 26:
            T_sn = 1.77 * 1e-07 * math.exp(11.9964+Na)
        elif tol == 27:
            T_sn = 1.77 * 1e-07 * math.exp(12.4578+Na)
        elif tol == 28:
            T_sn = 1.77 * 1e-07 * math.exp(12.9192+Na)
        elif tol == 29:
            T_sn = 1.77 * 1e-07 * math.exp(13.3806+Na)
        elif tol == 30:
            T_sn = 1.77 * 1e-07 * math.exp(13.8420+Na)
    elif A_Sne_min != None or A_Sne_max != None :
        A_sne = A_Sne_min
        T_sn = A_Sne_max - A_sne

    S_n = m_n * ((math.pi/2) + 2*x*math.tan(math.radians(alpha_n)))
    T_n = m_n * ((math.pi/2) - 2*x*math.tan(math.radians(alpha_n)))
    S_ns = S_n - A_sne
    T_ni = T_n + A_sne
    S_ni = S_ns - T_sn
    T_ns = T_ni + T_sn

    S_t =  S_n/math.cos(math.radians(beta))
    T_t =  T_n/math.cos(math.radians(beta))
    S_ts = S_ns/math.cos(math.radians(beta))
    T_ti = T_ni/math.cos(math.radians(beta))
    S_ti = S_ni/math.cos(math.radians(beta))
    T_ts = T_ns/math.cos(math.radians(beta))

    return S_n,S_ns,S_ni,T_n,T_ns,T_ni,A_sne,T_sn,S_t,S_ts,T_ti,T_t,S_ti,T_ts


def diam_cabeca2 (m_n,d,x,k_a,Q,K):
    # Correção do blank K (Henriot): encurta a cabeça em K·m para manter a folga de pé quando a ≠ a padrão.
    # x entra sempre com o sinal da convenção DIN (d, z e x2 da anelar com sinal). O K, porém, é um ENCURTAMENTO da cabeça:
    # na externa (d > 0) encurtar é diminuir d_a; na interna (d < 0) a cabeça aponta para dentro e encurtar é AUMENTAR |d_a|,
    # isto é, tornar d_a mais negativo. Antes o K era subtraído com o sinal da externa também na anelar, e a cabeça da anelar
    # saía 2·K·m mais LONGA (Ex. 6 da ISO/TR 6336-30: -1163,75 vs -1166,00 da norma; folga de pé 0,26 m em vez de 0,25 m).
    sgn = 1 if d > 0 else -1
    h_a = m_n*(k_a + x - K )
    d_a = d + 2*m_n*(k_a + x) - sgn*2*m_n*K
    A_da = 0.0007 * (0.45 * abs(d_a)**(1/3) + (abs(d_a)/1000)) * math.exp(0.45*Q)
    if d_a > 0 :
        A_da_i = -A_da
        A_da_s = 0
    elif d_a < 0 :
        A_da_i = 0
        A_da_s = A_da

    return h_a,d_a,A_da_i,A_da_s
def d_nk (m_n,Z_i,alpha_n,db,d_a,alpha_t,S_n,S_ns,S_ni,T_n,T_ns,T_ni,beta,f,x,ind):

    if Z_i > 0 :
        alpha_a = math.acos(db/d_a)
        inv_alpha_t = math.tan(math.radians(alpha_t)) - math.radians(alpha_t)
        inv_alpha_a = math.tan(alpha_a) - alpha_a
        A = S_n/(Z_i * m_n) + inv_alpha_t - inv_alpha_a
        A_s = S_ns/(Z_i * m_n) + inv_alpha_t - inv_alpha_a
        A_i = S_ni/(Z_i * m_n) + inv_alpha_t - inv_alpha_a
        S_na = (A * Z_i * math.cos(math.radians(alpha_t)) /math.cos(alpha_a)) * m_n
        S_na_s = (A_s * Z_i * math.cos(math.radians(alpha_t)) /math.cos(alpha_a)) * m_n
        S_na_i = (A_i * Z_i * math.cos(math.radians(alpha_t)) /math.cos(alpha_a)) * m_n
        if m_n * 0.275 > S_na:
            AVISO = f"AVISO : Espessura da cabeça sem chanfro nominal ({round(S_na,3)} mm) menor do que a mínima para o/a {ind} (Mínima = {round(m_n * 0.275,4)}) \n"
        elif m_n * 0.275 > S_na_s:
            AVISO = f"AVISO : Espessura da cabeça sem chanfro superior ({round(S_na_s,3)} mm) menor do que a mínima para o/a {ind} (Mínima = {round(m_n * 0.275,4)}) \n"
        elif m_n * 0.275 > S_na_i:
            AVISO = f"AVISO : Espessura da cabeça sem chanfro inferior ({round(S_na_i,3)} mm) menor do que a mínima para o/a {ind} (Mínima = {round(m_n * 0.275,4)}) \n"
        else:
            AVISO = None
        phi_na = round(math.degrees(math.radians(45) + 0.5*math.acos(db/d_a) - S_na_s/d_a))
        phi_ta = math.atan(math.tan(math.radians(phi_na))/math.cos(math.radians(beta)))
        C_a = f * (S_na_s/math.cos(math.radians(phi_na)))
        if f != 0 and (f < 0.125 or f > 0.2) :
            AVISO = (AVISO or "") + f"AVISO : Valor de f ({round(f,3)}) está fora do intervalo recomendado para o/a {ind} (0.125 <= f <= 0.2). Valor recomendado f = 0.15 \n"
        A = ((4*x *math.tan(math.radians(alpha_n)) + math.pi)/(2*Z_i)) + inv_alpha_t
        def d_nk_int(dnk):
            B = math.acos(db/dnk)
            B = math.tan(B) -B
            C = (180/math.pi)*(A-B)
            D = math.asin((dnk*math.sin(math.radians(C))-2*C_a*math.sin(math.radians(phi_na)))/(4*d_a))
            return dnk - math.sqrt(4*C_a**2 + d_a**2 - 4*C_a*d_a*math.cos(math.radians(phi_na)+D))
        d_nk = newton(d_nk_int, (d_a - 2*C_a),tol=0.0001, maxiter=100)
        if d_nk > d_a:
            AVISO = (AVISO or "") + f"AVISO : o valor de d_nk ({round(d_nk,3)} mm) está fora do limite superior para o/a {ind} (limite superior ={d_a} mm) \n"
        A_dnk = (S_ns - S_ni)/(1.25*math.sin(math.radians(alpha_n)))
        if Z_i > 0 :
            A_dnk_i = - A_dnk
            A_dnk_s = 0
        elif Z_i < 0 :
            A_dnk_i = 0
            A_dnk_s = A_dnk

    elif Z_i < 0 :
        alpha_a = math.acos(db/d_a)
        inv_alpha_t = math.tan(math.radians(alpha_t)) - math.radians(alpha_t)
        inv_alpha_a = math.tan(alpha_a) - alpha_a
        A = T_n/(abs(Z_i) * m_n) + inv_alpha_t - inv_alpha_a
        A_s = T_ns/(abs(Z_i) * m_n) + inv_alpha_t - inv_alpha_a
        A_i = T_ni/(abs(Z_i) * m_n) + inv_alpha_t - inv_alpha_a
        T_na = (A * abs(Z_i) * math.cos(math.radians(alpha_t)) /math.cos(alpha_a)) * m_n
        T_na_s = (A_s * abs(Z_i) * math.cos(math.radians(alpha_t)) /math.cos(alpha_a)) * m_n
        T_na_i = (A_i * abs(Z_i) * math.cos(math.radians(alpha_t)) /math.cos(alpha_a)) * m_n
        S_na = ((d_a*math.pi)/Z_i) - T_na
        S_na_s = ((d_a*math.pi)/Z_i) - T_na_s
        S_na_i = ((d_a*math.pi)/Z_i) - T_na_i
        if m_n * 0.275 > S_na:
            AVISO = f"AVISO : Espessura da cabeça sem chanfro nominal ({round(S_na,3)} mm) menor do que a mínima para o/a {ind} (Mínima = {round(m_n * 0.275,4)}) \n"
        elif m_n * 0.275 > S_na_s:
            AVISO = f"AVISO : Espessura da cabeça sem chanfro superior ({round(S_na_s,3)} mm) menor do que a mínima para o/a {ind} (Mínima = {round(m_n * 0.275,4)}) \n"
        elif m_n * 0.275 > S_na_i:
            AVISO = f"AVISO : Espessura da cabeça sem chanfro inferior ({round(S_na_i,3)} mm) menor do que a mínima para o/a {ind} (Mínima = {round(m_n * 0.275,4)}) \n"
        else:
            AVISO = None
        phi_na = round(math.degrees(math.radians(45) + 0.5*math.acos(db/d_a) - S_na_s/d_a))
        phi_ta = math.atan(math.tan(math.radians(phi_na))/math.cos(math.radians(beta)))
        C_a = f * (S_na_s/math.cos(math.radians(phi_na)))
        if f != 0 and (f < 0.125 or f > 0.2) :
            AVISO = (AVISO or "") + f"AVISO : Valor de f ({round(f,3)}) está fora do intervalo recomendado para o/a {ind} (0.125 <= f <= 0.2). Valor recomendado f = 0.15 \n"
        A = ((4*x *math.tan(math.radians(alpha_n)) + math.pi)/(2*Z_i)) + inv_alpha_t
        def d_nk_int(dnk):
            B = math.acos(db/dnk)
            B = math.tan(B) -B
            C = (180/math.pi)*(A-B)
            D = math.asin((dnk*math.sin(math.radians(C))-2*C_a*math.sin(math.radians(phi_na)))/(4*d_a))
            return dnk - math.sqrt(4*C_a**2 + d_a**2 - 4*C_a*d_a*math.cos(math.radians(phi_na)+D))
        d_nk = newton(d_nk_int, (d_a - 2*C_a),tol=0.0001, maxiter=100)
        d_nk = -d_nk
        if d_nk > d_a:
            AVISO = (AVISO or "") + f"AVISO : o valor de d_nk ({round(d_nk,3)} mm) está fora do limite superior para o/a {ind} (limite superior ={d_a} mm) \n"
        A_dnk = (S_ns - S_ni)/(1.25*math.sin(math.radians(alpha_n)))
        if Z_i > 0 :
            A_dnk_i = - A_dnk
            A_dnk_s = 0
        elif Z_i < 0 :
            A_dnk_i = 0
            A_dnk_s = A_dnk


    return S_na,S_na_s,S_na_i,phi_na,math.degrees(phi_ta),C_a,d_nk,A_dnk_i,A_dnk_s,AVISO
def S_nk(m_n,Z_i,db,d_nk,d_a,phi_ta,alpha_t,beta,S_n,S_ns,S_ni,ind):
    alpha_tNa = math.acos(db/d_nk)
    inv_alpha_t = math.tan(math.radians(alpha_t)) - math.radians(alpha_t)
    inv_alpha_tNa = math.tan(alpha_tNa) - alpha_tNa
    db_nk = d_a * (math.cos(math.radians(phi_ta) +(S_ns/(m_n*Z_i)) + inv_alpha_t - inv_alpha_tNa))
    delta_t = math.acos(db_nk/d_a)
    inv_delta_t = math.tan(delta_t) - delta_t
    gamma_t = math.acos(db_nk/d_nk)
    inv_gamma_t = math.tan(gamma_t) - gamma_t
    s_nk = d_a * math.cos(math.radians(beta))*(S_n/(m_n*Z_i) + inv_alpha_t - inv_alpha_tNa + inv_gamma_t - inv_delta_t)
    s_nk_s = d_a * math.cos(math.radians(beta))*(S_ns/(m_n*Z_i) + inv_alpha_t - inv_alpha_tNa + inv_gamma_t - inv_delta_t)
    s_nk_i = d_a * math.cos(math.radians(beta))*(S_ni/(m_n*Z_i) + inv_alpha_t - inv_alpha_tNa + inv_gamma_t - inv_delta_t)
    if m_n * 0.2 > s_nk:
        AVISO =f"AVISO : Espessura da cabeça com chanfro nominal ({round(s_nk,3)} mm) está menor do que a mínima para o/a {ind} (Mínima = {round(m_n * 0.2,3)} mm) \n"
    elif m_n * 0.2 > s_nk_s:
        AVISO =f"AVISO : Espessura da cabeça com chanfro superior ({round(s_nk_s,3)} mm) está menor do que a mínima para o/a {ind} (Mínima = {round(m_n * 0.2,3)} mm) \n"
    elif m_n * 0.2 > s_nk_i:
        AVISO =f"AVISO : Espessura da cabeça com chanfro inferior ({round(s_nk_i,3)} mm) está menor do que a mínima para o/a {ind} (Mínima = {round(m_n * 0.2,3)} mm) \n"
    else :
        AVISO = None

    return s_nk,s_nk_s,s_nk_i,AVISO
def diam_pe(m_n,alpha_n,x,d,f,T_sn,ind):
    h_f = m_n*(f - x)
    d_f = d - 2  *m_n*(f - x)
    A_df = ((1.2 * T_sn)/(math.sin(math.radians(alpha_n))))

    if d> 0:
        A_df_i = -A_df
        A_df_s = 0
    elif d< 0 :
        A_df_i = 0
        A_df_s = A_df
    return h_f,d_f,A_df_i,A_df_s
def folga_pe_dente(da_pinhao,A_da_i_pinhao,A_da_s_pinhao,df_pinhao,A_df_i_pinhao,A_df_s_pinhao,da_coroa,A_da_i_coroa,A_da_s_coroa,df_coroa,A_df_i_coroa,A_df_s_coroa,a,Aa_i,Aa_s):


    da_s_pinhao = da_pinhao + A_da_s_pinhao
    da_i_pinhao = da_pinhao + A_da_i_pinhao
    df_s_pinhao = df_pinhao + A_df_s_pinhao
    df_i_pinhao = df_pinhao + A_df_i_pinhao


    da_s_coroa = da_coroa + A_da_s_coroa
    da_i_coroa = da_coroa + A_da_i_coroa
    df_s_coroa = df_coroa + A_df_s_coroa
    df_i_coroa = df_coroa + A_df_i_coroa


    a_i = a + Aa_i
    a_s = a + Aa_s

    Csi_pinhao = (a_i) - ((df_s_pinhao)/2) - ((da_s_coroa)/2)
    Css_pinhao = (a_s) - ((df_i_pinhao)/2) - ((da_i_coroa)/2)

    Csi_coroa = (a_i) - ((da_s_pinhao)/2) - ((df_s_coroa)/2)
    Css_coroa = (a_s) - ((da_i_pinhao)/2) - ((df_i_coroa)/2)

    Cs_pinhao = a - (df_pinhao/2 + da_coroa/2 )
    Cs_coroa = a - (df_coroa/2 + da_pinhao/2 )

    if Csi_pinhao < 0 or Csi_coroa < 0 :
        AVISO = f"AVISO : Está havendo interferência entre os den tes das rodas (Folga inferior do pinhão [mm] : {Csi_pinhao} ; Folga inferior do coroa [mm] : {Csi_coroa} )"
    else :
        AVISO = None

    return Cs_pinhao,Csi_pinhao,Css_pinhao,Cs_coroa,Csi_coroa,Css_coroa,AVISO



def corre_blank(Z_pinhao,Z_coroa,x_1,x_2,beta,alpha_t,alpha_wt):

    K = (x_1+x_2) - (Z_pinhao+Z_coroa)/(2*math.cos(math.radians(beta))) * ((math.cos(math.radians(alpha_t))/math.cos(math.radians(alpha_wt))) - 1)

    rel_aux = (x_1+x_2)/(Z_pinhao+Z_coroa)

    return K, rel_aux
def diam_util_pe(Z_coroa,a,alpha_wt,d_nk_coroa,d_nk_pinhao,d_b_coroa,d_b_pinhao):

    d_nf_pinhao = math.sqrt((2*a*math.sin(math.radians(alpha_wt)) - (Z_coroa/abs(Z_coroa)) * math.sqrt(d_nk_coroa**2 - d_b_coroa**2))**2 + d_b_pinhao**2)

    d_nf_coroa =  (Z_coroa/abs(Z_coroa))  * math.sqrt((2*a*math.sin(math.radians(alpha_wt)) -  math.sqrt(d_nk_pinhao**2 - d_b_pinhao**2))**2 + d_b_coroa**2)

    return d_nf_pinhao,d_nf_coroa
def diam_util_cabeca(Z_coroa,d_b_pinhao,d_b_coroa,d_w_pinhao,d_w_coroa,d_util_pe_pinhao,d_util_pe_coroa):
    A = math.acos(d_b_pinhao/d_w_pinhao)
    B = math.pi - math.asin(d_w_pinhao * ((math.sin((math.pi/2)-A))/(d_util_pe_pinhao)))
    C = ((d_w_pinhao)/(2* math.sin(B))) * math.cos(A-B)
    d_na_coroa = (Z_coroa/abs(Z_coroa)) * math.sqrt(d_w_coroa**2 + 4*d_w_coroa*C*math.sin(A) + 4*C**2)

    A = math.acos(d_b_coroa/d_w_coroa)
    B = math.pi - math.asin(d_w_coroa * ((math.sin((math.pi/2)-A))/(d_util_pe_coroa)))
    C = ((d_w_coroa)/(2* math.sin(B))) * math.cos(A-B)
    d_na_pinhao = math.sqrt(d_w_pinhao**2 + 4*d_w_pinhao*C*math.sin(A) + 4*C**2)

    return d_na_pinhao,d_na_coroa
def falso_engrenamento(d_na,d_rk,ind):
    error = abs(d_na - d_rk)
    if error > 1e-03:
        a = f"AVISO : O {ind} apresenta falso engrenamento (diâmetro de inicio de chanfo = {round(d_rk,3)} mm / diâmetro útil de cabeça = {round(d_na,3)} mm) \n"
    else :
       a =  None
    return a
def interf_montagem_int(d_b_pinhao,d_b_coroa,d_a_pinhao,d_a_coroa,a,alpha_wt,u):
    phi = math.acos((d_a_coroa**2 - 4*a**2 - d_a_pinhao**2)/(4*d_a_pinhao*abs(a)))
    alpha_at1 = math.acos(d_b_pinhao/d_a_pinhao)
    inv_alpha_at1 = math.tan(alpha_at1) - alpha_at1
    inv_alpha_wt = math.tan(math.radians(alpha_wt)) - math.radians(alpha_wt)
    nu = inv_alpha_at1 - inv_alpha_wt
    theta = math.acos((d_a_coroa**2 + 4*a**2 - d_a_pinhao**2)/(4*d_a_coroa*a))
    alpha_at2 = math.acos(d_b_coroa/d_a_coroa)
    inv_alpha_at2 = math.tan(alpha_at2) - alpha_at2
    epsilon = inv_alpha_wt - inv_alpha_at2
    xi_1 = math.atan((1/d_b_pinhao) * math.sqrt((d_a_pinhao**2*d_b_coroa**2 - d_a_coroa**2*d_b_pinhao**2 )/(d_a_coroa**2 - d_a_pinhao**2)))
    xi_2 = ((xi_1 + nu)/abs(u)) + epsilon
    A = 0.5*(abs(d_a_coroa) * math.sin(xi_2) - d_a_pinhao*math.sin(xi_1))
    K = (phi + nu)/(abs(u)*(theta -epsilon))

    if K > 1 :
        av1 =  f' Não há interferência entre as cabeças das engrenagens internas e externas (K = {round(K,3)}) \n'
    elif K <= 1 :
        av1 =  f' Haverá interferência entre as cabeças das engrenagens internas e externas (K = {round(K,3)}) \n'

    if A <= 0 :
        av2 =  f' Não há possibilidade de montagem radial da engrenagem de dentes externos na engrenagem de dentes internos (A = {round(A,3)}) \n'
    elif A > 0 :
        av2 =  f' É possivel a montagem radial da engrenagem de dentes externos na engrenagem de dentes internos (A = {round(A,3)}) \n'

    return av1,av2
def Z_min(m_n,alpha_n,alpha_t,beta,h_fP,r_k,x,K) :
    # Número mínimo de dentes sem undercut (DIN 3960): adendo da ferramenta geradora h_aP0 = h_fP da roda.
    # O encurtamento de cabeça K da própria roda não entra.
    Z_min = (2*math.cos(math.radians(beta)) * (((m_n*h_fP - r_k*(1-math.sin(math.radians(alpha_n))))/m_n) - x))/(math.sin(math.radians(alpha_t))**2)
    return(math.ceil(Z_min))
def grau_recob_perfil (Z_coroa,m_n,alpha_n,d_b_pinhao,d_b_coroa,d_ucabeca_pinhao,d_ucabeca_coroa,alpha_wt,alpha_t):
    g_alpha = 0.5 *(math.sqrt(d_ucabeca_pinhao**2 - d_b_pinhao**2) + (Z_coroa/abs(Z_coroa)) * math.sqrt(d_ucabeca_coroa**2 - d_b_coroa**2) - (d_b_pinhao + d_b_coroa)*math.tan(math.radians(alpha_wt)))
    epsilon_alpha = (g_alpha * math.tan(math.radians(alpha_n)))/(m_n * math.pi * math.sin(math.radians(alpha_t)))
    return(epsilon_alpha)

def grau_recob_helice(m_n,b,beta):
    if beta != 0 :
        p_t = (m_n * math.pi)/math.cos(math.radians(abs(beta)))
        epsilon_beta = abs(b * math.tan(math.radians(beta)))/(p_t)
    else :
        epsilon_beta = 0
    return epsilon_beta
def grau_recob_total(epsilon_alpha,epsilon_beta):
    epsilon_total = epsilon_alpha + epsilon_beta
    return (epsilon_total)
def vel_escorregamento(Z_coroa,d_Na1,d_b1,d_Na2,d_b2,alpha_wt,u,n1):
    w = (n1*math.pi)/30000
    g_a = 0.5 * (math.sqrt(d_Na1**2 - d_b1**2) - d_b1 * math.tan(math.radians(alpha_wt)))
    g_f = 0.5 * ((Z_coroa/abs(Z_coroa)) * math.sqrt(d_Na2**2 - d_b2**2) - d_b2 * math.tan(math.radians(alpha_wt)))
    v_ga = w*g_a*(1+(1/u))
    v_gf = w*g_f*(1+(1/u))
    return(v_ga,v_gf)
def raio_crista_max(m_n,alpha_n,S_ns,d,d_f):
    A = (m_n *math.pi - S_ns)/(2*math.tan(math.radians(alpha_n)))
    B = (d-d_f)/2
    rk_max = (A-B)/((1/math.sin(math.radians(alpha_n))) - 1)
    return(rk_max)


def Yf_interno_rack(m_n, alpha_n, Z_i, x, d, d_f, d_na, beta, rho_fP, h_fP_star, S_pr = 0.0, d_load_n = None, rho_F_min_fator = 0.1):
    """Fator de forma de ENGRENAGEM INTERNA pela cremalheira equivalente (DIN 3990 / ISO 6336-3).
    O dente da cremalheira é o VÃO da anelar; o pé do dente da anelar fica na raiz da cremalheira (dedendo h_fP = h_fP*·m_n,
    canto do cortador rho_fP). Seção crítica na tangente a 30° com a linha de centro do dente; força com alpha_Fen = alpha_n aplicada
    em d_load_n (diâmetro da RODA VIRTUAL): ponta d_Na (método C) ou ponto exterior de engrenamento individual d_en (método B).
    Plano normal (roda virtual z_n). Devolve Yf, rho_F, h_Fe, S_Fn.
    Validado contra KISSsoft 2024 (método C; anelar z=150, m=3, x=-0.408: s_Fn 8.66 / h_Fe 6.58 / Y_F 1.58; helicoidal 20°: 8.78 / 6.56 / 1.53).
    rho_F = max(rho_fP, rho_F_min_fator·m_n): piso usado pelo KISSsoft (0.1 m_n) para canto de cortador quase vivo."""
    inv = lambda a: math.tan(a) - a
    al = math.radians(alpha_n)
    beta_b = math.asin(math.sin(math.radians(beta)) * math.cos(al))
    zn = abs(Z_i) / (math.cos(beta_b) ** 2 * math.cos(math.radians(beta)))
    dn = m_n * zn
    d_fn = dn + abs(d_f) - abs(d)                     # pé da roda virtual
    d_ln = (dn + abs(d_na) - abs(d)) if d_load_n is None else abs(d_load_n)   # diâmetro de aplicação da carga (virtual)
    d_bn = dn * math.cos(al)
    s_n = m_n * (math.pi / 2 + 2 * x * math.tan(al))  # espessura do dente da anelar na referência (x com sinal DIN)
    e_n = math.pi * m_n - s_n                         # vão na referência = dente da cremalheira equivalente
    h_fP = h_fP_star * m_n
    rho_F = max(rho_fP, rho_F_min_fator * m_n)
    S_Fn = e_n + 2 * (h_fP - rho_fP) * math.tan(al) + 2 * (rho_fP - S_pr) / math.cos(al) - 2 * rho_fP * math.cos(math.radians(30))
    alpha_ln = math.acos(d_bn / d_ln)
    s_ln = d_ln * (s_n / dn - inv(al) + inv(alpha_ln))          # espessura normal do dente da anelar no diâmetro de carga (cresce para a ponta)
    h_Fe = (d_fn - d_ln) / 2 - (s_ln / 2) * math.tan(al) - rho_F * (1 - math.sin(math.radians(30)))
    alpha_Fen = al
    Yf = (6 * (h_Fe / m_n) * math.cos(alpha_Fen)) / ((S_Fn / m_n) ** 2 * math.cos(al))
    return Yf, rho_F, h_Fe, S_Fn
def Yf_interno_cortador(m_n, alpha_n, Z_i, x, d, d_na, beta, z0, x0, h_fP_star, rho_a0, S_pr, epsilon_alpha, metodo = "B", theta_deg = 60.0, rho_F_min_fator = 0.1):
    """Fator de forma de ENGRENAGEM INTERNA pela geometria do pé gerada por PINHÃO-CORTADOR (ISO 6336-3:2019 §6.2.4 e §6.2.5,
    Eqs. 33–61). O filete é a trocoide descrita pelo canto arredondado (raio rho_a0) do cortador (z0 dentes, deslocamento x0,
    adendo h_aP0 = h_fP*·m_n) no engrenamento de geração com a anelar; a seção crítica é a tangente a theta = 60° com a linha
    de centro do dente (30° para dentado externo); rho_F é o raio de curvatura da trocoide nesse ponto (Euler-Savary, Eq. 60).
    A carga é aplicada em d_en (método B: ponto exterior de engrenamento individual, Eqs. 21–25) ou em d_Na (método C), com a
    linha de ação tangente ao círculo de base da roda virtual. Convenção de sinal negativo da anelar tratada em módulo.
    rho_F recebe o piso rho_F_min_fator·m_n (0,1 m_n, convenção do KISSsoft): com canto de cortador vivo (rho_a0 -> 0) a trocoide tem raio
    de curvatura muito pequeno na seção crítica e q_s sai da faixa 1 <= q_s < 8 em que o Y_S da ISO 6336-3 é válido. Y_F não depende de rho_F.
    Devolve Yf, rho_F, h_Fe, S_Fn (plano normal, roda virtual z_n). Exige z0; x0 = 0 e rho_a0 = 0 quando desconhecidos."""
    inv = lambda a: math.tan(a) - a
    al = math.radians(alpha_n)
    beta_b = math.asin(math.sin(math.radians(beta)) * math.cos(al))
    cb = math.cos(beta_b) ** 2 * math.cos(math.radians(beta))
    zn = abs(Z_i) / cb                                   # roda virtual (Eq. 16)
    z0v = z0 / cb                                        # cortador virtual (Eq. 33)
    dn = m_n * zn
    rbn = 0.5 * dn * math.cos(al)
    # engrenamento de geração cortador x anelar (Eqs. 34–40)
    inv_aw0 = inv(al) + 2 * (x + x0) * math.tan(al) / (z0v - zn)
    aw0 = al
    for _ in range(100):
        aw0 -= (inv(aw0) - inv_aw0) / math.tan(aw0) ** 2
    a0 = m_n * (zn - z0v) / 2 * math.cos(al) / math.cos(aw0)     # distância entre centros de geração (módulo)
    rw = a0 * zn / (zn - z0v)                                    # raio primitivo de geração da anelar
    rw0 = a0 * z0v / (zn - z0v)                                  # raio primitivo de geração do cortador
    rb0 = 0.5 * m_n * z0v * math.cos(al)
    # cortador (Eqs. 41–45): centro M do arredondamento da ponta
    ra0 = m_n * (z0v / 2 + h_fP_star + x0)
    rM = ra0 - rho_a0
    aM = math.acos(rb0 / rM)
    d_alpha = (0.5 * math.pi + 2 * x0 * math.tan(al)) / z0v + inv(al) - inv(aM) - (rho_a0 - S_pr) / rb0
    def ponto(psi):
        # psi = ângulo da linha de centros (anelar no centro; dente estudado no eixo +Y); rolamento interno sem escorregamento
        O0 = (a0 * math.sin(psi), a0 * math.cos(psi))
        P = (rw * math.sin(psi), rw * math.cos(psi))
        mu = math.pi / 2 - math.pi / z0v + d_alpha + psi * a0 / rw0
        M = (O0[0] + rM * math.cos(mu), O0[1] + rM * math.sin(mu))
        K = math.hypot(M[0] - P[0], M[1] - P[1])
        u = ((M[0] - P[0]) / K, (M[1] - P[1]) / K)                 # normal à trocoide (passa pelo polo P)
        F = (M[0] + rho_a0 * u[0], M[1] + rho_a0 * u[1])           # ponto do filete gerado
        return F, M, P, K, u
    def ang_tangente(psi, h = 1e-6):
        F1 = ponto(psi - h)[0]; F2 = ponto(psi + h)[0]
        return math.degrees(math.atan2(abs(F2[0] - F1[0]), abs(F2[1] - F1[1])))     # ângulo da tangente com o eixo do dente
    # fundo do vão = ponto de raio máximo; a partir dele procura-se a tangente a theta no flanco +X
    psi0 = max((i * 1e-3 for i in range(-400, 401)), key = lambda p: math.hypot(*ponto(p)[0]))
    sol = None
    for sgn in (1, -1):
        g_ant = ang_tangente(psi0) - theta_deg
        for i in range(1, 4000):
            p = psi0 + sgn * i * 2e-4
            g = ang_tangente(p) - theta_deg
            if (g_ant < 0) != (g < 0):
                a_, b_ = p - sgn * 2e-4, p
                for _ in range(80):
                    mid = 0.5 * (a_ + b_)
                    if (ang_tangente(a_) - theta_deg < 0) == (ang_tangente(mid) - theta_deg < 0):
                        a_ = mid
                    else:
                        b_ = mid
                cand = 0.5 * (a_ + b_)
                if ponto(cand)[0][0] > 0:
                    sol = cand
                    break
            g_ant = g
        if sol is not None:
            break
    if sol is None:
        raise ValueError("Yf_interno_cortador: seção crítica (tangente a %g°) não encontrada no filete gerado" % theta_deg)
    F, M, P, K, u = ponto(sol)
    X, Y = F
    S_Fn = 2 * X                                                  # Eq. 59
    # raio de curvatura da trocoide no ponto (Euler-Savary, Eq. 60) + raio do canto
    e_lc = (math.sin(sol), math.cos(sol))
    sin_zeta = abs(u[0] * e_lc[0] + u[1] * e_lc[1])
    R_es = rw * rw0 / (rw - rw0)
    rho_F = K ** 2 / (K + R_es * sin_zeta) + rho_a0
    rho_F = max(rho_F, rho_F_min_fator * m_n)                     # piso 0,1 m_n (KISSsoft) para canto de cortador quase vivo
    # ponto de aplicação da carga na roda virtual (Eqs. 21–25); interna: a espessura CRESCE para a ponta
    ran = 0.5 * (dn + abs(d_na) - abs(d))
    D = math.sqrt(ran ** 2 - rbn ** 2)
    eps_an = epsilon_alpha / math.cos(beta_b) ** 2
    E = (math.pi * abs(d) * math.cos(math.radians(beta)) * math.cos(al) / abs(Z_i)) * (eps_an - 1) if metodo == "B" else 0.0
    ren = math.sqrt((D + E) ** 2 + rbn ** 2)
    aen = math.acos(rbn / ren)
    gamma_e = (0.5 * math.pi + 2 * x * math.tan(al)) / zn - inv(al) + inv(aen)
    alpha_Fen = aen + gamma_e
    Y_carga = ren * (math.cos(gamma_e) + math.sin(gamma_e) * math.tan(alpha_Fen))   # Eq. 61 (ponto onde a linha de ação cruza o eixo do dente)
    h_Fe = Y - Y_carga
    Yf = (6 * (h_Fe / m_n) * math.cos(alpha_Fen)) / ((S_Fn / m_n) ** 2 * math.cos(al))
    return Yf, rho_F, h_Fe, S_Fn
def Yf(m_n,alpha_n,d,d_f,S_ns,pr,SM,rk,x,Z_i,beta,epsilon_alpha,d_nk,d_nf,T_ns,d_na,f,metodo = "B",z0_shaper = None,x0_shaper = 0.0,metodo_interno = "cortador"):
    # metodo: "B" = carga no ponto exterior de engrenamento individual (ISO 6336-3 método B, padrão)
    #         "C" = carga na ponta do dente (ISO 6336-3 método C / DIN 3990 "YF-C", usado pelo KISSsoft)
    # metodo_interno: "cortador" = pé gerado pelo pinhão-cortador z0 (ISO 6336-3 §6.2.4/6.2.5, padrão; cai em "rack" se z0 não for dado),
    #                 "rack" = cremalheira equivalente ao vão (DIN 3990, validado c/ KISSsoft), "legado" = formulação anterior

    if Z_i > 0 :
        hfp = f*m_n
        if pr == 0 :
            S_pr = 0
        else:
            S_pr = pr - SM
        epsilon = (math.pi/4) * m_n - hfp * math.tan(math.radians(alpha_n)) + (S_pr/math.cos(math.radians(alpha_n))) - (1-math.sin(math.radians(alpha_n))) * (rk/math.cos(math.radians(alpha_n)))
        A = x + ((rk-hfp)/m_n)
        beta_b = math.asin(math.sin(math.radians(beta)) * math.cos(math.radians(alpha_n)))
        zn = Z_i / (math.cos(beta_b)**2 *math.cos(math.radians(beta)))
        B = (2/zn) * ((math.pi/2) - (epsilon/m_n))  - math.pi/3
        def resp(C):
            return((2*A)/zn) * math.tan(C) - B - C
        Cc = newton(resp, math.pi/6,tol=1e-05, maxiter=300)
        S_fn = m_n*(zn * math.sin((math.pi/3) - Cc) + math.sqrt(3)*(((A)/(math.cos(Cc))) - (rk/m_n)))
        p_f = m_n*((rk/m_n) + ((2*(A**2))/(math.cos(Cc)*(zn*math.cos(Cc)**2 - 2*A))))
        epsilon_alpha_n = (epsilon_alpha)/(math.cos(beta_b)**2)
        dn = m_n * zn
        d_bn = dn * math.cos(math.radians(alpha_n))
        d_nkn = dn + d_nk - d
        D = math.sqrt((d_nkn/2)**2 - (d_bn/2)**2)
        E = ((math.pi * d * math.cos(math.radians(beta)) * math.cos(math.radians(alpha_n)))/abs(Z_i)) * (epsilon_alpha_n-1)
        if metodo == "C" :
            E = 0.0   # carga na ponta (d_Na)
        d_en = 2* (Z_i/abs(Z_i)) * math.sqrt(((D-E)**2 + (d_bn/2)**2))
        alpha_en = math.acos(d_bn/d_en)
        inv_alpha_en = math.tan(alpha_en) - alpha_en
        inv_alpha_n = math.tan(math.radians(alpha_n)) - math.radians(alpha_n)
        gamma_e = (S_ns/(m_n*zn)) + inv_alpha_n - inv_alpha_en
        alpha_Fen = alpha_en - gamma_e
        F = (math.cos(gamma_e) - math.sin(gamma_e) * math.tan(alpha_Fen))*(d_en/m_n)
        G = zn* math.cos(math.radians(60)-Cc)
        H = (rk/m_n) - (A/math.cos(Cc))
        h_fe = (m_n/2)* (F-G+H)
    elif Z_i < 0 and metodo_interno == "cortador" and z0_shaper not in (None, 0) :
        rho_a0 = rk if (rk != None and rk > 0) else 0.0
        S_pr_i = (pr - SM) if (pr != None and pr != 0) else 0.0
        return Yf_interno_cortador(m_n, alpha_n, Z_i, x, d, d_na, beta, z0_shaper, x0_shaper, f, rho_a0, S_pr_i, epsilon_alpha, metodo, 60.0)
    elif Z_i < 0 and metodo_interno in ("rack", "cortador") :
        rho_fP = rk if (rk != None and rk > 0) else 0.0
        S_pr_i = (pr - SM) if (pr != None and pr != 0) else 0.0
        d_load_n = None                                   # método C: carga na ponta d_Na
        if metodo == "B" :                                # método B: ponto exterior de engrenamento individual (roda virtual)
            beta_b = math.asin(math.sin(math.radians(beta)) * math.cos(math.radians(alpha_n)))
            zn = abs(Z_i) / (math.cos(beta_b)**2 * math.cos(math.radians(beta)))
            dn = m_n * zn
            d_bn = dn * math.cos(math.radians(alpha_n))
            d_nan = dn + abs(d_na) - abs(d)
            epsilon_alpha_n = epsilon_alpha / (math.cos(beta_b)**2)
            D = math.sqrt((d_nan/2)**2 - (d_bn/2)**2)
            E = ((math.pi * abs(d) * math.cos(math.radians(beta)) * math.cos(math.radians(alpha_n)))/abs(Z_i)) * (epsilon_alpha_n - 1)
            d_load_n = 2 * math.sqrt((D + E)**2 + (d_bn/2)**2)   # interna: ponta no menor raio -> ponto B/D além da ponta (D + E)
        Yf_i, p_f, h_fe, S_fn = Yf_interno_rack(m_n, alpha_n, Z_i, x, d, d_f, d_na, beta, rho_fP, f, S_pr_i, d_load_n)
        return Yf_i, p_f, h_fe, S_fn
    elif Z_i < 0 :
        beta_b = math.asin(math.sin(math.radians(beta)) * math.cos(math.radians(alpha_n)))
        zn = Z_i / (math.cos(beta_b)**2 *math.cos(math.radians(beta)))
        S_pr = pr - SM
        dn = m_n * zn
        d_bn = dn * math.cos(math.radians(alpha_n))
        d_fn = dn + d_f - d
        d_nan = dn + d_na - d
        epsilon_alpha_n = (epsilon_alpha)/(math.cos(beta_b)**2)
        D = math.sqrt((d_nan/2)**2 - (d_bn/2)**2)
        E = ((math.pi * d * math.cos(math.radians(beta)) * math.cos(math.radians(alpha_n)))/abs(Z_i)) * (epsilon_alpha_n-1)
        d_en = 2* (Z_i/abs(Z_i)) * math.sqrt(((D-E)**2 + (d_bn/2)**2))
        alpha_Fen = math.radians(alpha_n)
        hfp = f*m_n
        p_fp = (d_nf - d_f)/(2*(1-math.sin(math.radians(alpha_n))))
        p_f = p_fp/2
        S_fn = 2*(0.5*(dn*(math.pi/zn) - T_ns) +(hfp-p_fp)*math.tan(math.radians(alpha_n))+((p_fp - S_pr)/math.cos(math.radians(alpha_n)))-p_fp*math.cos(math.radians(30)))
        I = (d_en - d_fn)/(2*m_n)
        J = math.tan(math.radians(alpha_n))*(((1/(2*m_n))*(dn*(math.pi/zn) - T_ns))+math.tan(math.radians(alpha_n))*((hfp/m_n) -I))
        K = p_fp/(2*m_n)
        h_fe = m_n*(I-J-K)
    Yf =(((6*h_fe)/m_n)*math.cos(alpha_Fen))/(((S_fn/m_n)**2)*math.cos(math.radians(alpha_n)))
    return Yf,p_f,h_fe,S_fn

def Ft(T,d,Ky,N_cp,Tipo):
    # Força tangencial nominal por malha. Em planetário, T é o torque TOTAL no membro de entrada da malha
    # (sol para a malha externa; soma dos planetas para a malha interna) e Ft = 2000*T*K_gamma/(d*N_cp).
    if Tipo == "Planetário":
        if N_cp in (None, 0):
            N_cp = 1
        if Ky == None:
            Ky = 1
        Ft = (2000*T*Ky)/(abs(d)*N_cp)
    else :
        Ft = (2000*T)/abs(d)
    return Ft
def b_i(m_n,alpha_n,S_Fmin,f,Ft,h_fe,Yf,sigma_Flim):
    b_i = f*((Ft*S_Fmin*(h_fe/m_n)*math.cos(math.radians(alpha_n)))/(m_n*Yf*sigma_Flim))
    return b_i
def carreg_específico(Ft,Ka,b):
    w = (Ft*Ka)/b
    if w < 50 :
        AVISO = f"AVISO : O carregamento espefcífico está abaixo do recomendado (50 N/mm), o valor atual é de  {round(w,3)} N/mm \n"
    else :
        AVISO =None
    return w,AVISO
def S_min(d_a,d_f,di,eng,m_n):
    if d_a > 0 :
        h = ((d_a-d_f)/2)
        s = (-di + d_f)/2
        s_min = h*0.51
        s_recom = h*1.2
        if (s > s_min) and (s < s_recom)  :
            di_rec = d_f - 2*s_recom
            AVISO = f"AVISO : Região anelar do/da {eng} está mais fina do que o recomendado ({round(s_recom,3)}) mm, sendo que o valor atual é de {round(s,3)} mm, o valor recomendado possui um diâmetro de aro de {round(di_rec,3)} mm \n"
        elif s < s_min :
            di = d_f - 2*s_min
            di_rec = d_f - 2*s_recom
            AVISO = f"AVISO : Região anelar do/da {eng} está mais fina do que o mínimo ({round(s_min,3)}) mm, sendo que o valor atual é de {round(s,3)} mm, com isso ela será corrigida para o mínimo e o novo diâmetro de aro será {round(di,4)}, porém o diâmetro de aro recomendado é de {round(di_rec,3)} mm \n"
            s = s_min
        else :
            AVISO = None

    elif d_a < 0 :
        s = abs((-di + d_f))/2
        s_min = m_n*1.76
        s_recom = m_n*3.5
        if s> s_min and s < s_recom  :
            di_rec = d_f - 2*s_recom
            AVISO = f"AVISO : Região anelar do/da {eng} está mais fina do que o recomendado ({round(s_recom,3)}) mm, sendo que o valor atual é de {round(s,3)} mm, o valor recomendado possui um diâmetro de aro de {round(di_rec,3)} mm \n"
        elif s < s_min :
            di = d_f - 2*s_min
            di_rec = d_f - 2*s_recom
            AVISO = f"AVISO : Região anelar do/da {eng} está mais fina do que o mínimo ({round(s_min,3)}) mm, sendo que o valor atual é de {round(s,3)} mm, com isso ela será corrigida para o mínimo e o novo diâmetro de aro será {round(di,4)}, porém o diâmetro de aro recomendado é de {round(di_rec,3)} mm \n"
            s = s_min
        else :
            AVISO = None
    return di,s_min,s,AVISO
def fatores_modificadores_flancos(alpha_n,L,Z_pinhao,Z_coroa,T_Rmd,T_Cmd,d_sh_pinhao,a,Aa_i,Aa_s,beta,alpha_wt,bc,F_beta1,F_f1,f_p1,F_beta2,F_f2,f_p2,f_B,F_rd,C_Rdil1,C_Rdil2,C_Cdil):
    VT_Aa_min = 2*Aa_i *(math.tan(math.radians(alpha_n))/math.cos(math.radians(beta)))
    VT_Aa_max = 2*Aa_s *(math.tan(math.radians(alpha_n))/math.cos(math.radians(beta)))
    f_Sc = abs(Aa_s)
    VT_Ce_min = -((f_Sc * bc)/L)
    VT_Ce_max = ((f_Sc * bc)/L)
    VT_Ei1_min = math.sqrt((F_beta1/math.cos(math.radians(alpha_wt)))**2 + (F_f1/math.cos(math.radians(alpha_wt)))**2 + f_p1**2)
    VT_Ei2_min = math.sqrt((F_beta2/math.cos(math.radians(alpha_wt)))**2 + (F_f2/math.cos(math.radians(alpha_wt)))**2 + f_p2**2)
    VT_Ei1_max=VT_Ei1_min/2
    VT_Ei2_max=VT_Ei2_min/2
    VT_Ex_min = -2*f_B *(math.tan(math.radians(alpha_n))/math.cos(math.radians(beta)))
    VT_Ex_max = 2*f_B *(math.tan(math.radians(alpha_n))/math.cos(math.radians(beta)))
    I_eixo = (math.pi/64)*d_sh_pinhao**4          # momento de inércia do eixo [mm^4]
    fl = (F_rd * L**3)/(48 * 206000 * I_eixo)     # flecha de viga biapoiada com carga central [mm]

    if fl < 0 :
        VT_El_min = 2*fl *(math.tan(math.radians(alpha_n))/math.cos(math.radians(beta)))
        VT_El_max = 0
    elif fl > 0 :
        VT_El_max = 2*fl *(math.tan(math.radians(alpha_n))/math.cos(math.radians(beta)))
        VT_El_min = 0
    A1 = ((C_Rdil1 * Z_pinhao*a)/(Z_coroa + Z_pinhao)) * (T_Rmd - 20)
    A2 = ((C_Rdil2 * Z_coroa*a)/(Z_coroa +  Z_pinhao)) * (T_Rmd - 20)
    VT_Aq_min = 2*((T_Cmd - 20)*C_Cdil*a-(A1+A2)) * (math.tan(math.radians(alpha_n))/math.cos(math.radians(beta)))
    VT_Aq_max = VT_Aq_min

    return VT_Aa_min,VT_Aa_max,VT_Ce_min,VT_Ce_max,VT_Ei1_min,VT_Ei1_max,VT_Ei2_min,VT_Ei2_max,VT_Ex_min,VT_Ex_max,VT_El_min,VT_El_max,VT_Aq_min,VT_Aq_max
def jogo_flancos(beta,A_sne1,A_sne2,T_sn1,T_sn2,VT_Aa_min,VT_Aa_max,VT_Ce_min,VT_Ce_max,VT_Ei1_min,VT_Ei1_max,VT_Ei2_min,VT_Ei2_max,VT_Ex_min,VT_Ex_max,VT_El_min,VT_El_max,VT_Aq_min,VT_Aq_max):

    jn1_min = A_sne1+A_sne2
    jn1_max = A_sne1+T_sn1+A_sne2+T_sn2

    jn2_min = ((jn1_min/math.cos(math.radians(beta))) + VT_Aa_min ) * math.cos(math.radians(beta))
    jn2_max = ((jn1_max/math.cos(math.radians(beta))) + VT_Aa_max ) * math.cos(math.radians(beta))

    A = VT_Aa_min**2 + VT_Ce_min**2
    B = -VT_Aa_max**2 + VT_Ce_max**2
    jn3_min = ((jn1_min/math.cos(math.radians(beta))) - math.sqrt(A) ) * math.cos(math.radians(beta))
    if B > 0 :
        jn3_max = ((jn1_max/math.cos(math.radians(beta))) - math.sqrt(B) ) * math.cos(math.radians(beta))
    elif B < 0 :
        jn3_max = ((jn1_max/math.cos(math.radians(beta))) + math.sqrt(abs(B)) ) * math.cos(math.radians(beta))


    A = VT_Aa_min**2 + VT_Ce_min**2 + VT_Ei1_min**2 + VT_Ei2_min**2
    B = -VT_Aa_max**2 + VT_Ce_max**2 + VT_Ei1_max**2 + VT_Ei2_max**2
    jn4_min = ((jn1_min/math.cos(math.radians(beta))) - math.sqrt(A) ) * math.cos(math.radians(beta))
    if B > 0 :
        jn4_max = ((jn1_max/math.cos(math.radians(beta))) - math.sqrt(B) ) * math.cos(math.radians(beta))
    elif B < 0 :
        jn4_max = ((jn1_max/math.cos(math.radians(beta))) + math.sqrt(abs(B)) ) * math.cos(math.radians(beta))


    A = VT_Aa_min**2 + VT_Ce_min**2 + VT_Ei1_min**2 + VT_Ei2_min**2 + VT_Ex_min**2
    B = -VT_Aa_max**2 + VT_Ce_max**2 + VT_Ei1_max**2 + VT_Ei2_max**2 + VT_Ex_max**2
    jn5_min = ((jn1_min/math.cos(math.radians(beta))) - math.sqrt(A) ) * math.cos(math.radians(beta))
    if B > 0 :
        jn5_max = ((jn1_max/math.cos(math.radians(beta))) - math.sqrt(B) ) * math.cos(math.radians(beta))
    elif B < 0 :
        jn5_max = ((jn1_max/math.cos(math.radians(beta))) + math.sqrt(abs(B)) ) * math.cos(math.radians(beta))


    jn6_min = ((jn1_min/math.cos(math.radians(beta))) - math.sqrt(A) + VT_El_min ) * math.cos(math.radians(beta))
    if B > 0 :
        jn6_max = ((jn1_max/math.cos(math.radians(beta))) - math.sqrt(B) + VT_El_max ) * math.cos(math.radians(beta))
    elif B < 0 :
        jn6_max = ((jn1_max/math.cos(math.radians(beta))) + math.sqrt(abs(B)) + VT_El_max) * math.cos(math.radians(beta))


    jn7_min = ((jn1_min/math.cos(math.radians(beta))) - math.sqrt(A) + VT_El_min + VT_Aq_min) * math.cos(math.radians(beta))
    if B > 0 :
        jn7_max = ((jn1_max/math.cos(math.radians(beta))) - math.sqrt(B) + VT_El_max + VT_Aq_max) * math.cos(math.radians(beta))
    elif B < 0 :
        jn7_max = ((jn1_max/math.cos(math.radians(beta))) + math.sqrt(abs(B)) + VT_El_max + VT_Aq_max) * math.cos(math.radians(beta))

    return jn1_min,jn1_max,jn2_min,jn2_max,jn3_min,jn3_max,jn4_min,jn4_max,jn5_min,jn5_max,jn6_min,jn6_max,jn7_min,jn7_max
def dimensao_W(alpha_n,m_n,Z_i,x,S_ns,S_ni,beta,alpha_t,k_otimi):
    if k_otimi == None:
        if beta == 0 :
            # DIN 3960: k tal que o ponto de medição fique no diâmetro d_M = d + 2 x m_n (meio da altura útil);
            # k = z/pi*(tan(alpha_M) - inv(alpha_n)) - 2x tan(alpha_n)/pi + 0.5, com cos(alpha_M) = d_b/d_M; arredondado
            inv_alpha_n = math.tan(math.radians(alpha_n)) - math.radians(alpha_n)
            d_M = m_n*(abs(Z_i) + 2*x)
            alpha_M = math.acos(m_n*abs(Z_i)*math.cos(math.radians(alpha_n))/d_M)
            k = int(round(abs(Z_i)/math.pi*(math.tan(alpha_M) - inv_alpha_n) - 2*x*math.tan(math.radians(alpha_n))/math.pi + 0.5))
            k = max(k, 2)
        elif beta != 0 :
            if x == 0 :
                beta_b = math.asin(math.sin(math.radians(beta)) * math.cos(math.radians(alpha_n)))
                k = int(Z_i * (alpha_t/180 + (math.tan(math.radians(alpha_t)) * math.tan((beta_b))**2 )/math.pi) + 0.5)

            elif x!= 0 :
                A = 4*(x/Z_i) * math.cos(math.radians(beta)) * (1+(x/Z_i)*math.cos(math.radians(beta)))
                B = math.tan(math.radians(alpha_n))**2 + math.cos(math.radians(beta))**2
                C = math.cos(math.radians(beta))* (math.sin(math.radians(alpha_n))**2 + math.cos(math.radians(beta))**2 * math.cos(math.radians(alpha_n))**2)
                D = (Z_i/math.pi) * math.tan(math.radians(alpha_t)) + 2* x/math.pi * math.tan(math.radians(alpha_n))
                k_linha = Z_i * alpha_t/180 +0.5 + Z_i/math.pi *(math.sqrt(math.tan(math.radians(alpha_n))**2 + A*B))/C - D
                k = abs(int(k_linha + 0.5))

    elif k_otimi != None:
        k = abs(k_otimi)

    inv_alpha_t = math.tan(math.radians(alpha_t)) - math.radians(alpha_t)
    A = abs(Z_i) * inv_alpha_t + (k-1)*math.pi
    Wk_s = (A + (S_ns/m_n)) * m_n *math.cos(math.radians(alpha_n))
    Wk_i = (A + (S_ni/m_n)) * m_n *math.cos(math.radians(alpha_n))

    return k,Wk_s,Wk_i
def dimensao_M(alpha_n,m_n,Z_i,alpha_t,x,beta,S_ns,S_ni,T_ns,T_ni,d,d_b,Dim_sobre_pinos):

    inv_alpha_t = math.tan(math.radians(alpha_t)) - math.radians(alpha_t)
    inv_alpha_n = math.tan(math.radians(alpha_n)) - math.radians(alpha_n)
    Z_nw = Z_i* (inv_alpha_t/inv_alpha_n)
    beta_v = math.atan((Z_i+2*x*math.cos(math.radians(beta)))/Z_i * math.tan(math.radians(beta)))
    alpha_vn = math.acos((math.cos(math.radians(beta)) * math.cos(math.radians(alpha_n)))/ (math.cos(beta_v) * (1+2*(x/Z_i)*math.cos(math.radians(beta)))))
    k_DM = Z_nw/math.pi * (math.tan(alpha_vn) - 2*(x/Z_nw)*math.tan(math.radians(alpha_n)) - inv_alpha_n) + Z_i/(2*abs(Z_i))
    alpha_kn = 180*(k_DM + 0.5 - Z_i/(2*abs(Z_i)))/Z_nw

    if Dim_sobre_pinos == None:
        Dm = Z_nw * m_n * math.cos(math.radians(alpha_n)) * (math.tan(math.radians(alpha_kn)) - math.tan(alpha_vn))
        Dm_padrao = np.array([0.195,0.220,0.250,0.290,0.335,0.390,0.455,0.530,0.620,0.725,0.895,1.000,1.100,1.250,1.400,1.500,1.750,2.000,2.250,2.500,2.750,3.000,3.250,3.500,3.750,4.000,4.250,4.500,5.000,5.250,5.500,6.000,6.500,7.000,7.500,8.000,9.000,10.000,10.500,11.000,12.000,14.000,15.000,16.000,18.000,20.000,22.000,25.000,28.000,30.000,35.000,40.000,45.000,50.000,60.000,70.000,80.000,90.000,100.000,120.000])
        error = abs(Dm -Dm_padrao)
        indice_menor = np.argmin(error)
        Dm = Dm_padrao[indice_menor]

    elif Dim_sobre_pinos != None :
        Dm = Dim_sobre_pinos

    if Z_i > 0 :
        if beta == 0 :
            inv_alpha_k_s = (S_ns/d) + (Dm/d_b) + inv_alpha_n - (math.pi/Z_i)
            inv_alpha_k_i = (S_ni/d) + (Dm/d_b) + inv_alpha_n - (math.pi/Z_i)
            def find_alpha_k_s(alpha_k_s):
                return math.tan(math.radians(alpha_k_s)) - math.radians(alpha_k_s) - inv_alpha_k_s
            def find_alpha_k_i(alpha_k_i):
                return math.tan(math.radians(alpha_k_i)) - math.radians(alpha_k_i) - inv_alpha_k_i
            alpha_k_s = newton(find_alpha_k_s, alpha_n,tol=1.48e-08, maxiter=50)
            alpha_k_i = newton(find_alpha_k_i, alpha_n,tol=1.48e-08, maxiter=50)

            C_s = d_b/(2*math.cos(math.radians(alpha_k_s)))
            C_i = d_b/(2*math.cos(math.radians(alpha_k_i)))

            if Z_i % 2 == 0:
                Md_s = 2*C_s+Dm
                Md_i = 2*C_i+Dm
            elif Z_i % 2 != 0:
                Md_s = 2*C_s * math.cos(math.radians(90/Z_i))+Dm
                Md_i = 2*C_i* math.cos(math.radians(90/Z_i))+Dm

            alpha_m_s = math.atan(math.tan(math.radians(alpha_k_s)) - Dm/d_b)
            alpha_m_i = math.atan(math.tan(math.radians(alpha_k_i)) - Dm/d_b)

            d_m_s = d_b/ math.cos(alpha_m_s)
            d_m_i = d_b/ math.cos(alpha_m_i)


        if beta != 0 :
            As = (S_ns/(d* math.cos(math.radians(beta))))
            Ai = (S_ni/(d* math.cos(math.radians(beta))))
            beta_b = math.asin(math.sin(math.radians(beta))*math.cos(math.radians(alpha_n)))
            inv_alpha_k_s = As + (Dm/(d_b*math.cos(beta_b))) + inv_alpha_t - (math.pi/Z_i)
            inv_alpha_k_i = Ai + (Dm/(d_b*math.cos(beta_b))) + inv_alpha_t - (math.pi/Z_i)
            def find_alpha_k_s(alpha_k_s):
                return math.tan(math.radians(alpha_k_s)) - math.radians(alpha_k_s) - inv_alpha_k_s
            def find_alpha_k_i(alpha_k_i):
                return math.tan(math.radians(alpha_k_i)) - math.radians(alpha_k_i) - inv_alpha_k_i
            alpha_k_s = newton(find_alpha_k_s,alpha_n,tol=1.48e-08, maxiter=50)
            alpha_k_i = newton(find_alpha_k_i,alpha_n,tol=1.48e-08, maxiter=50)

            C_s = d_b/(2*math.cos(math.radians(alpha_k_s)))
            C_i = d_b/(2*math.cos(math.radians(alpha_k_i)))

            if Z_i % 2 == 0:
                Md_s = 2*C_s+Dm
                Md_i = 2*C_i+Dm
            elif Z_i % 2 != 0:
                Md_s = 2*C_s * math.cos(math.radians(90/Z_i))+Dm
                Md_i = 2*C_i* math.cos(math.radians(90/Z_i))+Dm

            alpha_m_s = math.atan(math.tan(math.radians(alpha_k_s)) - (Dm*math.cos(beta_b))/d_b)
            alpha_m_i = math.atan(math.tan(math.radians(alpha_k_i)) - (Dm*math.cos(beta_b))/d_b)

            d_m_s = d_b/ math.cos(alpha_m_s)
            d_m_i = d_b/ math.cos(alpha_m_i)

    elif Z_i < 0 :
        if beta == 0 :
            inv_alpha_k_s = (T_ns/d) - (Dm/d_b) + inv_alpha_n
            inv_alpha_k_i = (T_ni/d) - (Dm/d_b) + inv_alpha_n
            def find_alpha_k_s(alpha_k_s):
                return math.tan(math.radians(alpha_k_s)) - math.radians(alpha_k_s) - inv_alpha_k_s
            def find_alpha_k_i(alpha_k_i):
                return math.tan(math.radians(alpha_k_i)) - math.radians(alpha_k_i) - inv_alpha_k_i
            alpha_k_s = newton(find_alpha_k_s, alpha_n,tol=1.48e-08, maxiter=50)
            alpha_k_i = newton(find_alpha_k_i, alpha_n,tol=1.48e-08, maxiter=50)

            C_s = d_b/(2*math.cos(math.radians(alpha_k_s)))
            C_i = d_b/(2*math.cos(math.radians(alpha_k_i)))

            if abs(Z_i) % 2 == 0:
                Md_s = 2*C_s-Dm
                Md_i = 2*C_i-Dm
            elif abs(Z_i) % 2 != 0:
                Md_s = 2*C_s * math.cos(math.radians(90/abs(Z_i)))-Dm
                Md_i = 2*C_i* math.cos(math.radians(90/abs(Z_i)))-Dm

            alpha_m_s = math.atan(math.tan(math.radians(alpha_k_s)) + Dm/d_b)
            alpha_m_i = math.atan(math.tan(math.radians(alpha_k_i)) + Dm/d_b)

            d_m_s = d_b/ math.cos(alpha_m_s)
            d_m_i = d_b/ math.cos(alpha_m_i)


        if beta != 0 :
            As = (T_ns/(d* math.cos(math.radians(beta))))
            Ai = (T_ni/(d* math.cos(math.radians(beta))))
            beta_b = math.asin(math.sin(math.radians(beta))*math.cos(math.radians(alpha_n)))
            inv_alpha_k_s = As - (Dm/(d_b*math.cos(beta_b))) + inv_alpha_t
            inv_alpha_k_i = Ai - (Dm/(d_b*math.cos(beta_b))) + inv_alpha_t
            def find_alpha_k_s(alpha_k_s):
                return math.tan(math.radians(alpha_k_s)) - math.radians(alpha_k_s) - inv_alpha_k_s
            def find_alpha_k_i(alpha_k_i):
                return math.tan(math.radians(alpha_k_i)) - math.radians(alpha_k_i) - inv_alpha_k_i
            alpha_k_s = newton(find_alpha_k_s,alpha_n,tol=1.48e-08, maxiter=50)
            alpha_k_i = newton(find_alpha_k_i,alpha_n,tol=1.48e-08, maxiter=50)

            C_s = d_b/(2*math.cos(math.radians(alpha_k_s)))
            C_i = d_b/(2*math.cos(math.radians(alpha_k_i)))

            if Z_i % 2 == 0:
                Md_s = 2*C_s-Dm
                Md_i = 2*C_i-Dm
            elif Z_i % 2 != 0:
                Md_s = 2*C_s * math.cos(math.radians(90/Z_i))-Dm
                Md_i = 2*C_i* math.cos(math.radians(90/Z_i))-Dm

            alpha_m_s = math.atan(math.tan(math.radians(alpha_k_s)) + (Dm*math.cos(beta_b))/d_b)
            alpha_m_i = math.atan(math.tan(math.radians(alpha_k_i)) + (Dm*math.cos(beta_b))/d_b)

            d_m_s = d_b/ math.cos(alpha_m_s)
            d_m_i = d_b/ math.cos(alpha_m_i)

    return(Dm,Md_s,Md_i,d_m_s,d_m_i)
def micro_geometria(m_n,d,b,Q,Z_i,k):
    # Tolerâncias do dentado pela ISO 1328-1:1995 (a mesma referência da ISO 6336-1 §7.5.3.3 e do ISO/TR 6336-30).
    # Cada tolerância é dada para o grau 5 em função do módulo m_n, do diâmetro de referência d e da largura b, e sobe
    # um passo de sqrt(2) por grau de qualidade. A norma usa, em cada faixa de m_n / d / b, a MÉDIA GEOMÉTRICA dos limites
    # da faixa (não o valor nominal), e arredonda: < 5 µm ao 0,1 µm mais próximo; 5–10 µm ao 0,5 µm; > 10 µm ao inteiro.
    # Verificado contra os 8 exemplos do ISO/TR 6336-30:2017 (48/48 valores de f_pt, f_falpha e f_Hbeta reproduzidos).
    # Grandezas sem fórmula própria na ISO 1328-1 (R_s, F_pk, F''_i, f''_i, F'_i, f'_i) mantêm a formulação de MAZZO (2013) / DIN 3962.
    def arred(v):
        if v < 5 :
            return round(v*10)/10
        elif v <= 10 :
            return round(v*2)/2
        return float(round(v))
    def media_geo(v, limites):
        for lo, hi in zip(limites[:-1], limites[1:]):
            if v <= hi :
                return math.sqrt(lo*hi)
        return math.sqrt(limites[-2]*limites[-1])
    d = abs(d)
    m_g = media_geo(m_n, [0.5, 2, 3.5, 6, 10, 16, 25, 40, 70])
    d_g = media_geo(d, [5, 20, 50, 125, 280, 560, 1000, 1600, 2500, 4000, 6000, 8000, 10000])
    b_g = media_geo(b, [4, 10, 20, 40, 80, 160, 250, 400, 650, 1000])
    esc = lambda Qi: 2**((Qi - 5)/2)
    tol = lambda base, Qi: arred(base * esc(Qi))

    fp = tol(0.3*(m_g + 0.4*math.sqrt(d_g)) + 4, Q)                       # f_pt  desvio de passo individual
    fpe = fp                                                                # f_pb (desvio de passo de base): ISO 1328-1 usa f_pt; o K_v converte com cos(alpha_t) onde preciso
    fu = tol(0.3*(m_g + 0.4*math.sqrt(d_g)) + 4, Q)                        # f_u (diferença entre passos consecutivos) ~ f_pt (ISO 1328-1 não tabela f_u)
    Fp = tol(0.3*m_g + 1.25*math.sqrt(d_g) + 7, Q)                         # F_p  erro total de passo
    f_f = tol(2.5*math.sqrt(m_g) + 0.17*math.sqrt(d_g) + 0.5, Q)            # f_falpha  desvio de forma do perfil
    f_Halpha = tol(2*math.sqrt(m_g) + 0.14*math.sqrt(d_g) + 0.5, Q)         # f_Halpha  desvio angular do perfil
    F_f = tol(3.2*math.sqrt(m_g) + 0.22*math.sqrt(d_g) + 0.7, Q)            # F_alpha  desvio total do perfil
    f_Hbeta = tol(0.07*math.sqrt(d_g) + 0.45*math.sqrt(b_g) + 3, Q)         # f_Hbeta  desvio angular de hélice
    f_betaf = f_Hbeta                                                       # f_fbeta  desvio de forma da hélice (= f_Hbeta na ISO 1328-1)
    F_beta = tol(0.1*math.sqrt(d_g) + 0.63*math.sqrt(b_g) + 4.2, Q)         # F_beta  desvio total de hélice
    Fr = tol(0.24*m_g + 1.0*math.sqrt(d_g) + 5.6, Q)                        # F_r  desvio de concentricidade (ISO 1328-2)
    f_Hbeta_6 = tol(0.07*math.sqrt(d_g) + 0.45*math.sqrt(b_g) + 3, 5)       # f_Hbeta do grau 5 (ISO 6336-1 Eq. 53: F_betax = |1,33 f_sh - f_Hbeta5|)

    # --- grandezas de Mazzo (2013) / DIN 3962 sem equivalente direto na ISO 1328-1 (mantidas: só informativas e no jogo entre flancos)
    if m_n <= 2:
        m_np = 1.4
    elif m_n <= 3.55 :
        m_np = 2.5
    elif m_n <= 6 :
        m_np = 5
    elif m_n <= 10 :
        m_np = 8
    elif m_n <= 16 :
        m_np = 12.5
    elif m_n <= 25 :
        m_np = 20
    elif m_n <= 40 :
        m_np = 31.5
    else :
        m_np = 50
    if d <= 50 :
        dp = 22.4
    elif d <= 125 :
        dp = 80
    elif d <= 280 :
        dp = 180
    elif d <= 560 :
        dp = 400
    elif d <= 1000 :
        dp = 710
    elif d <= 1600 :
        dp = 1250
    elif d <= 2500 :
        dp = 2000
    elif d <= 4000 :
        dp = 3150
    elif d <= 6300 :
        dp = 5000
    else :
        dp = 8000
    fq = 1.4**(Q-5) if Q <= 9 else 1.6**(Q-5)
    Rs = int(1.4**(Q-5) * (1 + 1.28 * math.sqrt(m_np) + (1.33 + 0.7 *math.log(m_np)) * dp**(0.25))+0.5)
    L = math.pi*m_n * abs(k)
    Fpk = int(fq * (6.25* m_np**(1/7)* (L**(1/3)/dp**(1/7)))+0.5)
    L = math.pi*m_n * int(abs(Z_i)/8)
    Fpk_8 = int(fq * (6.25* m_np**(1/7)* (L**(1/3)/dp**(1/7)))+0.5)
    F_i_llinha = int(1.4**(Q-5) * (2+2.57*math.sqrt(m_np) + (3.12 + 0.432 * math.log(m_np)) * dp**(0.25)) + 0.5)
    f_i_llinha = int(1.4**(Q-5) * (1.8*math.sqrt(m_np) + 1.6*dp**(0.25) - 1) + 0.5)
    F_i_linha = int(0.8*(Fp+F_f) + 0.5)   # Fp e F_f já incluem o escalonamento do grau de qualidade
    f_i_linha = int(0.7*(fp+F_f) + 0.5)

    return(Fr/1000,Rs/1000,fp/1000,fu/1000,Fp/1000,Fpk/1000,Fpk_8/1000,fpe/1000,F_beta/1000,f_Hbeta/1000,f_betaf/1000,f_Halpha/1000,f_f/1000,F_f/1000,F_i_llinha/1000,f_i_llinha/1000,F_i_linha/1000,f_i_linha/1000,f_Hbeta_6/1000)
def lubrificante(m_n,Z_i,beta,v_t,P_t):

    A = ((0.1/(Z_i * math.cos(math.radians(beta))))+(0.03/(v_t+2))) * P_t

    if 2.5 *A <= 0.01 :
        V_li = 0.01
    elif 2.5 *A > 0.01 :
        V_li = 2.5 * A

    if 3.2 *A <= 1.2 * V_li :
        V_ls = 1.2 * V_li
    elif 3.2 * A > 1.2 * V_li :
        V_ls = 3.2 * A

    P_ri = m_n + 0.5
    P_rs = 6 * m_n + 0.5

    return V_li,V_ls,P_ri,P_rs
def forças (Ft,alpha_wt,beta,beta_w):
    F_rd = Ft*math.tan(math.radians(alpha_wt))
    F_ax = Ft*math.tan(math.radians(beta_w))
    F_b = Ft/math.cos(math.radians(beta_w))
    alpha_wn = math.atan(math.tan(math.radians(alpha_wt)) * math.cos(math.radians(beta)))
    F = F_b/math.cos(math.radians(alpha_wn))

    return(F_rd,F_ax,F_b,F)
import math
from scipy.interpolate import interp1d
def kv (Engrenagem_1,Engrenagem_2,c_linha1,c_linha2,c_gamma1,c_gamma2,Ck1,Ck2,Tipo_planetario,Ring):

    if Engrenagem_1.epsilon_total > 1 and Engrenagem_1.epsilon_total <= 2 :
        Cv1_1 = 0.32
        Cv2_1 = 0.34
        Cv3_1 = 0.23
        Cv4_1 = 0.90
        Cv5_1 = 0.47
        Cv6_1 = 0.47
    elif Engrenagem_1.epsilon_total > 2 :
        Cv1_1 = 0.32
        Cv2_1 = 0.57/(Engrenagem_1.epsilon_total - 0.3)
        Cv3_1 = 0.096/(Engrenagem_1.epsilon_total - 1.56)
        Cv4_1 = (0.57-0.05*Engrenagem_1.epsilon_total)/(Engrenagem_1.epsilon_total - 1.44)
        Cv5_1 = 0.47
        Cv6_1 = 0.12/(Engrenagem_1.epsilon_total - 1.74)

    if Engrenagem_1.epsilon_total > 1 and Engrenagem_1.epsilon_total <= 1.5:
        Cv7_1 = 0.75
    elif Engrenagem_1.epsilon_total > 1.5 and Engrenagem_1.epsilon_total <= 2.5:
        Cv7_1 = 0.125 * math.sin(math.pi*(Engrenagem_1.epsilon_total-2)) + 0.875
    elif Engrenagem_1.epsilon_total > 2.5:
        Cv7_1 = 1

    if Engrenagem_1.material_pinhao.classe_KHbeta == 1 :
        ya1 = (160/(Engrenagem_1.material_pinhao.Lim_pressao)) * (Engrenagem_1.fpe_pinhao*1000)
        if Engrenagem_1.v_t > 5 and Engrenagem_1.v_t <= 10 :
            if ya1 <= (12800/Engrenagem_1.material_pinhao.Lim_pressao) :
                ya1 = (160/(Engrenagem_1.material_pinhao.Lim_pressao)) *  (Engrenagem_1.fpe_pinhao*1000)
            else :
                ya1 = (12800/Engrenagem_1.material_pinhao.Lim_pressao)
        if Engrenagem_1.v_t > 10 :
            if ya1 <= (6400/Engrenagem_1.material_pinhao.Lim_pressao) :
                ya1 = (160/(Engrenagem_1.material_pinhao.Lim_pressao)) *  (Engrenagem_1.fpe_pinhao*1000)
            else :
                ya1 = (6400/Engrenagem_1.material_pinhao.Lim_pressao)

    elif Engrenagem_1.material_pinhao.classe_KHbeta == 2 :
        ya1 = 0.275 * (Engrenagem_1.fpe_pinhao*1000)
        if Engrenagem_1.v_t > 5 and Engrenagem_1.v_t <= 10 :
            if ya1 <= 22 :
                ya1 = 0.275 * (Engrenagem_1.fpe_pinhao*1000)
            else :
                ya1 = 22
        if Engrenagem_1.v_t > 10 :
            if ya1 <= 11 :
                ya1 = 0.275 * (Engrenagem_1.fpe_pinhao*1000)
            else :
                ya1 = 11
    elif Engrenagem_1.material_pinhao.classe_KHbeta == 3 :
        ya1 = 0.075 * (Engrenagem_1.fpe_pinhao*1000)
        if ya1 <= 3 :
            ya1 = 0.075 * (Engrenagem_1.fpe_pinhao*1000)
        else:
            ya1 = 3

    if Engrenagem_1.material_coroa.classe_KHbeta == 1 :
        ya2 = (160/(Engrenagem_1.material_coroa.Lim_pressao)) * (Engrenagem_1.fpe_coroa*1000)
        if Engrenagem_1.v_t > 5 and Engrenagem_1.v_t <= 10 :
            if ya2 <= (12800/Engrenagem_1.material_coroa.Lim_pressao) :
                ya2 = (160/(Engrenagem_1.material_coroa.Lim_pressao)) *  (Engrenagem_1.fpe_coroa*1000)
            else :
                ya2 = (12800/Engrenagem_1.material_coroa.Lim_pressao)
        if Engrenagem_1.v_t > 10 :
            if ya2 <= (6400/Engrenagem_1.material_coroa.Lim_pressao) :
                ya2 = (160/(Engrenagem_1.material_coroa.Lim_pressao)) *  (Engrenagem_1.fpe_coroa*1000)
            else :
                ya2 = (6400/Engrenagem_1.material_coroa.Lim_pressao)

    elif Engrenagem_1.material_coroa.classe_KHbeta == 2 :
        ya2 = 0.275 * (Engrenagem_1.fpe_coroa*1000)
        if Engrenagem_1.v_t > 5 and Engrenagem_1.v_t <= 10 :
            if ya2 <= 22 :
                ya2 = 0.275 * (Engrenagem_1.fpe_coroa*1000)
            else :
                ya2 = 22
        if Engrenagem_1.v_t > 10 :
            if ya2 <= 11 :
                ya2 = 0.275 * (Engrenagem_1.fpe_coroa*1000)
            else :
                ya2 = 11
    elif Engrenagem_1.material_coroa.classe_KHbeta == 3 :
        ya2 = 0.075 * (Engrenagem_1.fpe_coroa*1000)
        if ya2 <= 3 :
            ya2 = 0.075 * (Engrenagem_1.fpe_coroa*1000)
        else:
            ya2 = 3

    if (Engrenagem_1.material_coroa.classe_KHbeta != Engrenagem_1.material_pinhao.classe_KHbeta) or (Engrenagem_1.material_coroa.Lim_pressao != Engrenagem_1.material_pinhao.Lim_pressao) :
        ya = (ya1+ya2)/2
    else :
        ya = max([ya1,ya2])

    fpe = max([Engrenagem_1.fpe_pinhao,Engrenagem_1.fpe_coroa])
    f_f = max([Engrenagem_1.f_f_pinhao,Engrenagem_1.f_f_coroa])

    fpe_eff1 = fpe*1000 - ya
    ff_eff1 = f_f*1000 - ya

    if Ck1 != None :
        Ck1 = Ck1
    elif Ck1 == None :
        Ck1 = 1/36 * ((Engrenagem_1.material_pinhao.Lim_pressao/97 - 18.45)**2 + (Engrenagem_1.material_coroa.Lim_pressao/97 - 18.45)**2  ) + 1.5


    Bp1 = (c_linha1 * fpe_eff1)/(Engrenagem_1.Ka*(Engrenagem_1.Ft/Engrenagem_1.b))
    Bf1 = (c_linha1 * ff_eff1)/(Engrenagem_1.Ka*(Engrenagem_1.Ft/Engrenagem_1.b))
    Bk1 = abs(1 - ((c_linha1 * Ck1 )/(Engrenagem_1.Ka*(Engrenagem_1.Ft/Engrenagem_1.b))))

    K1 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv3_1*Bk1



    if Engrenagem_2 != None :

        if Engrenagem_2.epsilon_total > 1 and Engrenagem_2.epsilon_total <= 2 :
            Cv1_2 = 0.32
            Cv2_2 = 0.34
            Cv3_2 = 0.23
            Cv4_2 = 0.90
            Cv5_2 = 0.47
            Cv6_2 = 0.47
        elif Engrenagem_2.epsilon_total > 2 :
            Cv1_2 = 0.32
            Cv2_2 = 0.57/(Engrenagem_2.epsilon_total - 0.3)
            Cv3_2 = 0.096/(Engrenagem_2.epsilon_total - 1.56)
            Cv4_2 = (0.57-0.05*Engrenagem_2.epsilon_total)/(Engrenagem_2.epsilon_total - 1.44)
            Cv5_2 = 0.47
            Cv6_2 = 0.12/(Engrenagem_2.epsilon_total - 1.74)
        if Engrenagem_2.epsilon_total > 1 and Engrenagem_2.epsilon_total <= 1.5:
            Cv7_2 = 0.75
        elif Engrenagem_2.epsilon_total > 1.5 and Engrenagem_2.epsilon_total <= 2.5:
            Cv7_2 = 0.125 * math.sin(math.pi*(Engrenagem_2.epsilon_total-2)) + 0.875
        elif Engrenagem_2.epsilon_total > 2.5:
            Cv7_2 = 1

        if Engrenagem_2.material_pinhao.classe_KHbeta == 1 :
            ya1 = (160/(Engrenagem_2.material_pinhao.Lim_pressao)) * (Engrenagem_2.fpe_pinhao*1000)
            if Engrenagem_2.v_t > 5 and Engrenagem_2.v_t <= 10 :
                if ya1 <= (12800/Engrenagem_2.material_pinhao.Lim_pressao) :
                    ya1 = (160/(Engrenagem_2.material_pinhao.Lim_pressao)) *  (Engrenagem_2.fpe_pinhao*1000)
                else :
                    ya1 = (12800/Engrenagem_2.material_pinhao.Lim_pressao)
            if Engrenagem_2.v_t > 10 :
                if ya1 <= (6400/Engrenagem_2.material_pinhao.Lim_pressao) :
                    ya1 = (160/(Engrenagem_2.material_pinhao.Lim_pressao)) *  (Engrenagem_2.fpe_pinhao*1000)
                else :
                    ya1 = (6400/Engrenagem_2.material_pinhao.Lim_pressao)

        elif Engrenagem_2.material_pinhao.classe_KHbeta == 2 :
            ya1 = 0.275 * (Engrenagem_2.fpe_pinhao*1000)
            if Engrenagem_2.v_t > 5 and Engrenagem_2.v_t <= 10 :
                if ya1 <= 22 :
                    ya1 = 0.275 * (Engrenagem_2.fpe_pinhao*1000)
                else :
                    ya1 = 22
            if Engrenagem_2.v_t > 10 :
                if ya1 <= 11 :
                    ya1 = 0.275 * (Engrenagem_2.fpe_pinhao*1000)
                else :
                    ya1 = 11
        elif Engrenagem_2.material_pinhao.classe_KHbeta == 3 :
            ya1 = 0.075 * (Engrenagem_2.fpe_pinhao*1000)
            if ya1 <= 3 :
                ya1 = 0.075 * (Engrenagem_2.fpe_pinhao*1000)
            else:
                ya1 = 3

        if Engrenagem_2.material_coroa.classe_KHbeta == 1 :
            ya2 = (160/(Engrenagem_2.material_coroa.Lim_pressao)) * (Engrenagem_2.fpe_coroa*1000)
            if Engrenagem_2.v_t > 5 and Engrenagem_2.v_t <= 10 :
                if ya2 <= (12800/Engrenagem_2.material_coroa.Lim_pressao) :
                    ya2 = (160/(Engrenagem_2.material_coroa.Lim_pressao)) *  (Engrenagem_2.fpe_coroa*1000)
                else :
                    ya2 = (12800/Engrenagem_2.material_coroa.Lim_pressao)
            if Engrenagem_2.v_t > 10 :
                if ya2 <= (6400/Engrenagem_2.material_coroa.Lim_pressao) :
                    ya2 = (160/(Engrenagem_2.material_coroa.Lim_pressao)) *  (Engrenagem_2.fpe_coroa*1000)
                else :
                    ya2 = (6400/Engrenagem_2.material_coroa.Lim_pressao)

        elif Engrenagem_2.material_coroa.classe_KHbeta == 2 :
            ya2 = 0.275 * (Engrenagem_2.fpe_coroa*1000)
            if Engrenagem_2.v_t > 5 and Engrenagem_2.v_t <= 10 :
                if ya2 <= 22 :
                    ya2 = 0.275 * (Engrenagem_2.fpe_coroa*1000)
                else :
                    ya2 = 22
            if Engrenagem_2.v_t > 10 :
                if ya2 <= 11 :
                    ya2 = 0.275 * (Engrenagem_2.fpe_coroa*1000)
                else :
                    ya2 = 11
        elif Engrenagem_2.material_coroa.classe_KHbeta == 3 :
            ya2 = 0.075 * (Engrenagem_2.fpe_coroa*1000)
            if ya2 <= 3 :
                ya2 = 0.075 * (Engrenagem_2.fpe_coroa*1000)
            else:
                ya2 = 3

        if (Engrenagem_2.material_coroa.classe_KHbeta != Engrenagem_2.material_pinhao.classe_KHbeta) or (Engrenagem_2.material_coroa.Lim_pressao != Engrenagem_2.material_pinhao.Lim_pressao) :
            ya = (ya1+ya2)/2
        else :
            ya = max([ya1,ya2])

        fpe = max([Engrenagem_2.fpe_pinhao,Engrenagem_2.fpe_coroa])
        f_f = max([Engrenagem_2.f_f_pinhao,Engrenagem_2.f_f_coroa])

        fpe_eff2= fpe*1000 - ya
        ff_eff2 = f_f*1000 - ya

        if Ck2 != None :
            Ck2 = Ck2
        elif Ck2 == None :
            Ck2 = 1/36 * (((Engrenagem_2.material_pinhao.Lim_pressao/97) - 18.45)**2 + ((Engrenagem_2.material_coroa.Lim_pressao/97) - 18.45)**2  ) + 1.5


        Bp2 = (c_linha2 * fpe_eff2)/(Engrenagem_2.Ka*(Engrenagem_2.Ft/Engrenagem_2.b))
        Bf2 = (c_linha2 * ff_eff2)/(Engrenagem_2.Ka*(Engrenagem_2.Ft/Engrenagem_2.b))
        Bk2 = abs(1 - ((c_linha2 * Ck2 )/(Engrenagem_2.Ka*(Engrenagem_2.Ft/Engrenagem_2.b))))

        K2 = Cv1_2*Bp2 + Cv2_2*Bf2 + Cv3_2*Bk2

    if Engrenagem_1.trans == "Simples" :
        if Engrenagem_1.Z_pinhao > 0 and Engrenagem_1.Z_coroa > 0 :
            rm_pinhao = (Engrenagem_1.d_a_pinhao + Engrenagem_1.d_f_pinhao)/4
            rm_coroa = (Engrenagem_1.d_a_coroa + Engrenagem_1.d_f_coroa)/4
            i_1 = Engrenagem_1.material_pinhao.rho *(math.pi/2)*Engrenagem_1.b_pinhao*((rm_pinhao)**4 - (Engrenagem_1.di_pinhao/2)**4 + (Engrenagem_1.d_sh_pinhao/2)**4)
            i_2 = Engrenagem_1.material_coroa.rho *(math.pi/2)*Engrenagem_1.b_coroa*abs((rm_coroa)**4 - (Engrenagem_1.di_coroa/2)**4)
            J1_b = i_1/Engrenagem_1.b_pinhao
            J2_b = i_2/Engrenagem_1.b_coroa
            m1_b = J1_b/(Engrenagem_1.db_pinhao/2)**2
            m2_b = J2_b/(Engrenagem_1.db_coroa/2)**2
            m_red = (m1_b*m2_b)/((m1_b + m2_b))
            n_e1=(30e03/(math.pi*Engrenagem_1.Z_pinhao))* math.sqrt(c_gamma1/m_red)
            n_e2= None
            N_1 = Engrenagem_1.n_rel/n_e1
            N_2 = None
            if (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b < 100 :
                Ns1 = 0.5+0.35*math.sqrt((Engrenagem_1.Ft * Engrenagem_1.Ka)/(100*Engrenagem_1.b))
            elif (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b >= 100 :
                Ns1 = 0.85
            Ns2 = None
            if N_1 < Ns1 :
                Kv1 = N_1*K1 +1
                zona1 = f'Operação em zona subcrítica (N = {round(N_1,3)} < NS = {round(Ns1,3)}) '
            elif N_1 >= Ns1 and N_1 <1.15:
                Kv1 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
                zona1 = f'Operação em zona crítica (NS = {round(Ns1,3)} <= N = {round(N_1,3)} < 1.15) '
            elif N_1 >= 1.15 and N_1 < 1.5 :
                Kv115 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
                Kv150 = Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
                Kv1 = Kv150 + ((Kv115-Kv150)/(0.35))*(1.5-N_1)
                zona1 = f'Operação em zona intermediária (1.15 < N = {round(N_1,3)} < 1.5) '
            elif N_1 >= 1.5 :
                Kv1= Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
                zona1 = f'Operação em zona supercrítica (N = {round(N_1,3)} >= 1.5) '
            Kv2 = None
            zona2 = None

        elif Engrenagem_1.Z_pinhao < 0 or Engrenagem_1.Z_coroa < 0 :
            if Ring == "Fixo" :
                rm_pinhao = (Engrenagem_1.d_a_pinhao + Engrenagem_1.d_f_pinhao)/4
                i_1 = Engrenagem_1.material_pinhao.rho *(math.pi/2)*Engrenagem_1.b_pinhao*((rm_pinhao)**4 - (Engrenagem_1.di_pinhao/2)**4 + (Engrenagem_1.d_sh_pinhao/2)**4)
                J1_b = i_1/Engrenagem_1.b_pinhao
                m1_b = J1_b/(Engrenagem_1.db_pinhao/2)**2
                m_red = m1_b
                n_e1=(30e03/(math.pi*Engrenagem_1.Z_pinhao))* math.sqrt(c_gamma1/m_red)
                n_e2= None
                N_1 = Engrenagem_1.n_rel/n_e1
                N_2 = None
                if (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b < 100 :
                    Ns1 = 0.5+0.35*math.sqrt((Engrenagem_1.Ft * Engrenagem_1.Ka)/(100*Engrenagem_1.b))
                elif (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b >= 100 :
                    Ns1 = 0.85
                Ns2 = None
                if N_1 < Ns1 :
                    Kv1 = N_1*K1 +1
                    zona1 = f'Operação em zona subcrítica (N = {round(N_1,3)} < NS = {round(Ns1,3)}) '
                elif N_1 >= Ns1 and N_1 <1.15:
                    Kv1 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
                    zona1 = f'Operação em zona crítica (NS = {round(Ns1,3)} <= N = {round(N_1,3)} < 1.15) '
                elif N_1 >= 1.15 and N_1 < 1.5 :
                    Kv115 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
                    Kv150 = Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
                    Kv1 = Kv150 + ((Kv115-Kv150)/(0.35))*(1.5-N_1)
                    zona1 = f'Operação em zona intermediária (1.15 < N = {round(N_1,3)} < 1.5) '
                elif N_1 >= 1.5 :
                    Kv1= Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
                    zona1 = f'Operação em zona supercrítica (N = {round(N_1,3)} >= 1.5) '
                Kv2 = None
                zona2 = None


            elif Ring == "Rotativo" :
                rm_pinhao = (Engrenagem_1.d_a_pinhao + Engrenagem_1.d_f_pinhao)/4
                rm_coroa = (Engrenagem_1.d_a_coroa + Engrenagem_1.d_f_coroa)/4
                i_1 = Engrenagem_1.material_pinhao.rho *(math.pi/2)*Engrenagem_1.b_pinhao*((rm_pinhao)**4 - (Engrenagem_1.di_pinhao/2)**4 + (Engrenagem_1.d_sh_pinhao/2)**4)
                i_2 = Engrenagem_1.material_coroa.rho *(math.pi/2)*Engrenagem_1.b_coroa*abs((rm_coroa)**4 - (Engrenagem_1.di_coroa/2)**4)
                J1_b = i_1/Engrenagem_1.b_pinhao
                J2_b = i_2/Engrenagem_1.b_coroa
                m1_b = J1_b/(Engrenagem_1.db_pinhao/2)**2
                m2_b = J2_b/(Engrenagem_1.db_coroa/2)**2
                m_red = (m1_b*m2_b)/((m1_b + m2_b))
                n_e1=(30e03/(math.pi*Engrenagem_1.Z_pinhao))* math.sqrt(c_gamma1/m_red)
                n_e2= None
                if (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b < 100 :
                    Ns1 = 0.5+0.35*math.sqrt((Engrenagem_1.Ft * Engrenagem_1.Ka)/(100*Engrenagem_1.b))
                elif (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b >= 100 :
                    Ns1 = 0.85
                Ns2 = None
                N_1 = Engrenagem_1.n_rel/n_e1
                if N_1 < Ns1 :
                    Kv1 = N_1*K1 +1
                    zona1 = f'Operação em zona subcrítica (N = {round(N_1,3)} < NS = {round(Ns1,3)}) '
                elif N_1 >= Ns1 and N_1 <1.15:
                    Kv1 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
                    zona1 = f'Operação em zona crítica (NS = {round(Ns1,3)} <= N = {round(N_1,3)} < 1.15) '
                elif N_1 >= 1.15 and N_1 < 1.5 :
                    Kv115 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
                    Kv150 = Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
                    Kv1 = Kv150 + ((Kv115-Kv150)/(0.35))*(1.5-N_1)
                    zona1 = f'Operação em zona intermediária (1.15 < N = {round(N_1,3)} < 1.5) '
                elif N_1 >= 1.5 :
                    Kv1= Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
                    zona1 = f'Operação em zona supercrítica (N = {round(N_1,3)} >= 1.5) '
                Kv2 = None
                zona2 = None
    elif Engrenagem_1.trans == "Planetário" :
            if Tipo_planetario == "Simples":
                if Ring == "Fixo" :
                    rm_pinhao = (Engrenagem_1.d_a_pinhao + Engrenagem_1.d_f_pinhao)/4
                    rm_coroa = (Engrenagem_1.d_a_coroa + Engrenagem_1.d_f_coroa)/4
                    i_1 = Engrenagem_1.material_pinhao.rho *(math.pi/2)*Engrenagem_1.b_pinhao*((rm_pinhao)**4 - (Engrenagem_1.di_pinhao/2)**4 + (Engrenagem_1.d_sh_pinhao/2)**4)
                    i_2 = Engrenagem_1.material_coroa.rho *(math.pi/2)*Engrenagem_1.b_coroa*abs((rm_coroa)**4 - (Engrenagem_1.di_coroa/2)**4)
                    J1_b = i_1/Engrenagem_1.b_pinhao
                    J2_b = i_2/Engrenagem_1.b_coroa
                    m1_b = J1_b/(Engrenagem_1.db_pinhao/2)**2
                    m2_b = J2_b/(Engrenagem_1.db_coroa/2)**2
                    m_red_1 = (m1_b*m2_b)/((m1_b + m2_b*Engrenagem_1.N_cp))
                    n_e1=(30e03/(math.pi*Engrenagem_1.Z_pinhao))* math.sqrt(c_gamma1/m_red_1)
                    N_1 = Engrenagem_1.n_rel/n_e1
                    m_red_2 = m2_b                       # anelar fixa: massa infinita
                    n_e2=(30e03/(math.pi*Engrenagem_2.Z_pinhao))* math.sqrt(c_gamma2/m_red_2)
                    N_2 = Engrenagem_2.n_rel/n_e2
                    if (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b < 100 :
                        Ns1 = 0.5+0.35*math.sqrt((Engrenagem_1.Ft * Engrenagem_1.Ka)/(100*Engrenagem_1.b))
                    elif (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b >= 100 :
                        Ns1 = 0.85
                    if (Engrenagem_2.Ft * Engrenagem_2.Ka)/Engrenagem_2.b < 100 :
                        Ns2 = 0.5+0.35*math.sqrt((Engrenagem_2.Ft * Engrenagem_2.Ka)/(100*Engrenagem_2.b))
                    elif (Engrenagem_2.Ft * Engrenagem_2.Ka)/Engrenagem_2.b >= 100 :
                        Ns2 = 0.85
                    if N_1 < Ns1 :
                        Kv1 = N_1*K1 +1
                        zona1 = f'Operação em zona subcrítica (N = {round(N_1,3)} < NS = {round(Ns1,3)}) '
                    elif N_1 >= Ns1 and N_1 <1.15:
                        Kv1 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
                        zona1 = f'Operação em zona crítica (NS = {round(Ns1,3)} <= N = {round(N_1,3)} < 1.15) '
                    elif N_1 >= 1.15 and N_1 < 1.5 :
                        Kv115 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
                        Kv150 = Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
                        Kv1 = Kv150 + ((Kv115-Kv150)/(0.35))*(1.5-N_1)
                        zona1 = f'Operação em zona intermediária (1.15 < N = {round(N_1,3)} < 1.5) '
                    elif N_1 >= 1.5 :
                        Kv1= Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
                        zona1 = f'Operação em zona supercrítica (N = {round(N_1,3)} >= 1.5) '

                    if N_2 < Ns2 :
                        Kv2 = N_2*K2 +1
                        zona2 = f'Operação em zona subcrítica (N = {round(N_2,3)} < NS = {round(Ns2,3)}) '
                    elif N_2 >= Ns2 and N_2 <1.15:
                        Kv2 = Cv1_2*Bp2 + Cv2_2*Bf2 + Cv4_2 *Bk2 + 1
                        zona2 = f'Operação em zona crítica (NS = {round(Ns2,3)} <= N = {round(N_2,3)} < 1.15) '
                    elif N_2 >= 1.15 and N_2 < 1.5 :
                        Kv115 = Cv1_2*Bp2 + Cv2_2*Bf2 + Cv4_2 *Bk2 + 1
                        Kv150 = Cv5_2*Bp2 + Cv6_2*Bf2 + Cv7_2
                        Kv2 = Kv150 + ((Kv115-Kv150)/(0.35))*(1.5-N_2)
                        zona2 = f'Operação em zona intermediária (1.15 < N = {round(N_2,3)} < 1.5) '
                    elif N_2 >= 1.5 :
                        Kv2= Cv5_2*Bp2 + Cv6_2*Bf2 + Cv7_2
                        zona2 = f'Operação em zona supercrítica (N = {round(N_2,3)} >= 1.5)'


                elif Ring == "Rotativo" :
                    rm_pinhao = (Engrenagem_1.d_a_pinhao + Engrenagem_1.d_f_pinhao)/4
                    rm_coroa = (Engrenagem_1.d_a_coroa + Engrenagem_1.d_f_coroa)/4
                    rm2_coroa = (Engrenagem_2.d_a_coroa + Engrenagem_2.d_f_coroa)/4
                    i_1 = Engrenagem_1.material_pinhao.rho *(math.pi/2)*Engrenagem_1.b_pinhao*((rm_pinhao)**4 - (Engrenagem_1.di_pinhao/2)**4 + (Engrenagem_1.d_sh_pinhao/2)**4)
                    i_2 = Engrenagem_1.material_coroa.rho *(math.pi/2)*Engrenagem_1.b_coroa*abs((rm_coroa)**4 - (Engrenagem_1.di_coroa/2)**4)
                    i2_1 = Engrenagem_2.material_coroa.rho *(math.pi/2)*Engrenagem_2.b_coroa*abs((rm2_coroa)**4 - (Engrenagem_2.di_coroa/2)**4)
                    J1_b = i_1/Engrenagem_1.b_pinhao
                    J2_b = i_2/Engrenagem_1.b_coroa
                    J12_b = i2_1/Engrenagem_2.b_coroa
                    m1_b = J1_b/(Engrenagem_1.db_pinhao/2)**2
                    m2_b = J2_b/(Engrenagem_1.db_coroa/2)**2
                    m12_b = J12_b/(Engrenagem_2.db_coroa/2)**2
                    B = c_gamma1 * (1/m1_b + 1/m2_b) + c_gamma2 *(1/m12_b + 1/m2_b)
                    C = c_gamma1 * c_gamma2 * ((m1_b + m2_b + m12_b)/(m1_b * m2_b * m12_b))
                    n_e1 = (30e03/(math.pi*Engrenagem_1.Z_pinhao)) * math.sqrt(0.5 *(B + math.sqrt(B**2 - 4*C)))
                    n_e2 = (30e03/(math.pi*Engrenagem_1.Z_pinhao)) * math.sqrt(0.5 *(B - math.sqrt(B**2 - 4*C)))
                    N_1 = Engrenagem_1.n_rel/n_e1
                    N_2 = Engrenagem_1.n_rel/n_e2
                    if (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b < 100 :
                        Ns1 = 0.5+0.35*math.sqrt((Engrenagem_1.Ft * Engrenagem_1.Ka)/(100*Engrenagem_1.b))
                    elif (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b >= 100 :
                        Ns1 = 0.85
                    if (Engrenagem_2.Ft * Engrenagem_2.Ka)/Engrenagem_2.b < 100 :
                        Ns2 = 0.5+0.35*math.sqrt((Engrenagem_2.Ft * Engrenagem_2.Ka)/(100*Engrenagem_2.b))
                    elif (Engrenagem_2.Ft * Engrenagem_2.Ka)/Engrenagem_2.b >= 100 :
                        Ns2 = 0.85
                    if N_1 < Ns1 :
                        Kv1 = N_1*K1 +1
                        zona1 = f'Operação em zona subcrítica (N = {round(N_1,3)} < NS = {round(Ns1,3)}) '
                    elif N_1 >= Ns1 and N_1 <1.15:
                        Kv1 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
                        zona1 = f'Operação em zona crítica (NS = {round(Ns1,3)} <= N = {round(N_1,3)} < 1.15) '
                    elif N_1 >= 1.15 and N_1 < 1.5 :
                        Kv115 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
                        Kv150 = Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
                        Kv1 = Kv150 + ((Kv115-Kv150)/(0.35))*(1.5-N_1)
                        zona1 = f'Operação em zona intermediária (1.15 < N = {round(N_1,3)} < 1.5) '
                    elif N_1 >= 1.5 :
                        Kv1= Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
                        zona1 = f'Operação em zona supercrítica (N = {round(N_1,3)} >= 1.5) '

                    if N_2 < Ns2 :
                        Kv2 = N_2*K2 +1
                        zona2 = f'Operação em zona subcrítica (N = {round(N_2,3)} < NS = {round(Ns2,3)}) '
                    elif N_2 >= Ns2 and N_2 <1.15:
                        Kv2 = Cv1_2*Bp2 + Cv2_2*Bf2 + Cv4_2 *Bk2 + 1
                        zona2 = f'Operação em zona crítica (NS = {round(Ns2,3)} <= N = {round(N_2,3)} < 1.15) '
                    elif N_2 >= 1.15 and N_2 < 1.5 :
                        Kv115 = Cv1_2*Bp2 + Cv2_2*Bf2 + Cv4_2 *Bk2 + 1
                        Kv150 = Cv5_2*Bp2 + Cv6_2*Bf2 + Cv7_2
                        Kv2 = Kv150 + ((Kv115-Kv150)/(0.35))*(1.5-N_2)
                        zona2 = f'Operação em zona intermediária (1.15 < N = {round(N_2,3)} < 1.5) '
                    elif N_2 >= 1.5 :
                        Kv2= Cv5_2*Bp2 + Cv6_2*Bf2 + Cv7_2
                        zona2 = f'Operação em zona supercrítica (N = {round(N_2,3)} >= 1.5)'

            elif Tipo_planetario == "Composto":
                if Ring == "Fixo" :
                    rm_pinhao = (Engrenagem_1.d_a_pinhao + Engrenagem_1.d_f_pinhao)/4
                    rm_coroa = (Engrenagem_1.d_a_coroa + Engrenagem_1.d_f_coroa)/4
                    rm2_pinhao = (Engrenagem_2.d_a_pinhao + Engrenagem_2.d_f_pinhao)/4
                    i_1 = Engrenagem_1.material_pinhao.rho *(math.pi/2)*Engrenagem_1.b_pinhao*((rm_pinhao)**4 - (Engrenagem_1.di_pinhao/2)**4 + (Engrenagem_1.d_sh_pinhao/2)**4)
                    i_2 = Engrenagem_1.material_coroa.rho *(math.pi/2)*Engrenagem_1.b_coroa*abs((rm_coroa)**4 - (Engrenagem_1.di_coroa/2)**4)
                    i2_1 = Engrenagem_2.material_pinhao.rho *(math.pi/2)*Engrenagem_2.b_pinhao*((rm2_pinhao)**4 - (Engrenagem_2.di_pinhao/2)**4 + (Engrenagem_2.d_sh_pinhao/2)**4)
                    J1_b = i_1/Engrenagem_1.b_pinhao
                    J2_b = i_2/Engrenagem_1.b_coroa
                    J12_b = i2_1/Engrenagem_2.b_pinhao
                    m1_b = J1_b/(Engrenagem_1.db_pinhao/2)**2
                    m2_b = J2_b/(Engrenagem_1.db_coroa/2)**2
                    m12_b = J12_b/(Engrenagem_2.db_pinhao/2)**2
                    # planeta composto: um único corpo -> inércia total (dois degraus) por unidade de largura da malha considerada,
                    # referida ao raio de base do degrau que engrena naquela malha (ISO 6336-1 §6.5.3: m* = J/(b r_b^2))
                    J_pla = i_2 + i2_1
                    m2_b = J_pla/(Engrenagem_1.b_coroa*(Engrenagem_1.db_coroa/2)**2)
                    m12_b = J_pla/(Engrenagem_2.b_pinhao*(Engrenagem_2.db_pinhao/2)**2)
                    m_red_1 = (m1_b*m2_b)/((m1_b + m2_b*Engrenagem_1.N_cp))
                    n_e1=(30e03/(math.pi*Engrenagem_1.Z_pinhao))* math.sqrt(c_gamma1/m_red_1)
                    N_1 = Engrenagem_1.n_rel/n_e1
                    m_red_2 = m12_b                      # anelar fixa: massa infinita
                    n_e2=(30e03/(math.pi*Engrenagem_2.Z_pinhao))* math.sqrt(c_gamma2/m_red_2)
                    N_2 = Engrenagem_2.n_rel/n_e2
                    if (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b < 100 :
                        Ns1 = 0.5+0.35*math.sqrt((Engrenagem_1.Ft * Engrenagem_1.Ka)/(100*Engrenagem_1.b))
                    elif (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b >= 100 :
                        Ns1 = 0.85
                    if (Engrenagem_2.Ft * Engrenagem_2.Ka)/Engrenagem_2.b < 100 :
                        Ns2 = 0.5+0.35*math.sqrt((Engrenagem_2.Ft * Engrenagem_2.Ka)/(100*Engrenagem_2.b))
                    elif (Engrenagem_2.Ft * Engrenagem_2.Ka)/Engrenagem_2.b >= 100 :
                        Ns2 = 0.85
                    if N_1 < Ns1 :
                        Kv1 = N_1*K1 +1
                        zona1 = f'Operação em zona subcrítica (N = {round(N_1,3)} < NS = {round(Ns1,3)}) '
                    elif N_1 >= Ns1 and N_1 <1.15:
                        Kv1 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
                        zona1 = f'Operação em zona crítica (NS = {round(Ns1,3)} <= N = {round(N_1,3)} < 1.15) '
                    elif N_1 >= 1.15 and N_1 < 1.5 :
                        Kv115 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
                        Kv150 = Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
                        Kv1 = Kv150 + ((Kv115-Kv150)/(0.35))*(1.5-N_1)
                        zona1 = f'Operação em zona intermediária (1.15 < N = {round(N_1,3)} < 1.5) '
                    elif N_1 >= 1.5 :
                        Kv1= Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
                        zona1 = f'Operação em zona supercrítica (N = {round(N_1,3)} >= 1.5) '

                    if N_2 < Ns2 :
                        Kv2 = N_2*K2 +1
                        zona2 = f'Operação em zona subcrítica (N = {round(N_2,3)} < NS = {round(Ns2,3)}) '
                    elif N_2 >= Ns2 and N_2 <1.15:
                        Kv2 = Cv1_2*Bp2 + Cv2_2*Bf2 + Cv4_2 *Bk2 + 1
                        zona2 = f'Operação em zona crítica (NS = {round(Ns2,3)} <= N = {round(N_2,3)} < 1.15) '
                    elif N_2 >= 1.15 and N_2 < 1.5 :
                        Kv115 = Cv1_2*Bp2 + Cv2_2*Bf2 + Cv4_2 *Bk2 + 1
                        Kv150 = Cv5_2*Bp2 + Cv6_2*Bf2 + Cv7_2
                        Kv2 = Kv150 + ((Kv115-Kv150)/(0.35))*(1.5-N_2)
                        zona2 = f'Operação em zona intermediária (1.15 < N = {round(N_2,3)} < 1.5) '
                    elif N_2 >= 1.5 :
                        Kv2= Cv5_2*Bp2 + Cv6_2*Bf2 + Cv7_2
                        zona2 = f'Operação em zona supercrítica (N = {round(N_2,3)} >= 1.5)'
                elif Ring == "Rotativo" :
                    rm_pinhao = (Engrenagem_1.d_a_pinhao + Engrenagem_1.d_f_pinhao)/4
                    rm_coroa = (Engrenagem_1.d_a_coroa + Engrenagem_1.d_f_coroa)/4
                    rm2_pinhao = (Engrenagem_2.d_a_pinhao + Engrenagem_2.d_f_pinhao)/4
                    rm2_coroa = (Engrenagem_2.d_a_coroa + Engrenagem_2.d_f_coroa)/4
                    i_1 = Engrenagem_1.material_pinhao.rho *(math.pi/2)*Engrenagem_1.b_pinhao*((rm_pinhao)**4 - (Engrenagem_1.di_pinhao/2)**4 + (Engrenagem_1.d_sh_pinhao/2)**4)
                    i_2 = Engrenagem_1.material_coroa.rho *(math.pi/2)*Engrenagem_1.b_coroa*abs((rm_coroa)**4 - (Engrenagem_1.di_coroa/2)**4)
                    i2_1 = Engrenagem_2.material_pinhao.rho *(math.pi/2)*Engrenagem_2.b_pinhao*((rm2_pinhao)**4 - (Engrenagem_2.di_pinhao/2)**4 + (Engrenagem_2.d_sh_pinhao/2)**4)
                    i2_2 = Engrenagem_2.material_coroa.rho *(math.pi/2)*Engrenagem_2.b_coroa*abs((rm2_coroa)**4 - (Engrenagem_2.di_coroa/2)**4)
                    J1_b = i_1/Engrenagem_1.b_pinhao
                    J2_b = i_2/Engrenagem_1.b_coroa
                    J12_b = i2_1/Engrenagem_2.b_pinhao
                    J22_b = i2_2/Engrenagem_2.b_coroa
                    m1_b = J1_b/(Engrenagem_1.db_pinhao/2)**2
                    m2_b = J2_b/(Engrenagem_1.db_coroa/2)**2
                    J_pla = i_2 + i2_1                   # planeta composto: corpo único
                    m2_b = J_pla/(Engrenagem_1.b_coroa*(Engrenagem_1.db_coroa/2)**2)
                    m12_b = J_pla/(Engrenagem_2.b_pinhao*(Engrenagem_2.db_pinhao/2)**2)
                    m22_b = J22_b/(Engrenagem_2.db_coroa/2)**2
                    m_red_1 = (m1_b*m2_b)/((m1_b + m2_b*Engrenagem_1.N_cp))
                    n_e1=(30e03/(math.pi*Engrenagem_1.Z_pinhao))* math.sqrt(c_gamma1/m_red_1)
                    N_1 = Engrenagem_1.n_rel/n_e1
                    m_red_2 = (m12_b*m22_b)/((m12_b*Engrenagem_2.N_cp + m22_b))
                    n_e2=(30e03/(math.pi*Engrenagem_2.Z_pinhao))* math.sqrt(c_gamma2/m_red_2)
                    N_2 = Engrenagem_2.n_rel/n_e2
                    if (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b < 100 :
                        Ns1 = 0.5+0.35*math.sqrt((Engrenagem_1.Ft * Engrenagem_1.Ka)/(100*Engrenagem_1.b))
                    elif (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b >= 100 :
                        Ns1 = 0.85
                    if (Engrenagem_2.Ft * Engrenagem_2.Ka)/Engrenagem_2.b < 100 :
                        Ns2 = 0.5+0.35*math.sqrt((Engrenagem_2.Ft * Engrenagem_2.Ka)/(100*Engrenagem_2.b))
                    elif (Engrenagem_2.Ft * Engrenagem_2.Ka)/Engrenagem_2.b >= 100 :
                        Ns2 = 0.85
                    if N_1 < Ns1 :
                        Kv1 = N_1*K1 +1
                        zona1 = f'Operação em zona subcrítica (N = {round(N_1,3)} < NS = {round(Ns1,3)}) '
                    elif N_1 >= Ns1 and N_1 <1.15:
                        Kv1 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
                        zona1 = f'Operação em zona crítica (NS = {round(Ns1,3)} <= N = {round(N_1,3)} < 1.15) '
                    elif N_1 >= 1.15 and N_1 < 1.5 :
                        Kv115 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
                        Kv150 = Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
                        Kv1 = Kv150 + ((Kv115-Kv150)/(0.35))*(1.5-N_1)
                        zona1 = f'Operação em zona intermediária (1.15 < N = {round(N_1,3)} < 1.5) '
                    elif N_1 >= 1.5 :
                        Kv1= Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
                        zona1 = f'Operação em zona supercrítica (N = {round(N_1,3)} >= 1.5) '

                    if N_2 < Ns2 :
                        Kv2 = N_2*K2 +1
                        zona2 = f'Operação em zona subcrítica (N = {round(N_2,3)} < NS = {round(Ns2,3)}) '
                    elif N_2 >= Ns2 and N_2 <1.15:
                        Kv2 = Cv1_2*Bp2 + Cv2_2*Bf2 + Cv4_2 *Bk2 + 1
                        zona2 = f'Operação em zona crítica (NS = {round(Ns2,3)} <= N = {round(N_2,3)} < 1.15) '
                    elif N_2 >= 1.15 and N_2 < 1.5 :
                        Kv115 = Cv1_2*Bp2 + Cv2_2*Bf2 + Cv4_2 *Bk2 + 1
                        Kv150 = Cv5_2*Bp2 + Cv6_2*Bf2 + Cv7_2
                        Kv2 = Kv150 + ((Kv115-Kv150)/(0.35))*(1.5-N_2)
                        zona2 = f'Operação em zona intermediária (1.15 < N = {round(N_2,3)} < 1.5) '
                    elif N_2 >= 1.5 :
                        Kv2= Cv5_2*Bp2 + Cv6_2*Bf2 + Cv7_2
                        zona2 = f'Operação em zona supercrítica (N = {round(N_2,3)} >= 1.5)'
    elif Engrenagem_1.trans == "Intermediario" :
        rm_pinhao = (Engrenagem_1.d_a_pinhao + Engrenagem_1.d_f_pinhao)/4
        rm_coroa = (Engrenagem_1.d_a_coroa + Engrenagem_1.d_f_coroa)/4
        rm2_coroa = (Engrenagem_2.d_a_coroa + Engrenagem_2.d_f_coroa)/4
        i_1 = Engrenagem_1.material_pinhao.rho *(math.pi/2)*Engrenagem_1.b_pinhao*((rm_pinhao)**4 - (Engrenagem_1.di_pinhao/2)**4 + (Engrenagem_1.d_sh_pinhao/2)**4)
        i_2 = Engrenagem_1.material_coroa.rho *(math.pi/2)*Engrenagem_1.b_coroa*abs((rm_coroa)**4 - (Engrenagem_1.di_coroa/2)**4)
        i2_1 = Engrenagem_2.material_coroa.rho *(math.pi/2)*Engrenagem_2.b_coroa*abs((rm2_coroa)**4 - (Engrenagem_2.di_coroa/2)**4)
        J1_b = i_1/Engrenagem_1.b_pinhao
        J2_b = i_2/Engrenagem_1.b_coroa
        J12_b = i2_1/Engrenagem_2.b_coroa
        m1_b = J1_b/(Engrenagem_1.db_pinhao/2)**2
        m2_b = J2_b/(Engrenagem_1.db_coroa/2)**2
        m12_b = J12_b/(Engrenagem_2.db_coroa/2)**2
        B = c_gamma1 * (1/m1_b + 1/m2_b) + c_gamma2 *(1/m12_b + 1/m2_b)
        C = c_gamma1 * c_gamma2 * ((m1_b + m2_b + m12_b)/(m1_b * m2_b * m12_b))
        n_e1 = (30e03/(math.pi*Engrenagem_1.Z_pinhao)) * math.sqrt(0.5 *(B + math.sqrt(B**2 - 4*C)))
        n_e2 = (30e03/(math.pi*Engrenagem_1.Z_pinhao)) * math.sqrt(0.5 *(B - math.sqrt(B**2 - 4*C)))
        N_1 = Engrenagem_1.n_rel/n_e1
        N_2 = Engrenagem_1.n_rel/n_e2

        if (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b < 100 :
            Ns1 = 0.5+0.35*math.sqrt((Engrenagem_1.Ft * Engrenagem_1.Ka)/(100*Engrenagem_1.b))
        elif (Engrenagem_1.Ft * Engrenagem_1.Ka)/Engrenagem_1.b >= 100 :
            Ns1 = 0.85
        if (Engrenagem_2.Ft * Engrenagem_2.Ka)/Engrenagem_2.b < 100 :
            Ns2 = 0.5+0.35*math.sqrt((Engrenagem_2.Ft * Engrenagem_2.Ka)/(100*Engrenagem_2.b))
        elif (Engrenagem_2.Ft * Engrenagem_2.Ka)/Engrenagem_2.b >= 100 :
            Ns2 = 0.85
        if N_1 < Ns1 :
            Kv1 = N_1*K1 +1
            zona1 = f'Operação em zona subcrítica (N = {round(N_1,3)} < NS = {Ns1}) '
        elif N_1 >= Ns1 and N_1 <1.15:
            Kv1 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
            zona1 = f'Operação em zona crítica (NS = {Ns1} <= N = {round(N_1,3)} < 1.15) '
        elif N_1 >= 1.15 and N_1 < 1.5 :
            Kv115 = Cv1_1*Bp1 + Cv2_1*Bf1 + Cv4_1*Bk1 + 1
            Kv150 = Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
            Kv1 = Kv150 + ((Kv115-Kv150)/(0.35))*(1.5-N_1)
            zona1 = f'Operação em zona intermediária (1.15 < N = {round(N_1,3)} < 1.5) '
        elif N_1 >= 1.5 :
            Kv1= Cv5_1*Bp1 + Cv6_1*Bf1 + Cv7_1
            zona1 = f'Operação em zona supercrítica (N = {round(N_1,3)} >= 1.5) '

        if N_2 < Ns2 :
            Kv2 = N_2*K2 +1
            zona2 = f'Operação em zona subcrítica (N = {round(N_2,3)} < NS = {Ns2}) '
        elif N_2 >= Ns2 and N_2 <1.15:
            Kv2 = Cv1_2*Bp2 + Cv2_2*Bf2 + Cv4_2 *Bk2 + 1
            zona2 = f'Operação em zona crítica (NS = {Ns2} <= N = {round(N_2,3)} < 1.15) '
        elif N_2 >= 1.15 and N_2 < 1.5 :
            Kv115 = Cv1_2*Bp2 + Cv2_2*Bf2 + Cv4_2 *Bk2 + 1
            Kv150 = Cv5_2*Bp2 + Cv6_2*Bf2 + Cv7_2
            Kv2 = Kv150 + ((Kv115-Kv150)/(0.35))*(1.5-N_2)
            zona2 = f'Operação em zona intermediária (1.15 < N = {round(N_2,3)} < 1.5) '
        elif N_2 >= 1.5 :
            Kv2= Cv5_2*Bp2 + Cv6_2*Bf2 + Cv7_2
            zona2 = f'Operação em zona supercrítica (N = {round(N_2,3)} >= 1.5)'




    return n_e1,n_e2,zona1,zona2,Kv1,Kv2
def rigidez (Engrenagem) :
    A1 = 0.04723
    A2 = 0.15551/Engrenagem.zn_pinhao
    if Engrenagem.Z_pinhao > 0 and Engrenagem.Z_coroa > 0 :
        A3 = 0.25791/Engrenagem.zn_coroa
        A7 = (-0.24188 * Engrenagem.x_coroa)/Engrenagem.zn_coroa
    elif Engrenagem.Z_pinhao < 0 or Engrenagem.Z_coroa < 0 :
        A3 = 0
        A7 = 0
    A4 = -0.00635 * Engrenagem.x_pinhao
    A5 = (-0.11654 * Engrenagem.x_pinhao)/Engrenagem.zn_pinhao
    A6 = -0.00193 * Engrenagem.x_coroa
    A8 = 0.00529 * Engrenagem.x_pinhao**2
    A9 = 0.00182 * Engrenagem.x_coroa**2

    q_linha = A1 + A2 + A3 + A4 + A5 + A6 + A7 +A8 + A9

    c_linha_th = 1/q_linha


    C_M = 0.8

    if Engrenagem.d_sh_coroa == Engrenagem.di_coroa :
        C_R = 1
    else :
        a = Engrenagem.bs_coroa/Engrenagem.b_coroa
        if a < 0.2 :
            a = 0.2
        elif a > 1.2 :
            a = 1.2
        b = Engrenagem.s_coroa/Engrenagem.m_n
        if b < 1 :
            b = 1
        C_R = 1 + (math.log(a))/(5*math.e**(0.2 * (b)))

    C_B1 = (1 + 0.5 * (1.2 - (Engrenagem.ferramenta_pinhao.cp_dedendo*Engrenagem.m_n)/Engrenagem.m_n)) * (1 - 0.02 * (20 - Engrenagem.alpha_n))
    C_B2 = (1 + 0.5 * (1.2 - (Engrenagem.ferramenta_coroa.cp_dedendo*Engrenagem.m_n)/Engrenagem.m_n)) * (1 - 0.02 * (20 - Engrenagem.alpha_n))
    C_B = (C_B1 + C_B2) / 2

    if Engrenagem.w >= 100 :
        c_linha = c_linha_th * C_M * C_R * C_B * math.cos(math.radians(Engrenagem.beta))
    elif Engrenagem.w < 100 :
        c_linha = c_linha_th * C_M * C_R * C_B * math.cos(math.radians(Engrenagem.beta)) * (Engrenagem.w/100)**(0.25)

    if Engrenagem.material_pinhao.tipo != "Aço" or Engrenagem.material_coroa.tipo != "Aço" :
        E = (2 * Engrenagem.material_pinhao.E * Engrenagem.material_coroa.E)/(Engrenagem.material_pinhao.E + Engrenagem.material_coroa.E)
        c_linha = c_linha * E/206

    c_gamma_alpha = c_linha * (0.75 * Engrenagem.epsilon_alpha + 0.25)
    if Engrenagem.epsilon_alpha < 1.2 :
        c_gamma_alpha = c_gamma_alpha * 0.9
    c_gamma_beta = c_gamma_alpha*0.85

    return c_linha_th,c_linha,c_gamma_alpha,c_gamma_beta

def K_Hbeta (Engrenagem_1,Kv1,c_gamma_beta1,k,K_Hbeta_imposto = None,regra_fma = "64"):
    # regra_fma (ISO 6336-1:2006 §7.5.3.3): "64" = sqrt(f_Hb1^2 + f_Hb2^2) (padrão da norma e do ISO/TR 6336-30),
    #                                     "63" = 1,0·f_Hb2 (controle de qualidade rigoroso), "62" = f_Hb1 + f_Hb2 (combinação mais desfavorável, sem f_sigma_beta)
    if K_Hbeta_imposto != None :
        return K_Hbeta_imposto, Engrenagem_1.b, "imposto"
    def f_ma_regra(f1, f2):
        if regra_fma == "62" :
            return f1 + f2
        elif regra_fma == "63" :
            return 1.0 * max([f1, f2])
        return math.sqrt(f1**2 + f2**2)

    Fm = Engrenagem_1.Ft * Engrenagem_1.Ka * Kv1
    B_linha = 1+2*((100-k)/k)
    gamma = (abs(B_linha+ Engrenagem_1.K_linha_pinhao * (Engrenagem_1.L_pinhao * Engrenagem_1.sh_pinhao)/(Engrenagem_1.d_pinhao**2) * (Engrenagem_1.d_pinhao/Engrenagem_1.d_sh_pinhao)**4 - 0.3)+0.3) * (Engrenagem_1.b/Engrenagem_1.d_pinhao)**2
    if Engrenagem_1.crwon_s_pinhao != 0 or Engrenagem_1.crwon_s_coroa != 0 :
        fsh0 = 0.012 * gamma
        f_ma = 0.5 * f_ma_regra(Engrenagem_1.f_Hbeta_pinhao*1000, Engrenagem_1.f_Hbeta_coroa*1000)   # B2 = 0,5 (Tabela 8, abaulamento)
        fsh = fsh0 * (Fm/Engrenagem_1.b)
        F_betaxa = abs(1.33 * fsh - Engrenagem_1.f_Hbeta_6*1000)   # Eq. (53): f_Hbeta_6 guarda a tolerância do GRAU 5 (f_Hbeta5)

    elif Engrenagem_1.crwon_s_pinhao == 0 and Engrenagem_1.crwon_s_coroa == 0 :
        fsh0 = 0.023 * gamma
        f_ma = f_ma_regra(Engrenagem_1.f_Hbeta_pinhao*1000, Engrenagem_1.f_Hbeta_coroa*1000)         # Eq. (64) por padrão
        fsh = fsh0 * (Fm/Engrenagem_1.b)
        F_betaxa = 1.33 * fsh + f_ma                                                                   # Eq. (52), B1 = B2 = 1


    F_betaxb = 0.005 * (Fm/Engrenagem_1.b)
    F_betaxc = 0.5 * max([Engrenagem_1.f_Hbeta_pinhao,Engrenagem_1.f_Hbeta_coroa])*1000
    F_betax = max([F_betaxa,F_betaxb,F_betaxc])

    if Engrenagem_1.material_pinhao.classe_KHbeta == 1 :
        y_beta1 = (320/(Engrenagem_1.material_pinhao.Lim_pressao)) * (F_betax)
        x_beta1 = 1 - (320/(Engrenagem_1.material_pinhao.Lim_pressao))
        if Engrenagem_1.v_t > 5 and Engrenagem_1.v_t <= 10 :
            if y_beta1 <= (25600/Engrenagem_1.material_pinhao.Lim_pressao) :
                y_beta1 = (320/(Engrenagem_1.material_pinhao.Lim_pressao)) * (F_betax)
            else :
                y_beta1 = (25600/Engrenagem_1.material_pinhao.Lim_pressao)
        if Engrenagem_1.v_t > 10 :
            if y_beta1 <= (12800/Engrenagem_1.material_pinhao.Lim_pressao) :
                y_beta1 = (320/(Engrenagem_1.material_pinhao.Lim_pressao)) * (F_betax)
            else :
                y_beta1 = (12800/Engrenagem_1.material_pinhao.Lim_pressao)

    elif Engrenagem_1.material_pinhao.classe_KHbeta == 2 :
        y_beta1 = 0.55 * (F_betax)
        x_beta1 = 0.45
        if Engrenagem_1.v_t > 5 and Engrenagem_1.v_t <= 10 :
            if y_beta1 <= 45 :
                y_beta1 = 0.55 * (F_betax)
            else :
                y_beta1 = 45
        if Engrenagem_1.v_t > 10 :
            if y_beta1 <= 22 :
                y_beta1 = 0.55 * (F_betax)
            else :
                y_beta1 = 22
    elif Engrenagem_1.material_pinhao.classe_KHbeta == 3 :
        y_beta1 = 0.15 * (F_betax)
        x_beta1 = 0.85
        if y_beta1 <= 6 :
            y_beta1 = 0.15 * (F_betax)
        else:
            y_beta1 = 6

    if Engrenagem_1.material_coroa.classe_KHbeta == 1 :
        y_beta2 = (320/(Engrenagem_1.material_coroa.Lim_pressao)) * (F_betax)
        x_beta2 = 1 - (320/(Engrenagem_1.material_coroa.Lim_pressao))
        if Engrenagem_1.v_t > 5 and Engrenagem_1.v_t <= 10 :
            if y_beta2 <= (25600/Engrenagem_1.material_coroa.Lim_pressao) :
                y_beta2 = (320/(Engrenagem_1.material_coroa.Lim_pressao)) * (F_betax)
            else :
                y_beta2 = (25600/Engrenagem_1.material_coroa.Lim_pressao)
        if Engrenagem_1.v_t > 10 :
            if y_beta2 <= (12800/Engrenagem_1.material_coroa.Lim_pressao) :
                y_beta2 = (320/(Engrenagem_1.material_coroa.Lim_pressao)) * (F_betax)
            else :
                y_beta2 = (12800/Engrenagem_1.material_coroa.Lim_pressao)

    elif Engrenagem_1.material_coroa.classe_KHbeta == 2 :
        y_beta2 = 0.55 * (F_betax)
        x_beta2 = 0.45
        if Engrenagem_1.v_t > 5 and Engrenagem_1.v_t <= 10 :
            if y_beta2 <= 45 :
                y_beta2 = 0.55 * (F_betax)
            else :
                y_beta2 = 45
        if Engrenagem_1.v_t > 10 :
            if y_beta2 <= 22 :
                y_beta2 = 0.55 * (F_betax)
            else :
                y_beta2 = 22
    elif Engrenagem_1.material_coroa.classe_KHbeta == 3 :
        y_beta2 = 0.15 * (F_betax)
        x_beta2 = 0.85
        if y_beta2 <= 6 :
            y_beta2 = 0.15 * (F_betax)
        else:
            y_beta2 = 6


    if (Engrenagem_1.material_coroa.classe_KHbeta != Engrenagem_1.material_pinhao.classe_KHbeta) or (Engrenagem_1.material_coroa.Lim_pressao != Engrenagem_1.material_pinhao.Lim_pressao) :
        y_beta = (y_beta1+y_beta2)/2
    else :
        y_beta = max([y_beta1,y_beta2])

    F_betay = F_betax - y_beta

    # c_gamma_beta ja inclui o fator 0.85 (c_gamma_beta = 0.85*c_gamma_alpha, ISO 6336-1 eq. 7.x)
    condicao = (F_betay * c_gamma_beta1)/(2*(Fm/Engrenagem_1.b))

    if condicao >= 1 :
        b_cal = (math.sqrt((2*(Fm/Engrenagem_1.b))/(F_betay * c_gamma_beta1)))*Engrenagem_1.b
        K_Hbeta = math.sqrt((2*F_betay*c_gamma_beta1)/((Fm)/(Engrenagem_1.b)))
        Cond = "A"
    elif condicao < 1 :
        b_cal = (0.5+ ((Fm/Engrenagem_1.b))/(F_betay * c_gamma_beta1))*Engrenagem_1.b
        K_Hbeta = 1 + condicao
        Cond = "B"


    return K_Hbeta,b_cal,Cond

def K_Fbeta(Engrenagem,KHbeta) :
    rel_pinhao = Engrenagem.b/Engrenagem.h_dente_pinhao
    rel_coroa = Engrenagem.b/Engrenagem.h_dente_coroa

    if rel_pinhao >= rel_coroa :
        rel = rel_coroa
    elif rel_pinhao < rel_coroa :
        rel = rel_pinhao
    if rel < 3 :
        rel = 3

    Nf = (rel**2)/(1+rel+rel**2)

    K_Fbeta = KHbeta**Nf

    return K_Fbeta
def Z_epsilon(Engrenagem):
    if Engrenagem.beta == 0 :
        Z_epsilon = math.sqrt((4 - Engrenagem.epsilon_alpha)/3)
    elif Engrenagem.beta != 0 :
        if Engrenagem.epsilon_beta < 1 :
            Z_epsilon = math.sqrt(((4 - Engrenagem.epsilon_alpha)/3) * (1 - Engrenagem.epsilon_beta) + (Engrenagem.epsilon_beta/Engrenagem.epsilon_alpha))
        elif Engrenagem.epsilon_beta >= 1 :
            Z_epsilon = math.sqrt((1)/Engrenagem.epsilon_alpha)

    return Z_epsilon
def K_Halpha(Engrenagem,Kv,KHbeta,c_gamma_alpha,Z_epsilon) :
    FtH = Engrenagem.Ft * Engrenagem.Ka * Kv * KHbeta

    if Engrenagem.material_pinhao.classe_KHbeta == 1 :
        ya1 = (160/(Engrenagem.material_pinhao.Lim_pressao)) * (Engrenagem.fpe_pinhao*1000)
        if Engrenagem.v_t > 5 and Engrenagem.v_t <= 10 :
            if ya1 <= (12800/Engrenagem.material_pinhao.Lim_pressao) :
                ya1 = (160/(Engrenagem.material_pinhao.Lim_pressao)) *  (Engrenagem.fpe_pinhao*1000)
            else :
                ya1 = (12800/Engrenagem.material_pinhao.Lim_pressao)
        if Engrenagem.v_t > 10 :
            if ya1 <= (6400/Engrenagem.material_pinhao.Lim_pressao) :
                ya1 = (160/(Engrenagem.material_pinhao.Lim_pressao)) *  (Engrenagem.fpe_pinhao*1000)
            else :
                ya1 = (6400/Engrenagem.material_pinhao.Lim_pressao)

    elif Engrenagem.material_pinhao.classe_KHbeta == 2 :
        ya1 = 0.275 * (Engrenagem.fpe_pinhao*1000)
        if Engrenagem.v_t > 5 and Engrenagem.v_t <= 10 :
            if ya1 <= 22 :
                ya1 = 0.275 * (Engrenagem.fpe_pinhao*1000)
            else :
                ya1 = 22
        if Engrenagem.v_t > 10 :
            if ya1 <= 11 :
                ya1 = 0.275 * (Engrenagem.fpe_pinhao*1000)
            else :
                ya1 = 11
    elif Engrenagem.material_pinhao.classe_KHbeta == 3 :
        ya1 = 0.075 * (Engrenagem.fpe_pinhao*1000)
        if ya1 <= 3 :
            ya1 = 0.075 * (Engrenagem.fpe_pinhao*1000)
        else:
            ya1 = 3

    if Engrenagem.material_coroa.classe_KHbeta == 1 :
        ya2 = (160/(Engrenagem.material_coroa.Lim_pressao)) * (Engrenagem.fpe_coroa*1000)
        if Engrenagem.v_t > 5 and Engrenagem.v_t <= 10 :
            if ya2 <= (12800/Engrenagem.material_coroa.Lim_pressao) :
                ya2 = (160/(Engrenagem.material_coroa.Lim_pressao)) *  (Engrenagem.fpe_coroa*1000)
            else :
                ya2 = (12800/Engrenagem.material_coroa.Lim_pressao)
        if Engrenagem.v_t > 10 :
            if ya2 <= (6400/Engrenagem.material_coroa.Lim_pressao) :
                ya2 = (160/(Engrenagem.material_coroa.Lim_pressao)) *  (Engrenagem.fpe_coroa*1000)
            else :
                ya2 = (6400/Engrenagem.material_coroa.Lim_pressao)

    elif Engrenagem.material_coroa.classe_KHbeta == 2 :
        ya2 = 0.275 * (Engrenagem.fpe_coroa*1000)
        if Engrenagem.v_t > 5 and Engrenagem.v_t <= 10 :
            if ya2 <= 22 :
                ya2 = 0.275 * (Engrenagem.fpe_coroa*1000)
            else :
                ya2 = 22
        if Engrenagem.v_t > 10 :
            if ya2 <= 11 :
                ya2 = 0.275 * (Engrenagem.fpe_coroa*1000)
            else :
                ya2 = 11
    elif Engrenagem.material_coroa.classe_KHbeta == 3 :
        ya2 = 0.075 * (Engrenagem.fpe_coroa*1000)
        if ya2 <= 3 :
            ya2 = 0.075 * (Engrenagem.fpe_coroa*1000)
        else:
            ya2 = 3

    if (Engrenagem.material_coroa.classe_KHbeta != Engrenagem.material_pinhao.classe_KHbeta) or (Engrenagem.material_coroa.Lim_pressao != Engrenagem.material_pinhao.Lim_pressao) :
        ya = (ya1+ya2)/2
    else :
        ya = max([ya1,ya2])

    fpe = max([Engrenagem.fpe_pinhao,Engrenagem.fpe_coroa])
    if Engrenagem.epsilon_total <=2 :
        K_Halpha = Engrenagem.epsilon_total/2 * (0.9 + 0.4 * ((c_gamma_alpha * (fpe*1000 - ya))/((FtH/Engrenagem.b))))
    elif Engrenagem.epsilon_total > 2 :
        K_Halpha = 0.9 + 0.4 * math.sqrt(((2*(Engrenagem.epsilon_total - 1))/Engrenagem.epsilon_total)) * ((c_gamma_alpha*(fpe*1000 - ya))/((FtH/Engrenagem.b)))

    Engrenagem.K_Halpha_sem_limite = K_Halpha   # guardado para K_Falpha (limites distintos, ISO 6336-1 §8.3.2)
    if K_Halpha > ((Engrenagem.epsilon_total)/(Engrenagem.epsilon_alpha * Z_epsilon**2)) :
        K_Halpha = ((Engrenagem.epsilon_total)/(Engrenagem.epsilon_alpha * Z_epsilon**2))
    if K_Halpha < 1 :
        K_Halpha = 1

    return K_Halpha
def K_Falpha (Engrenagem,K_Halpha):
    # parte do K_Halpha sem o limite de contato e aplica o limite próprio de flexão
    K_Falpha = getattr(Engrenagem, "K_Halpha_sem_limite", K_Halpha)
    if  K_Falpha > ((Engrenagem.epsilon_total)/(0.25*Engrenagem.epsilon_alpha + 0.75)) :
        K_Falpha = ((Engrenagem.epsilon_total)/(0.25*Engrenagem.epsilon_alpha + 0.75))
    if K_Falpha < 1 :
        K_Falpha = 1
    return K_Falpha
def Z_H (Engrenagem):
    Z_H = math.sqrt(((2*math.cos(math.radians(Engrenagem.beta_b)) * math.cos(math.radians(Engrenagem.alpha_wt)))/(math.cos(math.radians(Engrenagem.alpha_t))**2 * math.sin(math.radians(Engrenagem.alpha_wt)))))

    return Z_H
def Z_E (Engrenagem) :
    if Engrenagem.material_coroa.tipo != Engrenagem.material_pinhao.tipo :
        Z_E = math.sqrt((1)/(math.pi * (((1- Engrenagem.material_pinhao.Possion**2)/ (Engrenagem.material_pinhao.E*1e03))+((1-Engrenagem.material_coroa.Possion**2)/(Engrenagem.material_coroa.E*1e03)))))
    elif Engrenagem.material_coroa.tipo == Engrenagem.material_pinhao.tipo :
        Z_E = math.sqrt(((Engrenagem.material_pinhao.E*1e03)/(2*math.pi*(1-Engrenagem.material_pinhao.Possion**2))))
    return Z_E
def Z_beta (Engrenagem):
    Z_beta = 1/math.sqrt(math.cos(math.radians(Engrenagem.beta)))
    return Z_beta

def Z_L (Engrenagem) :
    sigma_h_lim = min([Engrenagem.material_coroa.Lim_pressao,Engrenagem.material_pinhao.Lim_pressao])
    if sigma_h_lim >= 850 and sigma_h_lim <= 1200 :
        C_ZL = (sigma_h_lim/4375) + 0.6357
    elif  sigma_h_lim < 850 :
        C_ZL = 0.83
    elif sigma_h_lim > 1200 :
        C_ZL = 0.91

    Z_L = C_ZL + ((4*(1-C_ZL))/(1.2+(134/Engrenagem.lubrificante.visc_40))**2)
    return Z_L
def Z_V (Engrenagem):
    sigma_h_lim = min([Engrenagem.material_coroa.Lim_pressao,Engrenagem.material_pinhao.Lim_pressao])
    if sigma_h_lim >= 850 and sigma_h_lim <= 1200 :
        C_ZL = (sigma_h_lim/4375) + 0.6357
    elif  sigma_h_lim < 850 :
        C_ZL = 0.83
    elif sigma_h_lim > 1200 :
        C_ZL = 0.91
    C_ZV = C_ZL + 0.02

    Z_V = C_ZV + ((2*(1- C_ZV))/(math.sqrt(0.8 + (32/Engrenagem.v_t))))

    return Z_V
def Z_R (Engrenagem):
    sigma_h_lim = min([Engrenagem.material_coroa.Lim_pressao,Engrenagem.material_pinhao.Lim_pressao])
    if sigma_h_lim >= 850 and sigma_h_lim <= 1200 :
        C_ZR = 0.32 - 0.0002 *sigma_h_lim
    elif  sigma_h_lim < 850 :
        C_ZR = 0.15
    elif sigma_h_lim > 1200 :
        C_ZR = 0.08

    R_zm = (Engrenagem.Rz_flanco_pinhao + Engrenagem.Rz_flanco_coroa)/2
    p_1 = 0.5*Engrenagem.db_pinhao * math.tan(math.radians(Engrenagem.alpha_wt))
    p_2 = 0.5*Engrenagem.db_coroa * math.tan(math.radians(Engrenagem.alpha_wt))

    p_red = (p_1*p_2)/(p_1 + p_2)

    R_z10 = R_zm * (10/p_red)**(1/3)

    Z_R = (3/R_z10)**C_ZR

    return Z_R
def Z_W (Engrenagem):
    HC = [0,2,4,6,8,10,12,14,16,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65]
    HB = [152,158,165,171,179,187,194,203,212,219,226,231,237,243,247,253,258,264,271,279,286,294,301,311,319,327,336,344,353,362,371,381,390,400,409,421,432,443,455,469,481,496,512,525,543,560,577,595,615,634,654,670,688,705,722,739]
    HC_pinhao = Engrenagem.material_pinhao.dureza_superficial
    Interp = interp1d(HC, HB, kind='linear')
    HB_pinhao = Interp(HC_pinhao)

    HC_coroa = Engrenagem.material_coroa.dureza_superficial
    Interp = interp1d(HC, HB, kind='linear')
    HB_coroa = Interp(HC_coroa)

    superf = (12,13,14,15,16,17)   # classes com endurecimento superficial (IF, Eh, NT, NV, carbonitretados)
    def _zw(HB_mole, HB_dura, dura_superficial):
        # ISO 6336-2 §8 (método B). Aplica-se à roda MAIS MACIA.
        if HB_dura <= HB_mole :
            return 1.0
        if dura_superficial :
            # roda temperada/normalizada (130 <= HB <= 470) contra pinhão endurecido superficialmente
            if HB_mole > 470 :
                return 1.0
            if HB_mole < 130 :
                HB_mole = 130
            return 1.2 - (HB_mole - 130)/1700
        # pinhão e roda temperados: só conta para HB_dura/HB_mole >= 1.2 (efeito < 1 %)
        r = HB_dura/HB_mole
        if r < 1.2 :
            return 1.0
        if r > 1.7 :
            r = 1.7
        return 1 + 0.00898*r - 0.00829
    Z_W_pinhao = _zw(HB_pinhao, HB_coroa, Engrenagem.material_coroa.classe in superf)
    Z_W_coroa = _zw(HB_coroa, HB_pinhao, Engrenagem.material_pinhao.classe in superf)

    return Z_W_pinhao,Z_W_coroa
def Z_X(Engrenagem):

    if Engrenagem.material_pinhao.classe_Z_X == 1:
        Z_X_pinhao = 1
    elif  Engrenagem.material_pinhao.classe_Z_X == 2:
        if Engrenagem.m_n <= 10 :
            Z_X_pinhao = 1
        elif Engrenagem.m_n > 10 and Engrenagem.m_n < 30 :
            Z_X_pinhao = 1.05 - 0.005 * Engrenagem.m_n
        elif Engrenagem.m_n >=30 :
            Z_X_pinhao = 0.9
    elif Engrenagem.material_pinhao.classe_Z_X == 3:
        if Engrenagem.m_n <= 7.5 :
            Z_X_pinhao = 1
        elif Engrenagem.m_n > 7.5 and Engrenagem.m_n < 30 :
            Z_X_pinhao = 1.08 - 0.011 * Engrenagem.m_n
        elif Engrenagem.m_n >=30 :
            Z_X_pinhao = 0.75


    if  Engrenagem.material_coroa.classe_Z_X == 1:
        Z_X_coroa = 1
    elif Engrenagem.material_coroa.classe_Z_X == 2:
        if Engrenagem.m_n <= 10 :
            Z_X_coroa = 1
        elif Engrenagem.m_n > 10 and Engrenagem.m_n < 30 :
            Z_X_coroa = 1.05 - 0.005 * Engrenagem.m_n
        elif Engrenagem.m_n >=30 :
            Z_X_coroa = 0.9
    elif Engrenagem.material_coroa.classe_Z_X == 3:
        if Engrenagem.m_n <= 7.5 :
            Z_X_coroa = 1
        elif Engrenagem.m_n > 7.5 and Engrenagem.m_n < 30 :
            Z_X_coroa = 1.08 - 0.011 * Engrenagem.m_n
        elif Engrenagem.m_n >=30 :
            Z_X_coroa = 0.75


    return Z_X_pinhao,Z_X_coroa



def Z_B(Engrenagem):
    M1 = (math.tan(math.radians(Engrenagem.alpha_wt)))/(math.sqrt((math.sqrt((Engrenagem.d_a_pinhao**2)/(Engrenagem.db_pinhao**2) - 1) - ((2*math.pi)/Engrenagem.Z_pinhao))*(math.sqrt((Engrenagem.d_a_coroa**2)/(Engrenagem.db_coroa**2) - 1)- (Engrenagem.epsilon_alpha - 1) * ((2*math.pi)/Engrenagem.Z_coroa))))

    if Engrenagem.beta == 0 :
        if M1 <= 1 :
            Z_B = 1
        elif M1 > 1 :
            Z_B = M1
    elif Engrenagem.beta != 0 :
        if Engrenagem.epsilon_beta >= 1 :
            Z_B = 1
        elif Engrenagem.epsilon_beta < 1 :
            Z_B = M1 - Engrenagem.epsilon_beta * (M1 - 1)
            if Z_B < 1 :
                Z_B = 1
    return Z_B
def Z_D(Engrenagem):
    M2 = (math.tan(math.radians(Engrenagem.alpha_wt)))/(math.sqrt((math.sqrt((Engrenagem.d_a_coroa**2)/(Engrenagem.db_coroa**2) - 1) - ((2*math.pi)/Engrenagem.Z_coroa))*(math.sqrt((Engrenagem.d_a_pinhao**2)/(Engrenagem.db_pinhao**2) - 1)- (Engrenagem.epsilon_alpha - 1) * ((2*math.pi)/Engrenagem.Z_pinhao))))
    if Engrenagem.Z_pinhao > 0 and Engrenagem.Z_coroa > 0 :
        if Engrenagem.beta == 0 :
            if M2 <= 1 :
                Z_D = 1
            elif M2 > 1 :
                Z_D = M2
        elif Engrenagem.beta != 0 :
            if Engrenagem.epsilon_beta >= 1 :
                Z_D = 1
            elif Engrenagem.epsilon_beta < 1 :
                Z_D = M2 - Engrenagem.epsilon_beta * (M2 - 1)
                if Z_D < 1 :
                    Z_D = 1

    elif Engrenagem.Z_pinhao < 0 or Engrenagem.Z_coroa < 0 :
        Z_D = 1

    return Z_D
def Z_NT (Engrenagem):
    N_L12 = 60*Engrenagem.Vr*Engrenagem.n_rel*Engrenagem.contatos_pinhao

    if Engrenagem.material_pinhao.classe_Z_NT == 1 :
        if math.log10(N_L12) > 7.69897 :
            A = math.exp((7.69897 - math.log10(N_L12)) / 14.15854) if getattr(Engrenagem, "curva_vida", "ISO") == "ISO" else 1.0   # ISO: decai até 0.85 em 1e10 ; DIN 3990: 1.0
        elif math.log10(N_L12) <= 7.69897 :
            A = math.exp((7.69897 - math.log10(N_L12)) / 5.742445)

        # curva com pites limitados (Z_GT): 1.6 ate 6e5 ciclos, 1.3 em 1e7, 1.0 em 1e9
        if math.log10(N_L12) > 9 :
            B = math.exp((9 - math.log10(N_L12)) / 6.153129)
        elif math.log10(N_L12) > 7 :
            B = math.exp((9 - math.log10(N_L12)) / 7.622989)
        else :
            B = math.exp((8.54387 - math.log10(N_L12)) / 5.884475)

        Z_Nlim = 1.6

    elif Engrenagem.material_pinhao.classe_Z_NT == 2 :
        if math.log10(N_L12) > 6.30103 :
            A = math.exp((6.30103 - math.log10(N_L12)) / 22.76024)
        else :
            A = math.exp((6.30103 - math.log10(N_L12)) / 4.958869)

        B = 0

        Z_Nlim = 1.3

    elif Engrenagem.material_pinhao.classe_Z_NT == 3 :
        if math.log10(N_L12) > 6.30103 :
            A = math.exp((6.30103 - math.log10(N_L12)) / 22.76024)
        else :
            A = math.exp((6.30103 - math.log10(N_L12)) / 13.65043)

        B = 0

        Z_Nlim = 1.1

    Z_NT_pinhao = min([A, Z_Nlim])


    Z_GT_pinhao = min([B , 1.6])


    N_L12 = 60*Engrenagem.Vr*(Engrenagem.n_rel/abs(Engrenagem.u))*Engrenagem.contatos_coroa

    if Engrenagem.material_coroa.classe_Z_NT == 1 :
        if math.log10(N_L12) > 7.69897 :
            A = math.exp((7.69897 - math.log10(N_L12)) / 14.15854) if getattr(Engrenagem, "curva_vida", "ISO") == "ISO" else 1.0   # ISO: decai até 0.85 em 1e10 ; DIN 3990: 1.0
        elif math.log10(N_L12) <= 7.69897 :
            A = math.exp((7.69897 - math.log10(N_L12)) / 5.742445)

        # curva com pites limitados (Z_GT): 1.6 ate 6e5 ciclos, 1.3 em 1e7, 1.0 em 1e9
        if math.log10(N_L12) > 9 :
            B = math.exp((9 - math.log10(N_L12)) / 6.153129)
        elif math.log10(N_L12) > 7 :
            B = math.exp((9 - math.log10(N_L12)) / 7.622989)
        else :
            B = math.exp((8.54387 - math.log10(N_L12)) / 5.884475)

        Z_Nlim = 1.6

    elif Engrenagem.material_coroa.classe_Z_NT == 2 :
        if math.log10(N_L12) > 6.30103 :
            A = math.exp((6.30103 - math.log10(N_L12)) / 22.76024)
        else :
            A = math.exp((6.30103 - math.log10(N_L12)) / 4.958869)
        B = 0
        Z_Nlim = 1.3

    elif Engrenagem.material_coroa.classe_Z_NT == 3 :
        if math.log10(N_L12) > 6.30103 :
            A = math.exp((6.30103 - math.log10(N_L12)) / 22.76024)
        else :
            A = math.exp((6.30103 - math.log10(N_L12)) / 13.65043)
        B = 0
        Z_Nlim = 1.1

    Z_NT_coroa = min([A, Z_Nlim])

    Z_GT_coroa = min([B , 1.6])


    return Z_NT_pinhao,Z_NT_coroa,Z_GT_pinhao,Z_GT_coroa
def Y_S(Engrenagem):
    L_pinhao = Engrenagem.S_fn_pinhao/Engrenagem.h_fe_pinhao
    q_s_pinhao = Engrenagem.S_fn_pinhao/(2* Engrenagem.p_f_pinhao)
    Y_S_pinhao = (1.2 + 0.13*L_pinhao) * q_s_pinhao**(1/(1.21 + 2.3/L_pinhao))

    if q_s_pinhao < 1 or q_s_pinhao >= 8 :
        AVISO1 = f"AVISO : O valor de q_s do pinhão está fora do range do qual o cálculo do parâmetro é válido (q_s = {round(q_s_pinhao,3)}"
    else :
        AVISO1 = None

    L_coroa = Engrenagem.S_fn_coroa/Engrenagem.h_fe_coroa
    q_s_coroa = Engrenagem.S_fn_coroa/(2* Engrenagem.p_f_coroa)
    Y_S_coroa = (1.2 + 0.13*L_coroa) * q_s_coroa**(1/(1.21 + 2.3/L_coroa))

    if q_s_coroa < 1 or q_s_coroa >= 8 :
        AVISO2 = f"AVISO : O valor de q_s da coroa está fora do range do qual o cálculo do parâmetro é válido (q_s = {round(q_s_coroa,3)}"
    else :
        AVISO2 = None

    return Y_S_pinhao,Y_S_coroa,AVISO1,AVISO2

def Y_epsilon(Engrenagem):
    # Fator de recobrimento para a flexão (ISO 6336-3 §6.3, DIN 3990): só no método C (carga na ponta) — converte a tensão
    # com carga na ponta para a carga no ponto exterior de engrenamento individual. No método B vale 1.
    if getattr(Engrenagem, "metodo_YF", "B") != "C" :
        return 1.0
    beta_b = math.asin(math.sin(math.radians(abs(Engrenagem.beta))) * math.cos(math.radians(Engrenagem.alpha_n)))
    eps_an = Engrenagem.epsilon_alpha / (math.cos(beta_b)**2)
    Y_eps = 0.25 + 0.75/eps_an
    if Y_eps < 0.625 :
        Y_eps = 0.625
    return Y_eps
def Y_beta(Engrenagem):

    if Engrenagem.beta !=0 :
        if abs(Engrenagem.beta) > 30:
            beta = 30
        else :
            beta = abs(Engrenagem.beta)

        if Engrenagem.epsilon_beta > 1 :
            epsilon_beta = 1
        else :
            epsilon_beta = Engrenagem.epsilon_beta
        Y_beta = (1 - epsilon_beta * (beta / 120))
    elif Engrenagem.beta ==0 :
        Y_beta = 1
    return Y_beta
def Y_B(Engrenagem):
    # ISO 6336-3 §7: fator de espessura de aro. Externa: s_R/h_t ; interna: s_R/m_n.
    # Fora da faixa valida (s_R/h_t <= 0.5 ou s_R/m_n <= 1.75) o aro e inadmissivel: lanca erro em vez de Y_B = 0.
    def _yb(s_R, h_t, m_n, d, nome):
        if d > 0 :
            r = s_R/h_t
            if r >= 1.2 :
                return 1.0
            elif r > 0.5 :
                return 1.6 * math.log(2.242 * h_t/s_R)
            raise ValueError(f"Y_B: aro do/da {nome} muito fino (s_R/h_t = {r:.3f} <= 0.5). Aumente a espessura do aro.")
        else :
            r = abs(s_R)/m_n
            if r >= 3.5 :
                return 1.0
            elif r > 1.75 :
                return 1.15 * math.log(8.324 * m_n/abs(s_R))
            raise ValueError(f"Y_B: aro do/da {nome} muito fino (s_R/m_n = {r:.3f} <= 1.75). Aumente a espessura do aro.")
    Y_B_pinhao = _yb(Engrenagem.s_pinhao, Engrenagem.h_dente_pinhao, Engrenagem.m_n, Engrenagem.d_pinhao, "pinhão")
    Y_B_coroa = _yb(Engrenagem.s_coroa, Engrenagem.h_dente_coroa, Engrenagem.m_n, Engrenagem.d_coroa, "coroa")
    return Y_B_pinhao,Y_B_coroa
def Y_delta_RefT(Engrenagem,YS_pinhao,YS_coroa):
    if Engrenagem.material_pinhao.classe_Y_Rel == 1 and Engrenagem.material_pinhao.Lim_tracao == 150 :
        rho = 0.3124
    elif Engrenagem.material_pinhao.classe_Y_Rel == 2 and Engrenagem.material_pinhao.Lim_tracao == 300 :
        rho = 0.3095
    elif (Engrenagem.material_pinhao.classe_Y_Rel == 1 and Engrenagem.material_pinhao.Lim_tracao != 150) or (Engrenagem.material_pinhao.classe_Y_Rel == 2 and Engrenagem.material_pinhao.Lim_tracao != 300) :
        rho_interp = [0.3124, 0.3095]
        lim_interp = [150,300]
        f = interp1d(lim_interp, rho_interp, kind='linear', fill_value='extrapolate')
        rho = f(Engrenagem.material_pinhao.Lim_tracao)

    elif Engrenagem.material_pinhao.classe_Y_Rel == 3 :
        rho = 0.3095
    elif Engrenagem.material_pinhao.classe_Y_Rel == 4 and Engrenagem.material_pinhao.Lim_escoa == 500 :
        rho = 0.0281
    elif Engrenagem.material_pinhao.classe_Y_Rel == 5 and Engrenagem.material_pinhao.Lim_escoa == 600 :
        rho = 0.0194
    elif Engrenagem.material_pinhao.classe_Y_Rel == 6 and Engrenagem.material_pinhao.Lim_escoa == 800 :
        rho = 0.0064
    elif Engrenagem.material_pinhao.classe_Y_Rel == 7 and Engrenagem.material_pinhao.Lim_escoa == 1000 :
        rho = 0.0014
    elif (Engrenagem.material_pinhao.classe_Y_Rel == 4 and Engrenagem.material_pinhao.Lim_escoa != 500) or (Engrenagem.material_pinhao.classe_Y_Rel == 5 and Engrenagem.material_pinhao.Lim_escoa != 600) or (Engrenagem.material_pinhao.classe_Y_Rel == 6 and Engrenagem.material_pinhao.Lim_escoa != 800) or (Engrenagem.material_pinhao.classe_Y_Rel == 7 and Engrenagem.material_pinhao.Lim_escoa != 1000) :
        rho_interp = [0.0281, 0.0194,0.0064,0.0014]
        lim_interp = [500,600,800,1000]
        f = interp1d(lim_interp, rho_interp, kind='linear', fill_value='extrapolate')
        rho = f(Engrenagem.material_pinhao.Lim_escoa)
    elif Engrenagem.material_pinhao.classe_Y_Rel == 8 and Engrenagem.material_pinhao.Lim_escoa == 300 :
        rho = 0.0833
    elif Engrenagem.material_pinhao.classe_Y_Rel == 9 and Engrenagem.material_pinhao.Lim_escoa == 400 :
        rho = 0.0445
    elif (Engrenagem.material_pinhao.classe_Y_Rel == 8 and Engrenagem.material_pinhao.Lim_escoa != 300) or (Engrenagem.material_pinhao.classe_Y_Rel == 9 and Engrenagem.material_pinhao.Lim_escoa != 400):
        rho_interp = [0.0833, 0.0445]
        lim_interp = [300,400]
        f = interp1d(lim_interp, rho_interp, kind='linear', fill_value='extrapolate')
        rho = f(Engrenagem.material_pinhao.Lim_escoa)

    elif Engrenagem.material_pinhao.classe_Y_Rel == 10 and Engrenagem.material_pinhao.Lim_escoa == 500 :
        rho = 0.0281
    elif Engrenagem.material_pinhao.classe_Y_Rel == 11 and Engrenagem.material_pinhao.Lim_escoa == 600 :
        rho = 0.0194
    elif Engrenagem.material_pinhao.classe_Y_Rel == 12 and Engrenagem.material_pinhao.Lim_escoa == 800 :
        rho = 0.0064
    elif Engrenagem.material_pinhao.classe_Y_Rel == 13 and Engrenagem.material_pinhao.Lim_escoa == 1000 :
        rho = 0.0014

    elif (Engrenagem.material_pinhao.classe_Y_Rel == 10 and Engrenagem.material_pinhao.Lim_escoa != 500) or (Engrenagem.material_pinhao.classe_Y_Rel == 11 and Engrenagem.material_pinhao.Lim_escoa != 600) or (Engrenagem.material_pinhao.classe_Y_Rel == 12 and Engrenagem.material_pinhao.Lim_escoa != 800) or (Engrenagem.material_pinhao.classe_Y_Rel == 13 and Engrenagem.material_pinhao.Lim_escoa != 1000) :
        rho_interp = [0.0281, 0.0194,0.0064,0.0014]
        lim_interp = [500,600,800,1000]
        f = interp1d(lim_interp, rho_interp, kind='linear', fill_value='extrapolate')
        rho = max(float(f(Engrenagem.material_pinhao.Lim_escoa)), 1e-6)
    elif Engrenagem.material_pinhao.classe_Y_Rel == 14 :
        rho = 0.1005
    elif Engrenagem.material_pinhao.classe_Y_Rel == 15 :
        rho = 0.0030
    elif Engrenagem.material_pinhao.classe_Y_Rel == 16 :
        rho = 0.0030

    q_s = Engrenagem.S_fn_pinhao/(2* Engrenagem.p_f_pinhao)

    chi = 0.2*(1+2*q_s)
    chi_T = 0.2*(1+2*2.5)

    Y_delta_RefT_Ref = (1+ math.sqrt(rho * chi ))/(1+ math.sqrt(rho * chi_T))

    if Engrenagem.material_pinhao.classe_Y_Rel == 8 or Engrenagem.material_pinhao.classe_Y_Rel == 9 :
        Y_delta_RefT_Est = (1+ 0.93*(YS_pinhao - 1) * (200/Engrenagem.material_pinhao.Lim_escoa)**0.25)/(1+ 0.93 * (200/Engrenagem.material_pinhao.Lim_escoa)**0.25)
    elif Engrenagem.material_pinhao.classe_Y_Rel == 6 or Engrenagem.material_pinhao.classe_Y_Rel == 7 or Engrenagem.material_pinhao.classe_Y_Rel == 12 or Engrenagem.material_pinhao.classe_Y_Rel == 13 or Engrenagem.material_pinhao.classe_Y_Rel == 4 or Engrenagem.material_pinhao.classe_Y_Rel == 5 or Engrenagem.material_pinhao.classe_Y_Rel == 10 or Engrenagem.material_pinhao.classe_Y_Rel == 11:
        Y_delta_RefT_Est = (1+ 0.82*(YS_pinhao - 1) * (300/Engrenagem.material_pinhao.Lim_escoa)**0.25)/(1+ 0.82 * (300/Engrenagem.material_pinhao.Lim_escoa)**0.25)
    elif Engrenagem.material_pinhao.classe_Y_Rel == 15 or Engrenagem.material_pinhao.classe_Y_Rel == 16  :
        Y_delta_RefT_Est = 0.44*YS_pinhao + 0.12
    elif Engrenagem.material_pinhao.classe_Y_Rel == 14 :
        Y_delta_RefT_Est = 0.20*YS_pinhao + 0.60
    elif Engrenagem.material_pinhao.classe_Y_Rel == 1 or Engrenagem.material_pinhao.classe_Y_Rel == 2 or Engrenagem.material_pinhao.classe_Y_Rel == 3 :
        Y_delta_RefT_Est = 1

    N_L1 = 60*Engrenagem.Vr*Engrenagem.n_rel*Engrenagem.contatos_pinhao

    if N_L1 > 3e06  :
        N_LL = 3e06
    elif N_L1 <= 3e06  :
        N_LL = N_L1

    if Engrenagem.material_pinhao.classe_Y_Rel >=4 and  Engrenagem.material_pinhao.classe_Y_Rel <=13 :
        if N_L1 <= 1e04 :
            Y_delta_RefT_pinhao = Y_delta_RefT_Est
        elif N_L1 > 1e04 :
            Y_delta_RefT_pinhao = ((Y_delta_RefT_Est - Y_delta_RefT_Ref)/(3e06 - 1e04))*(3e06  - N_LL) + Y_delta_RefT_Ref

    elif (Engrenagem.material_pinhao.classe_Y_Rel >=1 and  Engrenagem.material_pinhao.classe_Y_Rel <=3) or ((Engrenagem.material_pinhao.classe_Y_Rel >=14 and  Engrenagem.material_pinhao.classe_Y_Rel <=16)) :
        if N_L1 <= 1e03 :
            Y_delta_RefT_pinhao = Y_delta_RefT_Est
        elif N_L1 > 1e03 :
            Y_delta_RefT_pinhao = ((Y_delta_RefT_Est - Y_delta_RefT_Ref)/(3e06 - 1e03))*(3e06  - N_LL) + Y_delta_RefT_Ref


    if Engrenagem.material_coroa.classe_Y_Rel == 1 and Engrenagem.material_coroa.Lim_tracao == 150 :
        rho = 0.3124
    elif Engrenagem.material_coroa.classe_Y_Rel == 2 and Engrenagem.material_coroa.Lim_tracao == 300 :
        rho = 0.3095
    elif (Engrenagem.material_coroa.classe_Y_Rel == 1 and Engrenagem.material_coroa.Lim_tracao != 150) or (Engrenagem.material_coroa.classe_Y_Rel == 2 and Engrenagem.material_coroa.Lim_tracao != 300) :
        rho_interp = [0.3124, 0.3095]
        lim_interp = [150,300]
        f = interp1d(lim_interp, rho_interp, kind='linear', fill_value='extrapolate')
        rho = f(Engrenagem.material_coroa.Lim_tracao)

    elif Engrenagem.material_coroa.classe_Y_Rel == 3 :
        rho = 0.3095
    elif Engrenagem.material_coroa.classe_Y_Rel == 4 and Engrenagem.material_coroa.Lim_escoa == 500 :
        rho = 0.0281
    elif Engrenagem.material_coroa.classe_Y_Rel == 5 and Engrenagem.material_coroa.Lim_escoa == 600 :
        rho = 0.0194
    elif Engrenagem.material_coroa.classe_Y_Rel == 6 and Engrenagem.material_coroa.Lim_escoa == 800 :
        rho = 0.0064
    elif Engrenagem.material_coroa.classe_Y_Rel == 7 and Engrenagem.material_coroa.Lim_escoa == 1000 :
        rho = 0.0014
    elif (Engrenagem.material_coroa.classe_Y_Rel == 4 and Engrenagem.material_coroa.Lim_escoa != 500) or (Engrenagem.material_coroa.classe_Y_Rel == 5 and Engrenagem.material_coroa.Lim_escoa != 600) or (Engrenagem.material_coroa.classe_Y_Rel == 6 and Engrenagem.material_coroa.Lim_escoa != 800) or (Engrenagem.material_coroa.classe_Y_Rel == 7 and Engrenagem.material_coroa.Lim_escoa != 1000) :
        rho_interp = [0.0281, 0.0194,0.0064,0.0014]
        lim_interp = [500,600,800,1000]
        f = interp1d(lim_interp, rho_interp, kind='linear', fill_value='extrapolate')
        rho = f(Engrenagem.material_coroa.Lim_escoa)
    elif Engrenagem.material_coroa.classe_Y_Rel == 8 and Engrenagem.material_coroa.Lim_escoa == 300 :
        rho = 0.0833
    elif Engrenagem.material_coroa.classe_Y_Rel == 9 and Engrenagem.material_coroa.Lim_escoa == 400 :
        rho = 0.0445
    elif (Engrenagem.material_coroa.classe_Y_Rel == 8 and Engrenagem.material_coroa.Lim_escoa != 300) or (Engrenagem.material_coroa.classe_Y_Rel == 9 and Engrenagem.material_coroa.Lim_escoa != 400):
        rho_interp = [0.0833, 0.0445]
        lim_interp = [300,400]
        f = interp1d(lim_interp, rho_interp, kind='linear', fill_value='extrapolate')
        rho = f(Engrenagem.material_coroa.Lim_escoa)

    elif Engrenagem.material_coroa.classe_Y_Rel == 10 and Engrenagem.material_coroa.Lim_escoa == 500 :
        rho = 0.0281
    elif Engrenagem.material_coroa.classe_Y_Rel == 11 and Engrenagem.material_coroa.Lim_escoa == 600 :
        rho = 0.0194
    elif Engrenagem.material_coroa.classe_Y_Rel == 12 and Engrenagem.material_coroa.Lim_escoa == 800 :
        rho = 0.0064
    elif Engrenagem.material_coroa.classe_Y_Rel == 13 and Engrenagem.material_coroa.Lim_escoa == 1000 :
        rho = 0.0014

    elif (Engrenagem.material_coroa.classe_Y_Rel == 10 and Engrenagem.material_coroa.Lim_escoa != 500) or (Engrenagem.material_coroa.classe_Y_Rel == 11 and Engrenagem.material_coroa.Lim_escoa != 600) or (Engrenagem.material_coroa.classe_Y_Rel == 12 and Engrenagem.material_coroa.Lim_escoa != 800) or (Engrenagem.material_coroa.classe_Y_Rel == 13 and Engrenagem.material_coroa.Lim_escoa != 1000) :
        rho_interp = [0.0281, 0.0194,0.0064,0.0014]
        lim_interp = [500,600,800,1000]
        f = interp1d(lim_interp, rho_interp, kind='linear', fill_value='extrapolate')
        rho = max(float(f(Engrenagem.material_coroa.Lim_escoa)), 1e-6)
    elif Engrenagem.material_coroa.classe_Y_Rel == 14 :
        rho = 0.1005
    elif Engrenagem.material_coroa.classe_Y_Rel == 15 :
        rho = 0.0030
    elif Engrenagem.material_coroa.classe_Y_Rel == 16 :
        rho = 0.0030

    q_s = Engrenagem.S_fn_coroa/(2* Engrenagem.p_f_coroa)

    chi = 0.2*(1+2*q_s)
    chi_T = 0.2*(1+2*2.5)

    Y_delta_RefT_Ref = (1+ math.sqrt(rho * chi ))/(1+ math.sqrt(rho * chi_T))

    if Engrenagem.material_coroa.classe_Y_Rel == 8 or Engrenagem.material_coroa.classe_Y_Rel == 9 :
        Y_delta_RefT_Est = (1+ 0.93*(YS_coroa - 1) * (200/Engrenagem.material_coroa.Lim_escoa)**0.25)/(1+ 0.93 * (200/Engrenagem.material_coroa.Lim_escoa)**0.25)
    elif Engrenagem.material_coroa.classe_Y_Rel == 6 or Engrenagem.material_coroa.classe_Y_Rel == 7 or Engrenagem.material_coroa.classe_Y_Rel == 12 or Engrenagem.material_coroa.classe_Y_Rel == 13 or Engrenagem.material_coroa.classe_Y_Rel == 4 or Engrenagem.material_coroa.classe_Y_Rel == 5 or Engrenagem.material_coroa.classe_Y_Rel == 10 or Engrenagem.material_coroa.classe_Y_Rel == 11:
        Y_delta_RefT_Est = (1+ 0.82*(YS_coroa - 1) * (300/Engrenagem.material_coroa.Lim_escoa)**0.25)/(1+ 0.82 * (300/Engrenagem.material_coroa.Lim_escoa)**0.25)
    elif Engrenagem.material_coroa.classe_Y_Rel == 15 or Engrenagem.material_coroa.classe_Y_Rel == 16  :
        Y_delta_RefT_Est = 0.44*YS_coroa + 0.12
    elif Engrenagem.material_coroa.classe_Y_Rel == 14 :
        Y_delta_RefT_Est = 0.20*YS_coroa + 0.60
    elif Engrenagem.material_coroa.classe_Y_Rel == 1 or Engrenagem.material_coroa.classe_Y_Rel == 2 or Engrenagem.material_coroa.classe_Y_Rel == 3 :
        Y_delta_RefT_Est = 1

    N_L2 = 60*Engrenagem.Vr*(Engrenagem.n_rel/abs(Engrenagem.u))*Engrenagem.contatos_coroa

    if N_L2 > 3e06 :
        N_LL = 3e06
    elif N_L2 <= 3e06  :
        N_LL = N_L2

    if Engrenagem.material_coroa.classe_Y_Rel >=4 and  Engrenagem.material_coroa.classe_Y_Rel <=13 :
        if N_L2 <= 1e04 :
            Y_delta_RefT_coroa = Y_delta_RefT_Est
        elif N_L2 > 1e04 :
            Y_delta_RefT_coroa = ((Y_delta_RefT_Est - Y_delta_RefT_Ref)/(3e06 - 1e04))*(3e06  - N_LL) + Y_delta_RefT_Ref

    elif (Engrenagem.material_coroa.classe_Y_Rel >=1 and  Engrenagem.material_coroa.classe_Y_Rel <=3) or ((Engrenagem.material_coroa.classe_Y_Rel >=14 and  Engrenagem.material_coroa.classe_Y_Rel <=16)) :
        if N_L2 <= 1e03 :
            Y_delta_RefT_coroa = Y_delta_RefT_Est
        elif N_L2 > 1e03 :
            Y_delta_RefT_coroa = ((Y_delta_RefT_Est - Y_delta_RefT_Ref)/(3e06 - 1e03))*(3e06  - N_LL) + Y_delta_RefT_Ref


    return Y_delta_RefT_pinhao,Y_delta_RefT_coroa







def Y_R_RefT(Engrenagem) :

    if Engrenagem.Rz_pe_pinhao < 1 :
        if Engrenagem.material_pinhao.classe_Y_R_RelT == 1 :
            Y_R_RelT_Ref = 1.120
        elif Engrenagem.material_pinhao.classe_Y_R_RelT == 2 :
            Y_R_RelT_Ref = 1.070
        elif Engrenagem.material_pinhao.classe_Y_R_RelT == 3 :
            Y_R_RelT_Ref = 1.025

    if Engrenagem.Rz_pe_pinhao >= 1 :
        if  Engrenagem.material_pinhao.classe_Y_R_RelT == 1  :
            Y_R_RelT_Ref = 1.674 - 0.529*(Engrenagem.Rz_pe_pinhao + 1)**0.1
        elif Engrenagem.material_pinhao.classe_Y_R_RelT == 2  :
            Y_R_RelT_Ref = 5.306 - 4.203*(Engrenagem.Rz_pe_pinhao + 1)**0.01
        elif Engrenagem.material_pinhao.classe_Y_R_RelT == 3  :
            Y_R_RelT_Ref = 4.299 - 3.259*(Engrenagem.Rz_pe_pinhao + 1)**0.005

    Y_R_RelT_Est = 1

    N_L1 = 60*Engrenagem.Vr*Engrenagem.n_rel*Engrenagem.contatos_pinhao

    if Engrenagem.material_pinhao.classe_Y_Rel >=4 and  Engrenagem.material_pinhao.classe_Y_Rel <=13 :
        if N_L1 <= 1e04 :
            Y_R_RefT_pinhao = Y_R_RelT_Est
        elif N_L1 > 1e04 :
            Y_R_RefT_pinhao = Y_R_RelT_Ref

    elif (Engrenagem.material_pinhao.classe_Y_Rel >=1 and  Engrenagem.material_pinhao.classe_Y_Rel <=3) or ((Engrenagem.material_pinhao.classe_Y_Rel >=14 and  Engrenagem.material_pinhao.classe_Y_Rel <=16)) :
        if N_L1 <= 1e03 :
            Y_R_RefT_pinhao = Y_R_RelT_Est
        elif N_L1 > 1e03 :
            Y_R_RefT_pinhao = Y_R_RelT_Ref



    if Engrenagem.Rz_pe_coroa < 1 :
        if  Engrenagem.material_coroa.classe_Y_R_RelT == 1 :
            Y_R_RelT_Ref = 1.120
        elif Engrenagem.material_coroa.classe_Y_R_RelT == 2 :
            Y_R_RelT_Ref = 1.070
        elif Engrenagem.material_coroa.classe_Y_R_RelT == 3 :
            Y_R_RelT_Ref = 1.025

    if Engrenagem.Rz_pe_coroa >= 1 :
        if  Engrenagem.material_coroa.classe_Y_R_RelT == 1 :
            Y_R_RelT_Ref = 1.674 - 0.529*(Engrenagem.Rz_pe_coroa + 1)**0.1
        elif Engrenagem.material_coroa.classe_Y_R_RelT == 2 :
            Y_R_RelT_Ref = 5.306 - 4.203*(Engrenagem.Rz_pe_coroa + 1)**0.01
        elif Engrenagem.material_coroa.classe_Y_R_RelT == 3:
            Y_R_RelT_Ref = 4.299 - 3.259*(Engrenagem.Rz_pe_coroa + 1)**0.005

    Y_R_RelT_Est = 1

    N_L1 = 60*Engrenagem.Vr*(Engrenagem.n_rel/abs(Engrenagem.u))*Engrenagem.contatos_coroa

    if Engrenagem.material_coroa.classe_Y_Rel >=4 and  Engrenagem.material_coroa.classe_Y_Rel <=13 :
        if N_L1 <= 1e04 :
            Y_R_RefT_coroa = Y_R_RelT_Est
        elif N_L1 > 1e04 :
            Y_R_RefT_coroa = Y_R_RelT_Ref

    elif (Engrenagem.material_coroa.classe_Y_Rel >=1 and  Engrenagem.material_coroa.classe_Y_Rel <=3) or ((Engrenagem.material_coroa.classe_Y_Rel >=14 and  Engrenagem.material_coroa.classe_Y_Rel <=16)) :
        if N_L1 <= 1e03 :
            Y_R_RefT_coroa = Y_R_RelT_Est
        elif N_L1 > 1e03 :
            Y_R_RefT_coroa = Y_R_RelT_Ref

    return Y_R_RefT_pinhao,Y_R_RefT_coroa

def Y_X(Engrenagem):
    if Engrenagem.material_pinhao.classe_Y_X == 1 :
        if Engrenagem.m_n <= 5 :
            Y_X_Ref_pinhao = 1
        elif Engrenagem.m_n > 5  and Engrenagem.m_n < 30 :
            Y_X_Ref_pinhao = 1.03 - 0.006*Engrenagem.m_n
        elif Engrenagem.m_n >= 30 :
            Y_X_Ref_pinhao = 0.85
    elif Engrenagem.material_pinhao.classe_Y_X == 2 :
        if Engrenagem.m_n <= 5 :
            Y_X_Ref_pinhao = 1
        elif Engrenagem.m_n > 5  and Engrenagem.m_n < 25 :
            Y_X_Ref_pinhao = 1.05 - 0.01*Engrenagem.m_n
        elif Engrenagem.m_n >= 25 :
            Y_X_Ref_pinhao = 0.8
    elif Engrenagem.material_pinhao.classe_Y_X == 3 :
        if Engrenagem.m_n <= 5 :
            Y_X_Ref_pinhao = 1
        elif Engrenagem.m_n > 5  and Engrenagem.m_n < 25 :
            Y_X_Ref_pinhao = 1.075 - 0.015*Engrenagem.m_n
        elif Engrenagem.m_n >= 25 :
            Y_X_Ref_pinhao = 0.7

    Y_X_Est_pinhao = 1
    N_L = 60*Engrenagem.Vr*Engrenagem.n_rel*Engrenagem.contatos_pinhao
    if N_L <= 3e06 :
        Y_X_pinhao = ((Y_X_Est_pinhao - Y_X_Ref_pinhao )/(3e06 - 1e03))*(3e06 - N_L) + Y_X_Ref_pinhao
    else :
        Y_X_pinhao = Y_X_Ref_pinhao



    if Engrenagem.material_coroa.classe_Y_X == 1 :
        if Engrenagem.m_n <= 5 :
            Y_X_Ref_coroa = 1
        elif Engrenagem.m_n > 5  and Engrenagem.m_n < 30 :
            Y_X_Ref_coroa = 1.03 - 0.006*Engrenagem.m_n
        elif Engrenagem.m_n >= 30 :
            Y_X_Ref_coroa = 0.85
    elif Engrenagem.material_coroa.classe_Y_X == 2 :
        if Engrenagem.m_n <= 5 :
            Y_X_Ref_coroa = 1
        elif Engrenagem.m_n > 5  and Engrenagem.m_n < 25 :
            Y_X_Ref_coroa = 1.05 - 0.01*Engrenagem.m_n
        elif Engrenagem.m_n >= 25 :
            Y_X_Ref_coroa = 0.8
    elif Engrenagem.material_coroa.classe_Y_X == 3 :
        if Engrenagem.m_n <= 5 :
            Y_X_Ref_coroa = 1
        elif Engrenagem.m_n > 5  and Engrenagem.m_n < 25 :
            Y_X_Ref_coroa = 1.075 - 0.015*Engrenagem.m_n
        elif Engrenagem.m_n >= 25 :
            Y_X_Ref_coroa = 0.7

    Y_X_Est_coroa = 1
    N_L = 60*Engrenagem.Vr*(Engrenagem.n_rel/abs(Engrenagem.u))*Engrenagem.contatos_coroa
    if N_L <= 3e06 :
        Y_X_coroa = ((Y_X_Est_coroa - Y_X_Ref_coroa )/(3e06 - 1e03))*(3e06 - N_L) + Y_X_Ref_coroa
    else :
         Y_X_coroa = Y_X_Ref_coroa


    return(Y_X_pinhao,Y_X_coroa)

def Y_NT (Engrenagem) :

    N_L = 60 * Engrenagem.Vr * Engrenagem.n_rel * Engrenagem.contatos_pinhao
    if N_L <= 3e06 :
        if Engrenagem.material_pinhao.classe_Y_NT == 1 :
            if N_L <= 1e04 :
                Y_NT_pinhao = 2.5
            elif  N_L > 1e04 and N_L <= 3e06 :
                Y_NT_pinhao = (10.978)/(N_L**0.160646)
        elif Engrenagem.material_pinhao.classe_Y_NT== 2 :
            if N_L <= 1e03 :
                Y_NT_pinhao = 2.5
            elif  N_L > 1e03 and N_L <= 3e06 :
                Y_NT_pinhao = (5.49921)/(N_L**0.114295)
        elif Engrenagem.material_pinhao.classe_Y_NT == 3 :
            if N_L <= 1e03 :
                Y_NT_pinhao = 1.6
            elif  N_L > 1e03 and N_L <= 3e06 :
                Y_NT_pinhao = (2.40011)/(N_L**0.0587037)
        elif Engrenagem.material_pinhao.classe_Y_NT == 4 :
            if N_L <= 1e03 :
                Y_NT_pinhao = 1.1
            elif  N_L > 1e03 and N_L <= 3e06 :
                Y_NT_pinhao = (1.19428)/(N_L**0.0119043)
    elif N_L > 3e06 :
        Y_NT_pinhao = (1.34825)/(N_L**0.0200351) if getattr(Engrenagem, "curva_vida", "ISO") == "ISO" else 1.0   # ISO: decai até 0.85 em 1e10 ; DIN 3990: 1.0



    N_L = 60 * Engrenagem.Vr * (Engrenagem.n_rel/abs(Engrenagem.u)) * Engrenagem.contatos_coroa
    if N_L <= 3e06 :
        if Engrenagem.material_coroa.classe_Y_NT == 1 :
            if N_L <= 1e04 :
                Y_NT_coroa = 2.5
            elif  N_L > 1e04 and N_L <= 3e06 :
                Y_NT_coroa = (10.978)/(N_L**0.160646)
        elif Engrenagem.material_coroa.classe_Y_NT== 2 :
            if N_L <= 1e03 :
                Y_NT_coroa = 2.5
            elif  N_L > 1e03 and N_L <= 3e06 :
                Y_NT_coroa = (5.49921)/(N_L**0.114295)
        elif Engrenagem.material_coroa.classe_Y_NT == 3 :
            if N_L <= 1e03 :
                Y_NT_coroa = 1.6
            elif  N_L > 1e03 and N_L <= 3e06 :
                Y_NT_coroa = (2.40011)/(N_L**0.0587037)
        elif Engrenagem.material_coroa.classe_Y_NT == 4 :
            if N_L <= 1e03 :
                Y_NT_coroa = 1.1
            elif  N_L > 1e03 and N_L <= 3e06 :
                Y_NT_coroa = (1.19428)/(N_L**0.0119043)
    elif N_L > 3e06 :
        Y_NT_coroa = (1.34825)/(N_L**0.0200351) if getattr(Engrenagem, "curva_vida", "ISO") == "ISO" else 1.0

    return Y_NT_pinhao, Y_NT_coroa
def Tensao_contato (Engrenagem,Kv,K_Hbeta,K_Halpha,Z_H,Z_E,Z_epsilon,Z_beta,Z_L,Z_V,Z_R,Z_W_pinhao,Z_W_coroa,Z_Xpinhao,Z_Xcoroa,Z_B,Z_D,Z_NT_pinhao,Z_NT_coroa,Z_GT_pinhao,Z_GT_coroa) :

    sigma_H0 = Z_H * Z_E * Z_epsilon * Z_beta * math.sqrt(((Engrenagem.Ft)/(Engrenagem.d_pinhao * Engrenagem.b)) * ((Engrenagem.u+1)/(Engrenagem.u)))
    sigma_Hpinhao = Z_B * sigma_H0 * math.sqrt(Engrenagem.Ka * Kv * K_Hbeta * K_Halpha)
    sigma_Hcoroa = Z_D * sigma_H0 * math.sqrt(Engrenagem.Ka * Kv * K_Hbeta * K_Halpha)
    sigma_HP_pinhao = Engrenagem.material_pinhao.Lim_pressao * Z_NT_pinhao * Z_L * Z_V * Z_R * Z_W_pinhao * Z_Xpinhao
    sigma_HP_coroa = Engrenagem.material_coroa.Lim_pressao * Z_NT_coroa * Z_L * Z_V * Z_R * Z_W_coroa * Z_Xcoroa
    sigma_GP_pinhao = Engrenagem.material_pinhao.Lim_pressao * Z_GT_pinhao * Z_L * Z_V * Z_R * Z_W_pinhao * Z_Xpinhao
    sigma_GP_coroa = Engrenagem.material_coroa.Lim_pressao * Z_GT_coroa * Z_L * Z_V * Z_R * Z_W_coroa * Z_Xcoroa

    S_Hpinhao = sigma_HP_pinhao/sigma_Hpinhao
    S_Hcoroa = sigma_HP_coroa/sigma_Hcoroa

    S_Gpinhao = sigma_GP_pinhao/sigma_Hpinhao
    S_Gcoroa = sigma_GP_coroa/sigma_Hcoroa

    if S_Hpinhao < Engrenagem.S_Hmin :
        AVISO1 = f"AVISO : Coeficiente de segurança sem pites para o pinhão menor que o mínimo (coeficient mínimo = {round(Engrenagem.S_Hmin,4)} ; Coeficiente de segurança calculado = {round(S_Hpinhao,4)}) \n"
    else :
        AVISO1 = None
    if S_Hcoroa < Engrenagem.S_Hmin :
        AVISO2 = f"AVISO : Coeficiente de segurança sem pites para a coroa menor que o mínimo (coeficient mínimo = {round(Engrenagem.S_Hmin,4)} ; Coeficiente de segurança calculado = {round(S_Hcoroa,4)}) \n"
    else:
        AVISO2 = None

    if S_Gpinhao < Engrenagem.S_Hmin :
        AVISO3 = f"AVISO : Coeficiente de segurança com pites para o pinhão menor que o mínimo (coeficient mínimo = {round(Engrenagem.S_Hmin,4)} ; Coeficiente de segurança calculado = {round(S_Gpinhao,4)}) \n"
    else :
        AVISO3 = None
    if S_Gcoroa < Engrenagem.S_Hmin :
        AVISO4 = f"AVISO : Coeficiente de segurança com pites para a coroa menor que o mínimo (coeficient mínimo = {round(Engrenagem.S_Hmin,4)} ; Coeficiente de segurança calculado = {round(S_Gcoroa,4)}) \n"
    else:
        AVISO4 = None

    Z_N_pinhao = (sigma_Hpinhao)/(Engrenagem.material_pinhao.Lim_pressao * Z_L * Z_V * Z_R * Z_W_pinhao * Z_Xpinhao)
    Z_N_coroa = (sigma_Hcoroa)/(Engrenagem.material_coroa.Lim_pressao * Z_L * Z_V * Z_R * Z_W_coroa * Z_Xcoroa)

    if Engrenagem.material_pinhao.classe_Z_NT == 1 :
        if Z_N_pinhao < 1 :
            N_LH_pinhao = 10**(7.69897 - 14.158535 * math.log(Z_N_pinhao))
        elif Z_N_pinhao >= 1 and Z_N_pinhao <=1.6 :
            N_LH_pinhao = 10**(7.69897 - 5.742445 * math.log(Z_N_pinhao))
        elif Z_N_pinhao > 1.6 :
            N_LH_pinhao = 1e05
        if Z_N_pinhao < 1 :
            N_LG_pinhao = 10**(9 - 6.153129 * math.log(Z_N_pinhao))
        elif Z_N_pinhao >= 1 and Z_N_pinhao < 1.3 :
            N_LG_pinhao = 10**(9 - 7.622989 * math.log(Z_N_pinhao))
        elif Z_N_pinhao >= 1.3 and Z_N_pinhao <= 1.6 :
            N_LG_pinhao = 10**(8.54387 - 5.884475 * math.log(Z_N_pinhao))
        elif Z_N_pinhao > 1.6 :
            N_LG_pinhao = 6e05
    if Engrenagem.material_pinhao.classe_Z_NT == 2 :
        if Z_N_pinhao < 1 :
            N_LH_pinhao = 10**(6.30103 - 22.76024 * math.log(Z_N_pinhao))
        elif Z_N_pinhao >= 1 and Z_N_pinhao <=1.3 :
            N_LH_pinhao = 10**(6.30103 - 4.958869 * math.log(Z_N_pinhao))
        elif Z_N_pinhao > 1.3 :
            N_LH_pinhao = 1e05
        N_LG_pinhao = 0
    if Engrenagem.material_pinhao.classe_Z_NT == 3 :
        if Z_N_pinhao < 1 :
            N_LH_pinhao = 10**(6.30103 - 22.76024 * math.log(Z_N_pinhao))
        elif Z_N_pinhao >= 1 and Z_N_pinhao <=1.1 :
            N_LH_pinhao = 10**(6.30103 - 13.65048 * math.log(Z_N_pinhao))
        elif Z_N_pinhao > 1.1 :
            N_LH_pinhao = 1e05
        N_LG_pinhao = 0

    if Engrenagem.material_coroa.classe_Z_NT == 1 :
        if Z_N_coroa < 1 :
            N_LH_coroa = 10**(7.69897 - 14.158535 * math.log(Z_N_coroa))
        elif Z_N_coroa >= 1 and Z_N_coroa <=1.6 :
            N_LH_coroa = 10**(7.69897 - 5.742445 * math.log(Z_N_coroa))
        elif Z_N_coroa > 1.6 :
            N_LH_coroa = 1e05
        if Z_N_coroa < 1 :
            N_LG_coroa = 10**(9 - 6.153129 * math.log(Z_N_coroa))
        elif Z_N_coroa >= 1 and Z_N_coroa < 1.3 :
            N_LG_coroa = 10**(9 - 7.622989 * math.log(Z_N_coroa))
        elif Z_N_coroa >= 1.3 and Z_N_coroa <= 1.6 :
            N_LG_coroa = 10**(8.54387 - 5.884475 * math.log(Z_N_coroa))
        elif Z_N_coroa > 1.6 :
            N_LG_coroa = 6e05
    if Engrenagem.material_coroa.classe_Z_NT == 2 :
        if Z_N_coroa < 1 :
            N_LH_coroa = 10**(6.30103 - 22.76024 * math.log(Z_N_coroa))
        elif Z_N_coroa >= 1 and Z_N_coroa <=1.3 :
            N_LH_coroa = 10**(6.30103 - 4.958869 * math.log(Z_N_coroa))
        elif Z_N_coroa > 1.3 :
            N_LH_coroa = 1e05
        N_LG_coroa = 0
    if Engrenagem.material_coroa.classe_Z_NT == 3 :
        if Z_N_coroa < 1 :
            N_LH_coroa = 10**(6.30103 - 22.76024 * math.log(Z_N_coroa))
        elif Z_N_coroa >= 1 and Z_N_coroa <=1.1 :
            N_LH_coroa = 10**(6.30103 - 13.65048 * math.log(Z_N_coroa))
        elif Z_N_coroa > 1.1 :
            N_LH_coroa = 1e05
        N_LG_coroa = 0

    VH_pinhao = (N_LH_pinhao)/(60 * Engrenagem.n_rel * Engrenagem.contatos_pinhao)
    VH_coroa = (N_LH_coroa)/(60 * (Engrenagem.n_rel/abs(Engrenagem.u)) * Engrenagem.contatos_coroa)
    VG_pinhao = (N_LG_pinhao)/(60 * Engrenagem.n_rel * Engrenagem.contatos_pinhao)
    VG_coroa = (N_LG_coroa)/(60 * (Engrenagem.n_rel/abs(Engrenagem.u)) * Engrenagem.contatos_coroa)

    return sigma_H0,sigma_Hpinhao,sigma_Hcoroa,sigma_HP_pinhao,sigma_HP_coroa,sigma_GP_pinhao,sigma_GP_coroa,S_Hpinhao,S_Hcoroa,S_Gpinhao,S_Gcoroa,VH_pinhao,VH_coroa,VG_pinhao,VG_coroa,AVISO1,AVISO2,AVISO3,AVISO4


def Tensao_flexao (Engrenagem,Kv,K_Fbeta,K_Falpha,Y_F1,Y_F2,Y_S1,Y_S2,Y_beta1,Y_delta_RefT_pinhao,Y_delta_RefT_coroa,Y_R_RefT_pinhao,Y_R_RefT_coroa,Y_Xpinhao,Y_Xcoroa,Y_NT_pinhao,Y_NT_coroa,Y_B1_pinhao,Y_B1_coroa) :

    Y_eps = Y_epsilon(Engrenagem)   # = 1 no método B ; 0.25 + 0.75/eps_alpha_n no método C (carga na ponta)
    sigma_F01 = ((Engrenagem.Ft)/(Engrenagem.b_pinhao * Engrenagem.m_n)) * Y_F1 * Y_S1 * Y_beta1 * Y_B1_pinhao * Y_eps
    sigma_F02 = ((Engrenagem.Ft)/(Engrenagem.b_coroa * Engrenagem.m_n)) * Y_F2 * Y_S2 * Y_beta1 * Y_B1_coroa * Y_eps
    sigma_Fpinhao = sigma_F01 * Engrenagem.Ka * Kv * K_Fbeta * K_Falpha
    sigma_Fcoroa = sigma_F02 * Engrenagem.Ka * Kv * K_Fbeta * K_Falpha
    # Y_ST = 2 ; Y_M = 1 para flexão pulsante, 0.7 para carga alternada (planeta de planetário simples - ISO 6336-3/-5)
    sigma_FP_pinhao = Engrenagem.material_pinhao.Lim_flexao * 2 * Engrenagem.Y_M_pinhao * Y_NT_pinhao * Y_delta_RefT_pinhao * Y_R_RefT_pinhao * Y_Xpinhao
    sigma_FP_coroa = Engrenagem.material_coroa.Lim_flexao * 2 * Engrenagem.Y_M_coroa * Y_NT_coroa * Y_delta_RefT_coroa * Y_R_RefT_coroa * Y_Xcoroa


    S_Fpinhao = sigma_FP_pinhao/sigma_Fpinhao
    S_Fcoroa = sigma_FP_coroa/sigma_Fcoroa

    if S_Fpinhao < Engrenagem.S_Fmin :
        AVISO1 = f"AVISO : Coeficiente de segurança de flexão para o pinhão menor que o mínimo (coeficient mínimo = {round(Engrenagem.S_Fmin,4)} ; Coeficiente de segurança calculado = {round(S_Fpinhao,4)}) \n"
    else :
        AVISO1 = None
    if S_Fcoroa < Engrenagem.S_Fmin :
        AVISO2 = f"AVISO : Coeficiente de segurança  de flexão para a coroa menor que o mínimo (coeficient mínimo = {round(Engrenagem.S_Fmin,4)} ; Coeficiente de segurança calculado = {round(S_Fcoroa,4)}) \n"
    else:
        AVISO2 = None


    Y_N_pinhao = (sigma_Fpinhao)/(Engrenagem.material_pinhao.Lim_flexao * 2 * Engrenagem.Y_M_pinhao * Y_delta_RefT_pinhao * Y_R_RefT_pinhao * Y_Xpinhao)
    Y_N_coroa = (sigma_Fcoroa)/(Engrenagem.material_coroa.Lim_flexao * 2 * Engrenagem.Y_M_coroa * Y_delta_RefT_coroa * Y_R_RefT_coroa * Y_Xcoroa)

    if Engrenagem.material_pinhao.classe_Y_NT == 1 :
        if Y_N_pinhao < 1 :
            N_LF_pinhao = 10**(6.477121 - 21.67672 * math.log(Y_N_pinhao))
        elif Y_N_pinhao >= 1 and Y_N_pinhao <=2.5 :
            N_LF_pinhao = 10**(6.477121 - 2.703423 * math.log(Y_N_pinhao))
        elif Y_N_pinhao > 2.5 :
            N_LF_pinhao = 1e04
    if Engrenagem.material_pinhao.classe_Y_NT == 2 :
        if Y_N_pinhao < 1 :
            N_LF_pinhao = 10**(6.477121 - 21.67672 * math.log(Y_N_pinhao))
        elif Y_N_pinhao >= 1 and Y_N_pinhao <=2.5 :
            N_LF_pinhao = 10**(6.477121 - 3.799779 * math.log(Y_N_pinhao))
        elif Y_N_pinhao > 2.5 :
            N_LF_pinhao = 1e03
    if Engrenagem.material_pinhao.classe_Y_NT == 3 :
        if Y_N_pinhao < 1 :
            N_LF_pinhao = 10**(6.477121 - 21.67672 * math.log(Y_N_pinhao))
        elif Y_N_pinhao >= 1 and Y_N_pinhao <=1.6 :
            N_LF_pinhao = 10**(6.477121 - 7.398073 * math.log(Y_N_pinhao))
        elif Y_N_pinhao > 1.6 :
            N_LF_pinhao = 1e03
    if Engrenagem.material_pinhao.classe_Y_NT == 4 :
        if Y_N_pinhao < 1 :
            N_LF_pinhao = 10**(6.477121 - 21.67672 * math.log(Y_N_pinhao))
        elif Y_N_pinhao >= 1 and Y_N_pinhao <=1.1 :
            N_LF_pinhao = 10**(6.477121 - 36.482160 * math.log(Y_N_pinhao))
        elif Y_N_pinhao > 1.1 :
            N_LF_pinhao = 1e03

    if Engrenagem.material_coroa.classe_Y_NT == 1 :
        if Y_N_coroa < 1 :
            N_LF_coroa = 10**(6.477121 - 21.67672 * math.log(Y_N_coroa))
        elif Y_N_coroa >= 1 and Y_N_coroa <=2.5 :
            N_LF_coroa = 10**(6.477121 - 2.703423 * math.log(Y_N_coroa))
        elif Y_N_coroa > 2.5 :
            N_LF_coroa = 1e04
    if Engrenagem.material_coroa.classe_Y_NT == 2 :
        if Y_N_coroa < 1 :
            N_LF_coroa = 10**(6.477121 - 21.67672 * math.log(Y_N_coroa))
        elif Y_N_coroa >= 1 and Y_N_coroa <=2.5 :
            N_LF_coroa = 10**(6.477121 - 3.799779 * math.log(Y_N_coroa))
        elif Y_N_coroa > 2.5 :
            N_LF_coroa = 1e03
    if Engrenagem.material_coroa.classe_Y_NT == 3 :
        if Y_N_coroa < 1 :
            N_LF_coroa = 10**(6.477121 - 21.67672 * math.log(Y_N_coroa))
        elif Y_N_coroa >= 1 and Y_N_coroa <=1.6 :
            N_LF_coroa = 10**(6.477121 - 7.398073 * math.log(Y_N_coroa))
        elif Y_N_coroa > 1.6 :
            N_LF_coroa = 1e03
    if Engrenagem.material_coroa.classe_Y_NT == 4 :
        if Y_N_coroa < 1 :
            N_LF_coroa = 10**(6.477121 - 21.67672 * math.log(Y_N_coroa))
        elif Y_N_coroa >= 1 and Y_N_coroa <=1.1 :
            N_LF_coroa = 10**(6.477121 - 36.482160 * math.log(Y_N_coroa))
        elif Y_N_coroa > 1.1 :
            N_LF_coroa = 1e03

    VF_pinhao = (N_LF_pinhao)/(60 * Engrenagem.n_rel * Engrenagem.contatos_pinhao)
    VF_coroa = (N_LF_coroa)/(60 * (Engrenagem.n_rel/abs(Engrenagem.u)) * Engrenagem.contatos_coroa)


    return sigma_F01,sigma_F02,sigma_Fpinhao,sigma_Fcoroa,sigma_FP_pinhao,sigma_FP_coroa,S_Fpinhao,S_Fcoroa,VF_pinhao,VF_coroa,AVISO1,AVISO2


def Capacidade_Carga (Engrenagem,K_V,K_Hbeta,K_Fbeta,K_Halpha,K_Falpha,Z_H,Z_E,Z_epsilon,Z_beta,Z_B,Z_D,Y_F1,Y_F2,Y_S1,Y_S2,Y_beta,sigma_HP1,sigma_HP2,sigma_GP1,sigma_GP2,sigma_FP1,sigma_FP2,Y_B1 = 1,Y_B2 = 1) :
    # Perdas (Mazzo): potência de engrenamento = T * rotação relativa ao porta-planetas
    P_malha = (Engrenagem.n_rel *2*math.pi*Engrenagem.T)/(60*1000)
    P_NZ = (((0.1)/(abs(Engrenagem.Z_pinhao) * math.cos(math.radians(Engrenagem.beta)))) + ((0.03)/(Engrenagem.v_t + 2))) * P_malha
    P_NL = (Engrenagem.v_t + 5)/5000
    P_NP = (3 * Engrenagem.b * Engrenagem.m_n * Engrenagem.v_t**1.5)/(2e06)
    P_2 = Engrenagem.potencia - P_NZ - P_NL - P_NP
    eficencia = P_2/Engrenagem.potencia

    # Torques admissíveis: F_t admissível por malha -> torque TOTAL no membro (x N_cp / K_gamma em planetário)
    fator_conj = (Engrenagem.N_cp/Engrenagem.Ky) if (Engrenagem.trans == "Planetário" and Engrenagem.N_cp and Engrenagem.Ky) else 1.0
    A = math.sqrt(Engrenagem.Ka * K_V * K_Hbeta * K_Halpha)
    B = Z_H * Z_E * Z_epsilon * Z_beta
    F_tHP1 = ((((sigma_HP1)/(Z_B *A *B))**2) * Engrenagem.d_pinhao * Engrenagem.b * Engrenagem.u)/(Engrenagem.u+1)
    T_HP1 = (F_tHP1 * Engrenagem.d_pinhao )/2000 * fator_conj
    P_HP1 = (Engrenagem.n_t *2*math.pi*T_HP1)/(60)

    F_tHP2 = ((((sigma_HP2)/(Z_D *A *B))**2) * Engrenagem.d_pinhao * Engrenagem.b * Engrenagem.u)/(Engrenagem.u+1)
    T_HP2 = (F_tHP2 * abs(Engrenagem.d_coroa) )/2000 * fator_conj
    P_HP2 = ((Engrenagem.n_t/abs(Engrenagem.u))*2*math.pi*T_HP2)/(60)

    F_tGP1 = ((((sigma_GP1)/(Z_B *A *B))**2) * Engrenagem.d_pinhao * Engrenagem.b * Engrenagem.u)/(Engrenagem.u+1)
    T_GP1 = (F_tGP1 * Engrenagem.d_pinhao )/2000 * fator_conj
    P_GP1 = (Engrenagem.n_t *2*math.pi*T_GP1)/(60)

    F_tGP2 = ((((sigma_GP2)/(Z_D *A *B))**2) * Engrenagem.d_pinhao * Engrenagem.b * Engrenagem.u)/(Engrenagem.u+1)
    T_GP2 = (F_tGP2 * abs(Engrenagem.d_coroa) )/2000 * fator_conj
    P_GP2 = ((Engrenagem.n_t/abs(Engrenagem.u))*2*math.pi*T_GP2)/(60)

    A = Engrenagem.Ka * K_V * K_Fbeta * K_Falpha
    Y_eps = Y_epsilon(Engrenagem)
    B_1 = Y_F1 * Y_S1 * Y_beta * Y_B1 * Y_eps
    B_2 = Y_F2 * Y_S2 * Y_beta * Y_B2 * Y_eps
    F_tFP1 = (sigma_FP1 * Engrenagem.b_pinhao * Engrenagem.m_n)/(A*B_1)
    T_FP1 = (F_tFP1 * Engrenagem.d_pinhao )/2000 * fator_conj
    P_FP1 = (Engrenagem.n_t *2*math.pi*T_FP1)/(60)

    F_tFP2 = (sigma_FP2 * Engrenagem.b_coroa * Engrenagem.m_n)/(A*B_2)
    T_FP2 = (F_tFP2 * abs(Engrenagem.d_coroa) )/2000 * fator_conj
    P_FP2 = ((Engrenagem.n_t/abs(Engrenagem.u))*2*math.pi*T_FP2)/(60)

    return P_2, eficencia,T_HP1,P_HP1,T_HP2,P_HP2,T_GP1,P_GP1,T_GP2,P_GP2,T_FP1,P_FP1,T_FP2,P_FP2
