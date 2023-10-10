"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

num = abs(int(input("digite num: ")))

ant = num - 1
soma = num * ant
cont = num
while cont > 0:
    soma += soma * (ant - 1)
    ant -= 1
    cont -= 1
    
    
print(soma)