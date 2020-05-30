from math import pi


def circulo(raio):
    print(f"A area da circunferência é igual à: {pi * raio ** 2}")


if __name__ == '__main__':
    raio = float(input('Informe o raio da circunferência:'))
    circulo(raio)
