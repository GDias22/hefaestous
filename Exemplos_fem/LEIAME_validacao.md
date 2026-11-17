# Validação dos exemplos contra a interface web

Gerado por `web/tools/validacao_exemplos.py`. Cada exemplo é montado como projeto do app, calculado por `calcular_json` e comparado com `_revisao/depois/resultados.json` (código original corrigido) e, para os exemplos 1 e 6, com a ISO/TR 6336-30 (`NORMA` de `_revisao/comparar.py`).

## Ex. 6: efeito do campo Ring (o app fixa Ring='Fixo' em trens)

Com Ring='Fixo' (o que o app usa em qualquer trem: `calcular._params_analise(..., 'Fixo')`) o Ex. 6 desvia do original em 0 fatores (maior 0.00e+00); com Ring='Rotativo' (usado em `_revisao/run_casos.py` para o Ex. 6) calculando as mesmas geometrias: 68 fatores comparados, maior desvio 0.00e+00, 0 fatores acima de 1e-6.

## Resumo por caso (app × original corrigido)

| Caso | Fatores comparados | Maior desvio relativo | Fator do máx. | Fatores com desvio > 1e-6 | S_H mín | S_F mín |
|---|---|---|---|---|---|---|
| Validacao_ISO6336-30_Ex1 | 68 | 0.000e+00 | None | nenhum | 1.0267 | 1.8481 |
| Validacao_ISO6336-30_Ex6 | 68 | 0.000e+00 | None | nenhum | 1.1158 | 4.9514 |
| Validacao_Mazzo | 68 | 0.000e+00 | None | nenhum | 1.1040 | 1.2652 |
| Validacao_Galle | 68 | 0.000e+00 | None | nenhum | 0.8520 | 1.5288 |
| Planetario_Pla56_antiga | 136 | 0.000e+00 | None | nenhum | 0.9384 | 1.1911 |
| Planetario_Pla56_ref | 136 | 0.000e+00 | None | nenhum | 1.0817 | 1.0855 |
| Planetario_Pla41_antiga | 136 | 0.000e+00 | None | nenhum | 0.9862 | 1.6772 |
| Planetario_Pla41_ref | 136 | 0.000e+00 | None | nenhum | 0.9848 | 1.1803 |
| Planetario_Pla50_antiga | 136 | 0.000e+00 | None | nenhum | 0.9743 | 1.1204 |
| Planetario_Pla50_ref | 136 | 0.000e+00 | None | nenhum | 1.0007 | 0.8619 |

## Validacao_ISO6336-30_Ex1: app × ISO/TR 6336-30 (valores da norma arredondados a 2 casas)

| Fator | Norma | App | Desvio rel. |
|---|---|---|---|
| Ka | 1.0 | 1.0000 | +0.00% |
| Kv | 1.0 | 1.0063 | +0.63% |
| K_Hbeta | 1.16 | 1.1593 | -0.06% |
| K_Fbeta | 1.13 | 1.1278 | -0.19% |
| K_Halpha | 1.0 | 1.0000 | +0.00% |
| K_Falpha | 1.0 | 1.0000 | +0.00% |
| Z_H | 2.4 | 2.3953 | -0.19% |
| Z_E | 189.81 | 189.8117 | +0.00% |
| Z_epsilon | 0.8 | 0.8038 | +0.47% |
| Z_beta | 1.02 | 1.0194 | -0.05% |
| Z_L | 1.05 | 1.0474 | -0.25% |
| Z_V | 0.97 | 0.9692 | -0.09% |
| Z_R | 0.97 | 0.9660 | -0.41% |
| Z_W_p | 1.0 | 1.0000 | +0.00% |
| Z_W_c | 1.0 | 1.0000 | +0.00% |
| Z_X_p | 1.0 | 1.0000 | +0.00% |
| Z_B | 1.0 | 1.0000 | +0.00% |
| Z_D | 1.0 | 1.0000 | +0.00% |
| Z_NT_p | 0.91 | 0.9101 | +0.01% |
| Z_NT_c | 0.96 | 0.9618 | +0.18% |
| Y_F_p | 1.56 | 1.5599 | -0.01% |
| Y_F_c | 1.34 | 1.3409 | +0.07% |
| Y_S_p | 1.82 | 1.8232 | +0.18% |
| Y_S_c | 2.07 | 2.0727 | +0.13% |
| Y_B_p | 1.0 | 1.0000 | +0.00% |
| Y_B_c | 1.0 | 1.0000 | +0.00% |
| Y_d_p | 0.99 | 0.9923 | +0.23% |
| Y_d_c | 1.0 | 0.9989 | -0.11% |
| Y_R_p | 0.96 | 0.9639 | +0.40% |
| Y_R_c | 0.96 | 0.9639 | +0.40% |
| Y_X_p | 0.97 | 0.9700 | +0.00% |
| Y_X_c | 0.97 | 0.9700 | +0.00% |
| Y_NT_p | 0.89 | 0.8888 | -0.14% |
| Y_NT_c | 0.92 | 0.9214 | +0.15% |
| S_F_p | 1.86 | 1.8481 | -0.64% |
| S_F_c | 1.98 | 1.9737 | -0.32% |
| S_H_p | 1.03 | 1.0267 | -0.32% |
| S_H_c | 1.09 | 1.0851 | -0.45% |

