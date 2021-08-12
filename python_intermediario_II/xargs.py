'''
Exemplos de funcões utilizando varios argumentos e parametros
'''


# Exemplo de varios argumentos na função, somando diversos numeros (*)
def soma_xargs(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

print(soma_xargs(2,4,5,6,3,6,))


# Exemplo de varios parametros e argumentos na função (**)
def soma_xargs_param(**carro):
    return carro

dados_carro = soma_xargs_param(marca='Onix', cor='Chevrolet', motor=1.4, modelo='ltz', portas=5)

for i in dados_carro:
    print(i,'->', dict(dados_carro)[i])