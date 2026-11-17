# coding: utf-8
# Exemplos/instâncias do notebook dados_engrenagens.ipynb (gerado automaticamente)
from Dimensionamento_geometrico import *

cin_Dim_56_25_25_10_13_mat_Plat_antiga = cinematica_planetaria(Z_sol = 15, Z_pla_ext = 48, Z_pla_int = 21, Z_anel = -69, n_sol = 13000, T_sol = 31, N_cp = 3, Tipo = "Composto", Ring = "Fixo", Ky = 1.05)
# Malha externa: sol (n_t = n_sol absoluta) x planeta maior ; malha interna: planeta menor (n_t = n_planeta absoluta) x anelar fixa.
# n_carrier é passado para que a classe use a rotação relativa ao porta-planetas em v_t, K_v, Z_V e nos ciclos de carga.
Dim_56_ext_25_25_10_13_mat_Plat_antiga  = Engrenamento(apelido= "Malha externa 56_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_plat_antiga ,material_coroa = Material_plat_antiga,ferramenta_pinhao = Sun_ferramenta_pinhao ,
                     ferramenta_coroa = Bp_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = 48,a = 31.166666 ,b_pinhao = 26,b_coroa = 26,ISO = 7,alpha_n = 25,beta = 0,
                     x_pinhao = 0.025,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa =0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0.15,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
                     IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = cin_Dim_56_25_25_10_13_mat_Plat_antiga['n_sol_rel'] + cin_Dim_56_25_25_10_13_mat_Plat_antiga['n_c'],T = cin_Dim_56_25_25_10_13_mat_Plat_antiga['T_malha_ext'], di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
                     L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "sol",membro_coroa = "planeta",n_carrier = cin_Dim_56_25_25_10_13_mat_Plat_antiga['n_c'],Tipo_planetario = "Composto")


Dim_56_int_25_25_10_13_mat_Plat_antiga    = Engrenamento(apelido= "Malha interna 56_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_plat_antiga ,material_coroa = Material_plat_antiga,ferramenta_pinhao = base_ferramenta_pinhao ,
                     ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 21, Z_coroa = -69,a = -31.166666,b_pinhao = 11.5,b_coroa = 11.5,ISO = 7,alpha_n = 25,beta = 0,
                     x_pinhao = 0.27,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
                     IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 5,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = cin_Dim_56_25_25_10_13_mat_Plat_antiga['n_pla'],T = cin_Dim_56_25_25_10_13_mat_Plat_antiga['T_malha_int'], di_pinhao = 10,di_coroa = -113.94293,bs_pinhao = 10,bs_coroa = 10,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
                     L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "planeta",membro_coroa = "anelar",n_carrier = cin_Dim_56_25_25_10_13_mat_Plat_antiga['n_c'],Tipo_planetario = "Composto")

cin_Dim_56_25_25_10_13_mat_ref = cinematica_planetaria(Z_sol = 15, Z_pla_ext = 48, Z_pla_int = 21, Z_anel = -69, n_sol = 13000, T_sol = 31, N_cp = 3, Tipo = "Composto", Ring = "Fixo", Ky = 1.05)
# Malha externa: sol (n_t = n_sol absoluta) x planeta maior ; malha interna: planeta menor (n_t = n_planeta absoluta) x anelar fixa.
# n_carrier é passado para que a classe use a rotação relativa ao porta-planetas em v_t, K_v, Z_V e nos ciclos de carga.
Dim_56_ext_25_25_10_13_mat_ref  = Engrenamento(apelido= "Malha externa 56_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_Ref  ,material_coroa = Material_Ref ,ferramenta_pinhao = base_ferramenta_pinhao ,
                     ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = 48,a = 31.166666 ,b_pinhao = 25.5,b_coroa = 25.5,ISO = 7,alpha_n = 25,beta = 0,
                     x_pinhao = 0.15,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa =0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
                     IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = cin_Dim_56_25_25_10_13_mat_ref['n_sol_rel'] + cin_Dim_56_25_25_10_13_mat_ref['n_c'],T = cin_Dim_56_25_25_10_13_mat_ref['T_malha_ext'], di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
                     L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "sol",membro_coroa = "planeta",n_carrier = cin_Dim_56_25_25_10_13_mat_ref['n_c'],Tipo_planetario = "Composto")


Dim_56_int_25_25_10_13_mat_ref = Engrenamento(apelido= "Malha interna 56_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_Ref  ,material_coroa = Material_Ref ,ferramenta_pinhao = base_ferramenta_pinhao ,
                     ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 21, Z_coroa = -69,a = -31.166666,b_pinhao = 14,b_coroa = 14,ISO = 7,alpha_n = 25,beta = 0,
                     x_pinhao = 0.3,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
                     IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 5,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = cin_Dim_56_25_25_10_13_mat_ref['n_pla'],T = cin_Dim_56_25_25_10_13_mat_ref['T_malha_int'], di_pinhao = 10,di_coroa = -113.94293,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
                     L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "planeta",membro_coroa = "anelar",n_carrier = cin_Dim_56_25_25_10_13_mat_ref['n_c'],Tipo_planetario = "Composto")







##################################################################################################################################################################################################################################################

cin_Dim_41_25_25_10_14_mat_Plat_antiga = cinematica_planetaria(Z_sol = 15, Z_pla_ext = 48, Z_pla_int = 19, Z_anel = -63, n_sol = 13000, T_sol = 31, N_cp = 3, Tipo = "Composto", Ring = "Fixo", Ky = 1.05)
# Malha externa: sol (n_t = n_sol absoluta) x planeta maior ; malha interna: planeta menor (n_t = n_planeta absoluta) x anelar fixa.
# n_carrier é passado para que a classe use a rotação relativa ao porta-planetas em v_t, K_v, Z_V e nos ciclos de carga.
Dim_41_ext_25_25_10_14_mat_Plat_antiga  = Engrenamento(apelido= "Malha externa 40_25_25_10_14",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_plat_antiga ,material_coroa = Material_plat_antiga,ferramenta_pinhao = base_ferramenta_pinhao ,
                     ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = 48,a = 31.166666 ,b_pinhao = 29,b_coroa = 29,ISO = 7,alpha_n = 25,beta = 0,
                     x_pinhao = 0.108,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
                     IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = cin_Dim_41_25_25_10_14_mat_Plat_antiga['n_sol_rel'] + cin_Dim_41_25_25_10_14_mat_Plat_antiga['n_c'],T = cin_Dim_41_25_25_10_14_mat_Plat_antiga['T_malha_ext'], di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
                     L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "sol",membro_coroa = "planeta",n_carrier = cin_Dim_41_25_25_10_14_mat_Plat_antiga['n_c'],Tipo_planetario = "Composto")


Dim_41_int_25_25_10_14_mat_Plat_antiga   = Engrenamento(apelido= "Malha interna 41_25_25_10_14",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_plat_antiga ,material_coroa = Material_plat_antiga,ferramenta_pinhao = base_ferramenta_pinhao ,
                     ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.4, Z_pinhao = 19, Z_coroa = -63,a = -31.166666,b_pinhao = 15.75,b_coroa = 15.75,ISO = 7,alpha_n = 25,beta = 0,
                     x_pinhao = 0.13,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
                     IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 5,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = cin_Dim_41_25_25_10_14_mat_Plat_antiga['n_pla'],T = cin_Dim_41_25_25_10_14_mat_Plat_antiga['T_malha_int'], di_pinhao = 10,di_coroa = -113.741435,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
                     L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "planeta",membro_coroa = "anelar",n_carrier = cin_Dim_41_25_25_10_14_mat_Plat_antiga['n_c'],Tipo_planetario = "Composto")


cin_Dim_41_25_25_10_14_mat_ref = cinematica_planetaria(Z_sol = 15, Z_pla_ext = 48, Z_pla_int = 19, Z_anel = -63, n_sol = 13000, T_sol = 31, N_cp = 3, Tipo = "Composto", Ring = "Fixo", Ky = 1.05)
# Malha externa: sol (n_t = n_sol absoluta) x planeta maior ; malha interna: planeta menor (n_t = n_planeta absoluta) x anelar fixa.
# n_carrier é passado para que a classe use a rotação relativa ao porta-planetas em v_t, K_v, Z_V e nos ciclos de carga.
Dim_41_ext_25_25_10_14_mat_ref  = Engrenamento(apelido= "Malha externa 40_25_25_10_14",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_Ref ,material_coroa = Material_Ref,ferramenta_pinhao = base_ferramenta_pinhao ,
                     ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = 48,a = 31.166666 ,b_pinhao = 26,b_coroa = 26,ISO = 7,alpha_n = 25,beta = 0,
                     x_pinhao = 0.108,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
                     IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = cin_Dim_41_25_25_10_14_mat_ref['n_sol_rel'] + cin_Dim_41_25_25_10_14_mat_ref['n_c'],T = cin_Dim_41_25_25_10_14_mat_ref['T_malha_ext'], di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
                     L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "sol",membro_coroa = "planeta",n_carrier = cin_Dim_41_25_25_10_14_mat_ref['n_c'],Tipo_planetario = "Composto")


Dim_41_int_25_25_10_14_mat_ref   = Engrenamento(apelido= "Malha interna 41_25_25_10_14",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_Ref ,material_coroa = Material_Ref,ferramenta_pinhao = base_ferramenta_pinhao ,
                     ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.4, Z_pinhao = 19, Z_coroa = -63,a = -31.166666,b_pinhao = 14,b_coroa = 14,ISO = 7,alpha_n = 25,beta = 0,
                     x_pinhao = 0.08,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
                     IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 5,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = cin_Dim_41_25_25_10_14_mat_ref['n_pla'],T = cin_Dim_41_25_25_10_14_mat_ref['T_malha_int'], di_pinhao = 10,di_coroa = -113.741435,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
                     L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "planeta",membro_coroa = "anelar",n_carrier = cin_Dim_41_25_25_10_14_mat_ref['n_c'],Tipo_planetario = "Composto")


################################################################################################################################################################################################################################################################

cin_Dim_50_20_25_08_12_mat_Plat_antiga = cinematica_planetaria(Z_sol = 18, Z_pla_ext = 59, Z_pla_int = 23, Z_anel = -75, n_sol = 13000, T_sol = 31, N_cp = 3, Tipo = "Composto", Ring = "Fixo", Ky = 1.05)
# Malha externa: sol (n_t = n_sol absoluta) x planeta maior ; malha interna: planeta menor (n_t = n_planeta absoluta) x anelar fixa.
# n_carrier é passado para que a classe use a rotação relativa ao porta-planetas em v_t, K_v, Z_V e nos ciclos de carga.
Dim_50_ext_20_25_08_12_mat_Plat_antiga  = Engrenamento(apelido= "Malha externa 50_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_plat_antiga ,material_coroa = Material_plat_antiga,ferramenta_pinhao = base_ferramenta_pinhao ,
                     ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 59, a = 31.133333,b_pinhao = 28.5,b_coroa = 28.5,ISO = 7,alpha_n = 20,beta = 0,
                     x_pinhao = 0.45,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
                     IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = cin_Dim_50_20_25_08_12_mat_Plat_antiga['n_sol_rel'] + cin_Dim_50_20_25_08_12_mat_Plat_antiga['n_c'],T = cin_Dim_50_20_25_08_12_mat_Plat_antiga['T_malha_ext'], di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
                     L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "sol",membro_coroa = "planeta",n_carrier = cin_Dim_50_20_25_08_12_mat_Plat_antiga['n_c'],Tipo_planetario = "Composto")


Dim_50_int_20_25_08_12_mat_Plat_antiga  = Engrenamento(apelido= "Malha interna 50_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_plat_antiga ,material_coroa = Material_plat_antiga,ferramenta_pinhao = base_ferramenta_pinhao ,
                     ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 23, Z_coroa = -75 ,a = -31.133333,b_pinhao = 12,b_coroa = 12,ISO = 7,alpha_n = 25,beta = 0,
                     x_pinhao = 0.357516,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
                     IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 5,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = cin_Dim_50_20_25_08_12_mat_Plat_antiga['n_pla'],T = cin_Dim_50_20_25_08_12_mat_Plat_antiga['T_malha_int'], di_pinhao = 10,di_coroa = -113.7253,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
                     L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "planeta",membro_coroa = "anelar",n_carrier = cin_Dim_50_20_25_08_12_mat_Plat_antiga['n_c'],Tipo_planetario = "Composto")


