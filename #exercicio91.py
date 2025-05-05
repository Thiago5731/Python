#exercicio91
import random 
jogadores = {}
jogadores['jogador1'] = random.randrange(1, 6)
jogadores['jogador2'] = random.randrange(1, 6)
jogadores['jogador3'] = random.randrange(1, 6)
jogadores['jogador4'] = random.randrange(1, 6)
for k, v in jogadores.items():
    print(f'O jogador {k} tirou {v} no dado! ') 
print ('+'*30)
print (f'A ordem ficou: ')
for c in sorted(jogadores, key = jogadores.get, reverse=True):
    print (c, jogadores[c])

print ('+'*30)
print ('+'*30)
print ('+'*30)
print ('+'*30)
#guanabara fez importando o 
from operator import itemgetter 
#e colocando
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print (ranking)
#desse jeito o resultado sai como uma lista e não como um dicionario.