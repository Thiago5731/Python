#exercicio100
import random
numeros = []
valoresPares = []

#funções
#função que sorteia 5 numeros e coloca eles dentro da lista
def sorteia():
    for c in range(0, 5):
        numeros.append(random.randrange(0, 9))

#função que separa os valores pares e soma.
def somaPar(numeros):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0: 
            valoresPares = valor
            soma += valoresPares
            print('Valores pares:')
            print (f'{valoresPares}')
    print (f'A soma dos valores pares deu: {soma}')

sorteia()
print(f'Os numeros sorteados foram: {numeros}')
somaPar(numeros)


