#exercicio82
lista1 = []
listapar = []
listaimpar = []
valor = 0
cont = 0 
while cont == 0:
    valor = (int(input('Digite um valor: ')))
    print (f'O valor digitado foi: {valor}')
    lista1.append(valor)
    if valor % 2 == 0: 
        listapar.append(valor)
    else: 
        listaimpar.append(valor)
    fim = (str(input('Você deseja continuar? [S/N]'))).upper().strip()
    if fim == 'N':
        print ('Até a proxima!!!!!')
        cont += 1
print (f'Segue a lista completa: {lista1}')
print (f'Segue a lista somente com os numeros pares: {listapar}')
print (f'Segue a lista somente com os numeros impares: {listaimpar}')