# lambda com if, else

'''def par_ou_impar(num):
    if num % 2 == 0:
        return 'par'
    else:
        return 'impar'
'''

# transformando em apenas uma linha de código usando a função lambda


par_ou_impar = lambda num: 'Par' if num % 2 == 0 else 'impar'


user_number = int(input('digite um número: '))
print(f'O número {user_number} é {par_ou_impar(user_number)}')
