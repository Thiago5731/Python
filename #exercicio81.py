#exercicio81
c = 0
lista = []
cont = 0
while c == 0:
    lista.append(int(input('Digite um nuemero: ')))
    cont += 1
    pergunta = str(input('Você quer continuar?[S/N] ')).upper().strip()
    if pergunta == 'N':
        c += 1
print ('-'*38)
print (f'Foram digitados: {cont} numeros.')
lista.sort(reverse=True)
print (f'sua lista em ordem decrescente ficou assim: {lista}')
if 5 in lista:
    print ('O valor 5 está presente na lista! ')
else: 
    print ('Infelizmente não encontrei o valor 5')
    
