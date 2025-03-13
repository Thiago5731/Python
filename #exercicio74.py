#exercicio74
import random
n1 = random.randrange(6)
n2 = random.randrange(6)
n3 = random.randrange(6)
n4 = random.randrange(6)
n5 = random.randrange(6)
numeros = (n1, n2, n3, n4, n5)
maior_valor = max(numeros)
menor_valor = min(numeros)
print (f'Os 5 numeros gerados foram: {numeros}')
print (f'O maior valor na tupla é: {maior_valor}')
print (f'O menor valor é: {menor_valor}')