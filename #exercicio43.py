#exercicio43
# função para calcular o IMC
def IMC(peso, altura):
    quadrado = float(altura) ** 2
    resultado = peso / quadrado
    return resultado


# declarei as variaveis que vão reperesentar o que op usuario colocar.
peso = float(input("Adicione o peso:"))
altura = float(input("adiocione a altura:"))

# imprimi a função
print("Seu IMC é:")
final = IMC(peso, altura)
print(final)

# usei if elif e else para decrever como o usuario está.
if final <= 16.9:
    print("Você está muito abixo do peso")
elif final >= 17 and final < 18.4:
    print("Você está abixo do peso")
elif final >= 18.5 and final < 24.9:
    print("Você está com peso normal")
elif final >= 25 and final < 29.9:
    print("Você está acima do peso")
elif final >= 30 and final < 34.9:
    print("Você está com obesidade grau 1")
elif final >= 35 and final < 40:
    print("Você está com obesidade grau 2")
else:
    print("Você está com obesidade grau 3")
