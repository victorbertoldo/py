for x in range(1, 11):
    if x % 2 == 0:
        continue  # O continue interrompe a iteração falsa e vai p/
        # proxima de imediato
    print(x)
    print('\n')

for x in range(1, 11):
    if x == 5:
        # O break faz a iteração acabar. Qndo for verdadeiro, ele sai do laço.
        break
    print(x)
print('Fim!')
