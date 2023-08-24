# return - usar se for utilizar a informação depois
# return deixa armazenado na memória, podendo ser impresso mais tarde

def cliente1(nome):
    print(f'oi {nome}')


cliente1('Maria')


def cliente2(nome):
    return f'oi {nome}'


print(cliente2('Bruno'))

# argumentos xargs com números
# xargs - possibilidade de adicionar vários argumentos
# criar uma função que soma vários números


def soma(*titulos):  # * na frente invoca o xargs
    resultado = 0  # para o for ter um ponto de partida, começando a somar o número 0 ao próximo que estiver no loop
    for num in titulos:
        resultado += num
    return resultado


x = soma(6, 21, 3, 3, 1)
print(x)

# argumentos xargs nomeando prâmetros
# criar uma função que armazena dados


def agencia(**carro):  # com mais um asterico, o phyton entende que os parâmetros irão ser passados quando a função for invocada

    return carro


print(agencia(marca='nivus', cor='preto', motor=1.0))
