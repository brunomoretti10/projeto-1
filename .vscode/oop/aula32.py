from datetime import datetime
# calculando a idade do funcionário
# não colocar o ano que estamos - o ano de nascimento, pois assim no ano seguinte o código fica ultrapassado
# importar um módulo


class Funcionario:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual-self.ano_nascimento)
        return self.ano_nascimento


usuario1 = Funcionario('Bruno', 'Moretti', 2003)
usuario2 = Funcionario('Laura', 'Gois', 2006)
print(Funcionario.idade_funcionario(usuario1))
print(Funcionario.idade_funcionario(usuario2))