cin_Dim_50_20_25_08_12_mat_ref = cinematica_planetaria(Z_sol = 18, Z_pla_ext = 59, Z_pla_int = 23, Z_anel = -75, n_sol = 13000, T_sol = 31, N_cp = 3, Tipo = "Composto", Ring = "Fixo", Ky = 1.05)
# Malha externa: sol (n_t = n_sol absoluta) x planeta maior ; malha interna: planeta menor (n_t = n_planeta absoluta) x anelar fixa.
# n_carrier é passado para que a classe use a rotação relativa ao porta-planetas em v_t, K_v, Z_V e nos ciclos de carga.
Dim_50_ext_20_25_08_12_mat_ref   = Engrenamento(apelido= "Malha externa 50_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_Ref ,material_coroa = Material_Ref,ferramenta_pinhao = base_ferramenta_pinhao ,
                     ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 59, a = 31.133333,b_pinhao = 25.5,b_coroa = 25.5,ISO = 7,alpha_n = 20,beta = 0,
                     x_pinhao = 0.45,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
                     IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = cin_Dim_50_20_25_08_12_mat_ref['n_sol_rel'] + cin_Dim_50_20_25_08_12_mat_ref['n_c'],T = cin_Dim_50_20_25_08_12_mat_ref['T_malha_ext'], di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
                     L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "sol",membro_coroa = "planeta",n_carrier = cin_Dim_50_20_25_08_12_mat_ref['n_c'],Tipo_planetario = "Composto")


Dim_50_int_20_25_08_12_mat_ref   = Engrenamento(apelido= "Malha interna 50_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_Ref ,material_coroa = Material_Ref,ferramenta_pinhao = base_ferramenta_pinhao ,
                     ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 23, Z_coroa = -75 ,a = -31.133333,b_pinhao = 13,b_coroa = 13,ISO = 7,alpha_n = 25,beta = 0,
                     x_pinhao = 0,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
                     IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 5,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = cin_Dim_50_20_25_08_12_mat_ref['n_pla'],T = cin_Dim_50_20_25_08_12_mat_ref['T_malha_int'], di_pinhao = 10,di_coroa = -113.7253,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
                     L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "planeta",membro_coroa = "anelar",n_carrier = cin_Dim_50_20_25_08_12_mat_ref['n_c'],Tipo_planetario = "Composto")




cin_teste = cinematica_planetaria(Z_sol = 25, Z_pla_ext = 84, Z_pla_int = 26, Z_anel = -112, n_sol = 13000, T_sol = 31, N_cp = 3, Tipo = "Composto", Ring = "Fixo", Ky = 1.05)
# Malha externa: sol (n_t = n_sol absoluta) x planeta maior ; malha interna: planeta menor (n_t = n_planeta absoluta) x anelar fixa.
# n_carrier é passado para que a classe use a rotação relativa ao porta-planetas em v_t, K_v, Z_V e nos ciclos de carga.
teste_ext   = Engrenamento(apelido= "NTNU ext",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_Ref ,material_coroa = Material_Ref,ferramenta_pinhao = base_ferramenta_pinhao ,
                     ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.6, Z_pinhao = 25, Z_coroa = 84, a = 32.4,b_pinhao = 12.5,b_coroa = 12.5,ISO = 7,alpha_n = 20,beta = 0,
                     x_pinhao = 0.1094,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
                     IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = cin_teste['n_sol_rel'] + cin_teste['n_c'],T = cin_teste['T_malha_ext'], di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
                     L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "sol",membro_coroa = "planeta",n_carrier = cin_teste['n_c'],Tipo_planetario = "Composto")


teste_int   = Engrenamento(apelido= "NTNU int",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_Ref ,material_coroa = Material_Ref,ferramenta_pinhao = base_ferramenta_pinhao ,
                     ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.75, Z_pinhao = 26, Z_coroa = -112 ,a = -32.4,b_pinhao = 13,b_coroa = 13,ISO = 7,alpha_n = 20,beta = 0,
                     x_pinhao = 0.2749,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
                     IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 5,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = cin_teste['n_pla'],T = cin_teste['T_malha_int'], di_pinhao = 10,di_coroa = -113.7253,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
                     L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "planeta",membro_coroa = "anelar",n_carrier = cin_teste['n_c'],Tipo_planetario = "Composto")



teste_alef   = Engrenamento(apelido= "alef",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_Ref ,material_coroa = Material_Ref,ferramenta_pinhao = base_ferramenta_pinhao ,
                     ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 3, Z_pinhao = 66, Z_coroa = -150 ,a = -133,b_pinhao = 30,b_coroa = 30,ISO = 7,alpha_n = 20,beta = 20,
                     x_pinhao = 0.812951,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
                     ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
                     crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
                     IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 5,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
                     Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3966.102,T = 101.61, di_pinhao = 10,di_coroa = -113.7253,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
                     L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
                     trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0,membro_pinhao = "planeta",membro_coroa = "anelar",n_carrier = 0,Tipo_planetario = "Composto")





#######################################################################################################################################################################################################################################################






# Dim_197_ext_20_25_07_13 = Engrenamento(apelido= "Malha externa 197_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 24, Z_coroa = 65, a = 31.483333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.31756,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_197_int_20_25_07_13 = Engrenamento(apelido= "Malha interna 197_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 17, Z_coroa = -66,a = -31.483333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.46668,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4800,T = 83.96, di_pinhao = 10,di_coroa = -109.5500,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)






















# teste = Engrenamento(apelido= "Exemplo mazzo externo",Proj = "Mazzo",tipo="Otimização",  material_pinhao = Mazzo_material ,material_coroa = Mazzo_material,ferramenta_pinhao = Mazzo_ferramenta_pinhao ,
#                      ferramenta_coroa = Mazzo_ferramenta_coroa,lubrificante = Mazzo_lubrificante ,m_n = 3, Z_pinhao = 25, Z_coroa = 61,a = 140,b_pinhao = 20,b_coroa = 20,ISO = 7,
#                      alpha_n = 20,beta = 23.188056, x_pinhao = 0.115898,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",
#                      tol_pinhao =25,tol_coroa =25,ASNE_min_pinhao = None,ASNE_max_pinhao = None,ASNE_min_coroa = None,ASNE_max_coroa = None,
#                      f_chanfro_pinhao =0.15,f_chanfro_coroa = 0.15,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.01,
#                      crwon_i_pinhao = 0.007,crwon_s_coroa= 0,crwon_i_coroa= 0,irregularidade_movida = "Choque uniforme",irregularidade_motora = "Choque uniforme",
#                      op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",IQ_pinhao = 6,IQ_coroa = 6,Ra_flanco_pinhao = 0.8 ,Ra_flanco_coroa = 0.8,Ra_pe_pinhao = 4.7619,
#                      Ra_pe_coroa = 4.7619,S_Hmin = 1.00,S_Fmin = 1.10,S_Hmax = 1.2,S_Fmax = 1.4,Arranjo_pinhao = 3,Arranjo_coroa = 3,k_linha_pinhao = None,k_linha_coroa = None,n_t = 1750,
#                      T = 622, di_pinhao = 30,di_coroa = 140,bs_pinhao = 10,bs_coroa = 10,d_sh_pinhao = 30,d_sh_coroa = 70,L_pinhao=118,L_coroa=118,sh_pinhao =18,sh_coroa =18,C_Cdil = 1e-05 ,
#                      T_Rmd = 40,T_Cmd = 30,T_op = 50,Vr = 4160,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa = None,trans = "Simples",
#                      N_cp = None,Ky = None,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = None,S_M_coroa = None)

# Norma1 = Engrenamento(apelido= "Exemplo 1 da Norma ISO 6336-30",Proj = None,tipo="Otimização",  material_pinhao = Norma1_material ,material_coroa = Norma1_material,ferramenta_pinhao = Norma1_ferramenta_pinhao ,
#                      ferramenta_coroa = Norma1_ferramenta_coroa,lubrificante = Norma1_lubrificante ,m_n = 8, Z_pinhao = 17, Z_coroa = 103,a = 500 ,b_pinhao = 100,b_coroa = 100,ISO = 7,alpha_n = 20,beta = 15.8,
#                      x_pinhao = 0.145,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =25,tol_coroa =25,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao =0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0,crwon_i_pinhao = 0,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque uniforme",irregularidade_motora = "Choque uniforme",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 1 ,Ra_flanco_coroa = 1,Ra_pe_pinhao = 3,Ra_pe_coroa = 3,S_Hmin = 1.00,S_Fmin = 1.00,S_Hmax = 1.2,S_Fmax = 1.4,Arranjo_pinhao = 1,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 360,T = 9000, di_pinhao = 0,di_coroa = 0,bs_pinhao = 100,bs_coroa = 100,d_sh_pinhao = 100,d_sh_coroa = 100,L_pinhao=125,
#                      L_coroa=125,sh_pinhao =0,sh_coroa =0,C_Cdil = 1e-05 ,T_Rmd = 40,T_Cmd = 30,T_op = 50,Vr = 50000,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Simples",N_cp = None,Ky = None,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = None,S_M_coroa = None)


