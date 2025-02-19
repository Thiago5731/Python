#exercicio70
print ('==='*10)
print ('       Uai supermercado!')
print ('==='*10)
produto = ''
continua = ''
valor = cont = soma = mata = mais = menor = 0
barato =''
while True:
    if mata == 1:
        break
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: '))
    if valor > 1000:
        mais += 1
    cont += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    soma += valor
    while continua is not 'S' or 'N':
        continua = str(input('Você quer continuar? [S/N]: ')).upper()[0].strip()
        if continua == 'S':
            break
        else: 
            mata = 1
            break
print ('==='*10)
print(f'O total da compra foi: {soma}')
print(f'A quantidade de produtos que valem mais de 1000 reais é: {mais}')
print(f'O produto mais barato é: {barato} e o preço é: {menor} ')
print ('==='*10)