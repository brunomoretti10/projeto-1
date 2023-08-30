# desafio com funções
'''
criar um programa que calcula a quantidade de tinta necessária para pintar uma parede.
o usuário deverá fornecer as seguintes informações: rendimento, altura e largura.
o programa deve mostrar na tela a mensagem 'você necessita de x latas de tinta' 
'''

# largura*altura/rendimento = qntd de latas

rendimento = int(input('qual é o rendimento da lata?'))
largura = int(input('qual é a largura da parede?'))
altura = int(input('qual é a altura da parede?'))


def calculo_de_tinta():
    area = largura*altura
    qntdDeLatas = area/rendimento
    print(f'você precisa de {qntdDeLatas} latas de tinta')


calculo_de_tinta()