# Norma6 = Engrenamento(apelido= "Exemplo 6 da Norma ISO 6336-30",Proj = None,tipo="Otimização",  material_pinhao = Norma6_material_pinhao ,material_coroa = Norma6_material_coroa,ferramenta_pinhao = Norma6_ferramenta_pinhao ,
#                      ferramenta_coroa = Norma6_ferramenta_coroa,lubrificante = Norma6_lubrificante ,m_n = 12, Z_pinhao = 15, Z_coroa = -99,a = -500 ,b_pinhao = 125,b_coroa = 125,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.323,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =25,tol_coroa =25,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao =0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0,crwon_i_pinhao = 0,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 6,IQ_coroa = 8,Ra_flanco_pinhao = 1 ,Ra_flanco_coroa = 3,Ra_pe_pinhao = 3,Ra_pe_coroa = 3,S_Hmin = 1.00,S_Fmin = 1.00,S_Hmax = 1.2,S_Fmax = 1.4,Arranjo_pinhao = 1,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 360,T = 1000, di_pinhao = 0,di_coroa = -1317.9987,bs_pinhao = 125,bs_coroa = 125,d_sh_pinhao = 100,d_sh_coroa = 100,L_pinhao=200,
#                      L_coroa=200,sh_pinhao =0,sh_coroa =0,C_Cdil = 1e-05 ,T_Rmd = 40,T_Cmd = 30,T_op = 50,Vr = 10000,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Simples",N_cp = None,Ky = None,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_3_ext_25_25_1_1 = Engrenamento(apelido= "Malha externa 3_25_25_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 34,a = 22.6666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.115462,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_3_int_25_25_1_1   = Engrenamento(apelido= "Malha interna 3_25_25_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 17, Z_coroa = -63,a = -22.6666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 5,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4588.241,T = 87.83, di_pinhao = 10,di_coroa = -85.4201976894141,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_11_ext_25_25_1_1   = Engrenamento(apelido= "Malha externa 11_25_25_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 37,a = 24.16666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.126671,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_11_int_25_25_1_1   = Engrenamento(apelido= "Malha interna 11_25_25_1_1", Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 20, Z_coroa = -69,a = -24.16666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.417068,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 5,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4216.67,T = 95.573, di_pinhao = 10,di_coroa = -91.689086,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_15_ext_25_25_1_1   = Engrenamento(apelido= "Malha externa 15_25_25_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 39,a = 25.166666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1333062,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_15_int_25_25_1_1   = Engrenamento(apelido= "Malha interna 15_25_25_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 22, Z_coroa = -72,a = -25.166666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.3820880,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 5,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4000,T = 104, di_pinhao = 10,di_coroa = -95.602535,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_22_ext_25_25_1_1   = Engrenamento(apelido= "Malha externa 22_25_25_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 41,a = 26.1666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1395327,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_22_int_25_25_1_1   = Engrenamento(apelido= "Malha interna 22_25_25_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 25, Z_coroa = -78,a = -26.1666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.3264482,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 5,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3801.1695,T = 106.02, di_pinhao = 10,di_coroa = -100.506158,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_31_ext_25_25_1_1   = Engrenamento(apelido= "Malha externa 31_25_25_1_1 ",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 44,a = 27.66666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1480109,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_31_int_25_25_1_1   = Engrenamento(apelido= "Malha interna 31_25_25_1_1 ",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 29, Z_coroa = -84,a = -27.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.2711853,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 5,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3542.234,T = 113.77, di_pinhao = 10,di_coroa = -107.380279,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_87_ext_25_25_1_1   = Engrenamento(apelido= "Malha externa 87_25_25_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = 43,a = 28.66666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.097434178,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_87_int_25_25_1_1   = Engrenamento(apelido= "Malha interna 87_25_25_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 21, Z_coroa = -78,a = -28.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.359240,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 5,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4529.617,T = 88.97, di_pinhao = 10,di_coroa = -101.55623,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_94_ext_25_25_1_1   = Engrenamento(apelido= "Malha externa 94_25_25_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = 45,a = 29.6666666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.104710,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_94_int_25_25_1_1   = Engrenamento(apelido= "Malha interna 94_25_25_1_1 ",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 24, Z_coroa = -84,a = -29.6666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.30362,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4333.34,T = 93, di_pinhao = 10,di_coroa = -106.458109,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_7_ext_20_20_1_1  = Engrenamento(apelido= "Malha externa 7_20_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 18, Z_coroa = 45,a = 31.1666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.0657534549,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_7_int_20_20_1_1   = Engrenamento(apelido= "Malha interna 7_20_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 19, Z_coroa = -81,a = -31.1666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.364128,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5200,T = 77.5, di_pinhao = 10,di_coroa = -106.458109,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_12_ext_20_20_1_1   = Engrenamento(apelido= "Malha externa 12_20_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 18, Z_coroa = 45,a = 31.83333 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.255307,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_12_int_20_20_1_1   = Engrenamento(apelido= "Malha interna 12_20_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 20, Z_coroa = -84,a = -31.83333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.338534,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5200,T = 77.5, di_pinhao = 10,di_coroa = -106.458109,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_14_ext_20_20_1_1   = Engrenamento(apelido= "Malha externa 14_20_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 18, Z_coroa = 46,a = 31.66666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.255307,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_14_int_20_20_1_1   = Engrenamento(apelido= "Malha interna 14_20_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 20, Z_coroa = -84,a = -31.66666,b_pinhao = 25,b_coroa = 25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.3385344,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5088.0626,T = 79.205, di_pinhao = 10,di_coroa = -106.458109,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_0_ext_20_20_08_12  = Engrenamento(apelido= "Malha externa 0_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 52,a = 28.33333 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.2963859,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_0_int_20_20_08_12   = Engrenamento(apelido= "Malha interna 0_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 18, Z_coroa = -66,a = -28.33333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.454758,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4500,T = 89.55, di_pinhao = 10,di_coroa = -102.418782,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_0_ext_20_20_08_12  = Engrenamento(apelido= "Malha externa 0_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 52,a = 28.33333 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.2963859,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_0_int_20_20_08_12   = Engrenamento(apelido= "Malha interna 0_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 18, Z_coroa = -66,a = -28.33333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.454758,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4500,T = 89.55, di_pinhao = 10,di_coroa = -102.418782,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_18_ext_20_20_08_12  = Engrenamento(apelido= "Malha externa 18_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 55,a = 28.86666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.084179,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_18_int_20_20_08_12   = Engrenamento(apelido= "Malha interna 18_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -69,a = -28.86666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.417068,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4193.55,T = 96.1, di_pinhao = 10,di_coroa = -105.81258,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_22_ext_20_20_08_12  = Engrenamento(apelido= "Malha externa 22_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 56,a = 29.26666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.0874286,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_22_int_20_20_08_12   = Engrenamento(apelido= "Malha interna 22_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -69,a = -29.26666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.4170685,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4180.064,T = 96.41, di_pinhao = 10,di_coroa = -106.53893,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_35_ext_20_20_08_12  = Engrenamento(apelido= "Malha externa 35_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 58,a = 30.0666666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.093695,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_35_int_20_20_08_12   = Engrenamento(apelido= "Malha interna 35_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 22, Z_coroa = -72,a = -30.0666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.3820880,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4034.761,T = 99.882, di_pinhao = 10,di_coroa = -110.45145,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_36_ext_20_20_08_12  = Engrenamento(apelido= "Malha externa 36_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 58,a = 30.73333 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.304741,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_36_int_20_20_08_12   = Engrenamento(apelido= "Malha interna 36_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 23, Z_coroa = -75,a = -30.73333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.3575166,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4034.761,T = 99.882, di_pinhao = 10,di_coroa = -112.98044,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_39_ext_20_20_08_12  = Engrenamento(apelido= "Malha externa 39_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 59,a = 30.46666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.0966967,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_39_int_20_20_08_12   = Engrenamento(apelido= "Malha interna 39_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 22, Z_coroa = -72,a = -30.46666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.382088,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3975.5351,T = 101.37, di_pinhao = 10,di_coroa = -111.30239,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_40_ext_20_20_08_12  = Engrenamento(apelido= "Malha externa 40_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 59,a = 31.1333333 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.306050,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_40_int_20_20_08_12   = Engrenamento(apelido= "Malha interna 40_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 23, Z_coroa = -75,a = -31.1333333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.35751667,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3975.5351,T = 101.37, di_pinhao = 10,di_coroa = -113.7257,bs_pinhao = 15.75,bs_coroa = 16.25,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_84_ext_20_20_08_12  = Engrenamento(apelido= "Malha externa 84_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 21, Z_coroa = 59,a = 31.66666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.063621,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_84_int_20_20_08_12   = Engrenamento(apelido= "Malha interna 4_20_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 19, Z_coroa = -72,a = -31.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = -0.1,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4627.12,T = 87.1, di_pinhao = 10,di_coroa = -111.36487,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)





# Dim_1_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 1_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 12, Z_coroa = 40,a = 20.466666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1253944,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_1_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 1_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 16, Z_coroa = -51,a = -20.466666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.556421853,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -84.535497,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_6_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 6_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 12, Z_coroa = 45,a = 22.466666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1401171,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_6_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 6_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -57,a = -22.466666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4836050,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3466.667,T = 116.25, di_pinhao = 10,di_coroa = -93.108287,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_15_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 15_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 12, Z_coroa = 47,a = 23.26666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1453659,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_15_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 15_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 22, Z_coroa = -60,a = -23.26666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.44922855,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3319.149,T = 121.42, di_pinhao = 10,di_coroa = -97.053294,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_19_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 19_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 12, Z_coroa = 48,a = 23.66666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.14782828,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_19_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 19_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 24, Z_coroa = -63,a = -23.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.41632937,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3250,T = 124, di_pinhao = 10,di_coroa = -100.14611,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_28_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 28_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 12, Z_coroa = 50,a = 24.466666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1524611,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_28_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 28_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 26, Z_coroa = -66,a = -24.466666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.38497854,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3120,T = 129.17, di_pinhao = 10,di_coroa = -104.0970,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_42_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 42_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 12, Z_coroa = 53,a = 25.66666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1593536,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_42_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 42_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 30, Z_coroa = -72,a = -25.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.3270991,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 2943.396,T = 136.92, di_pinhao = 10,di_coroa = -111.156372,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_48_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 48_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 12, Z_coroa = 54,a = 26.066666666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.161573,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_48_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 48_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 32, Z_coroa = -75,a = -26.066666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.3006074,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 2888.889,T = 139.5, di_pinhao = 10,di_coroa = -114.26714,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_96_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 96_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 15, Z_coroa = 48,a = 24.866666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.099830585,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_96_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 96_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 18, Z_coroa = -60,a = -24.866666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.487262708,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4062.500,T = 99.2, di_pinhao = 10,di_coroa = -95.5237577,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_101_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 101_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 15, Z_coroa = 50,a = 25.666666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.10647534,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_101_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 101_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -63,a = -25.666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4502003,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -99.41702,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_102_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 102_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 15, Z_coroa = 51,a = 26.066666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.109622630,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_102_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 102_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -63,a = -26.066666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4502003341,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3823.529,T = 105.4, di_pinhao = 10,di_coroa = -100.22617,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_113_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 113_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 15, Z_coroa = 55,a = 27.66666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1211787,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_113_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 113_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 25, Z_coroa = -72,a = -27.66666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.35838454,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3545.455,T = 113.67, di_pinhao = 10,di_coroa = -109.242245,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_121_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 121_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 15, Z_coroa = 57,a = 28.46666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.12640604,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_121_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 121_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 27, Z_coroa = -75,a = -28.46666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.32865288,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3421.053,T = 117.8, di_pinhao = 10,di_coroa = -113.1403877,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_124_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 124_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 15, Z_coroa = 58,a = 28.86666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1288970,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_124_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 124_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 27, Z_coroa = -75,a = -28.86666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.32865288,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3362.069,T = 119.87, di_pinhao = 10,di_coroa = -113.9228,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_159_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 159_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 51,a = 27.266666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0690810,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_159_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 159_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 17, Z_coroa = -63,a = -27.266666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4827086,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4558.325,T = 87.83, di_pinhao = 10,di_coroa = -99.110942,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_160_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 160_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 52,a = 27.66666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0726344,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_160_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 160_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 17, Z_coroa = -63,a = -27.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4827086,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4500,T = 89.56, di_pinhao = 10,di_coroa = -99.89257,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_169_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 169_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 55,a = 28.8666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0826278,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_169_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 169_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -69,a = -28.8666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4170685,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4254.545,T = 94.72, di_pinhao = 10,di_coroa = -105.78099,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_171_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 171_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 56,a = 29.2666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.08582899,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_171_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 171_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -69,a = -29.2666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.417068570,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4178.571,T = 96.44, di_pinhao = 10,di_coroa = -106.53711,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_177_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 177_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 58,a = 30.0666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.092185101,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_177_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 177_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 22, Z_coroa = -72,a = -30.0666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.3820880,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4034.483,T = 99.89, di_pinhao = 10,di_coroa = -110.45102,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_179_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 179_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 59,a = 30.4666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.09522875,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_179_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 179_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 22, Z_coroa = -72,a = -30.4666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.382088050,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3966.103,T = 101.61, di_pinhao = 10,di_coroa = -111.28248,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_209_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 209_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 21, Z_coroa = 54,a = 29.6666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0441443,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_209_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 209_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 16, Z_coroa = -66,a = -29.6666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.47968164,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5055.556,T =79.71 , di_pinhao = 10,di_coroa = -102.70210,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_214_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 214_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 21, Z_coroa = 55,a = 30.73333333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.2893355,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_214_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 214_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 17, Z_coroa = -69,a = -30.73333333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.45068658,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4963.636,T =81.19 , di_pinhao = 10,di_coroa = -105.98170,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_226_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 226_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 21, Z_coroa = 59,a = 31.66666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0619923283,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_226_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 226_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 19, Z_coroa = -72,a = -31.66666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.411208103,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4627.119,T =87.1 , di_pinhao = 10,di_coroa = -110.1228315,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_241_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 241_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 24, Z_coroa = 55,a = 31.933333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.2806337,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_241_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 241_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 15, Z_coroa = -69,a = -31.933333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.478413295,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5672.727,T = 71.04 , di_pinhao = 10,di_coroa = -106.046965,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_242_ext_25_25_08_12  = Engrenamento(apelido= "Malha externa 242_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 24, Z_coroa = 56,a = 32.3333333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.2806337,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_242_int_25_25_08_12   = Engrenamento(apelido= "Malha interna 242_25_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 15, Z_coroa = -69,a = -32.3333333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4784132,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5571.429,T = 72.33 , di_pinhao = 10,di_coroa = -106.8154927,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_6_ext_25_20_1_1  = Engrenamento(apelido= "Malha externa 6_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 37,a = 24.166666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.126671,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_6_int_25_20_1_1   = Engrenamento(apelido= "Malha interna 6_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 20, Z_coroa = -69,a = -24.166666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.41706857,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4216.216,T = 95.58 , di_pinhao = 10,di_coroa = -91.7034916,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_10_ext_25_20_1_1  = Engrenamento(apelido= "Malha externa 10_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 39,a = 25.16666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.133306,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_10_int_25_20_1_1   = Engrenamento(apelido= "Malha interna 10_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 22, Z_coroa = -72,a = -25.16666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.3820880,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4000,T = 100.75 , di_pinhao = 10,di_coroa = -95.605707,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_17_ext_25_20_1_1  = Engrenamento(apelido= "Malha externa 17_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 41,a = 26.16666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.139532,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_17_int_25_20_1_1   = Engrenamento(apelido= "Malha interna 17_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 25, Z_coroa = -78,a = -26.16666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.326448,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3804.878,T = 105.92 , di_pinhao = 10,di_coroa = -100.51939,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_26_ext_25_20_1_1  = Engrenamento(apelido= "Malha externa 26_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 44,a = 27.666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.14801,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_26_int_25_20_1_1   = Engrenamento(apelido= "Malha interna 26_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 29, Z_coroa = -84,a = -27.666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.271185,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3545.455,T = 113.67 , di_pinhao = 10,di_coroa = -107.383171,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_31_ext_25_20_1_1  = Engrenamento(apelido= "Malha externa 31_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 45,a = 28.16666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.150588,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_31_int_25_20_1_1   = Engrenamento(apelido= "Malha interna 31_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 31, Z_coroa = -87,a = -28.16666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.24670,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3466.667,T = 116.25 , di_pinhao = 10,di_coroa = -110.33401,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_91_ext_25_20_1_1  = Engrenamento(apelido= "Malha externa 91_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = 43,a = 28.66666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.09743,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_91_int_25_20_1_1   = Engrenamento(apelido= "Malha interna 91_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 21, Z_coroa = -78,a = -28.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.359240,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4534.884,T = 88.87 , di_pinhao = 10,di_coroa = -101.5590,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_98_ext_25_20_1_1  = Engrenamento(apelido= "Malha externa 98_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = 45,a = 29.666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.104710,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_98_int_25_20_1_1   = Engrenamento(apelido= "Malha interna 98_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 24, Z_coroa = -84,a = -29.666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.30362,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4333.333,T = 93 , di_pinhao = 10,di_coroa = -106.46970,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_100_ext_25_20_1_1  = Engrenamento(apelido= "Malha externa 100_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = 46,a = 30.16666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1082083,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_100_int_25_20_1_1   = Engrenamento(apelido= "Malha interna 100_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 24, Z_coroa = -84,a = -30.16666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.303620,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4239.130,T = 95.07, di_pinhao = 10,di_coroa = -107.44743,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_107_ext_25_20_1_1  = Engrenamento(apelido= "Malha externa 107_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = 48,a = 31.16666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.114814,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_107_int_25_20_1_1   = Engrenamento(apelido= "Malha interna 107_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 27, Z_coroa = -90,a = -31.16666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.255127,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4062.5,T = 99.2, di_pinhao = 10,di_coroa = -112.3712,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_135_ext_25_20_1_1  = Engrenamento(apelido= "Malha externa 135_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 18, Z_coroa = 45,a = 31.166666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0643938,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_135_int_25_20_1_1   = Engrenamento(apelido= "Malha interna 135_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 19, Z_coroa = -81,a = -31.166666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.3641288,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5200,T = 77.50, di_pinhao = 10,di_coroa = -104.568231,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_138_ext_25_20_1_1  = Engrenamento(apelido= "Malha externa 138_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 18, Z_coroa = 46,a = 31.66666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.06843,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_138_int_25_20_1_1   = Engrenamento(apelido= "Malha interna 138_25_20_1_1",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 20, Z_coroa = -84,a = -31.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.33853,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5086.957,T = 79.22, di_pinhao = 10,di_coroa = -106.5376,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_3_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 3_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 12, Z_coroa = 45,a = 22.466666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1401171,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_3_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 3_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -57,a = -22.466666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.483605,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3466.67,T = 116.25, di_pinhao = 10,di_coroa = -93.117210,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_12_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 12_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 12, Z_coroa = 47,a = 23.26666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.145365,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_12_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 12_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 22, Z_coroa = -60,a = -23.26666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.4492285,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3319.149,T = 121.42, di_pinhao = 10,di_coroa = -97.07893,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_16_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 16_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 12, Z_coroa = 48,a = 23.666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.14782828,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_16_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 16_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 24, Z_coroa = -63,a = -23.666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.41632937,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3250,T = 124, di_pinhao = 10,di_coroa = -100.15460,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_25_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 25_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 12, Z_coroa = 50,a = 24.46666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.152461,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_25_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 25_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 26, Z_coroa = -66,a = -24.46666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.38497,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3120,T = 129.17, di_pinhao = 10,di_coroa = -104.1215,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_39_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 39_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 12, Z_coroa = 53,a = 25.66666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1593536,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_39_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 39_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 30, Z_coroa = -72,a = -25.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.32709919,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 2943.396,T = 136.92, di_pinhao = 10,di_coroa = -111.17976,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_45_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 45_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 12, Z_coroa = 54,a = 26.06666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1615732,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_45_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 45_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 32, Z_coroa = -75,a = -26.06666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.30060740,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 2888.889,T = 139.50, di_pinhao = 10,di_coroa = -114.2748,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_87_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 87_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 15, Z_coroa = 48,a = 24.86666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0998305,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_87_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 87_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 18, Z_coroa = -60,a = -24.86666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.4872627,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4062.5,T = 99.20, di_pinhao = 10,di_coroa = -95.537731,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_92_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 92_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 15, Z_coroa = 50,a = 25.66666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.106475,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_92_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 92_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -63,a = -25.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.450200,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -99.41911,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_93_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 93_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 15, Z_coroa = 51,a = 26.06666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.10962263,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_93_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 93_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -63,a = -26.06666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.450200,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3823.529,T = 105.4, di_pinhao = 10,di_coroa = -100.233906,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_104_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 104_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 15, Z_coroa = 55,a = 27.6666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1211787,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_104_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 104_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 25, Z_coroa = -72,a = -27.6666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.358384,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3545.455,T = 113.67, di_pinhao = 10,di_coroa = -109.2753,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_112_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 112_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 15, Z_coroa = 57,a = 28.4666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.12640,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_112_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 112_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 27, Z_coroa = -75,a = -28.4666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.3286528,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3421.053,T = 117.8, di_pinhao = 10,di_coroa = -113.1524,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_115_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 115_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 15, Z_coroa = 58,a = 28.8666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1288970,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_115_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 115_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 27, Z_coroa = -75,a = -28.8666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.328652,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3362.069,T = 119.87, di_pinhao = 10,di_coroa = -113.9232,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_148_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 148_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 55,a = 28.866666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.082627,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_148_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 148_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -69,a = -28.866666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.417068,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4254.545,T = 94.72, di_pinhao = 10,di_coroa = -105.8125,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_150_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 150_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 56,a = 29.26666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0858289,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_150_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 150_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -69,a = -29.26666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.4170685,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4178.571,T = 96.44, di_pinhao = 10,di_coroa = -106.5389,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)





