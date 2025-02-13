#exercicio67
cont = numero = 0
print('---'*10)
print('Bem vindo a tabuada! V3')
print('---'*10)
while True:
    numero = int(input('Digite um numero para ver sua tabuada: '))
    if numero <= -1:
        print (f'Fim do programa! O numero selecionado foi: {numero} Não existe tabuada de numeros negativos!')
    else:
        while cont < 10:
            cont += 1
            tabu = numero * cont
            print (f'{cont} X {numero} = {tabu}')
        cont = 0
            