## Validacao_ISO6336-30_Ex6: app × ISO/TR 6336-30 (valores da norma arredondados a 2 casas)

| Fator | Norma | App | Desvio rel. |
|---|---|---|---|
| Ka | 1.3 | 1.3000 | +0.00% |
| Kv | 1.12 | 1.1231 | +0.27% |
| K_Hbeta | 2.28 | 2.3302 | +2.20% |
| K_Fbeta | 1.92 | 1.9528 | +1.71% |
| K_Halpha | 1.24 | 1.2845 | +3.59% |
| K_Falpha | 1.38 | 1.4274 | +3.43% |
| Z_H | 2.59 | 2.5868 | -0.12% |
| Z_E | 189.81 | 189.8117 | +0.00% |
| Z_epsilon | 0.9 | 0.8823 | -1.96% |
| Z_beta | 1.0 | 1.0000 | +0.00% |
| Z_L | 1.09 | 1.0895 | -0.05% |
| Z_V | 0.95 | 0.9434 | -0.69% |
| Z_R | 0.86 | 0.8632 | +0.37% |
| Z_W_p | 1.0 | 1.0000 | +0.00% |
| Z_W_c | 1.0 | 1.0000 | +0.00% |
| Z_X_p | 1.0 | 1.0000 | +0.00% |
| Z_B | 1.01 | 1.0030 | -0.69% |
| Z_D | 1.0 | 1.0000 | +0.00% |
| Z_NT_p | 0.96 | 0.9561 | -0.41% |
| Z_NT_c | 1.03 | 1.0326 | +0.25% |
| Y_F_p | 1.31 | 1.1840 | -9.61% |
| Y_F_c | 1.18 | 1.1226 | -4.86% |
| Y_S_p | 2.08 | 2.1652 | +4.10% |
| Y_S_c | 3.14 | 3.4537 | +9.99% |
| Y_B_p | 1.0 | 1.0000 | +0.00% |
| Y_B_c | 1.0 | 1.0000 | +0.00% |
| Y_d_p | 0.99 | 0.9900 | +0.00% |
| Y_d_c | 1.05 | 1.1031 | +5.05% |
| Y_R_p | 0.96 | 0.9639 | +0.40% |
| Y_R_c | 0.96 | 0.9639 | +0.40% |
| Y_X_p | 0.96 | 0.9580 | -0.21% |
| Y_X_c | 0.96 | 0.9580 | -0.21% |
| Y_NT_p | 0.92 | 0.9179 | -0.23% |
| Y_NT_c | 0.95 | 0.9533 | +0.34% |
| S_F_p | 6.89 | 6.9272 | +0.54% |
| S_F_c | 5.37 | 4.9514 | -7.80% |
| S_H_p | 1.14 | 1.1253 | -1.29% |
| S_H_c | 1.14 | 1.1158 | -2.12% |

