#exercicio38
numero = int(input('Digite um numero: '))
numero2 = int(input('Digite outo numero: '))
if numero == numero2:
    print ('Não tem numero maior, os dois são iguais.')
elif numero > numero2:
    print (f'O numero {numero} é maior que o {numero2}')
else:
    print (f'O numero {numero2} é maior que o {numero}')
