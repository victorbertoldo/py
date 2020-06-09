﻿# Apesar do python teoricamente não possuir constantes,
# existe uma convenção que diz que constantes devem ser
# criadas com letras maiusculas
PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'politica')
textos = [
    'Jão gosta de futebol e politica',
    'A praia foi divertida'
]


for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:', palavra)
            break

    else:
        print('Texto autorizado:', texto)
