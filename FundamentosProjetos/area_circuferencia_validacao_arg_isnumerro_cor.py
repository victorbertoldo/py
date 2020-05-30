#!python

from math import pi
import sys
import errno
import colorama

colorama.init()


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


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

    if not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO
              + "Atenção! O raio deve ser um valor numerico."
              + TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)  # ERRO para argumento invalido

    raio = sys.argv[1]
    area = circulo(raio)
    print("Área do círculo", area)
