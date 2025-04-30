#exercicio87
matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = mai = colu = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha] [coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))  
        print('--'*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print (f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha] [coluna] % 2 == 0:
            par += matriz[linha] [coluna]
    print()
print('--'*30)
print (f'A soma dos pares é {par}')
for linha in range(0,3):
    colu += matriz[linha] [coluna]
print (f'A soma dos valores da terceira coluna é {coluna}')
for coluna in range(0,3):
    mai = matriz[1] [coluna]
    if coluna == 0:
        mai = matriz[1] [coluna]
    elif matriz[1] [coluna] > mai:
        mai = matriz[1] [coluna]
print (f'O maior valor da segunda linha é {mai}')