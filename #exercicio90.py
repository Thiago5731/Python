#exercicio90
dados = {}
dados['nome'] = str(input('Digite o nome do aluno: '))
dados['nota'] = float(input('Digite media do aluno (0/10): '))
if dados['nota'] < 7: 
    print (f'O aluno {dados["nome"]} foi reprovado!')
else: 
    print (f'Parabens! o aluno {dados["nome"]} foi aprovado!!!')