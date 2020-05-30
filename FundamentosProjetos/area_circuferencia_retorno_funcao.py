from math import pi


def circulo(raio):
    return pi * raio ** 2


if __name__ == '__main__':
    raio = float(input('Informe o raio da circunferência:'))
    area = circulo(raio)
    print("Área do círculo", area)
