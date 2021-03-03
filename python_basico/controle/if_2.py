a = 'valor'     # True
a = 0           # False
a = -0.00001    # True
a = ''          # False
a = ' '         # True
a = []          # False
a = {}          # False

if a:
    print('Existe!!!')
else:
    print('não existe ou é zero, ou é vazio')