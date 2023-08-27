# sets (em '{}', e em ordem aleatória)
# similar a listas
# evita itens duplicados
# não utiliza index (não importa a ordem)

lista1 = [10, 20, 30, 40]
lista2 = [10, 45, 87, 92]

num1 = set(lista1)
num2 = set(lista2)
print(num1)
print(num2)
print(num1 | num2)  # | union
print(num1 - num2)  # difference
print(num2 - num1)  # difference
print(num1 ^ num2)  # symmetric differences (tira os duplicados das duas listas)
print(num1 & num2)  # and (mostra o que é duplicado)

print(len(num2))  # len (tamanho)

# funções em sets

s1 = {1, 2, 3, 4, 5, 6}
s1.add(7)
s1.update([8, 9, 10])  # adiciona vários itens
s1.remove(10)
# diferença entre discard e remove é que em discard não emite erro ao colocar número que não está dentro do set
s1.discard(90)
print(s1)

# sets com strings

set1 = {'a', 'b', 'c', 'd'}
set2 = {'f', 'w', 'a', 'i'}
set3 = {'b', 'w', 'z', 'i'}

set4 = set1.union(set3)
set5 = set2.difference(set3)
set6 = set3.difference(set2)
set7 = set1.symmetric_difference(set2)
set8 = set3.intersection(set1)  # imprime o que tem de igual
print(set4)
print(set5)
print(set6)
print(set7)
print(set8)
