#! python
'''
    Para usar o shebang no linux é só add o comentario conforme
    o exemplo abaixo:
    #!/usr/local/bin/python3
'''
pi = 3.1415

raio = float(input('Informe o raio da circunferência:'))

area = pi * raio ** 2

print(f"A area da circunferência é igual à: {area}")
