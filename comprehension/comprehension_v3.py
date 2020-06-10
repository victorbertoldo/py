# Generator - o generator vai gerando os dados confforme demanda
# diferente do list comprehension que já gera todos os dados
# da lista de uma vez só.
# Usa () e não []

import sys
generator = (i ** 2 for i in range(10) if i % 2 == 0)
# A forma de acessar os valores é usando o next

print(next(generator))  # saida 0
print(next(generator))  # saida 4
print(next(generator))  # saida 16
print(next(generator))  # saida 36
print(next(generator))  # saida 64
# print(next(generator))  # erro! Por não haver mais valores


a = [i * 2 for i in range(1000) if i % 2 == 0]
b = (i * 2 for i in range(1000) if i % 2 == 0)

print('a:', sys.getsizeof(a))
print('b:', sys.getsizeof(b))

# Generator usa menos memória por sua caracteristica
# de ser sobdemanda
