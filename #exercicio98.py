#exercicio98
from time import sleep
#função de contador
def contador(msg, msg2, msg3):
    print (f'Contagem de {msg} até {msg2} de {msg3} em {msg3}')
    if msg3 <0:
        msg3 *= -1
    if msg3 == 0:
        msg3 = 1
    if msg < msg2:
        cont = msg
        while cont <= msg2:
            print (f'{cont}', end='', flush=True)
            #sleep(0,5)
            cont += msg3
        print('FIM!')
    else: 
        cont = msg
        while cont >= msg2:
            print (f'{cont}', end='', flush=True)
            #sleep(0,5)
        print ('FIm!')

#programa principal
contador(1, 10, 1)
print('Sua vez de personalizar a contagem')
ini = int(input('inicio: '))
fim = int(input('fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)