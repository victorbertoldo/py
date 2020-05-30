#!python

from math import pi
import sys

# desta forma não pegaremos o imput do usuario, mas sim passaremos o valor
# como argumento na chamada do script via terminal


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    # print(sys.argv[0]) # script chamado
    # print(sys.argv[1]) # argumento console
    raio = sys.argv[1]
    area = circulo(raio)
    print("Área do círculo", area)
