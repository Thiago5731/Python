#exercicio37
numero = int(input('Digite um numero inteiro: '))
seleção = int(input('''para converter esse numero tecle:
                     binario: 1 
                     octal: 2
                     hexa: 3 :'''))
bi = bin(numero)
oc = oct(numero)
he = hex(numero)
if seleção == 1:
    print (f'O numero em binario é: {bi}')
elif seleção == 2:90
    print (f'O numero em octa é: {oc}')
else: 
    print (f'O numero em hexa é: {he}')