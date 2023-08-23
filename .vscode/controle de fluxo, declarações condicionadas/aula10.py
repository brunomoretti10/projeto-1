# for loop - utilizando if e else
# enviar um email com os detalhes da compra online (maximo 3 tentativas) para compras confirmadas

compra_confirmada = True
dados_compra = 'compra no valor de R$10,00 e transação aceita'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('detalhes enviados para o seu email')
        break
    else:
        print('falha na compra')
