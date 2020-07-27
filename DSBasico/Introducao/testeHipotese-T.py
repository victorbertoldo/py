# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 09:26:56 2020

@author: victor.bertoldo
"""

import pandas as pd
from scipy import stats
from scipy.stats import t
from scipy.stats import ttest_ind


dir = 'D:/github/py/DSBasico/Dados/'
arq = 'salarios.csv'
dados = pd.read_csv(dir + arq)

dados['INCOME'].describe()

"""
Hipótese:
Como mostrado no describe, apenas 25% da amostra ganha um valor
acima de 46 mil, que variavel influencia nesta questão?

Vamos analisar pela perspectiva de raça. Será que uma pessoa branca
ganha mais que uma pessoa não branca?♠
"""

is_branco = dados['RACE']=='White'
brancos = dados[is_branco]
salario_brancos = brancos['INCOME']
salario_brancos.describe()

not_branco = dados['RACE']!= 'White'
naobrancos = dados[not_branco]
salario_nao_brancos = naobrancos['INCOME']
salario_nao_brancos.describe()

"""
Apesar da média de pessoas não brancas ser menor que a média de brancos
não podemos afirmar com certeza que há uma grande diferença, pois a amostra
de pessoas não brancas não é significativa em relação ao todo.

Por isso vamos executar o teste T

"""

t_stat , p_value = ttest_ind(salario_brancos, salario_nao_brancos)
print('t=%.3f, p=%.9f' % (t_stat, p_value))

"""
Há 2 formas de verificar esse tipo de teste:
    1.Se é possivel rejeitar a hipotese nula
    2. Ou se não é possivel rejeitar a hipotese nula

Para isso é necessário calcular o valor crítico.
O valor crítico será comparado ao valor de t. 
Se o valor de t for maior que o valor de crítico,
significa que a diferença é estatisticamente significativa.
Então se quisermos rejeitar a hipotese nula o t deve ser maior que 
o valor crítico.

"""
n1, n2 = len(salario_brancos), len(salario_nao_brancos)

# Graus de liberdade
g1 = n1 + n2  - 2    # 2 pq são 2 amostras

alpha = 0.05 # nível de confiança é 95 %
valor_critico = t.ppf(1.0 - alpha, g1)
valor_critico

if abs(t_stat) <= valor_critico:
    print('Aceita-se a hipótese nula. Não há diferença de salarios.')
else:
    print('Rejeita-se a hipotese nula. Há uma diferença significativa.')
    
"""
Pode-se fazer o testa tbm usando o valor de P, porém sem comparar ao
valor crítico e sim com o alpha.
Considera-se por convenção que se o valor p for menor q 5%, ele é tão 
pequeno que de fato há uma diferença significativa.
Ou seja, que a probabilidade do fato ou evento ocorrer ao acaso é
muito pequena.

"""

if p_value > alpha:
    print('Aceita-se a hipótese nula. Não há diferença de salarios.')
else:
    print('Rejeita-se a hipotese nula. Há uma diferença significativa.')    