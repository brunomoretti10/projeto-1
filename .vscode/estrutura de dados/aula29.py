
# list comprehension
# forma muito mais simples de escrever expressões como for loop e if
# utilizado quando você precisa criar uma lista a partir de uma existente
# [ expressão for iten in itens ]
# com strings

# objetivo: criar outra lista que contém palavras com a letra b

'''frutas1 = ['banana', 'melancia', 'abacate', 'kiwi', 'abacaxi']
frutas2 = []

for itens in frutas1:
    if 'b' in itens:
        frutas2.append(itens)
print(frutas2)
'''
# agora deixando em apenas uma linha de código ( dentro de uma list comprehension)

frutas = ['banana', 'melancia', 'abacate', 'kiwi', 'abacaxi']
frutas2 = [x for x in frutas if 'n' in x]  # expressão: item
print(frutas2)

# list comprehension com números

'''valores=[]
for x in range(11):
    valores.append(x*10)
    print(valores)'''

# agora deixando em apenas uma linha de código (dentro de uma list comprehension)

valores = [x*10 for x in range(11)]
print(valores)

# generator expressions
# menos memória alocada
# usado quando a quantidade de itens é enorme
# valores em bytes
# generator expression - só muda o parênteses no lugar do colchete

numeros = (x*10 for x in range(11))
print(type(numeros))
print(list(numeros))
