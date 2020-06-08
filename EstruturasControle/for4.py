# for i in range(1, 11):
#     print(i)
#     if i == 6:
#         break
# else:
#     print('fim!')

# Função sortear_dado numeros entre 1 e 6
# For com range 1 a 6
# Se for impar continue
# Se o numero for par e for igual ao valor sorteado
# Pela função dado imprimir 'ACERTOU' e depois chamar o break
# Se não acertar chama o else... print('Não Acertou!')

from random import randint


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 != 0:
        continue
    elif i % 2 == 0 and i == sortear_dado():
        print("Acertooo misevavi!!")
        print(f"Numº Sorteado: {i}, Numero da iteração: {i}.")
        break
    else:
        print("Deu Ruim!")
