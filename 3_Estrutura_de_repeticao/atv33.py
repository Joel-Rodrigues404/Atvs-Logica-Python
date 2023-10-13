"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto 
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das 
temperaturas.
"""

cont = 0
soma = 0
menor = float('inf')
maior = float('-inf')
while True:
    temp = float(input("digite as temperaturas [10000] para parar: "))
    if temp == 10000:
        break
    if temp < menor:
        menor = temp
    elif temp > maior:
        maior = temp
    cont += 1
    soma += temp



media = soma/cont
print(f'Maior {maior} menor {menor} media {media}')


