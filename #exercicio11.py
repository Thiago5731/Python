largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = (largura * altura)
#a cada 2 m² de parede = 1 litro de tinta 
litros = (area / 2)
print (f'A area da sua parede é igual a: {area:.2f}m² \nVocê vai gastar {litros:.2f} litros de tinta.')

#Exercicio12 

produto = float(input('Qual o preço do produto? R$: '))
por5 = (5 * produto / 100) 
por10 = (10 * produto / 100)
por25 = (25 * produto / 100)
por30 = (30 * produto / 100)
por50 = (50 * produto / 100)
print (f'Seu desconto é de: {produto} \no desconto de 5% é {por5} \no desconto de 10% é {por10} \no desconto de 25% é {por25} \no desconto de 30% é {por30} \no desconto de 50% é {por50}')

#Exercicio13

salario = float(input('Qual o salario?' ))
porc5 = ((15 * salario / 100) + salario)
print (f'O seu salario com acresimo de 15% é: {porc5:.2f}')

#Exercicio14

formula = float(input('Digite a temperatura em c°' ))
conversao = (formula * 1.8 + 32)
print (f'Sua temperatira em F° é {conversao}')

#exercicio15

kmper = float(input('Quantos Km o carro percorreu? '))
dias = float(input('Quantos dias vc ficou com o carro? '))
#60 leleu por dia
#0.15 poir km rodado
pago = ((kmper * 0.15) + (dias * 60))
print (f'O total a apagr será: {pago}')
