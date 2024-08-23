# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

p1 = abs(float(input('Digite o preço do produto 1: ')))
p2 = abs(float(input('Digite o preço do produto 1: ')))
p3 = abs(float(input('Digite o preço do produto 1: ')))

if p1 < p2 and p1 < p3:
    menor = p1
elif p2 < p1 and p2 < p3:
    menor = p2
elif p3 < p1 and p3 < p2:
    menor = p3
else:
    menor = "iguais"

print(menor)
