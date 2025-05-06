#aula19
#dicionarios
#basicamente dicionarios são listas com nomes declarados por mim. 
#dicionarios são identificados por {}
#posso usar dados = dict() ou dados = {}
dados = {'nome':'Pedro', 'idade':25}
#nesse caso eu ja criei o nome e o indice
print (dados['nome']) #vou printar pedro, 
#eu também posso misturar isso com listas colocando dicionarios dentro de listas
#aqui não tem append mas para add eu teria que colcoar assim: 
dados['sexo']='Masculino'
del dados['idade'] #apaga idade

filme = {'titulo':'star wars', 
        'ano': 1977,
        'diretor': 'George Lucas'}
filme2 = {'titulo':'matrix'}
print(filme.values()) #vou imprimir somente os valores
print(filme.keys()) #vou imprimir somente as chaves
print(filme.items()) #vou imprimir os dois

for k, v in filme.items():
    print(f'O {k} é {v}')

locadora = [[filme], [filme2] ] #não pensei em mais filmes mas aqui seria uma lista com variosa dicionariso dentros
print(locadora[0]['titulo']) #vou imprimir starwars

pessoas = {'nome':'Thiago', 'sexo':'M', 'idade':  20}
print (f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #tenhoque usar aspas duplas pois já usei aspas simples
