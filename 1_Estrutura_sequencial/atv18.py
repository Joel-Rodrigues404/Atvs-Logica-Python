# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = str(input("Digite seu sexo [M/F]: "))
altura = abs(float(input("digite sua altura metros: ")))

if "Mm" in sexo:
    peso_ideal_M = (72.7 * altura) - 58
    print(peso_ideal_M)
elif "Ff" in sexo:
    peso_ideal_F = (62.1 * altura) - 44.7
    print(peso_ideal_F)
else:
    print('Digite uma resposta entre [M/F] para a resposta do sexo')
