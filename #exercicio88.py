#exercicio88
#o meu não deu certo. segue o do guanabara
"""import random
lista = []
listagg = []
cont = 0
print('=-'*14)
print('<======> MEGA SENA <======>')
print('=-'*14)
jogos = int(input('Digite o numero de jogos que você quer jogar: '))
while cont <= jogos - 1:
    cont += 1
    print (f'Jogo {cont}')
    for c in range(0, 6):
        valores = random.randrange(1, 60)
        lista.append(valores)
        listagg.append(lista[:])
        lista.clear
print(listagg)"""
#o do guanabara
from random import randint
from time import sleep
lista = list()
jogos = list()
print ('Jogos da mega sena')
quant = int(input('Quantso jogos você quer: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('Sorteando')
