# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:43:13 2020

@author: victor.bertoldo
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

from EstatisticaDescritiva import df_mamiferos

sono = df_mamiferos['sleep_total']

media = sono.mean()
devpd = sono.std()
min = sono.min()
max = sono.max()
n = sono.count()


# aqui assumiremos q a distribuição dos dados é normal
# usaremos uma funcão para gerar os valores teoricos
# baseados na média e no desviopadrão
distr_sono = stats.norm(media, devpd)

x = np.linspace(min, max, n)

# gerar valores de probalidade
y = distr_sono.pdf(x)

# calculando os valores probabilistics  "PDF"
# onde os valores estão concentrados próximos a média
plt.plot(x, y)

# "CDF" onde a probabilidade é acumulada
# onde a probabilidade cresce do decorrer do tempo


# Calcular valores de probabilidade

y = distr_sono.cdf(x)

plt.plot(x, y)