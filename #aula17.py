#aula17
#listas ao invés de parenteses é couchetes []
#se eu fizer: variavel[3] = outra coisa. Eu posso subistituir. 
#adidionar mais coisas na lista = lanche.append('coisa para add')
#add em uma posição especifica = lanche.insert(0'item')
#apagar alguma coisa = del lanche[3] ou lanche.pop(3)(normalmente usado para o ultimo item) lache.remove('item')(para remover pelo nome ou obj)
#lanche.pop()elimina o ultimo elemento
#para remover algo que não existe vai ter um erro 
#para verificar. Posso fazer: if 'pizza' in lanche e depois usar lanche.remove('pizza')
#posso declarar uma lista apartir de um range
#valores = list(range(4,11))
#.sort() ordena os valores já a ordem inversa fica .sort(reverse=True)
#len() mostra quando elementos tem na lista. 
lanche = ['pão', 'pizza', 'suco', 'maçã']
print (lanche)
lanche[3] = 'pepino'
print (lanche)
lanche.append('yogurte')
print (lanche)
del lanche[0]
print (lanche)
if 'pepino' in lanche:
    lanche.remove('pepino')
else: 
    print('Não achei nada para remover')
print (lanche)

valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)
for cont in range(0, 5):
    valores.append(int(input('Digite os valores: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print ('Cheguei ao final da lista')

#quando uma lista é igual a outra, se eu alterar o valode e uma das listas em uma posição, ele tamb altera na outra, exemplo:
a = [1, 2, 3, 5]
b = a 
b[2] = 8
print (a)
print (b)
#para fazer uma copia. O certo seria: 
a1 = [1, 2, 4, 7, 5]
b1= a1[:]
b1[2] = 8

print(a1)
print(b1)

#assim eu fatio a str