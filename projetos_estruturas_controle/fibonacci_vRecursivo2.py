#!python

# Na sequencia de Fibonacci, o próximo numero é o resultado
# entre a soma do numero atual com o anterior.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

# Aqui usaremos recursividade para mostrar a sequencia fibonacci
def fibonacci(quantidade, sequencia=(0, 1)):
    # Importante! Condição de parada.
    
    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))
    # essa soma entre tuplas é uma sobrecarga de operadores

if __name__ == '__main__':
    # Listar os 20 primeiros numeros da sequencia
    for fib in fibonacci(20):
        print(fib)