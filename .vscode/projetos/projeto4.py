# calculo de IMC - índice de massa corporal
# if elif

'''
qual é sua altura em cm
qualé seu peso em kg

'''
# menor que 18,5 - magreza
# entre 18,5 e 24,9 - normal
# entre 25,0 e 29,9 - sobrepeso
# entre 30,0 e 39,9 - obesidade
# maior que 40 - obesidade grave

altura = float(input('digite sua altura:'))
peso = float(input('digite seu peso:'))

# dividir por 100 pois pediu a altura em centimetro
imc = peso/(altura/100)**2
print(imc)

if imc < 18.5:
    print('magreza')
elif imc >= 18.5 and imc < 24.9:
    print('normal')
elif imc >= 25 and imc < 29.9:
    print('sobrepeso')
elif imc >= 30 and imc < 39.9:
    print('obesidade')
elif imc >= 40:
    print('obesidade grave')
