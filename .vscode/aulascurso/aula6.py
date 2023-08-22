#controle de curso, declarações condicionadas
#if e else
'''if condição1:
     - código a ser executado se condição1 for verdadeira
elif condição2:
     - código a ser executado se condição2 for verdadeira
elif condição3:
     - código a ser executado se condição3 for verdadeira
else:
    - código a ser executado se nenhuma das condições anteriores for verdadeira
'''

velocidade = 40
if velocidade>110:
    print('acima da velocidade permitida')
    print('favor, reduza a velocidade')
elif velocidade<60:
    print('favor dirigir acima de 80km/h')

else:
    print('velocidade ok')

nota = 8
if nota >= 8:
    print('medalha de honra')
elif nota >= 6:
    print('aprovado')
elif nota >= 4:
    print('recuperação')
else:
    print('reprovado')
