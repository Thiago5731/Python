#exercicio64
soma = 0
inteiro = 0
outro = 0
while inteiro != 999:
    inteiro = int(input('Digite um numero inteiro ou 999 para sair: '))
    soma += inteiro
    outro += 1
total = soma - 999
quantidade = outro - 1
print (f'A soma foi: {total}')
print (f'A quantidade de numeros digitada foi: {quantidade} ')