#exercicio35
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
n3 = float(input('Digite mais um numero: '))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n2 + n1:
    print ('Esses segmentos formam um triangulo. ')
else:
    print ('Esses segmentos não formam um triangulo. ')