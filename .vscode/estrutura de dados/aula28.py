# map em uma lista
# map(função, lista)

# exemplo 1
def dobrar_numero(x):
    return x*2


lista = [1, 2, 3, 4, 5]
lista2 = map(dobrar_numero, lista)
print(list(lista2))


def triplicar_numero(y):
    return y*3


# exemplo 2
num = [1, 2, 3, 4, 5]
num2 = map(triplicar_numero, num)
print(list(num2))

# função map com lambda
# reduzir linhas do código

# exemplo 1 usando lambda
numeros = [1, 2, 3, 4, 5]
# lambda no lugar da função
print(list(map(lambda x: x*2, numeros)))

# exemplo 2 usando lambda

numeros3 = [1, 2, 3, 4, 5]
print(list(map(lambda x: x*3, numeros3)))

# função filter
# filtrar valor acima de 20
valores = [10, 15, 19, 45, 76, 81, 99]


def remover20(x):
    return x > 20


# filter retorna os valores reais, map retornaria em boolean
print(list(filter(remover20, valores)))

# em lambda
valores1 = [10, 15, 19, 45, 76, 81, 99]
print(list(filter(lambda x: x > 20, valores1)))

# map retornaria valor booleano, filter seleciona os valores e retorna os valores reais
