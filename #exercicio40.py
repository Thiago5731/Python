#exercicio40
nota1 = float(input('Digite a primeira nota (entre 0 e 10): '))
nota2 = float(input('Digite a segunda nota (entre 0 e 10): '))
media = (nota1 + nota2) / 2
print (f'A media do aluno é: {media}')
if media < 5.0:
    print ('REPROVADO pois sua media é menor que 5')
elif media >= 5.0 and media <= 6.9:
    print ('RECUPERAÇÃO pois sua nota está entre 5.0 e 6.9')
else:
    print ('PASSOU pois sua nota é maior que 7.0')