# Dim_156_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 156_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 58,a = 30.06666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.092185,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_156_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 156_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 22, Z_coroa = -72,a = -30.06666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.3820880,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4034.483,T = 99.89, di_pinhao = 10,di_coroa = -110.45145,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_158_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 158_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 59,a = 30.4666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.095228,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_158_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 158_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 22, Z_coroa = -72,a = -30.4666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.38208,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3966.102,T = 101.61, di_pinhao = 10,di_coroa = -111.30239,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_190_ext_25_20_08_12  = Engrenamento(apelido= "Malha externa 190_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 21, Z_coroa = 59,a = 31.66666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0619923,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_190_int_25_20_08_12   = Engrenamento(apelido= "Malha interna 190_25_20_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 19, Z_coroa = -72,a = -31.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.4112081,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4627.119,T = 87.10, di_pinhao = 10,di_coroa = -110.12451,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_5_ext_20_20_09_11  = Engrenamento(apelido= "Malha externa 5_20_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 49,a = 30.48333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.275260,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_5_int_20_20_09_11   = Engrenamento(apelido= "Malha interna 5_20_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 19, Z_coroa = -75,a = -30.48333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.39523,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4775.510,T = 84.39, di_pinhao = 10,di_coroa = -105.5117,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_12_ext_20_20_09_11  = Engrenamento(apelido= "Malha externa 12_20_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 51,a = 30.71666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.080174,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_12_int_20_20_09_11   = Engrenamento(apelido= "Malha interna 12_20_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 20, Z_coroa = -75,a = -30.71666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.38473,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4588.235,T = 87.83, di_pinhao = 10,di_coroa = -107.081389,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_15_ext_20_20_09_11  = Engrenamento(apelido= "Malha externa 15_20_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 51,a = 31.383333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.278407,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_15_int_20_20_09_11   = Engrenamento(apelido= "Malha interna 15_20_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 21, Z_coroa = -78,a = -31.383333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.359240,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4588.235,T = 87.83, di_pinhao = 10,di_coroa = -109.4072,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_19_ext_20_20_09_11  = Engrenamento(apelido= "Malha externa 19_20_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 52,a = 31.16666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.08353164,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_19_int_20_20_09_11   = Engrenamento(apelido= "Malha interna 19_20_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 21, Z_coroa = -78,a = -31.16666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.359240,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4500,T = 89.56, di_pinhao = 10,di_coroa = -108.98192,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_3_ext_25_25_12_12  = Engrenamento(apelido= "Malha externa 3_25_25_12_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 34,a = 27.266666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.123927874,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_3_int_25_25_12_12   = Engrenamento(apelido= "Malha interna 3_25_25_12_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 17, Z_coroa = -63,a = -27.266666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4827086,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4558.235,T = 87.83, di_pinhao = 10,di_coroa = -99.1109426,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_11_ext_25_25_12_12  = Engrenamento(apelido= "Malha externa 11_25_25_12_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 37,a = 29.066666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1346833,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_11_int_25_25_12_12   = Engrenamento(apelido= "Malha interna 11_25_25_12_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -69,a = -29.066666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.417068570,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4216.216,T = 95.58, di_pinhao = 10,di_coroa = -106.152200 ,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_15_ext_25_25_12_12  = Engrenamento(apelido= "Malha externa 15_25_25_12_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 39,a = 30.26666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.141266,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_15_int_25_25_12_12   = Engrenamento(apelido= "Malha interna 15_25_25_12_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 22, Z_coroa = -72,a = -30.26666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.382088050,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4000,T = 100.75, di_pinhao = 10,di_coroa = -110.86100,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_33_ext_25_25_12_12  = Engrenamento(apelido= "Malha externa 33_25_25_12_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 15, Z_coroa = 36,a = 30.26666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0798054,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_33_int_25_25_12_12   = Engrenamento(apelido= "Malha interna 33_25_25_12_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 15, Z_coroa = -66,a = -30.26666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao =0.49391260,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5416.667,T = 74.40, di_pinhao = 10,di_coroa = -102.73590,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_4_ext_25_25_10_13  = Engrenamento(apelido= "Malha externa 4_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 40,a = 25.666666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.13642707,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_4_int_25_25_10_13   = Engrenamento(apelido= "Malha interna 4_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 18, Z_coroa = -57,a = -25.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.50341298,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -99.30984,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_11_ext_25_25_10_13  = Engrenamento(apelido= "Malha externa 11_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 44,a = 27.6666666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1480109,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_11_int_25_25_10_13   = Engrenamento(apelido= "Malha interna 11_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 23, Z_coroa = -66,a = -27.6666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.406964698,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3545.455,T = 113.67, di_pinhao = 10,di_coroa = -109.5550,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_20_ext_25_25_10_13  = Engrenamento(apelido= "Malha externa 20_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 46,a = 28.6666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1530544,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_20_int_25_25_10_13   = Engrenamento(apelido= "Malha interna 20_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 25, Z_coroa = -69,a = -28.6666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.374956,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3391.304,T = 118.83, di_pinhao = 10,di_coroa = -114.05893,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_43_ext_25_25_10_13  = Engrenamento(apelido= "Malha externa 43_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = 42,a = 28.16666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0937458,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_43_int_25_25_10_13   = Engrenamento(apelido= "Malha interna 43_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 16, Z_coroa = -60,a = -28.16666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.5110694,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4642.857,T = 86.80, di_pinhao = 10,di_coroa = -101.7435,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_47_ext_25_25_10_13  = Engrenamento(apelido= "Malha externa 47_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = 45,a = 29.6666666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.104710,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_47_int_25_25_10_13   = Engrenamento(apelido= "Malha interna 47_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 18, Z_coroa = -63,a = -29.6666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.471016,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4333.333,T = 93, di_pinhao = 10,di_coroa = -107.234337,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_50_ext_25_25_10_13  = Engrenamento(apelido= "Malha externa 50_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = 46,a = 30.1666666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.10820836,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_50_int_25_25_10_13   = Engrenamento(apelido= "Malha interna 50_25_25_10_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 19, Z_coroa = -66,a = -30.1666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.44375582,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4239.130,T = 95.07, di_pinhao = 10,di_coroa = -109.45995,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)












# Dim_4_ext_25_25_10_14  = Engrenamento(apelido= "Malha externa 4_25_25_10_14",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 40,a = 25.66666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.13642707,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_4_int_25_25_10_14   = Engrenamento(apelido= "Malha interna 4_25_25_10_14",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.4, Z_pinhao = 17, Z_coroa = -54,a = -25.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.5300761,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -100.12744,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_14_ext_25_25_10_14  = Engrenamento(apelido= "Malha externa 14_25_25_10_14",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 12, Z_coroa = 45,a = 28.166666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.150588,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_14_int_25_25_10_14   = Engrenamento(apelido= "Malha interna 14_25_25_10_14",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.4, Z_pinhao = 22, Z_coroa = -63,a = -28.166666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.43216376,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3466.67,T = 116.25, di_pinhao = 10,di_coroa = -111.8912,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_36_ext_25_25_10_14  = Engrenamento(apelido= "Malha externa 36_25_25_10_14",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = 45,a = 29.6666666 ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1047101,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_36_int_25_25_10_14   = Engrenamento(apelido= "Malha interna 36_25_25_10_14",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.4, Z_pinhao = 17, Z_coroa = -60,a = -29.6666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4986740,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4333.333,T = 93, di_pinhao = 10,di_coroa = -108.05941,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)








