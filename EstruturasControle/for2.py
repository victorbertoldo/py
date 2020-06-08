palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end=',')
print('fim')


aprovados = ['Rafaela', 'Pedro', 'Ana', 'João']
for i in aprovados:
    print(i)


for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

# Tuplas

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')

for dia in dias_semana:
    print(f"Hoje é {dia}")


# set

for letra in set('muito legal'):
    print(letra)

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
