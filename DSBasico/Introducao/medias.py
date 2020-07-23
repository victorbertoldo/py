# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:32:11 2020

@author: victor.bertoldo
"""
import numpy as np
#import pandas as pd
from EstatisticaDescritiva import df_mamiferos

df_mamiferos.head()

sono = df_mamiferos['sleep_total']


# média aritmética

ma = sono.mean()
ma

# média ponderada

peso = df_mamiferos['bodywt']
peso = np.ceil(peso)

mp = (sono * peso).sum() / peso.sum()
mp

# média aritmética
from  scipy.stats.mstats import gmean

mg = gmean(sono)
mg

# é importante notar que a média geométrica tende a ser sempre menor que a média aritimética

# média harmonica

from scipy.stats.mstats import hmean

mh = hmean(sono)
mh

# é importante notar que a média harmonica tende a ser sempre menor que a média geométrica
# média harmonica é a menor delas e a aritmetica é a maior
# na média harmonica não pode haver numero zero, pois não pode haver divisão por zero


# outra forma de calcular a media harmonica usando outra biblioteca

import statistics as sss

sss.harmonic_mean(sono)