# Dim_7_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 7_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 12, Z_coroa = 40,a = 23.0666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1314681,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_7_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 7_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 19, Z_coroa = -60,a = -23.0666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.47670897,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -90.8836243,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_8_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 8_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 12, Z_coroa = 40,a = 23.06666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.13146817,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_8_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 8_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 20, Z_coroa = -63,a = -23.06666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4502003,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -91.944528,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_14_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 14_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 12, Z_coroa = 44,a = 24.86666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.14323627,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_14_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 14_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 24, Z_coroa = -69,a = -24.86666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.38232967,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3545.455,T = 113.67, di_pinhao = 10,di_coroa = -99.7269580,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_22_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 22_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 12, Z_coroa = 46,a = 25.76666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1484761,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_22_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 22_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 26, Z_coroa = -72,a = -25.76666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.3514111,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3391.304,T = 118.83, di_pinhao = 10,di_coroa = -103.69429,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_37_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 37_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 12, Z_coroa = 49, a = 27.116666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.15568684,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_37_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 37_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 31, Z_coroa = -81,a = -27.116666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.27506206,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3183.673,T = 126.58, di_pinhao = 10,di_coroa = -111.7139616,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_41_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 41_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 12, Z_coroa = 50, a = 27.566666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1581489,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_41_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 41_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 33, Z_coroa = -84,a = -27.566666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.25105273,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3120,T = 129.17, di_pinhao = 10,di_coroa = -114.775744,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_96_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 96_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 15, Z_coroa = 46, a = 27.1166666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1012759,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_96_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 96_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 20, Z_coroa = -69,a = -27.1166666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4170685,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4239.130,T = 95.07, di_pinhao = 10,di_coroa = -99.90555,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_98_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 98_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 15, Z_coroa = 47, a = 27.566666
#                      ,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.10476710,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_98_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 98_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 21, Z_coroa = -72,a = -27.566666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.391097780,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4148.936,T = 97.13, di_pinhao = 10,di_coroa = -101.883843,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_106_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 106_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 15, Z_coroa = 49, a = 28.466666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1113673555,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_106_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 106_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 23, Z_coroa = -75,a = -28.466666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.35751667,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3979.592,T = 101.27, di_pinhao = 10,di_coroa = -105.7727,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_110_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 110_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 15, Z_coroa = 51, a = 29.36666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1175029,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_110_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 110_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 25, Z_coroa = -78,a = -29.36666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.35751667,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3823.529,T = 105.4, di_pinhao = 10,di_coroa = -109.708790,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_145_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 145_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 47, a = 28.9166666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.063974,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_145_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 145_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 17, Z_coroa = -69,a = -28.9166666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4506865,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4978.723,T = 80.94, di_pinhao = 10,di_coroa = -100.29053,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_152_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 152_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 51, a = 30.716666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.078795414,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_152_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 152_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 20, Z_coroa = -75,a = -30.716666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.384735863,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4588.325,T = 87.83, di_pinhao = 10,di_coroa = -107.061638,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_155_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 155_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 52, a = 31.16666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.082196147,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_155_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 155_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 21, Z_coroa = -78,a = -31.16666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.35924027,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4500,T = 89.56, di_pinhao = 10,di_coroa = -108.978667,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_177_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 177_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 21, Z_coroa = 47, a = 30.933333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.25908447,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_177_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 177_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 15, Z_coroa = -72,a = -30.933333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4629088,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5808.511,T = 69.39, di_pinhao = 10,di_coroa = -102.1614,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_185_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 185_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 21, Z_coroa = 50, a = 31.61666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao =0.0399152,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_185_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 185_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 17, Z_coroa = -75,a = -31.61666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4190035,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5460,T = 73.81, di_pinhao = 10,di_coroa = -105.616984,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_186_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 186_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 21, Z_coroa = 50, a = 32.2833333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao =0.2643143744,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_186_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 186_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 17, Z_coroa = -75,a = -32.2833333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.41900358,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5460,T = 73.81, di_pinhao = 10,di_coroa = -106.95904,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_187_ext_25_25_09_11 = Engrenamento(apelido= "Malha externa 187_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 21, Z_coroa = 51, a = 32.06666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.043989,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_187_int_25_25_09_11 = Engrenamento(apelido= "Malha interna 187_25_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 17, Z_coroa = -75,a = -32.06666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4190035,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5352.941,T = 75.29, di_pinhao = 10,di_coroa = -106.95904,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_5_ext_25_20_09_11 = Engrenamento(apelido= "Malha externa 5_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 12, Z_coroa = 40, a = 23.06666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.131468,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_5_int_25_20_09_11 = Engrenamento(apelido= "Malha interna 5_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 20, Z_coroa = -63,a = -23.06666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.45020033,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -91.99355,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_11_ext_25_20_09_11 = Engrenamento(apelido= "Malha externa 11_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 12, Z_coroa = 44, a = 24.86666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.143236,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_11_int_25_20_09_11 = Engrenamento(apelido= "Malha interna 11_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 24, Z_coroa = -69,a = -24.86666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.382329,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3545.455,T = 113.67, di_pinhao = 10,di_coroa = -99.7285,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_19_ext_25_20_09_11 = Engrenamento(apelido= "Malha externa 19_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 12, Z_coroa = 46, a = 25.76666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.14847,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_19_int_25_20_09_11 = Engrenamento(apelido= "Malha interna 19_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 26, Z_coroa = -72,a = -25.76666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.3514111,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3391.304,T = 118.83, di_pinhao = 10,di_coroa = -103.7176,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_34_ext_25_20_09_11 = Engrenamento(apelido= "Malha externa 34_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 12, Z_coroa = 49, a = 27.1166,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.155686,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_34_int_25_20_09_11 = Engrenamento(apelido= "Malha interna 34_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 31, Z_coroa = -81,a = -27.1166,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.27506,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3183.673,T = 126.58, di_pinhao = 10,di_coroa = -111.7309,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_38_ext_25_20_09_11 = Engrenamento(apelido= "Malha externa 38_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 12, Z_coroa = 50, a = 27.5666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.158148,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_38_int_25_20_09_11 = Engrenamento(apelido= "Malha interna 38_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 33, Z_coroa = -84,a = -27.5666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.251052,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3120,T = 129.17, di_pinhao = 10,di_coroa = -114.8027,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_83_ext_25_20_09_11 = Engrenamento(apelido= "Malha externa 83_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 15, Z_coroa = 46, a = 27.1166,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.10127,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_83_int_25_20_09_11 = Engrenamento(apelido= "Malha interna 83_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 20, Z_coroa = -69,a = -27.1166,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.417068,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4239.130,T = 95.07, di_pinhao = 10,di_coroa = -99.90850,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_85_ext_25_20_09_11 = Engrenamento(apelido= "Malha externa 85_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 15, Z_coroa = 47, a = 27.56666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.10476,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_85_int_25_20_09_11 = Engrenamento(apelido= "Malha interna 85_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 21, Z_coroa = -72,a = -27.56666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.391097,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4148.936,T = 97.13, di_pinhao = 10,di_coroa = -101.9108,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_93_ext_25_20_09_11 = Engrenamento(apelido= "Malha externa 93_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 15, Z_coroa = 49, a = 28.4666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1113,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_93_int_25_20_09_11 = Engrenamento(apelido= "Malha interna 93_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 23, Z_coroa = -75,a = -28.4666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.35751,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3979.592,T = 101.27, di_pinhao = 10,di_coroa = -105.7746,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_97_ext_25_20_09_11 = Engrenamento(apelido= "Malha externa 97_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 15, Z_coroa = 51, a = 29.3666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.11750,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_97_int_25_20_09_11 = Engrenamento(apelido= "Malha interna 97_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 25, Z_coroa = -78,a = -29.3666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.32644,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3823.529,T = 105.40, di_pinhao = 10,di_coroa = -109.71337,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_131_ext_25_20_09_11 = Engrenamento(apelido= "Malha externa 131_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 51, a = 30.71666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.078795,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_131_int_25_20_09_11 = Engrenamento(apelido= "Malha interna 131_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 20, Z_coroa = -75 ,a = -30.71666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.38473,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4588.235,T = 87.83, di_pinhao = 10,di_coroa = -107.08138,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_134_ext_25_20_09_11 = Engrenamento(apelido= "Malha externa 134_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 52, a = 31.16666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.08219,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_134_int_25_20_09_11 = Engrenamento(apelido= "Malha interna 134_25_20_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 21, Z_coroa = -78 ,a = -31.16666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.359240,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4588.235,T = 87.83, di_pinhao = 10,di_coroa = -108.9819,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_6_ext_20_25_10_10 = Engrenamento(apelido= "Malha externa 6_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 18, Z_coroa = 41, a = 29.16666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.0481758,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_6_int_20_25_10_10 = Engrenamento(apelido= "Malha interna 6_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 16, Z_coroa = -75 ,a = -29.16666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.432554,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5707.317,T = 70.61, di_pinhao = 10,di_coroa = -97.71628,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_7_ext_20_25_10_10 = Engrenamento(apelido= "Malha externa 7_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 18, Z_coroa = 41, a = 29.83333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.24712,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_7_int_20_25_10_10 = Engrenamento(apelido= "Malha interna 7_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 16, Z_coroa = -75 ,a = -29.83333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.432554,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5707.317,T = 70.61, di_pinhao = 10,di_coroa = -99.0486,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_13_ext_20_25_10_10 = Engrenamento(apelido= "Malha externa 13_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 18, Z_coroa = 42, a = 30.333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.24924,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_13_int_20_25_10_10 = Engrenamento(apelido= "Malha interna 13_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 17, Z_coroa = -78 ,a = -30.333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.40342,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5571.429,T = 72.33, di_pinhao = 10,di_coroa = -100.9777,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_23_ext_20_25_10_10 = Engrenamento(apelido= "Malha externa 23_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 18, Z_coroa = 45, a = 31.16666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.065753,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_23_int_20_25_10_10 = Engrenamento(apelido= "Malha interna 23_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 19, Z_coroa = -81 ,a = -31.16666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.36412,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5200,T = 77.50, di_pinhao = 10,di_coroa = -104.56565,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_28_ext_20_25_10_10 = Engrenamento(apelido= "Malha externa 28_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 18, Z_coroa = 45, a = 31.83333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.255307,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_28_int_20_25_10_10 = Engrenamento(apelido= "Malha interna 28_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 20, Z_coroa = -84 ,a = -31.83333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.338534,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5200,T = 77.50, di_pinhao = 10,di_coroa = -106.8477,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_30_ext_20_25_10_10 = Engrenamento(apelido= "Malha externa 30_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 18, Z_coroa = 46, a = 31.6666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.06974,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_30_int_20_25_10_10 = Engrenamento(apelido= "Malha interna 30_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 20, Z_coroa = -84 ,a = -31.6666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.338534,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5086.957,T = 79.22, di_pinhao = 10,di_coroa = -106.52680,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_57_ext_20_25_10_10 = Engrenamento(apelido= "Malha externa 57_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 21, Z_coroa = 43, a = 31.666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.020547,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_57_int_20_25_10_10 = Engrenamento(apelido= "Malha interna 57_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 15, Z_coroa = -78 ,a = -31.666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.432124,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 6348.837,T = 63.48, di_pinhao = 10,di_coroa = -101.7015,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_59_ext_20_25_10_10 = Engrenamento(apelido= "Malha externa 59_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 21, Z_coroa = 44, a = 32.1666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.02527,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_59_int_20_25_10_10 = Engrenamento(apelido= "Malha interna 59_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 16, Z_coroa = -81 ,a = -32.1666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.40180,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 6204.545,T = 64.95, di_pinhao = 10,di_coroa = -103.65310,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_60_ext_20_25_10_10 = Engrenamento(apelido= "Malha externa 60_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 21, Z_coroa = 44, a = 32.83333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.241272,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_60_int_20_25_10_10 = Engrenamento(apelido= "Malha interna 60_20_25_10_10",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1, Z_pinhao = 16, Z_coroa = -81 ,a = -32.83333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.401809,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 6204.545,T = 64.95, di_pinhao = 10,di_coroa = -104.9856,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_7_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 7_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 51, a = 27.26666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.0708396,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_7_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 7_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 17, Z_coroa = -63 ,a = -27.26666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.482708,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4588.235,T = 87.83, di_pinhao = 10,di_coroa = -99.11094,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_9_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 9_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 52, a = 27.666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.074337,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_9_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 9_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 17, Z_coroa = -63 ,a = -27.666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.48270,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4500,T = 89.56, di_pinhao = 10,di_coroa = -99.892570,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_10_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 10_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 52, a = 28.33333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.296385,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_10_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 10_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 17, Z_coroa = -66 ,a = -28.33333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.45475,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4500,T = 89.56, di_pinhao = 10,di_coroa = -102.3943,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_28_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 28_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 55, a = 28.8666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.0841,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_28_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 28_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -69 ,a = -28.8666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.41706,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4254.454,T = 94.72, di_pinhao = 10,di_coroa = -105.7809,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_29_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 29_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 55, a = 29.533333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.300674,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_29_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 29_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -69 ,a = -29.533333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.41706,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4254.545,T = 94.72, di_pinhao = 10,di_coroa = -107.0703,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_32_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 32_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 56, a = 29.2666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.0874286,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_32_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 32_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -69 ,a = -29.2666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4170,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4178.571,T = 96.44, di_pinhao = 10,di_coroa = -106.5371,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_33_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 33_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 56, a = 29.9333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.30205,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_33_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 33_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 20, Z_coroa = -69 ,a = -29.9333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.41706,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4178.571,T = 96.44, di_pinhao = 10,di_coroa = -107.9102,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_45_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 45_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 58, a = 30.06666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.09369,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_45_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 45_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 22, Z_coroa = -72 ,a = -30.06666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.382088,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4034.483,T = 99.89, di_pinhao = 10,di_coroa = -110.4510,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_46_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 46_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 58, a = 30.7333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.30474,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_46_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 46_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 23, Z_coroa = -75 ,a = -30.7333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.3575,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4034.483,T = 99.89, di_pinhao = 10,di_coroa = -112.9580,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_49_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 49_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = 59, a = 30.46666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.0966,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_49_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 49_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 22, Z_coroa = -72 ,a = -30.46666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.3820880,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3966.102,T = 101.61, di_pinhao = 10,di_coroa = -111.2824,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_95_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 95_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 21, Z_coroa = 54, a = 29.66666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.046016,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_95_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 95_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 16, Z_coroa = -66 ,a = -29.666663,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.479681,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5055.556,T = 79.71, di_pinhao = 10,di_coroa = -102.70210,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_100_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 100_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 21, Z_coroa = 55, a = 30.733333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.291526,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_100_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 100_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 17, Z_coroa = -69 ,a = -30.733333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4506865,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4963.636,T = 81.19, di_pinhao = 10,di_coroa = -105.98170,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_112_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 112_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 21, Z_coroa = 59, a = 31.6666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.06362,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_112_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 112_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 19, Z_coroa = -72,a = -31.6666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4112081,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4627.119,T = 87.10, di_pinhao = 10,di_coroa = -110.12283,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_127_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 127_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 24, Z_coroa = 55, a = 31.933333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.282854,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_127_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 127_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 15, Z_coroa = -69,a = -31.933333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.478413,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5672.727,T = 71.04, di_pinhao = 10,di_coroa = -106.0469,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_128_ext_20_25_08_12 = Engrenamento(apelido= "Malha externa 128_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 24, Z_coroa = 56, a = 32.3333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.284318,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_128_int_20_25_08_12 = Engrenamento(apelido= "Malha interna 128_20_25_08_12",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 15, Z_coroa = -69,a = -32.3333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4784132,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5571.429,T = 72.33, di_pinhao = 10,di_coroa = -106.81549,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_1_ext_20_25_09_11 = Engrenamento(apelido= "Malha externa 1_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 43, a = 27.78333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.2648991,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_1_int_20_25_09_11 = Engrenamento(apelido= "Malha interna 1_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 15, Z_coroa = -66,a = -27.78333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.49391,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5441.860,T = 74.06, di_pinhao = 10,di_coroa = -95.91522,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_10_ext_20_25_09_11 = Engrenamento(apelido= "Malha externa 10_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 47, a = 28.916666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.0655496,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_10_int_20_25_09_11 = Engrenamento(apelido= "Malha interna 10_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 17, Z_coroa = -69,a = -28.916666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.450686,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4978.723,T = 80.94, di_pinhao = 10,di_coroa = -100.290534,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_17_ext_20_25_09_11 = Engrenamento(apelido= "Malha externa 17_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 49, a = 30.48333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.27526,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_17_int_20_25_09_11 = Engrenamento(apelido= "Malha interna 17_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 19, Z_coroa = -75,a = -30.48333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.395237,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4775.510,T = 84.39, di_pinhao = 10,di_coroa = -105.5015,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_24_ext_20_25_09_11 = Engrenamento(apelido= "Malha externa 24_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 51, a = 30.716666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.08017,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_24_int_20_25_09_11 = Engrenamento(apelido= "Malha interna 24_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 20, Z_coroa = -75,a = -30.716666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.384735,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4588.235,T = 87.83, di_pinhao = 10,di_coroa = -107.061638,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_27_ext_20_25_09_11 = Engrenamento(apelido= "Malha externa 27_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 51, a = 31.38333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.27840,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_27_int_20_25_09_11 = Engrenamento(apelido= "Malha interna 27_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 21, Z_coroa = -78,a = -31.38333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.359240,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4588.235,T = 87.83, di_pinhao = 10,di_coroa = -109.4071,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_31_ext_20_25_09_11 = Engrenamento(apelido= "Malha externa 31_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 18, Z_coroa = 52, a = 31.166666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.0835316,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_31_int_20_25_09_11 = Engrenamento(apelido= "Malha interna 31_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 21, Z_coroa = -78,a = -31.166666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.3592402,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4500,T = 89.56, di_pinhao = 10,di_coroa = -108.978,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_61_ext_20_25_09_11 = Engrenamento(apelido= "Malha externa 61_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 21, Z_coroa = 47, a = 30.93333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.26104007,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_61_int_20_25_09_11 = Engrenamento(apelido= "Malha interna 61_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 15, Z_coroa = -72,a = -30.93333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.46290,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5808.511,T = 69.38, di_pinhao = 10,di_coroa = -102.16143,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_69_ext_20_25_09_11 = Engrenamento(apelido= "Malha externa 69_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 21, Z_coroa = 50, a = 31.616666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.041568,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_69_int_20_25_09_11 = Engrenamento(apelido= "Malha interna 69_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 17, Z_coroa = -75,a = -31.616666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4190035,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5460,T = 73.81, di_pinhao = 10,di_coroa = -105.6169,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_70_ext_20_25_09_11 = Engrenamento(apelido= "Malha externa 70_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 21, Z_coroa = 50, a = 32.28333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.266126,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_70_int_20_25_09_11 = Engrenamento(apelido= "Malha interna 70_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 17, Z_coroa = -75,a = -32.28333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.41900,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5460,T = 73.81, di_pinhao = 10,di_coroa = -106.959042,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_71_ext_20_25_09_11 = Engrenamento(apelido= "Malha externa 71_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.9, Z_pinhao = 21, Z_coroa = 51, a = 32.066666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.0455941,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_71_int_20_25_09_11 = Engrenamento(apelido= "Malha interna 71_20_25_09_11",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.1, Z_pinhao = 17, Z_coroa = -75,a = -32.066666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.419003,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5352.941,T = 75.29, di_pinhao = 10,di_coroa = -106.50909,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_3_ext_20_20_12_08 = Engrenamento(apelido= "Malha externa 3_20_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 18, Z_coroa = 35, a = 32.13333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.2112230,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_3_int_20_20_12_08 = Engrenamento(apelido= "Malha interna 3_20_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = -99,a = -32.13333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.290539,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 6685.714,T = 60.28, di_pinhao = 10,di_coroa = -101.14860,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_6_ext_25_25_12_08 = Engrenamento(apelido= "Malha externa 6_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 30, a = 24.86666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.10711218,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_6_int_25_25_12_08 = Engrenamento(apelido= "Malha interna 6_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 19, Z_coroa = -81,a = -24.86666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.364128,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5200,T = 77.5, di_pinhao = 10,di_coroa = -87.51675,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_11_ext_25_25_12_08 = Engrenamento(apelido= "Malha externa 11_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 32, a = 26.06666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1158053,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_11_int_25_25_12_08 = Engrenamento(apelido= "Malha interna 11_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 22, Z_coroa = -87,a = -26.06666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.30525,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4875,T = 82.67, di_pinhao = 10,di_coroa = -92.2225,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_19_ext_25_25_12_08 = Engrenamento(apelido= "Malha externa 19_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 34, a = 27.26666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.123927,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_19_int_25_25_12_08 = Engrenamento(apelido= "Malha interna 19_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 25, Z_coroa = -93,a = -27.26666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.254761,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4588.235,T = 87.83, di_pinhao = 10,di_coroa = -96.941698,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_24_ext_25_25_12_08 = Engrenamento(apelido= "Malha externa 24_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 36, a = 28.466666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.131301,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_24_int_25_25_12_08 = Engrenamento(apelido= "Malha interna 24_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 28, Z_coroa = -99,a = -28.466666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.21165,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4333.333,T = 93, di_pinhao = 10,di_coroa = -101.6726,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_33_ext_25_25_12_08 = Engrenamento(apelido= "Malha externa 33_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 38, a = 29.666666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1380356,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_33_int_25_25_12_08 = Engrenamento(apelido= "Malha interna 33_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 31, Z_coroa = -105,a = -29.666666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.175055,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4105.263,T = 98.17, di_pinhao = 10,di_coroa = -106.41410,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_38_ext_25_25_12_08 = Engrenamento(apelido= "Malha externa 38_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 39, a = 30.26666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1412669,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_38_int_25_25_12_08 = Engrenamento(apelido= "Malha interna 38_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 33, Z_coroa = -108,a = -30.26666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1570403,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4000,T = 100.75, di_pinhao = 10,di_coroa = -109.19526,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_45_ext_25_25_12_08 = Engrenamento(apelido= "Malha externa 45_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 40, a = 30.86666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.144337,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_45_int_25_25_12_08 = Engrenamento(apelido= "Malha interna 45_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 36, Z_coroa = -114,a = -30.86666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.129099,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -112.75673,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_93_ext_25_25_12_08 = Engrenamento(apelido= "Malha externa 93_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 15, Z_coroa = 34, a = 29.06666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.069921,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_93_int_25_25_12_08 = Engrenamento(apelido= "Malha interna 93_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 20, Z_coroa = -93,a = -29.06666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.29577,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5735.294,T = 70.27, di_pinhao = 10,di_coroa = -96.609411,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_95_ext_25_25_12_08 = Engrenamento(apelido= "Malha externa 95_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 15, Z_coroa = 35, a = 29.66666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.07497,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_95_int_25_25_12_08 = Engrenamento(apelido= "Malha interna 95_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 21, Z_coroa = -96,a = -29.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.272982,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5571.429,T = 72.33, di_pinhao = 10,di_coroa = -98.5876,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_133_ext_25_25_12_08 = Engrenamento(apelido= "Malha externa 133_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 18, Z_coroa = 31, a = 29.0666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.005158,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_133_int_25_25_12_08 = Engrenamento(apelido= "Malha interna 133_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 14, Z_coroa = -87,a = -29.0666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.404173,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 7548.387,T = 53.39, di_pinhao = 10,di_coroa = -91.98284,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_164_ext_25_25_12_08 = Engrenamento(apelido= "Malha externa 164_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 21, Z_coroa = 34, a = 33.33333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1920848,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_164_int_25_25_12_08 = Engrenamento(apelido= "Malha interna 164_25_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 15, Z_coroa = -99,a = -33.33333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.331114,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 8029.412,T = 50.19, di_pinhao = 10,di_coroa = -101.2063851,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_4_ext_20_25_12_08 = Engrenamento(apelido= "Malha externa 4_20_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 18, Z_coroa = 31, a = 29.066666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.00673760,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_4_int_20_25_12_08 = Engrenamento(apelido= "Malha interna 4_20_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 14, Z_coroa = -87,a = -29.066666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.404173,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 7548.387,T = 53.39, di_pinhao = 10,di_coroa = -91.982844,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_8_ext_20_25_12_08 = Engrenamento(apelido= "Malha externa 8_20_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 18, Z_coroa = 33, a = 30.93333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.20553,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_8_int_20_25_12_08 = Engrenamento(apelido= "Malha interna 8_20_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 16, Z_coroa = -93,a = -30.93333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.34339906,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 7090.909,T = 56.83, di_pinhao = 10,di_coroa = -97.218731,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_14_ext_20_25_12_08 = Engrenamento(apelido= "Malha externa 14_20_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 18, Z_coroa = 34, a = 31.533333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.20842,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_14_int_20_25_12_08 = Engrenamento(apelido= "Malha interna 14_20_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 17, Z_coroa = -96,a = -31.533333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.31603,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 6882.353,T = 58.56, di_pinhao = 10,di_coroa = -99.17296,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_19_ext_20_25_12_08 = Engrenamento(apelido= "Malha externa 19_20_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 18, Z_coroa = 35, a = 32.1333333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.2112230,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_19_int_20_25_12_08 = Engrenamento(apelido= "Malha interna 19_20_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 18, Z_coroa = -99,a = -32.1333333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.290539,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 6685.714,T = 60.28, di_pinhao = 10,di_coroa = -101.1418,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_59_ext_20_25_12_08 = Engrenamento(apelido= "Malha externa 59_20_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 21, Z_coroa = 34, a = 33.33333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.193639,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_59_int_20_25_12_08 = Engrenamento(apelido= "Malha interna 59_20_25_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 15, Z_coroa = -99,a = -33.33333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.33111463,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 8029.412,T = 50.19, di_pinhao = 10,di_coroa = -101.20638,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_2_ext_25_20_12_08 = Engrenamento(apelido= "Malha externa 2_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 30, a = 24.86666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.10711218,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_2_int_25_20_12_08 = Engrenamento(apelido= "Malha interna 2_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 19, Z_coroa = -81,a = -24.86666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.36412889,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5200,T = 77.5, di_pinhao = 10,di_coroa = -87.517279,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_7_ext_25_20_12_08 = Engrenamento(apelido= "Malha externa 7_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 32, a = 26.066666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1158053,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_7_int_25_20_12_08 = Engrenamento(apelido= "Malha interna 7_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 22, Z_coroa = -87,a = -26.066666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.30525,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4875,T = 82.67, di_pinhao = 10,di_coroa = -92.22302,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_15_ext_25_20_12_08 = Engrenamento(apelido= "Malha externa 15_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 34, a = 27.26666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.123927,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_15_int_25_20_12_08 = Engrenamento(apelido= "Malha interna 15_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 25, Z_coroa = -93,a = -27.26666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.254761,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4588.235,T = 87.83, di_pinhao = 10,di_coroa = -96.942,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_20_ext_25_20_12_08 = Engrenamento(apelido= "Malha externa 20_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 36, a = 28.4666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.131301,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_20_int_25_20_12_08 = Engrenamento(apelido= "Malha interna 20_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 28, Z_coroa = -99,a = -28.4666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.21165,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4333.333,T = 93, di_pinhao = 10,di_coroa = -101.673149,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_29_ext_25_20_12_08 = Engrenamento(apelido= "Malha externa 29_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 38, a = 29.6666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.138035,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_29_int_25_20_12_08 = Engrenamento(apelido= "Malha interna 29_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 31, Z_coroa = -105,a = -29.6666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.175055,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4105.263,T = 98.17, di_pinhao = 10,di_coroa = -106.414,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_34_ext_25_20_12_08 = Engrenamento(apelido= "Malha externa 34_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 39, a = 30.26666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1412669,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_34_int_25_20_12_08 = Engrenamento(apelido= "Malha interna 34_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 33, Z_coroa = -108,a = -30.26666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.157040,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4000,T = 100.75, di_pinhao = 10,di_coroa = -109.2019,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_41_ext_25_20_12_08 = Engrenamento(apelido= "Malha externa 41_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 12, Z_coroa = 40, a = 30.866666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.144337,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_41_int_25_20_12_08 = Engrenamento(apelido= "Malha interna 41_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 36, Z_coroa = -114,a = -30.866666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.129099,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -112.76785,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_77_ext_25_20_12_08 = Engrenamento(apelido= "Malha externa 77_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 15, Z_coroa = 34, a = 29.066666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.069921,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_77_int_25_20_12_08 = Engrenamento(apelido= "Malha interna 77_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 20, Z_coroa = -93,a = -29.066666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.29577,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5735.294,T = 70.27, di_pinhao = 10,di_coroa = -96.61125,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_79_ext_25_20_12_08 = Engrenamento(apelido= "Malha externa 79_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.2, Z_pinhao = 15, Z_coroa = 35, a = 29.66666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.074972,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_79_int_25_20_12_08 = Engrenamento(apelido= "Malha interna 79_25_20_12_08",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.8, Z_pinhao = 21, Z_coroa = -96,a = -29.66666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.2729828,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5571.429,T = 72.33, di_pinhao = 10,di_coroa = -98.59923,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_1_ext_20_20_07_13 = Engrenamento(apelido= "Malha externa 1_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 57, a = 26.583333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.32393,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_1_int_20_20_07_13 = Engrenamento(apelido= "Malha interna 1_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 18, Z_coroa = -60,a = -26.583333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.4872627,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4105.263,T = 98.17, di_pinhao = 10,di_coroa = -101.24130,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_11_ext_20_20_07_13 = Engrenamento(apelido= "Malha externa 11_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 60, a = 26.966666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.088516,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_11_int_20_20_07_13 = Engrenamento(apelido= "Malha interna 11_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 19, Z_coroa = -60,a = -26.966666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.4767089,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -103.15007,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_18_ext_20_20_07_13 = Engrenamento(apelido= "Malha externa 18_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 60, a = 27.63333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.3272428,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_18_int_20_20_07_13 = Engrenamento(apelido= "Malha interna 18_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 20, Z_coroa = -63,a = -27.63333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.450200,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -105.71542,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_41_ext_20_20_07_13 = Engrenamento(apelido= "Malha externa 41_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 66, a = 29.066666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.105249,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_41_int_20_20_07_13 = Engrenamento(apelido= "Malha interna 41_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 24, Z_coroa = -69,a = -29.066666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.382329,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3545.455,T = 113.67, di_pinhao = 10,di_coroa = -113.586,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_42_ext_20_20_07_13 = Engrenamento(apelido= "Malha externa 42_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 66, a = 29.733333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.3334031,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_42_int_20_20_07_13 = Engrenamento(apelido= "Malha interna 42_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 24, Z_coroa = -69,a = -29.733333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.382329,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3545.455,T = 113.67, di_pinhao = 10,di_coroa = -114.9678,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_96_ext_20_20_07_13 = Engrenamento(apelido= "Malha externa 96_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 63, a = 29.066666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.0636592,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_96_int_20_20_07_13 = Engrenamento(apelido= "Malha interna 96_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 18, Z_coroa = -63,a = -29.066666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.471016,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4333.333,T = 93, di_pinhao = 10,di_coroa = -106.01684,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_97_ext_20_20_07_13 = Engrenamento(apelido= "Malha externa 97_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 63, a = 29.733333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.322715,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_97_int_20_20_07_13 = Engrenamento(apelido= "Malha interna 97_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 18, Z_coroa = -63,a = -29.733333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.471016,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4333.333,T = 93, di_pinhao = 10,di_coroa = -107.3983,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_102_ext_20_20_07_13 = Engrenamento(apelido= "Malha externa 102_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 64, a = 30.08333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.32377,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_102_int_20_20_07_13 = Engrenamento(apelido= "Malha interna 102_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 19, Z_coroa = -66,a = -30.08333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.443755,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4265.625,T = 94.48, di_pinhao = 10,di_coroa = -109.32743,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_118_ext_20_20_07_13 = Engrenamento(apelido= "Malha externa 118_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 67, a = 30.46666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.075475,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_118_int_20_20_07_13 = Engrenamento(apelido= "Malha interna 118_20_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 20, Z_coroa = -66,a = -30.46666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.4335636,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4074.627,T = 98.9, di_pinhao = 10,di_coroa = -111.38679,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_0_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 0_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 45, a = 19.616666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1329188,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_0_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 0_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 17, Z_coroa = -48,a = -19.616666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.56004,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3466.667,T = 116.25, di_pinhao = 10,di_coroa = -86.10923,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_2_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 2_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 47, a = 20.31666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.13828,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_2_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 2_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 19, Z_coroa = -51,a = -20.31666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.52547394,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3319.4166,T = 121.4167, di_pinhao = 10,di_coroa = -90.0045,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_7_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 7_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 49, a = 21.016666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1433770,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_7_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 7_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 21, Z_coroa = -54,a = -21.016666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.491559,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3183.673469,T = 126.583, di_pinhao = 10,di_coroa = -93.9038,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_15_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 15_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 51, a = 21.71666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.14807833,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_15_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 15_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 23, Z_coroa = -57,a = -21.71666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.45852,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3058.823,T = 131.75, di_pinhao = 10,di_coroa = -97.8075,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_22_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 22_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 53, a = 22.4166,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.152429,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_22_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 22_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 25, Z_coroa = -60,a = -22.4166,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.426562,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 2943.396226,T = 136.9167, di_pinhao = 10,di_coroa = -101.7157,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_28_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 28_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 54, a = 22.76666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1544898,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_28_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 28_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 27, Z_coroa = -63,a = -22.76666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.39581,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 2888.889,T = 139.5, di_pinhao = 10,di_coroa = -104.9973,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_37_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 37_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 56, a = 23.46666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.158930,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_37_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 37_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 29, Z_coroa = -66,a = -23.46666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.36639805,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 2785.714,T = 144.66, di_pinhao = 10,di_coroa = -108.90546,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_52_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 52_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 59, a = 24.5166,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1650560,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_52_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 52_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 32, Z_coroa = -69,a = -24.5166,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.33330,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 2644.067,T = 152.416, di_pinhao = 10,di_coroa = -114.789,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_106_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 106_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 15, Z_coroa = 50, a = 22.41666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0964999,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_106_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 106_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 16, Z_coroa = -51,a = -22.41666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.556421,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -90.3533756,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_123_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 123_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 15, Z_coroa = 58, a = 25.21666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.119899,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_123_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 123_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 22, Z_coroa = -60,a = -25.21666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4492285,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3362.07,T = 119.87, di_pinhao = 10,di_coroa = -103.4985,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_129_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 129_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 15, Z_coroa = 60, a = 25.9166666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1249149,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_129_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 129_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 24, Z_coroa = -63,a = -25.9166666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.416329,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3250,T = 124, di_pinhao = 10,di_coroa = -107.42100,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_138_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 138_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 15, Z_coroa = 62, a = 26.61666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.129635,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_138_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 138_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 27, Z_coroa = -69,a = -26.61666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.3614416,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3145.16,T = 128.13, di_pinhao = 10,di_coroa = -112.6072,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_191_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 191_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 57, a = 25.9166666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.077471,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_191_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 191_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 17, Z_coroa = -57,a = -25.9166666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.5144962,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4105.26,T = 98.17, di_pinhao = 10,di_coroa = -98.5222619,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_195_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 195_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 60, a = 26.966666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.086635757,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_195_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 195_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 19, Z_coroa = -60,a = -26.966666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.47670897,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -103.13958,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_210_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 210_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 66, a = 29.066666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.103646,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_210_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 210_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 24, Z_coroa = -69,a = -29.066666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.38232,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3545.45,T = 113.67, di_pinhao = 10,di_coroa = -113.58276,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_246_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 246_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 59, a = 28.33333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.315708,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_246_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 246_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 16, Z_coroa = -60,a = -28.33333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.5110694,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4627.12,T = 87.1, di_pinhao = 10,di_coroa = -102.05716,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_260_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 260_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 63, a = 29.06666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0617276,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_260_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 260_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 18, Z_coroa = -63,a = -29.06666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.471016126,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4333.33,T = 93, di_pinhao = 10,di_coroa = -106.01334,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_261_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 261_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 63, a = 29.73333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.320309,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_261_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 261_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 18, Z_coroa = -63,a = -29.73333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.471016,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4333.33,T = 93, di_pinhao = 10,di_coroa = -107.376,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_266_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 266_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 64, a = 30.0833333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.321419,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_266_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 266_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 19, Z_coroa = -66,a = -30.0833333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.44375,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4265.63,T = 94.48, di_pinhao = 10,di_coroa = -109.3045,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_282_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 282_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 67, a = 30.4666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0737277,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_282_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 282_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 20, Z_coroa = -66,a = -30.4666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.433563646,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4074.63,T = 98.9, di_pinhao = 10,di_coroa = -111.3577,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_324_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 324_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 24, Z_coroa = 59, a = 29.38333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.30821403,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_324_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 324_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 14, Z_coroa = -60,a = -29.38333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.53946,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5288.14,T = 76.21, di_pinhao = 10,di_coroa = -101.6622,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_330_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 330_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 24, Z_coroa = 64, a = 30.46666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.033850,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_330_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 330_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 16, Z_coroa = -63,a = -30.46666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.495427,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4875,T = 82.67, di_pinhao = 10,di_coroa = -106.272497,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_331_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 331_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 24, Z_coroa = 65, a = 31.48333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.31520,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_331_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 331_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 17, Z_coroa = -66,a = -31.48333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.4666874,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4800,T = 83.96, di_pinhao = 10,di_coroa = -109.5500,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_346_ext_25_25_07_13 = Engrenamento(apelido= "Malha externa 346_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 27, Z_coroa = 63, a = 31.1666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.0014399,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_346_int_25_25_07_13 = Engrenamento(apelido= "Malha interna 346_25_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 14, Z_coroa = -63,a = -31.1666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.5246368,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5571.43,T = 72.33, di_pinhao = 10,di_coroa = -105.2188,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_7_ext_20_25_07_13 = Engrenamento(apelido= "Malha externa 7_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 57, a = 25.916666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.079398,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_7_int_20_25_07_13 = Engrenamento(apelido= "Malha interna 7_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 17, Z_coroa = -57,a = -25.916666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.514496,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4105.26,T = 98.17, di_pinhao = 10,di_coroa = -98.5222619,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_17_ext_20_25_07_13 = Engrenamento(apelido= "Malha externa 17_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 60, a = 26.9666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.088516,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_17_int_20_25_07_13 = Engrenamento(apelido= "Malha interna 17_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 19, Z_coroa = -60,a = -26.9666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.476708,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -103.1395,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_24_ext_20_25_07_13 = Engrenamento(apelido= "Malha externa 24_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 60, a = 27.6333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.3272,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_24_int_20_25_07_13 = Engrenamento(apelido= "Malha interna 24_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 20, Z_coroa = -63,a = -27.6333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.450200,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -105.704182,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_47_ext_20_25_07_13 = Engrenamento(apelido= "Malha externa 47_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 66, a = 29.066666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.10524,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_47_int_20_25_07_13 = Engrenamento(apelido= "Malha interna 47_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 24, Z_coroa = -69,a = -29.066666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.3823,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3545.45,T = 113.67, di_pinhao = 10,di_coroa = -113.5827,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_48_ext_20_25_07_13 = Engrenamento(apelido= "Malha externa 48_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 66, a = 29.73333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.3334031,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_48_int_20_25_07_13 = Engrenamento(apelido= "Malha interna 48_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 24, Z_coroa = -69,a = -29.73333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.382329,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3545.45,T = 113.67, di_pinhao = 10,di_coroa = -114.9460,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_112_ext_20_25_07_13 = Engrenamento(apelido= "Malha externa 112_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 59, a = 28.33333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.31831,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_112_int_20_25_07_13 = Engrenamento(apelido= "Malha interna 112_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 16, Z_coroa = -60,a = -28.33333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.511069,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4627.12,T = 87.1, di_pinhao = 10,di_coroa = -102.05716,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_126_ext_20_25_07_13 = Engrenamento(apelido= "Malha externa 126_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 63, a = 29.06666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.063659,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_126_int_20_25_07_13 = Engrenamento(apelido= "Malha interna 126_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 18, Z_coroa = -63,a = -29.06666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.47101,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4333.33,T = 93, di_pinhao = 10,di_coroa = -106.01334,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_127_ext_20_25_07_13 = Engrenamento(apelido= "Malha externa 127_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 63, a = 29.7333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.32271,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_127_int_20_25_07_13 = Engrenamento(apelido= "Malha interna 127_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 18, Z_coroa = -63,a = -29.7333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.471016,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4333.33,T = 93, di_pinhao = 10,di_coroa = -107.37659,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_132_ext_20_25_07_13 = Engrenamento(apelido= "Malha externa 127_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 64, a = 30.083333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.3237721,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_132_int_20_25_07_13 = Engrenamento(apelido= "Malha interna 127_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 19, Z_coroa = -66,a = -30.083333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.443755,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4265.63,T = 94.48, di_pinhao = 10,di_coroa = -109.30456,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_148_ext_20_25_07_13 = Engrenamento(apelido= "Malha externa 127_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 67, a = 30.46666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.07547,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_148_int_20_25_07_13 = Engrenamento(apelido= "Malha interna 127_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 20, Z_coroa = -66,a = -30.46666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.43356,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4074.63,T = 98.9, di_pinhao = 10,di_coroa = -111.3577,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_190_ext_20_25_07_13 = Engrenamento(apelido= "Malha externa 190_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 24, Z_coroa = 59, a = 29.38333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.31086,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_190_int_20_25_07_13 = Engrenamento(apelido= "Malha interna 190_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 14, Z_coroa = -60,a = -29.38333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.539469,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5288.14,T = 76.21, di_pinhao = 10,di_coroa = -101.66227,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_196_ext_20_25_07_13 = Engrenamento(apelido= "Malha externa 196_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 24, Z_coroa = 64, a = 30.46666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.03589,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_196_int_20_25_07_13 = Engrenamento(apelido= "Malha interna 196_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 16, Z_coroa = -63,a = -30.46666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.49542,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4875,T = 82.67, di_pinhao = 10,di_coroa = -106.272497,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)





