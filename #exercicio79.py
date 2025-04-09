#exercicio79
#usei set() aqui pois assim ele criou um conjunto retirando os duplicados e depois usei list() para converter para uma lista de novo
lista = []
cont = 0 
while cont == 0:
    lista.append(int(input('Digite um numero: ')))
    parar = str(input('Você quer parar? [S/N]')).upper().strip()
    if parar == 'S':
        cont += 1 
    print (f'sua lista está assim: {lista}')
#aqui está o set() que eu comentei.
#como fiz assim ele já colocou em ordem. eu tentei utilizar o .sort para organizar mas dava erro. 
list_sem_repetidos = list(set(lista))
print ('-' * 38)
print (f'A sua lista ficou assim: \n {list_sem_repetidos} \nEstá sem os repetido e em ordem :)')
print ('-' * 38)