# while loop
# É útil quando você não sabe exatamente quantas vezes o loop deve ser executado
# while=enquanto

#Leitura Complementar: Sobre o While
#Python While Loop é usado para executar um bloco de instruções repetidamente até que uma determinada condição seja satisfeita. E quando a condição se torna falsa, a linha imediatamente após o loop no programa é executada. O loop while cai na categoria de iteração indefinida . Iteração indefinida significa que o número de vezes que o loop é executado não é especificado explicitamente com antecedência.


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


