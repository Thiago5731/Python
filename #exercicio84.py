#exercicio84
c = 0
cont = 0 
pessoa = [] 
lista = []
mai = men = 0 
while c == 0:
    pessoa.append(str(input('Digite o nome da pessoa: ')))
    pessoa.append(float(input('Digte o peso: ')))
    lista.append(pessoa[:])
    #verificar se é maior ou menor
    if len(lista) == 0:
        mai = men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
        if pessoa[1] < men:
            men = pessoa[1]
    #serve para limpar a lista a cada loop.
    pessoa.clear()
    cont += 1
    validar = str(input('Você quer continuar? [S/N]')).upper().strip()
    if validar == 'N': 
        c += 1
print (f'Os dados são: {lista}')
pess_cadas = cont
print (f'O total de pessoas cadastradas é: {pess_cadas}')
print (f'O maior peso foi de: {mai}')
print (f'O menor peso foi de: {men}')