# if, elif e else

''' criar um programa que dependendo da temperatura (em celsius) do steak
ele retorna o ponto do cozimento em português. o usuário deverá fornecer a temperatura



temperaturas - cozimento
48 graus Celsius - rare (selada)
54 graus Celsius - medium rare (ao ponto para mal) 
60 graus Celsius - medium (ao ponto)
65 graus Celsius - medium well (ao ponto para bem)
71 graus Celsius - well done (bem passada)
'''

temperatura = int(input('Diga o valor da temperatura: '))


if temperatura < 48:
    print('a carne precisa cozinhar por mais alguns minutos')
elif temperatura in range(48, 53):
    print('selada')
elif temperatura in range(54, 59):
    print('ao ponto para mal')
elif temperatura in range(60, 64):
    print('ao ponto')
elif temperatura in range(65, 70):
    print('ao ponto para bem')
elif temperatura >= 71:
    print('bem passada')
