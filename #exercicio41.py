#exercicio41
ano = int(input('Digite sua data de nascimento: '))
idade = ano - 2025
if idade <= 9:
    print ('Atleta MIRIM')
elif idade >= 10 and idade <= 14:
    print ('Atleta INFANTIL')
elif idade >= 15 and idade <= 19:
    print ('Atleta JUNIOR')
elif idade >= 20 and idade <= 25:
    print ('Atleta SÊNIOR')
else:
    print ('Atleta MASTER')