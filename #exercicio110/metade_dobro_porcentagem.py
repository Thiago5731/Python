#metade_dobro_porcentagem

#metade
def metade(numero):
    resultado = numero/2
    return resultado


#dobro
def dobro(numero):
    resultado = numero*2
    return resultado


#porcentagem_aumentado em 10%
def porcentagem(numero):
    dez = numero/10
    resultado = dez + numero
    return resultado


#moeda
def moeda(numero = 0, moeda = 'R$'):
    return f'{moeda}{numero}'. replace('.', ',')