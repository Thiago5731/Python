#aula18
#listas parte 2 
#posso juntar uma lista dentro da outra com .append()
#exemplo: 
grupao = []
lista1 = ['joão', '25']
lista2 = ['jose', '26']
lista3 = ['Maria', '29']

grupao.append(lista1[:])
print (grupao)
grupao.append(lista2[:])
print (grupao)
grupao.append(lista3[:])
print (grupao)

#tambem da para declarar tudo de uma vez, assim: 
#pessoas = [['joão', '25'], ['jose', '26'], ['Maria', '29']]

#printa joao
print (grupao[0][0])
#printa 26 
print (grupao[1][1])
# por ai vai. tmb posso printar só [1] etc 
#caso eu queira fazer uam copia. tenhoq ue deixar o [:] no final, se naum vai ter uma ligação entre as duas ai se alterar uma altera a outra. 

#exemplos
galera = list()
#mesma coisa de fazer = galera =[]
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear
print (dado)