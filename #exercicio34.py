#exercicio34
salario = float(input('Qual o seu salario? '))
#########_calculo da porcentagem de 10%_##########
final1 = salario + (salario*10/100)
#########_cauculo da porcentagem de 15%_##########
final2 = salario + (salario*15/100)
###################
if salario >= 1250:
    print (f'O seu novo salario será: {final1} com um aumento de 10%')
else:
    print (f'O seu novo salario será {final2} com um aumento de 15%')