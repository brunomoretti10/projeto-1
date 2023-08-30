# constantes tb funcionam para serem importadas e não apenas funções
# para não importar o arquivo inteiro e gastar mais processamento sendo que não será usado todas as 
# funções que estaraão no arquivo, importar apenas a função que usará,ficando 'from módulo import soma ' 
# import módulo
# from módulo import * - '*' na programação em muitas linguagens seignifica 'tudo'
# from módulo import soma
# se quiser importar algo de uma outra pasta, é necessário que se faça o seguinte

from importar.módulo import soma, idade
from importar.módulo2 import subtrair
from itens.cadastro import cliente
print(subtrair(3,2))
print(soma(2,3))
print(idade)
print(cliente())

