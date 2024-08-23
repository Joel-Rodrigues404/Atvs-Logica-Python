"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.
"""

num1 = 0
num2 = 1
num3 = 0
print(f"{num1} {num2}", end=" ")
while num3 < 500:
    num3 = num1 + num2
    num1 = num2
    num2 = num3

    print(f"{num3}", end=" ")
