"""
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
"""

num = abs(int(input("Digite um numero: ")))

cont = 0
lista = []
for x in range(1, num + 1):
    if num % x == 0:
        cont += 1
        lista.append(x)

if cont == 2:
    print("Primo")
else:
    print(", ".join(map(str, lista)))
