# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:33:05 2020

@author: victor.bertoldo
"""

import numpy as np

lista_a =  [1, 2, 3]
array_a = np.array(lista_a)
print(array_a)

array_b = np.array([4, 5, 6, 7])
print(array_b)

array_c = np.array([[1, 3, 5, 7], [2, 4, 6, 8]])
print(array_c)

print(array_c.shape)

array_c = array_c.reshape(4, 2)
print(array_c)
print(array_c.shape)

array_d = np.arange(36)
print(array_d)

array_d.resize(6,6)
print(array_d)

print(array_d[2, 2])
print(array_d[3, 3:6])
print(array_d[array_d >= 30])
array_d[array_d >= 30] = 30
print(array_d)

print(array_d == 30)