# Tuplas não podem ser modificadas

tupla = tuple()
tupla = ()
print(type(tupla))
print(dir(tupla))
# print(help(tupla))
tupla = (1,)
print(type(tupla))

cores = ('azul', 'verde', 'branco', 'preto', 'azul')
print(cores.index('verde'))
print(cores.count('azul'))
