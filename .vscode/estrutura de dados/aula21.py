# extraindo variáveis de listas
cores = ['azul', 'vermelho', 'amarelo', 'laranja', 'preto', 'branco', 'rosa']
# se quiser extrair menos itens do que o total da lista, e não colocar *'alguma palavra' irá dar erro
cor1, cor2, cor3, *outras_cores, cor4 = cores
print(cor1)
print(cor2)
print(cor3)
print(outras_cores)
print(cor4)

# looping dentro de uma lista
valores = [10, 33, 50, 72, 81, 99]
for x in valores:
    print(f'O valor do produto é R$ {x}.')

# verificando itens em uma lista
clube_cliente = input('Digite seu clube do coração')
clubes = ['são paulo', 'corinthians',
          'palmeiras', 'santos', 'flamengo', 'grêmio']
if clube_cliente.lower() in clubes:
    print('O clube do cliente está dentro do top 6')
else:
    print('O clube do cliente não está dentro do top 6')
