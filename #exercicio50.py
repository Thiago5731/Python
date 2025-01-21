#exercicio50
soma = 0 
cont = 0
for digite in range (1,7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
        cont += num
        print (f'Esse valor: {num} é par')
print (f'A soma entre os valores pares é {soma}')