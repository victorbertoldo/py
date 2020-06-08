produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

# percorrendo as chaves. Também pode ser usado produto.keys()
for chave in produto:
    print(chave)

# percorrendo os valores.
for valor in produto.values():
    print(valor)

# percorrendo chaves e valores
for chave, valor in produto.items():
    print(chave, '=', valor)
