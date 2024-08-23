"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

maior = float("-inf")
menor = float("inf")
soma = 0
while True:
    n = abs(int(input("digite um numero [0 para parar]: ")))
    soma += n
    if n == 0:
        break
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n

print(f"Maior {maior} menor {menor} soma {soma}")
