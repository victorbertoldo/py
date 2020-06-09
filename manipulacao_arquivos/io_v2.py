#!python
# Neste exemplo o arquivo é servido sobdemana
# dentro do for - técnica de streaming
arquivo = open('pessoas.csv')
for registro in arquivo:
    # Desta forma ao retornar os itens, haverá uma quebra de linha
    # pois o padrão é o registro do csv vir com \n no fim da linha
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
arquivo.close()
