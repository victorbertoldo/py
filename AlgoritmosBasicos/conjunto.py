a = {1, 2, 3}
print(type(a))

a = set('abcd')
print(a)

# O set ou conjunto, não aceita valores repetidos, os valores
# repetidos são ignorados

a = set('abbbcccddd')
print(a)

# member operators tbm funcionam em set
print('a' in a)

# esta comparação retorna True pq o set não indexa pela ordem e não aceita
# repetidos
print({1, 2, 3} == {3, 2, 2, 1, 3})

# O operações com conjuntos
c1 = {1, 2}
c2 = {3, 2}
# o union não gera impacto no conjunto c1, ele gera um novo conjunto
# "temporario" e o mostra
print(c1.union(c2))
print(c1.intersection(c2))  # O intersection

# Para alterar o cconjunto c1 usamos update
c1.update(c2)
print(c1)
# Após a alteração, vamos verificar se o c2 é subconjunto do c1
print(c2 <= c1)
# E tbm é possivel verificar se c1 é superconjunto de c2
print(c1 >= c2)

# Diferença entre conjuntos

a = set('abcd')
b = set('asdf')
print(a - b)
print(b - a)

# Exclusão de elementos do conjunto
print(c1)
c1 -= {2}
print(c1)
