# comparação em sets

amigos1 = {'Bruno', 'Gabriel', 'Dani', 'Mari', 'Laura'}
amigos2 = {'May', 'Sophie', 'André', 'Laura', 'Bruno'}

result = amigos1.intersection(amigos2)
print(result)

# quadrado do número
''' def quadrado(x):
    return x**2

num1 = int(input('digite um número:'))
print(f'O quadrado de {num1} é {quadrado(num1)} ')
'''
# função de soma


def soma(a, b):
    return a + b


print(soma(2, 3))


def potencia(base, expoente=2):
    return base ** expoente


# potencia
'''user_number = int(input('digite um número'))
user_exponente = (input('digite mais um número (default 2)'))

if user_exponente:
    print(f'O resultado é  {potencia(user_number, int(user_exponente))}')
else:
    print(f'O resultado é  {potencia(user_number)}')
'''

