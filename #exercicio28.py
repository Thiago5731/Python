#exercicio 28
import random
numero = random.randint(0, 5) #escolhe um numero random de 0 a 5
print ('Olá! Eu sou o computador e estou pensando em um numero inteiro de 0 a 5!')
escolha = int(input('Você sabe me dizer em qual numero estou pensando? '))
if escolha == numero:
    print (f'Parabens você acertou, o numero que eu estva pensando era: {numero}')
else:
    print (f'Infelizmente você errou. Mas pode tentar de novo! O numero era: {numero}')
