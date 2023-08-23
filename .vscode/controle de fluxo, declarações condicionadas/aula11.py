# nested loops (um loop dentro do outro)
# outer loop - loop de fora
# inner loop - loop de dentro

for numero1 in range(5):
    print('produto'+str(numero1))
    for numero2 in range(5):
        print(numero1, numero2)
