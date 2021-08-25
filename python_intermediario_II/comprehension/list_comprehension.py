frutas1 = ['banana', 'abacate', 'morango', 'uva', 'maça', 'abacaxi']

frutas2= []

# esta é a forma de se fazer utilizando uma iteração comum
for item in frutas1:
    if 'b' in item:
        frutas2.append(item)

print(frutas2)        

# list comprehension
frutas3 = [item for item in frutas1 if 'n' in item]

print(frutas3)  

# com numeros
valores = [x * 10 for x in range(6)]
print(valores)