#aula16
#mundo3
#tuplas
#os elementos na tuplas são identificados por indices começados de 0, se tem 4 elementos eles vão ser: 0, 1, 2, 3,
#lanche = bolo, torta, suco
# se eu colocar: print: (lanche[2]) o print vai ser suco pode ser tmb [0:2] vai mostrar só o bolo e a torta pq é mesnos 1
#lanche[1:] vai printar bolo até o final
#lanche[-1] só o ultimo elemento 
#pode utilizar len(lanche) vai mostrar quantos elemntos tem lanche
#pode usaqr for c in lanche:
#print (c)
#as tuplas são imutaveis!!!
#para começar uma variavel composta pode ser ()tupla ou []lista ou {}dicionario
lanche = ('Hamburger', 'suco', 'pizza', 'pudim')
print (lanche)
print (lanche[1])
print (lanche[-2])
print (lanche[1:3])
print (lanche[2:])
print (lanche[:2])

print ('+++'*10)

for comida in lanche:
    print (f'Eu vou comer {comida}')
print ('+++'*10)

for cont in range(0, len(lanche)):
    print (f'Eu vou comer {lanche[cont]} na posição {cont}')

print ('+++'*10)
for pos, comida in enumerate(lanche):
    print (f'Eu vou comer {comida} na posição {pos}')

print ('+++'*10)
print ('Comi muito! ')
print ('+++'*10)

print (sorted(lanche)) #PARA COLOCAR EM ORDEM ALFABETICA. Mas é importante lkembrar que ele não muda e sim só o print 

a = (2, 5, 5)
b = (5, 8, 1, 2)
c = a + b
print (c)
print (c.count(5)) #mostra qunatas vezes aparece o numero 5 
print (c.index(8)) #em quer posição está o 8
#del(c) apaga a variavel c 
#tmb posso fazer tuplas com varios caracteres int, str, bol, float...