"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

lista = list()
for x in range(4):
    num = abs(int(input("digite o num: ")))
    lista.append(num)

print(f'As notas são')
for x in lista:
    print(f'{x}', end=', ')

print(f'A media eh {(sum(lista)) / 4}')