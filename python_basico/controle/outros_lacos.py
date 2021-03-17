pessoas = ['Pedrinho', 'Nalu']
adj = ['sapeca', 'inteligente']

for p in pessoas:
    for a in adj:
        print(f'{p} é {a}!')

# laços vazios não podem ser definidos a não ser que o 'pass' seja usado como parametro

for i in (1, 2, 3,):
    pass        

for i in range(1, 11):
    if i % 2: # vai retornar 0 se for par e 1 se for impar
        continue # sempre que for impar o continue será chamado, pois o continue interrompe aquela execução do laço e vai pra próxima
    print(i)


for i in range(1, 11):
    if i == 5:
        break # ao obedecer a condição o break é chamado, sua função é interromper a execução do laço
    print(i)

print('Fim!')