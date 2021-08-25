lista1 = list('1234')
print(lista1)

def multi(x):
    return x * 2

multi(lista1)    

# não faz a soma para cada item da lista, para isso teriamos que criar uma iteração com loop para somar à cada item da lista e substituir o valor de referencia na lista.

# para isso utilizaremos a função map em uma lambda, pois desta forma os valores novos serão iterados dentro da lista
lista_map_1 = map(lambda x: x * 2, lista1)
print(list(lista_map_1))

lista2 = [1, 2, 3, 4, 5]

lista_map_2 = map(lambda x: x * 2, lista2)
print(list(lista_map_2))

lista3 = ['João.SIlva', 'Victor.Bertoldo', 'Maria.Diniz']

lista_map_3 = map(lambda x: x.split('.'), lista3)
print(list(lista_map_3))