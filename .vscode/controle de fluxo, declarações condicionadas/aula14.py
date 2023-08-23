# while loop
# É útil quando você não sabe exatamente quantas vezes o loop deve ser executado
# while=enquanto

valor = 40
dia = 0

while valor <= 100:
    dia += 1
    print(f'no dia {dia} o produto vai ser vendido por R${valor}')
    valor += 2

    #operador ternário

idade = 20
resultado = 'Voto permitido' if idade>=16 else 'Voto não permitido' #operador ternário
print(resultado)


