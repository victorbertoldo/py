# Formato -> [ expressão for item in lista]

dobros = [i * 2 for i in range(10)]
print(dobros)

# exemplo mais comum

dobros = []
for i in range(0, 20, 2):
    dobros.append(i)
print(dobros)

dobros = []
for i in range(10):
    dobros.append(i * 2)
print(dobros)
