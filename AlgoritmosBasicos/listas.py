lista = []
print(type(lista))
print(dir(lista))
print(len(lista))

for i in range(1, 6):
    lista.append(i)
print(lista)

print(len(lista))

lista.append('Ana')
lista.append('Leo')
lista.append(True)

print(lista)

nova_lista = lista

nova_lista.remove(nova_lista[-1])
nova_lista.reverse()

print(nova_lista)
# Em uma lista é possivel armazenar vários tippos de dados

outra_lista = [1, 5, 'Pedro', 'Danielle', 3.1415]
print(outra_lista.index('Pedro'))
print(outra_lista[2])
print('Pedro' in outra_lista)

lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dany']
print(lista[2:4])
