# desafio com sets
'''
criar um programa que gera 3 listas de acordo com a necessidade abaixo:


lista1 = funcionários que tem carro e trabalham a noite
lista2 = funcionários que tem carro e trabalham durante o dia
lista3 = funcionários que não tem carro
'''
funcionarios = ['ana', 'marcos', 'alice',
                'pedro', 'sophia', 'bruno', 'melissa']
turno_dia = ['ana', 'marcos', 'alice', 'melissa']
turno_noite = ['pedro', 'sophia', 'bruno']
tem_carro = ['marcos', 'alice', 'bruno', 'melissa']

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)
