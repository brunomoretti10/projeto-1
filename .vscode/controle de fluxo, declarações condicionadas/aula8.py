# for
# for loop - utilizando números
# for in
# imprimir de 1 a 5
#Em Python, a função range() é usada para gerar uma sequência de números em um intervalo específico. Ela é comumente usada em laços for para iterar sobre uma série de valores. A função range() pode receber até três argumentos: início, fim e passo (opcional). A sintaxe básica é a seguinte:
#range(início, fim, passo)

for numero in range(6):
    print(numero)

    for clubes in range(10,4,-1):
        print(clubes)
    
    for numbers in range(50,101,5):
     print(numbers)

     for num in range(10,16):
        print(num)

#Lembre-se de que, ao usar o range(), o valor final especificado não será incluído na sequência. Isso ocorre porque o range() gera valores até, mas não incluindo, o valor final.

#criando uma lista usando a função range()

    nu = list(range(10,51,10)) #output: [10,20,30,40,50]
    print(nu)