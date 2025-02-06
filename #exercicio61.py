#exercicio61
termo = int(input('Digite um numero inteiro para calcular sua P.A.: '))
razao = int(input('Digite um numero inteiro para ser sua razão: '))
loop = 0
print (f'Você escolheu {termo} sua pa é:')
while loop < 10:
    loop += 1
    termo += razao
    print (termo)