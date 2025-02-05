#modulos
#acho que vai ter bibliotecas e importações
#comando import é oq usamos para importar as bibliotecas
#ao invez de importar a biblioteca toda eu posso importar uma coisa só
#exemplo: tenhoo uma biblioteca que chama doce, ela tem bolo, torta e pão
#se eu colocar import doce vai importar tudo da biblioteca doce
#mas eu posso colocar from doce import bolo, assim eu importo só o bolo, se colocar virgula deposi de bolo e add outra vc pode adicionar bolo, pao tmb
#biblioteca math dentro dela tem as funcionalidades(ceil(arredonda para cima) floor(arredonda para baixo))
#(trunc (elimina sem arredondar) pow(potencia) sqrt(raiz quadrada) factorial(fatorial))

#importando a bibliotaca
'''import math
numero = int(input('digite um numero:'))
raiz = (math.sqrt(numero))
print (f'A raiz quadrade de {numero} é: {raiz}')'''

#importando da biblioteca
'''from math import sqrt
numero = int(input('digite um numero'))
raiz = sqrt(numero)
print (f'A raiz quadrade de {numero} é {raiz}')'''

#desafio 1
'''from math import trunc
numero = float(input('Digite um numero quebrado: '))
inteiro = (trunc(numero))
print (f'O numero: {numero} apenas na parte inteira é: {inteiro}')'''

#desafio 2
'''import math
grau = float(input('Digite um numero: '))

coss = math.cos(math.radians(grau))
seno = math.sin(math.radians(grau))
tang = math.tan(math.radians(grau))

print (f'O valor de cosseno é {coss} de seno: {seno} e da tangente é {tang}')'''

#desafio19
'''import random
n1 = str(input("Digite uma palavra: "))
n2 = str(input("Digite uma palavra: "))
n3 = str(input("Digite uma palavra: "))
n4 = str(input("Digite uma palavra: "))
list = [n1, n2, n3, n4]
sorte = random.choice(list)
print (f'A palavra escolhida foi: {sorte}')'''

#desafio 20
import random
n1 = str(input("Digite uma palvra: "))
n2 = str(input("Digite uma palavra: "))
n3 = str(input("Digite uma palavra: "))
n4 = str(input("Digite uma palavra: "))
list = [n1, n2, n3, n4]
sorte = random.shuffle(list)
print (f'A nova ordem da lista será: {list}')