# Dim_214_ext_20_25_07_13 = Engrenamento(apelido= "Malha externa 214_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 27, Z_coroa = 63, a = 31.166666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.0036723,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_214_int_20_25_07_13 = Engrenamento(apelido= "Malha interna 214_20_25_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 14, Z_coroa = -63,a = -31.166666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.5246368,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 5571.43,T = 72.33, di_pinhao = 10,di_coroa = -105.21881,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_2_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 2_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 47, a = 20.3166666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.138281,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_2_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 2_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 19, Z_coroa = -51,a = -20.3166666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.525473,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3319.15,T = 121.42, di_pinhao = 10,di_coroa = -90.042464,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_8_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 8_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 49, a = 21.01666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.143377,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_8_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 8_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 21, Z_coroa = -54,a = -21.01666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.491559,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3183.67,T = 126.58, di_pinhao = 10,di_coroa = -93.93284,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_16_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 16_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 51, a = 21.716666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.148078,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_16_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 16_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 23, Z_coroa = -57,a = -21.716666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.458527,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3058.82,T = 131.75, di_pinhao = 10,di_coroa = -97.82912,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_22_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 22_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 53, a = 22.41666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.152429,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_22_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 22_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 25, Z_coroa = -60,a = -22.41666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.4265626,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 2943.4,T = 136.92, di_pinhao = 10,di_coroa = -101.731351,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_28_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 28_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 54, a = 22.7666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.15448,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_28_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 28_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 27, Z_coroa = -63,a = -22.7666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.39581,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 2888.89,T = 139.50, di_pinhao = 10,di_coroa = -105.0567,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_37_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 37_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 56, a = 23.4666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.1589,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_37_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 37_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 29, Z_coroa = -66,a = -23.4666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.36639,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 2785.71,T = 144.67, di_pinhao = 10,di_coroa = -108.9535,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_52_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 52_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 12, Z_coroa = 59, a = 24.5166,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.165056,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_52_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 52_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 32, Z_coroa = -69,a = -24.5166,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.333305,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 2644.07,T = 152.42, di_pinhao = 10,di_coroa = -114.8140,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)

