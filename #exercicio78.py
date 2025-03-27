#exercicio78
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print (f'Os valores escolhidos foram: {valores}')
valores.sort()
print (f'O menor valor digitado foi: {valores[0]} e o maior foi: {valores[4]}')

#guanabara fez utilizado aquele metodo de ler o primeiro valor e se ele for o maior continua e tals. Vou deixar comentado aqui. 
#maior= 0
#menor= 0
#esse if fica dentro do loop
#if cont == 0: 
#    maior = menor = valores[cont]
#else:
#    if valores[cont] > maior:
#        maior = valores[cont]
#    if valores[cont] < menor:
#        menor = valores[cont]
