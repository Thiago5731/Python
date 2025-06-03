#aula20
def lin():
    print('-'*30)

lin()
print('opa')
lin()

#posso trabalhar com parametros 
def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)

mensagem('sistema de alunos')

#tem que manter duas linhas de espaço entre def e  outro def ou outra coisa no programa principal
def soma(a, b):
    s = a+b
    print(s)


#programa ptrincipal
soma(4, 5)
soma(8, 9)
soma(2, 1)
#se passar so um parametro buga e naum passa 


#da para especificar o parametro dentro do def, colocando por exemplo a=4 + b=4 ou trocar eles de ordem 

#empacotar parametros
#empacotamento
#na hora de declarar função a gente passa vaores expecificos igual no caso anterior, se passei 2 é 2 se eu botar 3 da erro. 
#mas com o empacotador 
#posso faert 
def contador(*num):
    print (num)

contador (1, 3, 5)
contador (1)
#ele fez uma tupla 


#podemos fazer com lista tmb 
def dobra(lst):
    pos = 0 
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

        
valores = [1, 5, 7, 9, 0]
dobra(valores)
print(valores)