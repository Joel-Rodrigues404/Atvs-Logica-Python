""" 
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem 
ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

lado1 = abs(float(input("lado1: ")))
lado2 = abs(float(input("lado2: ")))
lado3 = abs(float(input("lado3: ")))

# if lado3 > abs(lado1 - lado2) and lado3 < (lado1 + lado2):
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("triangulo")
    if lado2 == lado1 and lado2 == lado3:
        print("Equilatero")
    elif lado1 != lado2 and lado1 != lado3 and lado3 != lado2:
        print("Escaleno")
    else:
        print("Isoceles")
else:
    print("Não e triangulo")