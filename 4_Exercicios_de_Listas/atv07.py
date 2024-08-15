"""
    Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

lista = list()

for x in range(5):
    num = abs(int(input("digite um numero: ")))
    lista.append(num)

soma_mult = 1
for x in lista:
    soma_mult = soma_mult * x

print(f'A soma e: {sum(lista)} \nA multiplicação e {soma_mult} \nOs numeros foram {[x for x in lista]}')
