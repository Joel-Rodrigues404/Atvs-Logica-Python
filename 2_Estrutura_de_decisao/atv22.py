"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica:
 utilize o operador módulo (resto da divisão).
"""

num = abs(int(input("digite um numero: ")))

if num % 2 == 0:
    print(f'O numero {num} e par')
elif num % 2 != 0:
    print(f'O numero {num} e impar')
else:
    print('erro')
