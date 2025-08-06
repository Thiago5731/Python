#exercicio107
import metade_dobro_porcentagem
#programa principal
tipo = int(input('Digite (1) para Real \nDigite (2) para Dolar\n'))
if tipo == 1:
    moeda_escolha = 'R$'
elif tipo == 2:
    moeda_escolha = 'U$'
numero = int(input('Digite um valor: '))
print(f'A metade do valor: {metade_dobro_porcentagem.moeda(numero, moeda_escolha)} é: {metade_dobro_porcentagem.moeda(metade_dobro_porcentagem.metade(numero), moeda_escolha)}')
print(f'O dobro de {metade_dobro_porcentagem.moeda(numero, moeda_escolha)} é: {metade_dobro_porcentagem.moeda(metade_dobro_porcentagem.dobro(numero), moeda_escolha)}')
print(f'10% + de {metade_dobro_porcentagem.moeda(numero, moeda_escolha)} é: {metade_dobro_porcentagem.moeda(metade_dobro_porcentagem.porcentagem(numero), moeda_escolha)}')
