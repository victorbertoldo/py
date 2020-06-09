PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'politica'}
textos = [
    'Jão gosta de futebol e politica',
    'A praia foi divertida'
]


for texto in textos:
    for palavra in texto.lower().split():
        intersecao = PALAVRAS_PROIBIDAS.intersection(
            set(texto.lower().split()))
        if intersecao:
            print('Texto possui pelo menos uma palavra proibida:', intersecao)
        else:
            print('Texto autorizado:', texto)
