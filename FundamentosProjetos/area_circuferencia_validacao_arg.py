#!python

from math import pi
import sys

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

    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print("Área do círculo", area)
