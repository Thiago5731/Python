#exercicio31
viagem = float(input('Qual a distancia percorrida? '))
pre = float(viagem * 0.50)
long = float(viagem*0.45)
if viagem <= 200:
    print (f'Sua viagem é mais curta e deu: {pre}')
else:
    print (f'Sua viagem é mais longa e deu: {long}')