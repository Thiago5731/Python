#gerador de senhas
#importa a biblioteca para randomizar e importa os alfabetos
import random
import string
#faz uma lista coma variavel senha
senha = list()
#variavel vazia. Nem sei para que to usando isso mais
senhapronta = ''
#importa os alfabetos e junta eles
alfabeto_Mai = string.ascii_lowercase
alfabeto_min = string.ascii_uppercase
alfabeto_comp = alfabeto_min + alfabeto_Mai
#faz uma seleção para o usuario (tamanho da senha)
selecao = int(input('Qual o tamanho da sua senha? '))
#faz um loop com o tamnhao selecionado
for c in range(0, selecao):
    numeros = random.randrange(0, 9)
    letras = random.choice(alfabeto_comp)
    senha.append(letras)
    senha.append(str(numeros))
    senha[:]
#mostra a senha 
senhapronta = ''.join(senha[:selecao])
print (senhapronta)
#senhapronta.join(senha)
#print (senhapronta)
