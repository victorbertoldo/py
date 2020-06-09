#!python
# Neste exemplo vamos tratar exceção para leitura do arquivo

try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
finally:
    print('Finally')
    arquivo.close()

if arquivo.closed:
    print('Arquivo já foi fechado.')
