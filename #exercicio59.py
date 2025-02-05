#exercicio59
menu = False
while menu != True:
    valor1 = float(input('Digite um valor. (Valores decimais devem ser digitados com ".")'))
    valor2 = float(input('Digite mais um valor. (Valores decimais devem ser digitados com ".")'))
    selecao = int(input('Slecione: \n (1)somar \n (2)multiplicar \n (3)maior \n (4)novos valores \n (5)sair \n Você selecionou: '))
    if selecao == 1:
        soma = valor1 + valor2
        print (f'A soma entre: {valor1} e {valor2} é: {soma}')
        menu = True
    elif selecao == 2:
        multiplica = valor1 * valor2
        print (f'A multiplicação entre {valor1} e {valor2} é {multiplica}')
        menu = True
    elif selecao == 3: 
        if valor1 > valor2:
            print (f'O maior é {valor1}')
        elif valor1 == valor2:
            print (f'Os dois valores são iguais')
        else:
            print (f'O maior valor é {valor2}')
        menu = True
    elif selecao == 4:
        menu = False
    elif selecao == 5:
        menu = True
    else:
        print ('Selecione uma opção valida!!!!')
