#!python

# Na sequencia de Fibonacci, o próximo numero é o resultado
# entre a soma do numero atual com o anterior.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...


# Nessa versão usaremos packing para troca de variaveis,
# desta forma não será necessária a variavel proximo
def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f"{penultimo}, {ultimo}", end=',')
    while ultimo < limite:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=',')


if __name__ == '__main__':
    fibonacci(100)
