from decimal import Decimal, getcontext
print(dir(int))

print(dir(float))

# desta forma é possivel visualizar tudo que está a diposição
# nos tipos numericos

a = 5
b = 1.5

print('\n')
print(type(a))
print(type(b))
print('\n')
print(type(a + b))

# Qlqr operação de um inteiro com um float

# Para um numero float a Função para verificar
# se o valor é inteiro
b.is_integer()
5.0.is_integer()

# É possivel acessar as funções builtins desta forma
print(int.__abs__(-3))

# Mas  a forma usual é assim:

print(abs(-1))

print(-3.5.__abs__())

# Trabalhando com numeros decimais

print(1.1+2.2)  # isso ocorre por conta da especificação da linguagem

# usando decimais

print(Decimal(1) / Decimal(7))

# para configurar a precisão vamos usar o getcontext

getcontext().prec = 4

print(Decimal(5) / Decimal(9))
print(Decimal.max(Decimal(3), Decimal(5)))
print('\n')


# usando o dir podemos ver os recursos dentro do Decimal

print(dir(Decimal))

print(2.1 + 3.2)

# Resolvendo para o valor esperado

print(Decimal(2.1)+Decimal(3.2))

# após realizarmos o import do Decimal e getcontext,
# podemos ver que agora eles integram ao builtin global
# desta aplicação

print(dir())
