"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
vetor3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

lista = []
for x in range(10):
    lista.append(vetor1[x])
    lista.append(vetor2[x])
    lista.append(vetor3[x])

print(lista)
