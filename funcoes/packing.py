def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c

# este carácter "*" gera uma tupla como resultado
# conhecido como * args


def soma_n(*numeros):
    print(type(numeros))
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(5, 6))
    print(soma_3(5, 7, 2))
    print(soma_n(5, 3, 5, 8, 9, 15))
