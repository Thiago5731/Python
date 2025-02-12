#aula15
#break 
#exemplo de loop infinito
'''cont = 1
while True:
    cont += 1
    print (cont)'''

numero = soma = 0 
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    soma += numero
print (soma)
# o comando break quebra isso
#exemplo:


