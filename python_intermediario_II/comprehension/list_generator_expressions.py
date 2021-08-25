from sys import getsizeof

numeros = [x * 10 for x in range(10)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

# o cod acima resolve o problema, porém se houver mtos itens na lista começa a ficar inviavel
# Generator expresion é uma forma do python alocar menos memoria para armazenar esses valores 
# esta opção não está builtin no python



numeros = (x * 10 for x in range(10)) # apos importar o modulo, basta substituir o [] por ()

print(type(numeros))
print(list(numeros))

print(getsizeof(numeros)) # generator usa muito menos memoria