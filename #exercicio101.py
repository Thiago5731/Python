#exercicio101

#voto é opicionar dos 16 aos 18 

#importar biblioteca 
import datetime

#calcular o ano
data_hora = datetime.datetime.now()
ano_atual = data_hora.year

#função para fazer o calculo da idade para votar
def calcular_idade():
    idade = ano_atual - ano_nascimento
    return idade

#programa principal
ano_nascimento = int(input('Digite o ano que você nasceu: '))
if calcular_idade() < 16: 
    print (f'VOCÊ NÃO PODE VOTAR!!! Pois sua idade é {calcular_idade()}')
elif calcular_idade() >= 16 and calcular_idade() <= 17:
    print(f'Seu voto é opcional! Pois sua idade é {calcular_idade()}')
else: 
    print (f'Você é obrigado a votar! Pois sua idade é {calcular_idade()}')