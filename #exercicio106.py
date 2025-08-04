#exercicio106
def ajuda(com):
    help(com)


#programa principal
loop = 0
while loop == 0:
    print('-'*30)
    valor = str(input('Digite a biblioteca que você quer saber(Digite "FIM" para sair): '))
    if valor.upper == 'FIM':
        loop += 1
    else:
        ajuda(valor)
    print('-'*30)