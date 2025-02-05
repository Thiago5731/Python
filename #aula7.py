# operadores aritimeticos
# + adição
# - subtração
# * multiplicação
# / divisão
# ** potencia 
# // divisão inteira (não coloco o resto e não coloco virgula para terminar a divisão, 5//2 = 2)
# % resto da divisão
# == sinal de igualdade é diferente de = que é um valor de atribuição. 
#pow(4,3) isso é = a 4**3
#ordem de execulsão
#1 ()
#2 **
#3 *, /, //, %  
#4 +, -
#para quebrar linah \n
#para juntar linha end ''
#exemplo:
#num = float(8.90892374)
#print(f'o valor é: {num:.2f}') 
#o valor imprimido vai ser 8.91 pois o :.2f faz com que eu imprima apenas duas casa decimais depois da virgula

#desafio 5
n1 = int(input('Digite um numero: '))
sub = int((n1 - 1))
som = int((n1 + 1))

print ('O antecessor desse numero é: {} O numero escolhido é: {} O sucessor desse numero é: {}' .format(sub, n1, som))

#desafio 6
n2 = int(input('Digite um numero: '))
dob = int(n2 * 2)
tri = int(n2 * 3)
raiz = float(n2 * (1/2))
print ('Numero: {} Dobro: {} Triplo {} Raiz quadrada {}' .format(n2, dob, tri, raiz))

#desafio 7 
n3 = float(input('Digite a primeira nota: '))
n4 = float(input('Digite a segunda nota: '))
media = float((n3 + n4)/2)
print ('A media é: {}' .format(media))

#desafio 8
valorm = float(input('Digite um valor em metros'))
centi = float(valorm * 100)
mili = float(valorm * 1000)
print (f'O valor escolhido em metros foi:{valorm} O valor em centimetros é: {centi} e em milimetros é: {mili}')

#desafio 9 

tabu = int(input('Digite um numero inteiro para ver sua tabuada.'))
tabu2 = int(tabu * 1)
tabu3 = int(tabu * 2)
tabu4 = int(tabu * 3)
tabu5 = int(tabu * 4)
tabu6 = int(tabu * 5)
tabu7 = int(tabu * 6)
tabu8 = int(tabu * 7)
tabu9 = int(tabu * 8)
tabu10 = int(tabu * 9)
tabu11 = int(tabu * 10)
print (f'A tabuada de: {tabu} é: \n{tabu2} \n{tabu3} \n{tabu4} \n{tabu5} \n{tabu6} \n{tabu7} \n{tabu8} \n{tabu9} \n{tabu10} \n{tabu11}')

#desafio10
reais = float(input('Quantos reais você tem? '))
buy = float(reais // 3.27)

print ('Você pode comprar: {} dolares'.format(buy))

#exercicio05

num01 = int(input('Digite um numero inteiro: '))
m1 = int(num01 - 1)
m2 = int(num01 + 1)
print (f'seu numero é: {num01} o antecessor dele é: {m1} e o sucessor dele é: {m2}')

#exercicio06

mum01 = int(input('Digite um numero: '))
e1 = int(mum01 * 2)
e2 = int(mum01 * 3)
e3 = int(mum01 ** (1/2))
print (f'O numero escolhido foi: {mum01} \n O seu dovro é: {e1} \n Seu triplo é {e2} \n e sua raiz quadrada é {e3}')

