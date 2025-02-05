#exercicio56
somaidade = 0
idadeh = 0
velho = ''
mulher = 0
print ('Digite o nome a idade e o sexo de 4 pessoas: ')
for v in range(1, 5):
    nome = str(input('Digite um nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite M/m para Mulher ou H/h para Homem: '))
    if v == 1 and sexo in 'Hh':
        idadeh = idade
        velho = nome
    if sexo in 'Hh' and idadeh < idade:
        idadeh = idade
        velho = nome
    if sexo in 'Mn' and idade < 20:
        mulher += 1
    somaidade += idade
media = somaidade / 4
print (f'A media das idades é: {media}')
print (f'As quantidade de mulheres com menos de 20 anos é: {mulher}')
print (f'O homem mais velho é: {velho} com idade {idadeh}')
