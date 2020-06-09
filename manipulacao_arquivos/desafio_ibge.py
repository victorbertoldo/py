#!python

import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o csv...')
        dados = entrada.read().decode('latin1')
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    # Em casos de uso de url ou outros tipos de string
    # alguns caracteres especiais podem ocasionar problemas
    # Como por exemplo o \n
    # Nesses casos é só usar o 'r' junto a string
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
