"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

num = abs(int(input("digite num: ")))

cont = num
aux = num - 1
while cont > 0:
    if aux == 0:
        aux = 1
    num *= (aux)
    cont -= 1
    aux -= 1

    
    
print(num)