## Checagens físicas / avisos / incoerências (automáticas)

- Validacao_ISO6336-30_Ex1/malha: S_H pinhão = 1.0267 (min 1.0) status=atencao
- Validacao_ISO6336-30_Ex1/malha: S_H coroa = 1.0851 (min 1.0) status=atencao
- Validacao_ISO6336-30_Ex6/malha: AVISO app: AVISO : Recomeda-se o uso de rasqueteamento para baratear o custo de operação da coroa
- Validacao_Mazzo/malha: AVISO app: AVISO : Espessura da cabeça com chanfro inferior (0.562 mm) está menor do que a mínima para o/a coroa (Mínima = 0.6 mm)
- Validacao_Galle/malha: S_H pinhão = 0.8520 (min 1.0) status=ruim
- Validacao_Galle/malha: S_H coroa = 0.8658 (min 1.0) status=ruim
- Validacao_Galle/malha: AVISO app: AVISO : Recomeda-se o uso de rasqueteamento para baratear o custo de operação do pinhão
- Validacao_Galle/malha: AVISO app: AVISO : Recomeda-se o uso de rasqueteamento para baratear o custo de operação da coroa
- Validacao_Galle/malha: AVISO app: AVISO : Coeficiente de segurança sem pites para o pinhão menor que o mínimo (coeficient mínimo = 1.0 ; Coeficiente de segurança calculado = 0.852)
- Validacao_Galle/malha: AVISO app: AVISO : Coeficiente de segurança sem pites para a coroa menor que o mínimo (coeficient mínimo = 1.0 ; Coeficiente de segurança calculado = 0.8658)
- Validacao_Galle/malha: AVISO app: AVISO : Coeficiente de segurança com pites para o pinhão menor que o mínimo (coeficient mínimo = 1.0 ; Coeficiente de segurança calculado = 0.964)
- Validacao_Galle/malha: AVISO app: AVISO : Coeficiente de segurança com pites para a coroa menor que o mínimo (coeficient mínimo = 1.0 ; Coeficiente de segurança calculado = 0.993)
- Planetario_Pla56_antiga/ext: S_H pinhão = 1.0930 (min 1.1) status=ruim
- Planetario_Pla56_antiga/ext: AVISO app: AVISO : Espessura da cabeça sem chanfro nominal (0.251 mm) menor do que a mínima para o/a pinhão (Mínima = 0.275)
- Planetario_Pla56_antiga/ext: AVISO app: AVISO : Espessura da cabeça com chanfro superior (0.2 mm) está menor do que a mínima para o/a pinhão (Mínima = 0.2 mm)
- Planetario_Pla56_antiga/ext: AVISO app: AVISO : Coeficiente de segurança sem pites para o pinhão menor que o mínimo (coeficient mínimo = 1.1 ; Coeficiente de segurança calculado = 1.093)
- Planetario_Pla56_antiga/int: S_H pinhão = 0.9384 (min 1.1) status=ruim
- Planetario_Pla56_antiga/int: S_H coroa = 0.9939 (min 1.1) status=ruim
- Planetario_Pla56_antiga/int: S_F pinhão = 1.2656 (min 1.2) status=atencao
- Planetario_Pla56_antiga/int: S_F coroa = 1.1911 (min 1.2) status=ruim
- Planetario_Pla56_antiga/int: AVISO app: AVISO : A ferramenta da coroa interna não informa o número de dentes do pinhão-cortador (Z_shaper); Y_F e Y_S da anelar foram calculados pela cremalheira equivalente (método 'rack'), não pela geometria do cortador da ISO 6336-3 §6
- Planetario_Pla56_antiga/int: AVISO app: AVISO : Dificuldade alta de alcançar o índice de qualidade da coroa com a operação de acabamento escolhida, recomenda-se utilização de rasquetemento
- Planetario_Pla56_antiga/int: AVISO app: AVISO : Coeficiente de segurança sem pites para o pinhão menor que o mínimo (coeficient mínimo = 1.1 ; Coeficiente de segurança calculado = 0.9384)
- Planetario_Pla56_antiga/int: AVISO app: AVISO : Coeficiente de segurança sem pites para a coroa menor que o mínimo (coeficient mínimo = 1.1 ; Coeficiente de segurança calculado = 0.9939)
- Planetario_Pla56_antiga/int: AVISO app: AVISO : Coeficiente de segurança com pites para o pinhão menor que o mínimo (coeficient mínimo = 1.1 ; Coeficiente de segurança calculado = 1.0992)
- Planetario_Pla56_antiga/int: AVISO app: AVISO : Coeficiente de segurança  de flexão para a coroa menor que o mínimo (coeficient mínimo = 1.2 ; Coeficiente de segurança calculado = 1.1911)
- Planetario_Pla56_antiga: INFO ext: Ft = 1446.67 N; n_rel = 11870.97 rpm; v_t = 9.225 m/s; sum_x = -0.3250; a = 31.166666; d_w/d (pinhao) = 0.9894; eps_a = 1.675; jn7_min = 0.0500
- Planetario_Pla56_antiga: INFO int: Ft = 2543.59 N; n_rel = 3709.68 rpm; v_t = 5.297 m/s; sum_x = 0.0256; a = -31.166666; d_w/d (pinhao) = 0.9989; eps_a = 1.517; jn7_min = 0.0835
- Planetario_Pla56_antiga: INFO equilibrio do planeta com raios de trabalho: Ft_ext*dw_maior/(Ft_int*dw_menor) = 0.9905 (Ft calculado em d; =1 so se d_w=d nas duas malhas)
- Planetario_Pla56_ref/ext: S_H pinhão = 1.1108 (min 1.1) status=atencao
- Planetario_Pla56_ref/int: S_H pinhão = 1.0817 (min 1.1) status=ruim
- Planetario_Pla56_ref/int: S_H coroa = 1.1367 (min 1.1) status=atencao
- Planetario_Pla56_ref/int: S_F pinhão = 1.1425 (min 1.2) status=ruim
- Planetario_Pla56_ref/int: S_F coroa = 1.0855 (min 1.2) status=ruim
- Planetario_Pla56_ref/int: AVISO app: AVISO : A ferramenta da coroa interna não informa o número de dentes do pinhão-cortador (Z_shaper); Y_F e Y_S da anelar foram calculados pela cremalheira equivalente (método 'rack'), não pela geometria do cortador da ISO 6336-3 §6
- Planetario_Pla56_ref/int: AVISO app: AVISO : Dificuldade alta de alcançar o índice de qualidade da coroa com a operação de acabamento escolhida, recomenda-se utilização de rasquetemento
- Planetario_Pla56_ref/int: AVISO app: AVISO : Coeficiente de segurança sem pites para o pinhão menor que o mínimo (coeficient mínimo = 1.1 ; Coeficiente de segurança calculado = 1.0817)
- Planetario_Pla56_ref/int: AVISO app: AVISO : Coeficiente de segurança de flexão para o pinhão menor que o mínimo (coeficient mínimo = 1.2 ; Coeficiente de segurança calculado = 1.1425)
- Planetario_Pla56_ref/int: AVISO app: AVISO : Coeficiente de segurança  de flexão para a coroa menor que o mínimo (coeficient mínimo = 1.2 ; Coeficiente de segurança calculado = 1.0855)
- Planetario_Pla56_ref: INFO ext: Ft = 1446.67 N; n_rel = 11870.97 rpm; v_t = 9.225 m/s; sum_x = -0.3250; a = 31.166666; d_w/d (pinhao) = 0.9894; eps_a = 1.455; jn7_min = 0.0500
- Planetario_Pla56_ref: INFO int: Ft = 2543.59 N; n_rel = 3709.68 rpm; v_t = 5.297 m/s; sum_x = 0.0256; a = -31.166666; d_w/d (pinhao) = 0.9989; eps_a = 1.507; jn7_min = 0.0833
- Planetario_Pla56_ref: INFO equilibrio do planeta com raios de trabalho: Ft_ext*dw_maior/(Ft_int*dw_menor) = 0.9905 (Ft calculado em d; =1 so se d_w=d nas duas malhas)
- Planetario_Pla41_antiga/ext: S_H pinhão = 1.1007 (min 1.1) status=atencao
- Planetario_Pla41_antiga/int: S_H pinhão = 0.9862 (min 1.1) status=ruim
- Planetario_Pla41_antiga/int: S_H coroa = 1.1506 (min 1.1) status=atencao
- Planetario_Pla41_antiga/int: AVISO app: AVISO : A ferramenta da coroa interna não informa o número de dentes do pinhão-cortador (Z_shaper); Y_F e Y_S da anelar foram calculados pela cremalheira equivalente (método 'rack'), não pela geometria do cortador da ISO 6336-3 §6
- Planetario_Pla41_antiga/int: AVISO app: AVISO : Dificuldade alta de alcançar o índice de qualidade da coroa com a operação de acabamento escolhida, recomenda-se utilização de rasquetemento
- Planetario_Pla41_antiga/int: AVISO app: AVISO : Coeficiente de segurança sem pites para o pinhão menor que o mínimo (coeficient mínimo = 1.1 ; Coeficiente de segurança calculado = 0.9862)
- Planetario_Pla41_antiga: INFO ext: Ft = 1446.67 N; n_rel = 11880.33 rpm; v_t = 9.232 m/s; sum_x = -0.3250; a = 31.166666; d_w/d (pinhao) = 0.9894; eps_a = 1.463; jn7_min = 0.0499
- Planetario_Pla41_antiga: INFO int: Ft = 2610.53 N; n_rel = 3712.60 rpm; v_t = 5.232 m/s; sum_x = -0.2689; a = -31.166666; d_w/d (pinhao) = 1.0119; eps_a = 1.514; jn7_min = 0.0829
- Planetario_Pla41_antiga: INFO equilibrio do planeta com raios de trabalho: Ft_ext*dw_maior/(Ft_int*dw_menor) = 0.9778 (Ft calculado em d; =1 so se d_w=d nas duas malhas)
- Planetario_Pla41_ref/ext: S_H pinhão = 1.1100 (min 1.1) status=atencao
- Planetario_Pla41_ref/int: S_H pinhão = 0.9848 (min 1.1) status=ruim
- Planetario_Pla41_ref/int: S_H coroa = 1.1675 (min 1.1) status=atencao
- Planetario_Pla41_ref/int: S_F pinhão = 1.1803 (min 1.2) status=ruim
- Planetario_Pla41_ref/int: S_F coroa = 1.2134 (min 1.2) status=atencao
- Planetario_Pla41_ref/int: AVISO app: AVISO : A ferramenta da coroa interna não informa o número de dentes do pinhão-cortador (Z_shaper); Y_F e Y_S da anelar foram calculados pela cremalheira equivalente (método 'rack'), não pela geometria do cortador da ISO 6336-3 §6
- Planetario_Pla41_ref/int: AVISO app: AVISO : Dificuldade alta de alcançar o índice de qualidade da coroa com a operação de acabamento escolhida, recomenda-se utilização de rasquetemento
- Planetario_Pla41_ref/int: AVISO app: AVISO : Coeficiente de segurança sem pites para o pinhão menor que o mínimo (coeficient mínimo = 1.1 ; Coeficiente de segurança calculado = 0.9848)
- Planetario_Pla41_ref/int: AVISO app: AVISO : Coeficiente de segurança de flexão para o pinhão menor que o mínimo (coeficient mínimo = 1.2 ; Coeficiente de segurança calculado = 1.1803)
- Planetario_Pla41_ref: INFO ext: Ft = 1446.67 N; n_rel = 11880.33 rpm; v_t = 9.232 m/s; sum_x = -0.3250; a = 31.166666; d_w/d (pinhao) = 0.9894; eps_a = 1.463; jn7_min = 0.0500
- Planetario_Pla41_ref: INFO int: Ft = 2610.53 N; n_rel = 3712.60 rpm; v_t = 5.232 m/s; sum_x = -0.2689; a = -31.166666; d_w/d (pinhao) = 1.0119; eps_a = 1.530; jn7_min = 0.0830
- Planetario_Pla41_ref: INFO equilibrio do planeta com raios de trabalho: Ft_ext*dw_maior/(Ft_int*dw_menor) = 0.9778 (Ft calculado em d; =1 so se d_w=d nas duas malhas)
- Planetario_Pla50_antiga/ext: S_H pinhão = 1.0902 (min 1.1) status=ruim
- Planetario_Pla50_antiga/ext: AVISO app: AVISO : Coeficiente de segurança sem pites para o pinhão menor que o mínimo (coeficient mínimo = 1.1 ; Coeficiente de segurança calculado = 1.0902)
- Planetario_Pla50_antiga/int: S_H pinhão = 0.9743 (min 1.1) status=ruim
- Planetario_Pla50_antiga/int: S_H coroa = 0.9967 (min 1.1) status=ruim
- Planetario_Pla50_antiga/int: S_F pinhão = 1.1716 (min 1.2) status=ruim
- Planetario_Pla50_antiga/int: S_F coroa = 1.1204 (min 1.2) status=ruim
- Planetario_Pla50_antiga/int: AVISO app: AVISO : A ferramenta da coroa interna não informa o número de dentes do pinhão-cortador (Z_shaper); Y_F e Y_S da anelar foram calculados pela cremalheira equivalente (método 'rack'), não pela geometria do cortador da ISO 6336-3 §6
- Planetario_Pla50_antiga/int: AVISO app: AVISO : Dificuldade alta de alcançar o índice de qualidade da coroa com a operação de acabamento escolhida, recomenda-se utilização de rasquetemento
- Planetario_Pla50_antiga/int: AVISO app: AVISO : Coeficiente de segurança sem pites para o pinhão menor que o mínimo (coeficient mínimo = 1.1 ; Coeficiente de segurança calculado = 0.9743)
- Planetario_Pla50_antiga/int: AVISO app: AVISO : Coeficiente de segurança sem pites para a coroa menor que o mínimo (coeficient mínimo = 1.1 ; Coeficiente de segurança calculado = 0.9967)
- Planetario_Pla50_antiga/int: AVISO app: AVISO : Coeficiente de segurança de flexão para o pinhão menor que o mínimo (coeficient mínimo = 1.2 ; Coeficiente de segurança calculado = 1.1716)
- Planetario_Pla50_antiga/int: AVISO app: AVISO : Coeficiente de segurança  de flexão para a coroa menor que o mínimo (coeficient mínimo = 1.2 ; Coeficiente de segurança calculado = 1.1204)
- Planetario_Pla50_antiga: INFO ext: Ft = 1506.94 N; n_rel = 11887.79 rpm; v_t = 9.060 m/s; sum_x = 0.4331; a = 31.133333; d_w/d (pinhao) = 1.0108; eps_a = 1.494; jn7_min = 0.0559
- Planetario_Pla50_antiga: INFO int: Ft = 2577.09 N; n_rel = 3626.78 rpm; v_t = 5.230 m/s; sum_x = 0.0553; a = -31.133333; d_w/d (pinhao) = 0.9979; eps_a = 1.499; jn7_min = 0.0834
- Planetario_Pla50_antiga: INFO equilibrio do planeta com raios de trabalho: Ft_ext*dw_maior/(Ft_int*dw_menor) = 1.0130 (Ft calculado em d; =1 so se d_w=d nas duas malhas)
- Planetario_Pla50_ref/ext: S_H pinhão = 1.0988 (min 1.1) status=ruim
- Planetario_Pla50_ref/ext: AVISO app: AVISO : Coeficiente de segurança sem pites para o pinhão menor que o mínimo (coeficient mínimo = 1.1 ; Coeficiente de segurança calculado = 1.0988)
- Planetario_Pla50_ref/int: S_H pinhão = 1.0007 (min 1.1) status=ruim
- Planetario_Pla50_ref/int: S_H coroa = 1.1231 (min 1.1) status=atencao
- Planetario_Pla50_ref/int: S_F pinhão = 1.0063 (min 1.2) status=ruim
- Planetario_Pla50_ref/int: S_F coroa = 0.8619 (min 1.2) status=ruim
- Planetario_Pla50_ref/int: AVISO app: AVISO : A ferramenta da coroa interna não informa o número de dentes do pinhão-cortador (Z_shaper); Y_F e Y_S da anelar foram calculados pela cremalheira equivalente (método 'rack'), não pela geometria do cortador da ISO 6336-3 §6
- Planetario_Pla50_ref/int: AVISO app: AVISO : Dificuldade alta de alcançar o índice de qualidade da coroa com a operação de acabamento escolhida, recomenda-se utilização de rasquetemento
- Planetario_Pla50_ref/int: AVISO app: AVISO : Coeficiente de segurança sem pites para o pinhão menor que o mínimo (coeficient mínimo = 1.1 ; Coeficiente de segurança calculado = 1.0007)
- Planetario_Pla50_ref/int: AVISO app: AVISO : Coeficiente de segurança de flexão para o pinhão menor que o mínimo (coeficient mínimo = 1.2 ; Coeficiente de segurança calculado = 1.0063)
- Planetario_Pla50_ref/int: AVISO app: AVISO : Coeficiente de segurança  de flexão para a coroa menor que o mínimo (coeficient mínimo = 1.2 ; Coeficiente de segurança calculado = 0.8619)
- Planetario_Pla50_ref: INFO ext: Ft = 1506.94 N; n_rel = 11887.79 rpm; v_t = 9.060 m/s; sum_x = 0.4331; a = 31.133333; d_w/d (pinhao) = 1.0108; eps_a = 1.494; jn7_min = 0.0560
- Planetario_Pla50_ref: INFO int: Ft = 2577.09 N; n_rel = 3626.78 rpm; v_t = 5.230 m/s; sum_x = 0.0553; a = -31.133333; d_w/d (pinhao) = 0.9979; eps_a = 1.615; jn7_min = 0.0834
- Planetario_Pla50_ref: INFO equilibrio do planeta com raios de trabalho: Ft_ext*dw_maior/(Ft_int*dw_menor) = 1.0130 (Ft calculado em d; =1 so se d_w=d nas duas malhas)

