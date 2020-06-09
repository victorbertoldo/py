#!python
# Neste formato, usando o with quem  gerencia qndo o arquivo
# será fechado é o proprio python

with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo já foi fechado.')
