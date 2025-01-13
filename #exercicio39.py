#exercicio39
ano = int(input('Digite o ano do seu nascimento: '))
idade = 2025 - ano
if idade > 18: 
    print (f'Você já deveria ter se alistado pois você tem {idade} anos')
elif idade < 18:
    print (f'Você não está na idade de alistar ainda pois você tem: {idade} anos')
else:
    print (f'Você deve se alistar pois você tem {idade} anos')