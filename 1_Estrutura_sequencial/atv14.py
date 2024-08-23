"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

tempF = (int(input('digite a temperatura em fahrenheit: ')))

tempC = 5 * ((tempF - 32) / 9)

print(f'A temperatura {tempC:.1f}C°')
