#!python

# Parametros opcionais: texto é um parametro obrigatório,
# já classe é um parametro opicional, que caso não seja preenchido,
# por default retornará ='success'

def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    #    Textes (assertions) - Verifica uma condição. Se for verdadeira
    # ele passa para próxima linha, se for falsa ele irá retornar um erro.
    assert tag_bloco('Incluido com sucesso!') == \
        '<div class="success">Incluido com sucesso!</div>'
    assert tag_bloco('Impossivel excluir!', 'error') == \
        '<div class="error">Impossivel excluir!</div>'
    print(tag_bloco('bloco'))
