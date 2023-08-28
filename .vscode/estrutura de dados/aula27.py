# função lambda
# função pequena
# pode ter vários argumentos, mas somente uma expressão
# muito utilizado dentro de outras funções
# código mais 'clean'
# argumento: x
# expressão: após os :

def somar(x, y): return x+y


print(somar(2, 10))

# lambda dentro de uma função


def soma(x, y):
    def func2(x, y): return x+y-10
    return func2(x, y) + 27.5


print(soma(10, 2.5))


def soma2(x, y, z):
    def func3(x, y, z): return x+y+z - 21
    return func3(x, y, z)


print(soma2(2,13,11))
