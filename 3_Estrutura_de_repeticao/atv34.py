"""
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro 
e determine se ele é ou não um número primo.
"""

num = abs(int(input("digite um numero: ")))

cont = 1
divisores = 0
while cont <= num:
    if num % cont == 0:
        divisores += 1
    cont += 1

if divisores == 2:
    print(f"O numero {num} e primo!")
