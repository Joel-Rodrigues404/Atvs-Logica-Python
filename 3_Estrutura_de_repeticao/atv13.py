"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo 
número. Não utilize a função de potência da linguagem.
"""

base = abs(int(input("digite a base: ")))
expo = abs(int(input("digite o expoente: ")))

aux = 1
for x in range(1, expo + 1):
    aux *= base

print(aux)
    

