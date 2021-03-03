x = 0

while x != -1:
    x = float(input('Informe o numero -1 para sair:'))

print('fim')    


total = 0
qtde = 0
nota = 0

while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair:'))
    if nota != -1:
        qtde += 1
        total += nota

print(f'A média da turma é {total / qtde}')        