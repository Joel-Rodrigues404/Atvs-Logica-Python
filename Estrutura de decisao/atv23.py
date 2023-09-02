"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: 
utilize uma função de arredondamento.
"""

num = float(input("digite um numero: "))

print(num)

if num.is_integer():
    print('inteiro')
elif not num.is_integer():
    print('decimal')
else:
    print('erro')