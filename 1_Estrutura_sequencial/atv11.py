"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""

raio = abs(float(input("digite o raio do circulo: ")))

area_circulo = (3.14 * raio) ** 2

print(f'print com o raio de {raio}cm tem area igual a {area_circulo:.2f}cm²')