# Dim_118_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 118_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 15, Z_coroa = 58, a = 25.21666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.11989,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_118_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 118_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 22, Z_coroa = -60,a = -25.21666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.44922,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3362.07,T = 119.87, di_pinhao = 10,di_coroa = -103.5275,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_124_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 124_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 15, Z_coroa = 60, a = 25.9166,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.124914,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_124_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 124_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 24, Z_coroa = -63,a = -25.9166,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.4163293,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3250,T = 124, di_pinhao = 10,di_coroa = -107.4547,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_132_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 132_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 15, Z_coroa = 62, a = 26.61666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.129635,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_132_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 132_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 27, Z_coroa = -69,a = -26.61666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.36144,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3145.16,T = 128.13, di_pinhao = 10,di_coroa = -112.66570,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_182_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 182_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 60, a = 26.96666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.086635,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_182_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 182_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 19, Z_coroa = -60,a = -26.96666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.476708,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3900,T = 103.33, di_pinhao = 10,di_coroa = -103.150070,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_197_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 197_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 18, Z_coroa = 66, a = 29.066666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.103646,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_197_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 197_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 24, Z_coroa = -69,a = -29.066666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.3823296,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 3545.45,T = 113.67, di_pinhao = 10,di_coroa = -113.58626,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)




# Dim_228_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 228_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 63, a = 29.06666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.061727,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_228_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 228_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 18, Z_coroa = -63,a = -29.06666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.471016,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4333.33,T = 93, di_pinhao = 10,di_coroa = -106.0168480,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_229_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 229_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 63, a = 29.7333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.32030,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_229_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 229_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 18, Z_coroa = -63,a = -29.7333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.471016,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4333.33,T = 93, di_pinhao = 10,di_coroa = -107.39839,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_234_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 234_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 64, a = 30.08333,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.3214130,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_234_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 234_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 19, Z_coroa = -66,a = -30.08333,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.44375,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4265.63,T = 94.48, di_pinhao = 10,di_coroa = -109.3274,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



