pessoa = {'nome': 'Profª Ana', 'Idade': 38, 'cursos': ['Ingles', 'Portugues']}
print(type(pessoa))

print(dir(pessoa))

print(len(pessoa))

print(pessoa['nome'])
print(pessoa['cursos'][1])
# print(pessoa['tags'])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('Idade'))
print(pessoa.get('tags'), '0')  # retornar um valor caso o campo não exista

pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
print(pessoa)
pessoa['idade'] = 44
# Aqui podemos usar o metodo append, pq neste campo do dicionario há uma lista
pessoa['cursos'].append('Angular')
print(pessoa)

# metodo pop le o campo que foi passado como parametro, porém remove o campo
print(pessoa.pop('idade'))
print(pessoa)

# Atualizar os campos do dicionario
pessoa.update({'idade': 40, 'Sexo': 'M'})
print(pessoa)

# Excluir o campo lista
del pessoa['cursos']
print(pessoa)

# Limpar o dicionario
pessoa.clear()
print(pessoa)
