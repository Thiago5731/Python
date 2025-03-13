#exercicio72
numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
contador = 0
while True:
    valor = int(input('Digite um numero entre 0 e 10: '))
    print (f'O valor digitado por extenso é: {numero[valor]}')
    parada = str(input('Você quer parar? [S/N]: ')).upper()[0].strip()
    if parada == 'N':
        print ('Acabou!')
        break
