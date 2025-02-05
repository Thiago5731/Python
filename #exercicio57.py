#exercicio57
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual seu sexo? (M)para masculino e (F)para feminino: ')).upper()[0].strip()
    print ('Digite um valor correspondente!!')
if sexo == 'M':
    print ('Você selecionou Masculino')
else: 
    print ('Você selecionou Feminino')