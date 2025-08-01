#exercicio104
def leia_int(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um numero valido.\033[m')
        if ok:
            break
    return valor
    


#programa principal
n = leia_int('Digite um numero: ')
print (f'Você acabou de digitar o numero: {n}')