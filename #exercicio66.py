#exercicio66
numero = soma = contador = 0
while True:
    numero = int(input('Digite um numero e digite (999) para parar: '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print (f'Você digitou {contador} valores e a soma dos numeros digitados é: {soma}')