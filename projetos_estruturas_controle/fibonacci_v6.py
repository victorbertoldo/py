#!python

# Na sequencia de Fibonacci, o próximo numero é o resultado
# entre a soma do numero atual com o anterior.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

# Vamos usar agora a quantidade de numeros
# q queremos mostrar, além de usar o while True + break
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    # listar os 20 primeiros numeros da sequencia
    for fib in fibonacci(20):
        print(fib)
