# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:23:11 2020

@author: victor.bertoldo
"""

import pandas as pd
import scipy.stats 
from scipy.stats import chi2
from scipy.stats import chi2_contingency


dir = 'D:/github/py/DSBasico/Dados/'
arq = 'titanic.csv'
dados = pd.read_csv(dir + arq)

dados.columns

"""
Quais foram os fatores que influenciaram na sobrevivencia das pessoas?
Será q o sexo influenciou?
"""
df_surv_sex = dados[['Sex', 'Survived']]

scipy.stats.chisquare(df_surv_sex['Sex'].value_counts())
scipy.stats.chisquare(df_surv_sex['Survived'].value_counts())

freq_table = pd.crosstab(df_surv_sex['Sex'], df_surv_sex['Survived'])
freq_table

"""
Ou seja, grande parte das mulheres sobreviveu ao acidente
e a maior parte dos homenes morreram.

Mas o quão significativa é essa diferença?

"""

chi2stat, p, dof, freq_exp= chi2_contingency(freq_table)

# dof é dregrees of freedom e freq_exp é frequecy expected

# dof = (linhas -1) * (colunas - 1)

prob = 0.95 # nivel de confiança

valor_critico = chi2.ppf(prob, dof)


if abs(chi2stat) >= valor_critico:
    print("Sexo influenciou na sobrevivencia. Rejeitar H0")
else:
    print('Sexo não influenciou na sobrevivencia. Não rejeitar H0')    
    
alpha = 1.0 - prob

if p < alpha:
    print("Sexo influenciou na sobrevivencia. Rejeitar H0")
else:
    print('Sexo não influenciou na sobrevivencia. Não rejeitar H0')        