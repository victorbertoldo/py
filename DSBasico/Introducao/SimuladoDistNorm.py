# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:15:03 2020

@author: victor.bertoldo
"""


import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
from scipy import stats

pasta_dados = "D:/github/py/DSBasico/Dados/"
arquivo = pasta_dados + "cereals.csv"

dados = pd.read_csv(arquivo)

sodium = dados['sodium']
sodium.quantile(0.85)

calories = dados['calories']

medcal = calories.mean()
stdcal = calories.std()
mincal = calories.min()
maxcal = calories.max()
n = calories.count()

x = np.linspace(mincal, maxcal, n)
distr_cal = stats.norm(medcal, stdcal)

y = distr_cal.pdf(x)

plt.plot(x, y) 


rating = dados['rating']

amp = rating.max() - rating.min()
amp.round()

fiber = dados ['fiber']
fiber.mode()

dados.skew(axis=0, skipna=True)
dados.kurtosis(axis=0, skipna=True)

calories.var().round()

dados.std()