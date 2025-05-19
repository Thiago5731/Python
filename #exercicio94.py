#exercicio94
galera = list()
pessoa = dict()
soma = media = 0 
while True:
    pessoa.clear
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print ('Erro!!! (Digite M ou F)')
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print ('Digite uma opção valida!!!')
    if resp == 'n':
        break
    print ('Bye!')
print ('-='*20)
print (f'Ao todos temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print (f'A media de idade é de {media:5.2f} pessoas cadastradas')
print (f'As mulheres cadastradas foram' , end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print ('Lista das pessoas que estão encima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print ('FIM!!!!')
    