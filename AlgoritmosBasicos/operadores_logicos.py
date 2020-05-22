# Operadores lógicos

print(True or False)
print(7 != 3 and 2 > 3)

print(True and True or False and False)

# Tabela verdade AND
print("\n ------> AND <-----\n")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True and True and False and True and True and True)

# Tabela verdade OR
print("\n ------> OR <-----\n")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(False or False or True or False or False or False)


'''
# Tabela verdade XOR (Ou exclusivo)
# o python não possui operador para o XOR então usa-se o "=!" (diferente)
print("\n ------> XOR <-----\n")
print(True != True)
print(True != False)
print(False != True)
print(False != False)
'''

# Operador de negação (unário)
print(not True)
print(not False)

print(not 0)
print(not 1)
print(not -1)

# Exemplo

saldo = 2000
salario = 5000
despesas = 3600

meta = saldo > 0 and salario - despesas >= (0.2 * salario)
print("\n", meta)

print("\n")

# Os trabalhos

trab_terca = True
trab_quinta = False

'''
- Confirmando os 2 trabalhos: tv 50´ + sorvete
- Confirmando apenas 1: TV 32 + sorvete
- Nenhum confirmado: Fica em casa
'''

tv_50 = trab_terca and trab_quinta
sorvete = trab_terca or trab_quinta
tv_32 = trab_terca or trab_quinta
mais_saude = not sorvete

print("tv50={}, Tv32={}, Sorvete={}, Saudável={}".format(
    tv_50, tv_32, sorvete, mais_saude))
