"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

rep = 5
soma = 0
for x in range(rep):
    print(x)
    num = abs(int(input("digite um num: ")))
    soma += num

media = soma / rep
    
print(f'A media eh {media}')