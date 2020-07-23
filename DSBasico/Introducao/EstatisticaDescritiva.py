# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:17:40 2020

@author: victor.bertoldo
"""

import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt

pasta_dados = "D:/github/py/DSBasico/Dados/"
arquivo = pasta_dados + "mamalia_sleep.csv"

df_mamiferos = pd.read_csv(arquivo)

df_mamiferos.head()

df_mamiferos.describe()

sono = df_mamiferos['sleep_total']
sono.describe()

# acessando os indicadores do describe individualmente

sono.count()
sono.mean()
sono.median()
sono.mode()
sono.min()
sono.max()

# a função quantile (pandas) usa sempre a distancia linear para calcular os quantis
sono.quantile(0.25)
sono.quantile(0.5)
sono.quantile(0.75)

sono2 = df_mamiferos[df_mamiferos['name'] != 'Horse']['sleep_total']

sono2.quantile(.75)

# a função percentile
np.percentile(sono2, 75, interpolation='midpoint') # 13.75

np.percentile(sono2, 75, interpolation='lower') # 13,7


np.percentile(sono2, 75, interpolation='higher') # 13.8


np.percentile(sono2, 75, interpolation='nearest') # 13.8


np.percentile(sono2, 75, interpolation='linear') # msm valor do quantile

# medidas de dispersao

# variancia
sono.var()
# Desvio padrão
sono.std()

sono.plot(kind='hist', bins=15) # bins limite de linhas
plt.xlabel('Horas de sono diárias')

sono.plot(kind='box')

sono_ordem = df_mamiferos.groupby('order')['sleep_total'].mean()

sono_ordem.plot(kind='bar')

# Top 7 q mais dormem

sono_ordem.sort_values()[-7:].plot(kind='bar')
plt.ylabel('Média de horas de sono')

lista = pd.DataFrame([5, 12, 7, 22, 64, 15, 13, 41, 42, 27])
lista.median()
lista.describe()
np.percentile(lista, 95, interpolation='linear')
 
