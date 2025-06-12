#exercicio99
def maior(* num):
    cont = maior = 0
    print('\nAnalisando valores..')
    for valor in num:
        print(f'{valor}', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior= valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


##programa principal
maior(3, 5, 8, 2, 7,)
maior(4, 6, 8)
maior(1, 3)
maior(6)
maior()