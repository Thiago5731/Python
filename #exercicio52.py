#exercicio52
soma = 0
numero = int(input('Digite um numero: '))
for num in range (1, numero +1 ):
    if numero % num == 0:
        print (f'\037')
        soma += 1
    else:
        print (f'\033[33m')
    print (f'{num}')
print (f'O numero {num} foi dividido por {soma} numeros ')
if soma == 2:
    print ('Esse numero é primo !')
else:
    print ('Esse numero não é primo !')