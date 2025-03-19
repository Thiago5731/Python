#exercicio76
tupla = ('café', 25.50, 'chocolate', 5.75, 'biscoito', 3.50, 'pão', 8.63)
print ('-'*18)
print ('LISTAGEM DE PREÇOS')
print ('-'*18)
for pos in range(0, len(tupla)): 
    if pos % 2 == 0:
        print (f'{tupla[pos]:.<30}', end='')
    else:
        print (f'R${tupla[pos]:<30}')