#exercicio89
ficha = []
c = 0
while c == 0:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    pergunta = str(input('Você quer continuar? [S/N]')).upper().strip()
    if pergunta == 'N':
        c += 1 
print (f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(ficha):
    print (f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Você quer ver a nota de qual aluno? (999 interrompe): '))
    if opc == 999: 
        print ('Finalizndo')
        break
    if opc <= len(ficha) -1:
        print (f'Notas de {ficha[opc] [0]} são {ficha[opc] [1]}')
