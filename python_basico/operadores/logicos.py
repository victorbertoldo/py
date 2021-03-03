b1 = True
b2 = False
b3 = True

# todos tem que ser verdadeiros
print(b1 and b2 and b3)

# pelo menos 1 precisa ser verdadeiro
print(b1 or b2 or b3)

# ou exclusivo: ou seja exclusivamente 1 deles é verdadeiro e outro é falso
# No python não existe ou exclusivo, Porém é possivel fazer a validação usando diferente
print(b1 != b2) # equivalente ao XOR

# operador de negação
print(not b1)
print(not b2)

print(b1 and not b2 and b3)


# usando operadores logicos com relacionais
x = 3
y = 4

print(b1 and not b2 and x < y)

