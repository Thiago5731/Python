#exercicio60
soma = 0
fatorial = 1
numero = int(input('Passe um numero: '))
while numero > soma:
    soma += 1
    fatorial *= soma
print (f'{soma} e {fatorial}')