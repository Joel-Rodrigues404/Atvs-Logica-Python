"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

print(sum([abs(int(input("digite numeros: "))) ** 2 for x in range(10)]))
