def mult(a, b):
    return a * b


parametro = 6
resultado = 1

for i in range(1, parametro + 1):
    resultado = mult(resultado, i)

print(resultado)
