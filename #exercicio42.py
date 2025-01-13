#exercicio42
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
n3 = float(input('Digite mais um numero: '))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n2 + n1:
    print ('Esses segmentos formam um triangulo. ')
else:
    print ('Esses segmentos não formam um triangulo. ')
if n1 == n2 and n1 == n3 and n2 == n3:
    print ('Esse triangulo é EQUILATERO pois todos lados são iguais')
elif n1 == n2 and n1 != n3 or n2 == n3 and n2 != n1 or n1 == n3 and n2 != n1:
    print ('Esse triangulo é ISOSCELES pois tem umn lado diferente')
else:
    print ('Esse triangulo é ESCALENO pois tem todos os lados diferentes')