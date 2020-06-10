# Generator - o generator vai gerando os dados confforme demanda
# diferente do list comprehension que já gera todos os dados
# da lista de uma vez só.
# Usa () e não []

generator = (i ** 2 for i in range(10) if i % 2 == 0)
# outra forma de acessar o generator é com um for
for numero in generator:
    print(numero)
