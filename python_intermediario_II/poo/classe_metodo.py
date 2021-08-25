from datetime import datetime

class Funcionarios:

    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
      

    def nome_completo(self):
        return (self.nome, self.sobrenome)

    def idade_funcionario(self):
        self.idade = int(datetime.today().year - self.ano_nascimento)
        return self.idade


usuario1 = Funcionarios('Jão', 'Berreza', 1998)
usuario2 = Funcionarios('Tião', 'Megenza', 1970)
usuario3 = Funcionarios('Maria', 'Jana', 1986)    

print(Funcionarios.idade_funcionario(usuario1))
