#!python

arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()

for registros in dados.splitlines():
    # print(registros.split(','))
    print('Nome: {}, Idade: {}'.format(*registros.split(',')))
