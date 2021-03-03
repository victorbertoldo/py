for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)
    
for i in range(1, 100, 5):
    print(i)    

    
for i in range(20, 0, -1):
    print(i)        

nums = [2, 4, 6, 8]    

for n in nums:
    print(n, end=' ')

texto = 'Um texto'

for letra in texto:
    print(letra, end=' ')

for n in {1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9}:
    print(n, end=' ')

print('\n')

produto = {
    'nome': 'Coca',
    'preco': 8.50,
    'desconto': 0.10
}        


for atributo in produto:
    print(atributo, '==>', produto[atributo])



for atributo, valor in produto.items():
    print(atributo, '==>', valor)


for valor in produto.values():
    print(valor, end=' ')

for atributo in produto.keys():
    print(atributo, end=' ')    