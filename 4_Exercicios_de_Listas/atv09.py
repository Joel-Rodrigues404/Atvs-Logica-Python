"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

print(sum([abs(int(input(f'digite numeros: '))) ** 2 for x in range(10)]))
# quadrados = [x**2 for x in range(10)]
# print(quadrados)