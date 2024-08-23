"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

lista = list()
for x in range(10):
    num = float(input("digite um num: "))
    lista.append(num)


print(lista[::-1])
