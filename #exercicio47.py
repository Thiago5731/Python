#exercicio47

for lista in range (1,50 + 1):
    #print('.')
    #tire a # da linha de cima para testar. 
    par = lista % 2
    if par == 0:
        print (f'Os numeros são: {lista}')
print ('Fim do programa!')

#posso tirar a variavel par e fazer só lista % 2 tmb da certo
#esse programa ta muito pesado pois ele ta fazendo varios loops para perceber isso basta imprimir um ponto na fente que vc verá
#segue outra maneira de resolver sem gastar tanta memoria. 

#51 é basicamente a mesam coisa que 5+1 e aqui eu começei no 2 pq já é um par entt eu tiro o 1 que é um loop atoa
#O dois ali é para pular de 2 em 2 
for lista1 in range (2, 51, 2):
    #print('.')
    #tire a # da linha de cima para testar. 
    print (f'{lista1}')
print ('fim')