nome, idade = 'Ana', 30

# Vamos usar o %s e o %d
# O %s para substituição de um valor string
# O %d para substituição de valores inteiros
# O %f para substituição de valores float
#       - para trazer menos casas use %.2f
# O %r para boolean
print("Nome: %s, Idade: %d" % (nome, idade))


# Format

print("Nome: {0}, Idade: {1}".format(nome, idade))

# Nova forma... Só funciona a partir do 3.6

print(f'Nome: {nome}, Idade: {idade} {2 ** 8 + 1}')
