#exercicio105
def notas(*n, sit=False):
    """
    ---> funjção para analisar notas e situações dos alunos
    :param n: uma ou mais notas dos alunos
    :param sit: valor indicando que deve ou não indicar uma situação
    :return: dicionario com varias informações sober situação da turma. 
    """
    r = dict()
    r ['total'] = len(n)
    r ['maior'] = max(n)
    r ['menor'] = min(n)
    r ['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Rasoavel'
        else:
            r['situação'] = 'Ruim'
    return r


#prigaram principal 
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)