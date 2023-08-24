# parâmetros e argumentos em uma função

def clubes_brasileiro(nome, quantidade):  # parâmetros
    print(f'O {nome} possui {quantidade} campeonatos brasileiros')


# argumentos
clubes_brasileiro('são paulo', 6)
clubes_brasileiro('palmeiras', 11)
clubes_brasileiro('flamengo', 7)

# argumento default = aquele que você define o valor no parâmetro
# argumento non-default = aquele que você não define o valor no parâmetro


# argumento non-default(time) argumento default(títulos)
def clubes_libertadores(time, títulos=3):
    print(f'O {time} possui {títulos} libertadores')


clubes_libertadores('São Paulo')
clubes_libertadores('Palmeiras')
clubes_libertadores('Flamengo')
clubes_libertadores('Corinthians', 1)  # pode alterar

# regra do default: sempre colocar como o parâmetro final


def boas_vindas(quantidade, nome='Bruno'):
    print(f'{nome} possui {quantidade} medalhas')


boas_vindas(5)
boas_vindas(2, 'Pedro')
boas_vindas(7)