# Dim_250_ext_25_20_07_13 = Engrenamento(apelido= "Malha externa 250_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 0.7, Z_pinhao = 21, Z_coroa = 67, a = 30.4666,b_pinhao = 14.25,b_coroa = 13.75,ISO = 7,alpha_n = 25,beta = 0,
#                      x_pinhao = 0.073727,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Retificação",
#                      IQ_pinhao = 5,IQ_coroa = 5,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 0.4,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 2,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 13000,T = 31, di_pinhao = 0,di_coroa = 10,bs_pinhao = 14.25,bs_coroa = 13.75,d_sh_pinhao =10.5 ,d_sh_coroa = 10,L_pinhao=134.100,
#                      L_coroa = 32,sh_pinhao =25,sh_coroa =4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)


# Dim_250_int_25_20_07_13 = Engrenamento(apelido= "Malha interna 250_25_20_07_13",Proj = "Gabriel Dias",tipo="Otimização",  material_pinhao = Material_base ,material_coroa = Material_base,ferramenta_pinhao = base_ferramenta_pinhao ,
#                      ferramenta_coroa = base_ferramenta_coroa,lubrificante = base_lubrificante ,m_n = 1.3, Z_pinhao = 20, Z_coroa = -66,a = -30.4666,b_pinhao = 15.75,b_coroa = 16.25,ISO = 7,alpha_n = 20,beta = 0,
#                      x_pinhao = 0.433563,metodo_x = "DIN",M_BS = None,Lambda = None, afastamento_pinhao ="d",afastamento_coroa ="d",tol_pinhao =26,tol_coroa =26,ASNE_min_pinhao = None,ASNE_max_pinhao = None,
#                      ASNE_min_coroa = None,ASNE_max_coroa = None,f_chanfro_pinhao = 0,f_chanfro_coroa = 0 ,f_b_pinhao = 1.6,f_b_coroa = 1.6,crwon_s_pinhao = 0.02,crwon_i_pinhao = 0.01,crwon_s_coroa= 0,
#                      crwon_i_coroa= 0,irregularidade_movida = "Choque leve",irregularidade_motora = "Choque leve",op_acabamento_pinhao = "Retificação",op_acabamento_coroa = "Fresamento",
#                      IQ_pinhao = 5,IQ_coroa = 8,Ra_flanco_pinhao = 0.4 ,Ra_flanco_coroa = 6.3,Ra_pe_pinhao = 5,Ra_pe_coroa = 5,S_Hmin = 1.1,S_Fmin = 1.2,S_Hmax = 1.3,S_Fmax = 1.4,Arranjo_pinhao = 7,
#                      Arranjo_coroa = 1,k_linha_pinhao = None,k_linha_coroa = None,n_t = 4074.63,T = 98.9, di_pinhao = 10,di_coroa = -111.3867,bs_pinhao = 18,bs_coroa = 18,d_sh_pinhao = 10,d_sh_coroa = 0,L_pinhao=30,
#                      L_coroa = 10,sh_pinhao = 4,sh_coroa = 4,C_Cdil = 1e-05 ,T_Rmd = 80,T_Cmd = 30,T_op = 80,Vr = 115 ,k_otimi_pinhao = None,k_otimi_coroa = None,Dim_sobre_pinos_pinhao = None,Dim_sobre_pinos_coroa =None,
#                      trans = "Planetário",N_cp = 3,Ky = 1.05,F_B_rolamento = 0.01,imersao = "pinhão", S_M_pinhao = 0,S_M_coroa = 0)



