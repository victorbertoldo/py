class Funcionarios:
    
    def __init__(self, nome, sobrenome, data_nascimento): # inicialização dos construtores
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento


    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome


# criando objetos e parametros
usuario1 = Funcionarios('Jão', 'Berreza', '19/01/2000')        
usuario2 = Funcionarios('Tião', 'Malaquias', '21/11/1998')        

# imprindo Funcionarios
print(usuario1.nome)
print(usuario2.nome)

print(usuario1.nome, usuario1.sobrenome)

print(usuario1.nome_completo())

print(Funcionarios.nome_completo(usuario1))