#exercicio63
valor = int(input('Digite quantos termos você quer que apareça: '))
loop = 0
sequencia = 0
sequencia2 = 1
while loop <= valor:
    loop += 1
    sequencia3 = sequencia2 + sequencia
    sequencia = sequencia2
    sequencia2 = sequencia3
    print (sequencia3)
