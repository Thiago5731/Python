'''#exercicio62
termo = int(input('Digite um termo: '))
razao = int(input('Digite uma razão: '))
loop = True
contador = 0
print (f'Você escolheu {termo}')
while loop != False:
    contador += 1
    termo += razao
    print (f'Sua P.A é: {termo}')
    if contador == 10:
        selecao = int(input('Quantos termos você quer mais? '))
        if selecao == 0:
            loop = False
            print ('Até mais!!')
        else: 
            termo += selecao'''
termo = int(input('Digite um termo: '))
razao = int(input('Digite uma razão: '))
contador = 1
mais = 10
total = 0
print (f'Você escolheu {termo}')
while mais != 0:
    total = total + mais
    while contador <= total:
        termo += razao
        contador += 1
        print (f'Sua P.A é: {termo}')
    print ('PAUSA')
    mais = int(input('Quantos termos você quer moastrar mais? '))
print ('Fim')