var = list('comprar')
print(var)  # output: ['c','o','m','p','r','a','r']
# agregando duas listas com o zip
# zip = função dentro do phyton
nome = ['Mauro', 'Fabiana', 'Bruno', 'Giovanna']
ano = [1972, 1976, 2003, 2010]
duas_listas = zip(nome, ano)
print(list(duas_listas))

# input em uma lista
# objetivo: criar uma lista de frutas a partir do input do usuário

frutas_usuario = input('Digite o nome das frutas separado por vírgulas')

# lista final, nessa variável será armazenada as frutas que o usuário digitar
# quando você chama a função spli(), em uma string, ela divide a string sempre que encontrar no caso ',' e cria uma lista.
frutas_lista = frutas_usuario.split(', ')
print(frutas_lista)
