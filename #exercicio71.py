#exercicio71
print('***'*10)
print ('Bem vindo ao caixa eletronico!')
print('***'*10)
calculo = nota50 = nota20 = nota10 = nota1 = 0
valor = int(input('Quantos reais você quer sacar? R$:'))
while True:
    while valor >= 50:
        calculo = valor - 50
        valor = calculo
        nota50 += 1
        if valor < 50:
            break
    while valor >= 20:
        calculo = valor - 20
        valor = calculo
        nota20 += 1
        if valor < 20:
            break
    while valor >= 10:
        calculo = valor - 10
        valor = calculo
        nota10 += 1
        if valor < 10:
            break
    while valor >= 1:
        calculo = valor - 1
        valor = calculo
        nota1 += 1
        if valor < 1:
            break
    break
print (f'A quantidade de notas de 50 foi: {nota50}')
print (f'A quantidade de notas de 20 foi: {nota20}')
print (f'A quantidade de notas de 10 foi: {nota10}')
print (f'A quantidade de notas de 1 foi: {nota1}')