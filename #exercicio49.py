#exercicio49
numero = int(input('Digite o numero da sua tabuada: '))
print ('Sua tabuada é:')
for tabuada in range(1,11):
    valor = numero * tabuada
    print (f'{numero} X {tabuada} = {valor}')