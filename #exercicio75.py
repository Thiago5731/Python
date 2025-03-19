#exercicio75
print ('Você vai digitar 4 valores. Dentre eles tem que ter o 9 e o 3')
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: ')) 
valor4 = int(input('Digite o quarto valor: '))
tupla = (valor1, valor2, valor3, valor4)
print (f'O valor 9 aparece: {tupla.count(9)} vezes') #quantas vezes aparece o 9
print (f'O valor 3 está na posição: {tupla.index(3)}') #em que posição está o 3 
if valor1 % 2 == 0: 
    print (f'O valor {valor1} é par')
if valor2 % 2 == 0:
    print (f'O valor {valor2} é par')
if valor3 % 2 == 0:
    print (f'O valor {valor3} é par')
if valor4 % 2 == 0: 
    print (f'O valor {valor4} é par')

#podia ter feito colocando o todos os 4 int, denbtro da tupla e na parte final poderia ter feito só uma verificação
#fazendo um loop para verificar se cada valor dentro da tupla é par ou não. 