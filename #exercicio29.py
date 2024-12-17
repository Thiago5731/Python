#exercicio29
#velocidade limite é 80km/h se for maior que isso cada km é = 7 reais 
velo = int(input('Qual velocidade seu carro estava? '))
sub = int(velo - 80)
veri = float(sub * 7)
if sub <= 0:
    print ('Você está em velocidade adequada!')
else:
    print (f'Você está fora do limite permitido pela via. Sua multa é de: {veri}R$')