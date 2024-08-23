"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

num = abs(int(input("Digite um numero: ")))

cont = 0
for x in range(1, num + 1):
    if num % x == 0:
        cont += 1

if cont == 2:
    print("Primo")
