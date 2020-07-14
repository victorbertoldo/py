def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c

# este carácter "*" gera uma tupla como resultado
# conhecido como * args


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    tupla_nums = (3, 4, 9)
    print(soma_3(*tupla_nums))

    lista_nums = [5, 3, 5, 8, 9, 15]
    print(soma_n(*lista_nums))
