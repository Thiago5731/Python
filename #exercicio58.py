#exercicio58
import random
numero = random.randint(0, 10) #escolhe um numero random de 0 a 10
print ('Olá! Eu sou o computador e estou pensando em um numero inteiro de 0 a 10!')
escolha = ''
tentativa = 0
while escolha != numero:
    escolha = int(input('Você sabe me dizer em qual numero estou pensando? '))
    tentativa += 1
    if escolha == numero:
        print (f'Parabens você acertou! com {tentativa} tentativas ')
    else:
        print (f'Infelizmente você errou. Mas pode tentar de novo!')