#exercicio36
print ('Ola! Você precisa de um emprestimo para financiar uma casa certo? Então vamos lá! ')
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Digite em quantos anos você quer pagar: '))
#claculo da prestação mensal 
mensalidade = (casa / (anos * 12))
#calculo da porcentagem
porcentagem = salario * 0.3
if mensalidade > porcentagem: 
    print (f'Nós não podemos fazer um emprestimo pois a mensalidade {mensalidade:.2f} excede os 30% do seu salario que é: {porcentagem:.2f}')
else:
    print (f'O emprestimo será feito pois a mensaladidade {mensalidade:.2f} não excede os 30% do seu salario que é: {porcentagem:.2f}')