## Arquivos .fem: releitura com `fem.ler` e recálculo

| Arquivo | Nº de cartões de segurança | Maior |ΔS| após reler | Nome no arquivo | ok |
|---|---|---|---|---|
| Validacao_ISO6336-30_Ex1.fem | 4 | 0.000e+00 | Validação ISO 6336-30 Ex. 1 (par externo, z=17/103, m_n=8) | True |
| Validacao_ISO6336-30_Ex6.fem | 4 | 0.000e+00 | Validação ISO 6336-30 Ex. 6 (par interno, z=15/-99, m_n=12, K_A imposto 1,3) | True |
| Validacao_Mazzo.fem | 4 | 0.000e+00 | Validação Mazzo (par helicoidal externo z=25/61, m_n=3) | True |
| Validacao_Galle.fem | 4 | 0.000e+00 | Validação Galle (par helicoidal z=15/25, m_n=3, 20MnCr5) | True |
| Planetario_Pla56_antiga.fem | 8 | 0.000e+00 | Planetário composto 56 (25/25/10/13), material da planetária antiga | True |
| Planetario_Pla56_ref.fem | 8 | 0.000e+00 | Planetário composto 56 (25/25/10/13), material de referência | True |
| Planetario_Pla41_antiga.fem | 8 | 0.000e+00 | Planetário composto 41 (25/25/10/14), material da planetária antiga | True |
| Planetario_Pla41_ref.fem | 8 | 0.000e+00 | Planetário composto 41 (25/25/10/14), material de referência | True |
| Planetario_Pla50_antiga.fem | 8 | 0.000e+00 | Planetário composto 50 (20/25/08/12), material da planetária antiga | True |
| Planetario_Pla50_ref.fem | 8 | 0.000e+00 | Planetário composto 50 (20/25/08/12), material de referência | True |
