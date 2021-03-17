

# print('Ola')
# import pacote.sub.arquivo


# print('Direto no main:')
# print(__name__)
# print(__package__)

# import tipos.variaveis
# from tipos import const, basicos

# import tipos.lista
# import tipos.tuplas
# import tipos.conjuntos
# import tipos.dicionario
# import operadores.unarios

# import operadores.aritmeticos
# import operadores.relacionais
# import operadores.atribuicao
# import operadores.logicos
# import operadores.ternario

# import controle.if_1
# import controle.if_2

# import controle.for_1
# import controle.while_1
# import controle.outros_lacos

from funcoes import basico

# basico.saudacao('Maria', 50)
# basico.saudacao()
# basico.saudacao(idade=21)

basico.soma_e_multi(x=10, a=3, b=2)

# não retorna nada, pois a função retorna um valor a partir da função. Ou seja, para imprimir a informação é necessário armazena-la dentro de uma variavel para depois imprimir
a = basico.soma_e_multi(x=10, a=3, b=2)
print(a)