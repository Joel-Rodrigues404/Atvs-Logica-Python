"""
Faça um programa que leia 5 números e informe o maior número.
"""
maior = 0
for x in range(5):
    num = abs(int(input("digite um num: ")))
    if num > maior:
        maior = num

print(maior)