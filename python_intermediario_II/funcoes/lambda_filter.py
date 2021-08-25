valores = [10, 20, 30, 40, 50, 60, 70, 80]

def remover20(x):
    return x > 20

print(list(map(remover20, valores))) #   retorna uma lista booleana de acordo com o retorno da função

# usando o filter para trazer somente os valores desejados

print(list(filter(remover20, valores)))

# utilizando o filter com lambda 

print(list(filter(lambda x: x > 20, valores)))