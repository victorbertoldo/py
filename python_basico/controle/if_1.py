nota = float(input('Informe a nota do aluno: '))
comportado = True if input('Comportado (y/n): ') == 'y' else False

if nota >= 9 and comportado:
    print('Duas palavras: para bens!')
    print('Quadro de honra')
elif nota >= 7:
    print('Aprovado')    
else:
    print('Reprovado')    

print(nota)    