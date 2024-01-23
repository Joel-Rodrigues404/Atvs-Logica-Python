"""
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
"""

num = abs(int(input('digite um numero: ')))

num = str(num)

for x in range(len(num) - 1, -1, -1):
    print(num[x], end='')