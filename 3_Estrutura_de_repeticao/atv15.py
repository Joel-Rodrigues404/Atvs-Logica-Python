"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n-ésimo termo.
"""


n = abs(int(input("digite o enesimo termo: ")))

num1 = 0
num2 = 1
num3 = 0 
print(f'{num1} {num2}', end=' ')
for x in range(n):
    num3 = num1 + num2
    num1 = num2
    num2 = num3

    print(f'{num3}', end=' ')
