# while true
# jogo: acerte a fruta
'''
while True:
    fruta = input('qual o nome da fruta:')
    if fruta.lower() == 'abacate':
        break
print('parabéns, você acertou a fruta')
'''

# par e ímpar

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero % 2 == 0:  # dividido por 2 e o resto for igual a zero
        print(f'O número {numero} é par')
    else:
        print(f'Onúmero {numero} é ímpar')
