#exercicio97
#contadores
cont = 0


#função de titulo
def titulo(msg):
    tamanho = len(msg) + 4
    print('-'*tamanho)
    print(f'  {msg}')
    print('-'*tamanho)


#programa principal: 
print ('Os titulos selecionados foram: ')
#no programa do guanabara ele deixou os titulos prontos mas eu preferi deixar para escrever na hora. 
#entretanto o resultado sai duplicado pq ele mostra oq eu escrevi depois o def 
for c in range (0, 3):
    cont += 1
    titulo(str(input(f'Digite o {cont}° titulo: ')))