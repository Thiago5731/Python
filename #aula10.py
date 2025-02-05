'''nome = str(input('Qual seu nome? '))
if nome == 'Thiago': 
    print ('Seu nome é lindo seu gostoso! ')
else:
    print ('Seu nome é legal! ')'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
soma = float(nota1 + nota2 + nota3)
media = float(soma / 3)

if media >= 15:
    print ('O aluno foi aprovado !!!')
else:
    print ('O aluno não foi aprovado :(')
