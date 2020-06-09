#!python
# Neste exemplo vamos tirar as quebras de linha usando strip
arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()
