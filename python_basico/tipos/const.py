'''
Em python não existe constantes, então
existe uma convenção em que ao se declarar uma constante, seu nome deve ser escrito com letras maiusculas
'''

PI = 3.14
raio = float(input('Informe o raio da circunferência: '))

print(type(raio))

area = PI * pow(raio, 2)
print(f'A área do circulo é {area} m2.')