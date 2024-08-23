"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento 
de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que 
calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população 
do país B, mantidas as taxas de crescimento.
"""

city_A = 80000
city_B = 200000

cont = 0
while city_A < city_B:
    city_A += (city_A) * (3 / 100)
    city_B += (city_B) * (1.5 / 100)
    cont += 1

print(f"{city_B}, {city_A}, {cont}")
