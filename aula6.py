n1 = int(input('digite um numero'))
n2 = int(input('digite outro numero'))
s = (n1 + n2)
print ('A soma entre {} + {} vale {}'.format(n1, n2, s))

#exercicio 3

nn1 =int(input('Digite um numero: '))
nn2 =int(input('Digite outro numero: '))
r = nn1 +nn2
print ('a soma entre: {} e {} é igual a: {} !'.format(nn1 ,nn2, r))

#exercicio 4
escrita = input('Digite alguma coisa:' )
a = type(escrita)
print ('O tipo primitivo de {} é {}'.format(escrita, a))

#importante falar sobre o .is que pode ser varias coisas exeplo: .isspace ou .isalnum, na frente
#do ponto deve vir a variavel em questão

print ('só tem espaços?', escrita.isspace())
print ('só tem numeros?', escrita.isnumeric())
print ('Tem numeros e letras? ', escrita.isalnum())
print ('Só tem letras?', escrita.isalpha())