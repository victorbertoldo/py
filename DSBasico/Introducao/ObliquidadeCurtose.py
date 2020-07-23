# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:37:13 2020

@author: victor.bertoldo
"""

import pandas as pd
from EstatisticaDescritiva import df_mamiferos

sono = df_mamiferos['sleep_total']

# se for uma tabela normal o axis=0, se for pivot axis=1
# skina=True ignora valores nulos
df_mamiferos.skew(axis=0, skipna=True) 

df_mamiferos.kurtosis(axis=0, skipna=True)


sono.skew(axis=0, skipna=True)

sono.describe()








pd.io.clipboards.to_clipboard(1, excel=False)
