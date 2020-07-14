# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:20:24 2020

@author: victor.bertoldo
"""

import pandas as pd
import numpy  as np

df_luas_jp_1 = pd.DataFrame([{'Nome': 'Ganimedes',   'Massa': 15000000,  'Eixo Semi-Maior': 1070412},
                             {'Nome': 'Calisto',     'Massa': 11000000,  'Eixo Semi-Maior': 1882709},
                             {'Nome': 'Io',          'Massa': 8900000,   'Eixo Semi-Maior': 421700},
                             {'Nome': 'Europa',      'Massa': 4800000,   'Eixo Semi-Maior': 671034}],
                             index=['III', 'IV', 'I', 'II'])
                             
print(df_luas_jp_1)                             

# add a column
df_luas_jp_1['Descobridor'] = 'Galileu'

df_luas_jp_1

df_luas_jp_2 = pd.DataFrame([{'Nome': 'Ganimedes',   'Ordem': 7,  'Inclinacao': 0.204},
                             {'Nome': 'Calisto',     'Ordem': 8,  'Inclinacao': 0.205},
                             {'Nome': 'Io',          'Ordem': 5,  'Inclinacao': 0.050},
                             {'Nome': 'Europa',      'Ordem': 6,  'Inclinacao': 0.471}])
                             
print(df_luas_jp_2) 

df_luas_jp = pd.merge(df_luas_jp_1, df_luas_jp_2, how="left", left_on='Nome', right_on='Nome')
df_luas_jp

df_luas_jp = df_luas_jp.set_index(np.array(['III', 'IV', 'I', 'II']))
df_luas_jp

