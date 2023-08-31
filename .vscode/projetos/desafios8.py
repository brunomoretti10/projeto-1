# lambda usando fo loop

numeros = [1, 2, 3, 4, 5, 6]
quadrado = lambda num: num ** 2


resultados = []  # outra lista vazia
for i in numeros:
    resultados.append(quadrado(i))
print(f'O quadrado dos números {numeros} são {resultados}')