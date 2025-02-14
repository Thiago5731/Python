#exercicio68
import random
#from random import randrange
while True:
    computador = random.randrange(0, 10)
    jogador = int(input('Escolha um numero de 0 a 10: '))
    if jogador > 10 or jogador < 0:
        print (f'O valor escolhido foi: {jogador} escolha uma valor valido.')
    soma = computador + jogador
    parim = str(input('Digite P para par e I para impar: ')).upper().strip()
    print(f'O computador escolheu: {computador}')
    print(f'O jogador escolheu: {jogador}')
    print(f'A soma deu: {soma}')
    if soma % 2 == 0 and parim == 'P':
        print ('Parabens você ganhou! ')
        print ('Vamos jogar de novo! ')
    elif soma % 2 != 0 and parim == 'I':
        print ('Parabens você ganhou! ')
        print ('Vamos jogar de novo ! ')
    elif soma % 2 != 0 and parim != 'P':
        print ('Você perdeu!')
        break
    else:
        print ('Você perdeu! ')
        break
    