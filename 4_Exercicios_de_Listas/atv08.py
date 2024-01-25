"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

idades, alturas = [abs(float(input("digite a idade: "))) for x in range(5)], [abs(float(input("digite a altura: "))) for y in range(5)]

