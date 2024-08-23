"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""

num_notas = abs(int(input("digite o numero de notas: ")))

soma = 0
for x in range(num_notas):
    notas = abs(float(input("digite as notas: ")))
    soma += notas


media = soma / num_notas
print(media)
