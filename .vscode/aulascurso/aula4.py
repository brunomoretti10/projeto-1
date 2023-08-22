#formated strings #reduz o código
nome = 'bruno '
sobrenome = 'moretti'
profissão = 'programador'

texto = nome + sobrenome + ' é ' +  profissão
print(texto)
texto2= f'{nome} {sobrenome} é {profissão}'#formated string começa com f'
print(texto2)

#metodos para strings
mensagem = '    são paulo futebol clube'
print(mensagem.lower()) #letras minusculas
print(mensagem.upper()) #letras maiusculas
print(mensagem.capitalize()) #metodo que deixa a primeira letra em maiusculo
print(mensagem.find('c')) #metodo que fala qual a posição da letra, qual o index
print(mensagem.replace('l','ç')) #metodo que faz a troca
print(mensagem.replace('são','santo'))
print(mensagem.strip()) #tira os espaços do começo da frase