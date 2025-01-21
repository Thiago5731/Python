#exercicio51
numero = int(input('Digite o primeiro termo da sua PA: '))
razao = int(input('Digite a razão: '))
decimo = numero + (10 -1) * razao
for pa in range(numero,decimo, razao):
    print (f'{pa}')
print ('Fim do programa!')