"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o 
fatorial a números inteiros positivos e menores que 16.
"""

while True:
    n = abs(int(input("\ndigite o enesimo termo: ")))
    if n < 0:
        break
    elif n > 16:
        break
    num1 = 0
    num2 = 1
    num3 = 0
    print(f"{num1} {num2}", end=" ")
    for x in range(n):
        num3 = num1 + num2
        num1 = num2
        num2 = num3

        print(f"{num3}", end=" ")
