# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 08:56:36 2020

@author: victor.bertoldo
"""

import pandas as pd
dir = 'D:/github/py/DSBasico/Dados/'
arq = 'mamalia_sleep.csv'
dados = pd.read_csv(dir + arq)

media_pop = dados['sleep_total'].mean()
devpd_pop = dados['sleep_total'].std()

dados['sleep_total'].describe()


""" 
Apesar da media e a mediana serem valores relativamente
proximos, podemos notar que há uma variação bem grande na população
ao olhar o valor minimo e valor máximo.

hipotese: O que influencia nesta variação? Será que é a ordem dos mamiferos?
"""
sono_ordem  = dados.groupby('order')['sleep_total'].mean()
sono_ordem.sort_values()

# Vamos comparar as horas de sono de roedores com o resto da população
# O Objetivo é analisar se a diferença é realmente significativa

# Rodentia

is_roedores = dados['order']=='Rodentia'
roedores = dados[is_roedores]
sono_roedores = roedores['sleep_total']

# Score Z
z = (sono_roedores.mean() - media_pop) / devpd_pop
z

"""
Ok, o valor de z ou o Z-Score dos roedores é proximo de 0,5, mas o que isso 
quer dizer?

Isso quer dizer que os roedores estão em média há 0.5 desvios padrões da 
média populacional de todos os mamiferos.
"""

""" 
Vamos verificar a significancia desta informação.

Mas qual é a probabilidade desse valor acontecer ao acaso?

Se ela for muito pequena, quer dizer que não foi o acaso q gerou essa
diferença e sim um fator especifico, dando a entender q realmente 
há uma diferença significativa entre roedores e o resto dos mamiferos.

Então quase sempre estaremos em busca desta probabilidade pequena,
para que possamos descartar a hipótese nula e trabalhar com a hipotese
alternativa
"""

"""

Mas qual é a probabilidade de acontecer um valor de Z de 0.45?

"""

from scipy import stats

(1 - stats.norm.cdf(z)) * 100

"""
Isso quer dizer que a probabilidade de um mamifero durma mais horas do 
que a média dos zoedores é de 32.37 %, o que é uma probabilidade alta.
Sendo assim, não foi possivel rejeitar nossa hipotese nula. Então não há
uma diferença significativa.
"""


"""
Vamos ver agora dentro de um dataframe cada valor individual, qntos 
desvios padrões esses valores individuais está à média de cada valor.

"""

stats.zscore(sono_roedores)

"""
Esta função retorna um array com a qtd de desvios padrões q cada item
tem de distancia da média. E isso nos mostra q os itens variam mais ou
menos da mesma forma.

"""
