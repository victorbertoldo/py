letras = ['a', 'b', 'c', 'd', 'e', 'f']
try:
    print(letras[10])
except IndexError:
    print('Index não existe.')