"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""


lista = list()
a = ''
for x in range(10):
    algo = input("ditite letras: ")
    a += algo
    if len(a) >= 10:
        break

a = a[:10]
conc = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']

for x in a:
    if x in conc:
        lista.append(x)

print(f'As concoantes são {lista}')