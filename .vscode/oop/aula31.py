# construtores
# reduz o código

class Funcionario:
    # Ao definir um método dentro de uma classe, como o método __init__,
    # o primeiro parâmetro deve ser self. O uso de self dentro do método __init__ e outros métodos
    #  permite que você acesse e manipule os atributos da instância específica da classe.
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome  # adicionando mais funções a classe


usuario1 = Funcionario('Bruno', 'Moretti', '14/08/2003')
usuario2 = Funcionario('Laura', 'Gois', '29/03/2006')
print(usuario1.data_nascimento)
print(usuario2.data_nascimento)

print(usuario1.nome_completo())
# ou
print(Funcionario.nome_completo(usuario1)) # mais usada, faz mais sentido



