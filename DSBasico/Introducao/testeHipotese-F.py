# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 08:18:45 2020

@author: victor.bertoldo
"""

import pandas as pd
import scipy.stats as stats

pasta_dados = "D:/github/py/DSBasico/Dados/"
arquivo = pasta_dados + "mamalia_sleep.csv"

df_mamiferos = pd.read_csv(arquivo)
df_mamiferos.columns

df_mamiferos = df_mamiferos.query("vore in ('carni', 'herbi', 'omni')")

"""
Teste 1: Testar se a variancia dentro dos grupos é diferente da variancia 
fora dos grupos.

Uma das formas de se fazer o F-test (ANOVA):
"""    

df_anova = df_mamiferos[["sleep_total",'vore']]

df_anova.boxplot('sleep_total', by='vore', figsize=(12, 6))

dietas = pd.unique(df_anova.vore.values)

f1_df = {dt:df_anova['sleep_total'][df_anova.vore == dt] for dt in dietas}
f1_df

F, p = stats.f_oneway(f1_df['carni'], f1_df['herbi'], f1_df['omni'])

if p < 0.05:
    print('Rejeitar H0')
else:
    print('Falhar em Rejeitar H0')    
    
"""
Como o teste falhou em rejeitar a H0, significa que a variancia dos grupos
é estatisticamente semelhante à variancia fora dos grupos

"""    
'''
 Outro tipo de teste F: Two way F-test
 No entanto temos que usar 2 variaveis dependentes
 '''
 
# Aqui vamos primeiramente usar um modelo para prever valores 
 
import statsmodels.api as fm
from statsmodels.formula.api import ols

modelo = ols('sleep_total ~ vore * order', df_mamiferos).fit()

modelo

# Para acesssar as propriedades  do modelo vamos usar seus parametros

print('df=%.0f,=, p=%.12f, res=%.0f, f-value=%.3f' % (modelo.df_model, modelo.f_pvalue, modelo.df_resid, modelo.fvalue))

if modelo.f_pvalue < 0.05:
    print('Rejeitar H0')
else:
    print('Não rejeitar H0') 
    
"""
Ao rejeitar a hipotese nula, identificamos que há sim uma diferença de sono 
quando consideramos a dieta junto a ordem que ele pertence
"""    

prob = 0.95 # nivel de confiança
n = df_mamiferos.sleep_total.count()
a_vore = 3
a_order = len(df_mamiferos.order.unique().tolist())

"""
NUm test-F é necessário usar o valor de a, que será utilizado para calcular
os graus de liberdade
"""
a = (a_vore -1) * (a_order -1)

"""
O 'a' é o numero total de grupos 
dfn é o numero total de linhas e tbm é o primeiro grau de liberdade

"""

dfn = a - 1

dfd = n - a

valor_critico = stats.f.ppf(prob, dfn, dfd)

if modelo.fvalue > valor_critico:
    print('Rejeitar H0')
else:
    print('Não rejeitar H0')    
    
"""
Ou seja, como a H0 foi rejeitada então há sim uma diferença 
nas horas de sono de mamiferos, se levarmos em consideração dieta e order
dos mamiferos
"""    