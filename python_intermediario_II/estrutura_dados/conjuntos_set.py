# Conjuntos ou Sets, são similares à listas, entretanto eles somente armazenam valores unicos
# evitando os duplicados e não possui index.
lista1 = [1,2,3,4,5]
lista2 = [1,2,6,8,9]

num1 = set(lista1)
num2 = set(lista2)

print(num1 | num2) # Union
print(num1 - num2) # Difference
print(num1 ^ num2) # Simetric Difference
print(num1 & num2) # And