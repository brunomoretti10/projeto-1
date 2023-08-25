# funções dentro da lista
# estudar funções para saberem que existem - 'list functions phyton'
nomes = ['Bruno', 'Gabriel', 'Mayara', 'Daniel', 'Laura']
# nomes.append('Sophie')
# nomes.remove('Bruno')
# nomes.insert(1, 'Giovanna')
# nomes.pop(0)
nomes.sort()  # organiza em ordem alfabética


print(nomes)

# concatenando listas (ligar,juntar)
numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']
# final = numeros*2
# final = numeros + letras
numeros.extend(letras)
print(numeros)


# criar uma lista dentro de outra lista
# index 0 da lista grande = 'item 1, item2' index 1 da lista grande = 'item 3, item 4'
# item 1 - posição 0 do index 0
# item 2 - posição 1 do index 0
# item 3 - posição 0 do index 1
# item 4 - posição 1 do index 1
itens = [['item 1', 'item 2'], ['item 3', 'item 4']]
print(itens)  # lista inteira
print(itens[0])  # lista index 0
print(itens[1])  # lista index 1
print(itens[0][0])  # index 0 e posição 0
print(itens[0][1])  # index 0 e posição 1
print(itens[1][0])  # index 1 e posição 0
print(itens[1][1])  # index 1 e posição 1
