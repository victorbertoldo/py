
def saudacao(nome = 'Pessoa', idade = 30):
    print(f'bom dia {nome}!\n Vc nem parece ter {idade} anos.')

print(__name__)    

# este teste faz com que esta chamada na função somente seja executada se este arquivo .py for chamado diretamente.
# apartir do main.py esta informação não é mostrada

if __name__ == '__main__':
    saudacao('Ana', idade=5)


def soma_e_multi(a, b, x):
    return a + b * x    