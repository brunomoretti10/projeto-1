# introdução a dicionários
# utiliza index no formato de keys e values

aluno = {'Nome': ' Bruno', 'idade': 20, 'nota': '10', 'aprovação': True}
print(aluno)
print(aluno['Nome'])
print(aluno['idade'])
print(aluno['nota'])
print(aluno['aprovação'])

# manipular dados no dicionário

aluno1 = {'Nome': ' Bruno', 'idade': 20, 'nota': '10', 'aprovação': True}
aluno1.update({'Nome': 'Junior', 'idade': 22, 'endereço': 'Rua A'})
print(aluno1.get('nome_mãe', 'não existe'))
print(aluno1)
print(aluno1.get('nota'))
del aluno1['idade']  # del: remove o índice
print(aluno1)

# diferença entre remove e del

lista1 = ['Bruno', 'dudu', 'juju', 'pedro']
lista1.remove('Bruno')
print(lista1)
lista2 = ['Bruno', 'dudu', 'juju', 'pedro']
del lista2[0]
print(lista2)

# looping dentro de um dicionário

aluno2 = {'Nome': ' Bruno', 'idade': 20, 'nota': '10', 'aprovação': True}
for x in aluno2:  # mesma coisa que for x in aluno2.keys()
    print(x)  # só imprime as keys e não os values

for x in aluno2.values():
    print(x)

    for x in aluno2.items():  # imprime keys e values
        print(x)
# tirar de dentro da tuple
for x, y in aluno2.items():  # x=keys, y=values
    print(x, y)
