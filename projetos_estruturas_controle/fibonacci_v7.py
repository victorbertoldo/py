#!python

# Na sequencia de Fibonacci, o próximo numero é o resultado
# entre a soma do numero atual com o anterior.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

# Mudando para o for. No for usaremos o "_",
# pois é uma convenção de variavel que não é usada
def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade):  # nº 2 pq já temos 2 numeros na lista
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    # listar os 20 primeiros numeros da sequencia
    for fib in fibonacci(20):
        print(fib)
