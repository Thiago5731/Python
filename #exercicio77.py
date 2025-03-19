#exercicio77
tupla = (str(input('Digite uma palavra: ')), str(input('Digite uma palavra: ')), str(input('Digite uma palavra: ')), str(input('Digite uma palavra: ')) )
for palavra in tupla:
    print (f'\nNa palavra {palavra.upper()} temos', end=' ')
    for letra in palavra: 
        if letra.lower() in 'aeiou':
            print (letra, end=' ')