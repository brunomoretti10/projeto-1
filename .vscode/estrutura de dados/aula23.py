from array import array  # import
# tuples
# não podem ser alterados (immutable)
# utiliza parênteses

numeros_list = [10, 20, 30, 40]
numeros_tuple = (10, 20, 30, 40)
print(type(numeros_list))
print(type(numeros_tuple))

# arrays - array phyton no google mostra os type codes
# types - str(u), int(i), float(f)...
# utilizar quando a lista for muito grande ( pois terá uma melhor performance utilizando array)
# necessário importar a array em phyton
# não pode errar o typecode


letras = array('u', ['a', 'b', 'c', 'd'])  # typecode = u
numeros_int = array('i', [10, 20, 30, 40])  # type code = i
numeros_float = array('f', [1.1, 2.2, 3.3, 4.4])  # typecode= f
print(letras)
print(numeros_int)
print(numeros_float)
