"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""

num1 = abs(int(input("digite num1: ")))
num2 = abs(int(input("digite num2: ")))

for x in range(num1, num2):
    print(x)
