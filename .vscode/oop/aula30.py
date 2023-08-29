# programação orientada à objetos
# classes - utilizada para criar objetos
# objetos são partes dentro de uma class
# classes tem como objetivo agrupar dados e funções, podendo reutilizar
'''
exemplo: 
Class: frutas
objetos: banana,manga,maça, etc... 
'''


'''class Funcionários:  # primeira letra maiúscula
    nome = 'Bruno'
    sobrenome = 'Moretti'
    data_nascimento = '14/08/2003'


usuario = Funcionários()  # adiciona os dados ao objeto(usuario)
print(usuario.nome)
print(usuario.sobrenome)
print(usuario.data_nascimento)
'''

# se a empresa tiver 1000 funcionarios o código ficaria gigante
# por isso a melhor forma de usar classes é jogando funções la dentro
# reduzindo assim a quantidade de linhas de código

# colocando os dados em parâmetros

# criar classe
class Funcionarios:
    pass # passa as informações

# criar o objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

# criar os parâmetros do usuário 1
usuario1.nome = 'Bruno'
usuario1.sobrenome = 'Moretti'
usuario1.data_nascimento = '14/08/2003'

# criar os parâmetros do usuário 2

usuario2.nome = 'Laura'
usuario2.sobrenome = 'Gois'

