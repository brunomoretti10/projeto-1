#operadores lógicos
# and e or
# em or,apenas uma afirmação deve ser true
# em and, ambas afirmações devem ser true

lucas_moura_titular=True
volta_morumbi=False

if lucas_moura_titular or volta_morumbi:
    print('são paulo campeão da copa do brasil'.upper())
else:
    print('flamengo campeão da copa do brasil')

pedro_titular = False
volta_maracana = True

if pedro_titular and volta_maracana:
        print('Flamengo campeão')
else: 
        print('São Paulo campeão')
    
