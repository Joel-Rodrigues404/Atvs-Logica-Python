"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio 
gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um
"""

soma = 0

qtde_cd = abs(int(input("digite a quantidades de cds na sua coleção: ")))

for x in range(qtde_cd):
    valor_cd = abs(int(input("digite o valor de cada cd em ordem: ")))
    soma += valor_cd

media = soma / qtde_cd

print(f"A media do valor de cada cd é {media}\nE o total investido foi {soma}")
