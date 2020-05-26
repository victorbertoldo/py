import pandas as pd
import numpy as np
b = [1, 2, 3]

a = 'fdsa'

c = 3


salario = 3450.45
despesas = 2456.20

perc = (despesas / salario) * 100

print("{}% do salario está comprometido.".format(perc))
print("\n")


lista = []
for i in range(0, 16):
    a = np.random.randint(1, 26)
    lista.append(a)
    
lista = pd.Series(lista)
lista = lista.drop_duplicates()
lista = lista.sort_values()
print(lista.values)
