#aula22
#modularização
#basicamente dividir problemas grandes em pequenos problemas

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f*=c
    return f


num = int(input('Digite um numero: '))
fat=fatorial(num)
print(f'O fatorial de {num} é {fat}')

#a principal ideia de modularização é separar as funções me modulos e chamar 
#em bibliotecas

#import *nome_do_arquivo*
#isso é para importar meus modulos
#se no caso acima a função é fatorial a variavel teria que ser:
#nome_do_arquivo.fatorial
#também poderia usar: from nome_do_arquivo import fatorial
#isso são modulos 

#ag vamos para pacotes/bibliotecas
#funções ficam dentro de modulos e modulos ficam dentro de pacotes seprados por assuntos
#posso fazer importação de pacotes 
#import pacote 
#iguais o gerenciador de pacotes do windows 
#__init__.py tem que ter esse arquivo dentro de cada pasta
#a pasta principal tem que ter e as pastasa dentro dela tmb 
#from pacote import modulo