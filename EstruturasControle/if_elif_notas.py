#!python
import sys


def nota_conceito(valor):
    nota = float(valor)
    if nota > 10.0:
        return 'Nota Inválida'
    if nota > 9.0:
        return 'A'
    elif nota > 8.0:
        return 'A-'
    elif nota > 7.0:
        return 'B'
    elif nota > 6.0:
        return 'B-'
    elif nota > 5.0:
        return 'C'
    elif nota > 4.0:
        return 'C-'
    elif nota > 3.0:
        return 'D'
    elif nota > 2.0:
        return 'D-'
    elif nota > 1.0:
        return 'E'
    elif nota > 0.0:
        return 'E-'
    else:
        return 'Nota Inválida'


if __name__ == "__main__":
    valor_informado = sys.argv[1]
    conceito = nota_conceito(valor_informado)
    print(conceito)
