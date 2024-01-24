"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
lista = list()
for x in range(5):
    num = abs(int(input("digite um numero: ")))
    lista.append(num)

print(lista)