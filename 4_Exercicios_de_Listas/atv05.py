"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os 
números IMPARES no vetor impar. Imprima os três vetores.
"""

pares = list()
impares = list()
numeros = list()

for x in range(20):
    num = abs(int(input("digite um num: ")))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(numeros)
print(pares)
print(impares)
