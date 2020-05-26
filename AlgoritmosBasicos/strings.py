# Visualizar os recursos builtins para strings
print(dir(str))

nome = 'Jão Mancebo'

print(nome[0])

# Quando houver aspas na string há duas formas de tratar:

print("Marca d'agua")
print('Marca d\'agua')
print('Entre "aspas"')
print("Entre \"aspas\"")

# Texto com multiplas linhas

print("""asdafsafads
asdfafasfdfaf
asdfsadfasdfasfas
asadfadfdasad
""")

print('Multiplas \n linhas')

# acessando valores dentro da string
print(nome[0])  # caracter na posição 0
print(nome[0:3])  # acessar um range da esquerda pra direita
print(nome[-7:])  # acessar um range da direita para esquerda

num = '123456789'
print(num[::2])  # acessa aos elementos da string pulando de 2 em 2
print(num[::-1])  # inversão da string
print(num[::-2])  # elementos da string pulando de 2 em 2 invertido

frase = 'Eu gosto de suco'
print('os' in frase)

# Outras possibilidades

print(len(frase))  # tamanho da scring
print(frase.lower())  # coloca em minusculo
print(frase.split())  # Fatia a string o delimmiter padrão é o espaço
