# tuple

'''cidades = ('São Paulo', 'Atibaia', 'Rio de Janeiro')
cidade_usuario = input('digite o nome de sua cidade: ')
if cidade_usuario in cidades:
    print('A cidade esta na lista de cidades')
else:
    print('A cidade não esta na lista de cidades')
'''

# dicionários
# países e suas capitais

capitais = {
    'Brasil'.lower(): 'Brasília',
    'Argentina'.lower(): 'Buenos Aires',
    'Chile'.lower(): 'Santiago',
    'Australia'.lower(): 'Canberra',
    'Canada'.lower(): 'Ottawa'
}
pais_usuario = input('digite o nome do país: ')
if pais_usuario in capitais:
    print(f'A capital de {pais_usuario} é {capitais[pais_usuario]}')
else:
    print(f'Não temos informação sobre a capital de {pais_usuario}')
