#exercicio44
valor = float(input('Digite o valor do protudo: '))
print ('Escolha entre: \n 0(a dinheiro/cheque) \n 1(cartão de debito) \n 2(duas vezes no artão de credito) \n 3(tres vezes no cartão de credito) ')
escolha = int(input('Qual sua escolha?'))
#calcuar dinheiro 10% de desconto 
dez = (valor / 10) 
desconto = valor - dez
#calcular cartão de debito 5%
cinco = (5/100)*valor
desconto2 = valor - cinco
#duas vezes no cartão de credito é o preço normal
duas = valor/2
#tres vezes no cartão de credito com 20% de juros no valor total
vinte = (20/100)*valor
aumento = valor + vinte
parcela = aumento/3
if escolha == 0:
    print (f'O seu produto sairá por: {desconto}')
elif escolha == 1:
    print (f'O seu produto sairá por: {desconto2}')
elif escolha == 2:
    print (f'O seu produto sairá por duas parcelas de: {duas}')
elif escolha == 3:
    print (f'O seu produto sairá por 3 parcelas de: {parcela}')
else:
    print ('Por favor escolha um valor dentro dos padrões')