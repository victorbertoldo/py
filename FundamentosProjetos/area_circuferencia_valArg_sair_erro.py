#!python

from math import pi
import sys
import errno

# desta forma não pegaremos o imput do usuario, mas sim passaremos o valor
# como argumento na chamada do script via terminal


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print(f"""\
                É necessário informar o raio do círculo.
                    Sintaxe: {sys.argv[0]} <raio>""")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

# sys.exit() com qlqr parametro diferente de 0
# significa que houve erro
# Usando o errno.EPERM como parametro, estamos retornando
# um erro compativel com sistema operacional,
# então sys.exit(errno.EPERM) é == sys.exit(1)
#    else:
# Usando o sys.exit(1), o sistema irá encerrar a execução ao encontrar um erro
# Por isso o else foi comentado.
    raio = sys.argv[1]
    area = circulo(raio)
    print("Área do círculo", area)
