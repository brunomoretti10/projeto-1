# for loop - criando um retângulo

linhas = 6
colunas = 6
simbolo = '$'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print() # a cada 6x imprimir um espaço(enter), jogando o código para a próxima linha
