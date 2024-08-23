"""
Altere o programa anterior para mostrar no final a soma dos números.
"""

num1 = abs(int(input("digite num1: ")))
num2 = abs(int(input("digite num2: ")))

soma = 0
for x in range(num1, num2):
    print(x)
    soma += x

print(soma)
