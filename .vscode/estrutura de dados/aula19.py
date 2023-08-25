# introdução a listas

numeros = [1, 2, 3, 4, 5]
print(numeros)
print(numeros[0])
print(numeros[4])
numeros[1] = 7
print(numeros)
numeros.append(10)
print(numeros)
print(numeros[0:3])  # output: 1,7,3 - 7 pois trocou em 'numeros[1]=7'


times = ['spfc', 'sccp', 'sep', 'sfc']
# Com a função enumerate() podemos percorrer também o índice referente a cada valor da lista
for indice, clube in enumerate(times):
    print(f'indice {indice} = clube {clube}')

