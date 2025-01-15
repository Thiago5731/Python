#exercicio45
print ('Pedra papel e tesoura.')
print ('Essa é uma guerra entre você a maquina... ')
print ('As seleções são: \n (1) Pedra \n (2) Papel \n (3) Tesoura ')
import random
jogador = int(input('Selecione um: '))
pc = random.randrange(1,3+1)
if jogador == pc:
    print (f'Vocês empataram! Vocês dois escolheram a mesma opção!')
elif jogador == 1 and pc == 2:
    print (f'A maquina venceu! ela escolheu: {pc} (papel) e você escolheu {jogador} (pedra)')
elif jogador == 2 and pc == 3:
    print (f'A maquina venceu! ela escolheu: {pc} (tesoura) e você escolheu {jogador} (papel)')
elif jogador == 3 and pc == 1:
    print (f'A maquina venceu! ela escolheu: {pc} (pedra) e você escolheu {jogador} (tesoura) ')
elif jogador == 1 and pc == 3:
    print (f'Parabens você ganhou!! você escolheu: {jogador} (pedra) e a maquina {pc} (tesoura)')
elif jogador == 2 and pc == 1:
    print (f'Parabens você ganhou!! você escolheu: {jogador} (papel) e a maquina {pc} (pedra)')
elif jogador == 3 and pc == 2:
    print (f'Parabens você ganhou!! você escolheu: {jogador} (tesoura) e a maquina {pc} (papel)')
else:
    print ('Selecione uma opção valida!')