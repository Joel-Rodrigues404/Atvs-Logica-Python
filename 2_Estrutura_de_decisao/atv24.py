""" 
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

num1 = float(input("num1: "))
num2 = float(input("num2: "))

operacao = abs(int(input("""
Escolha a operacão
[1] Adição
[2] Subtração
[3] Multiplição
[4] Divisão
> """)))

if operacao == 1:
    result = num1 + num2
elif operacao == 2:
    result = num1 - num2
elif operacao == 3:
    result = num1 * num2
elif operacao == 4:
    result = num1 / num2
else:
    print('Digite um valor valido')

if result % 2 == 0:
    print('par')
else:
    print('impar')

if result > 0:
    print('Positivo')

elif result < 0:
    print('Negativo')

else:
    print('zero')

if type(result) == int:
    print('Inteiro')
elif type(result) == float:
    print('decimal')
else:
    print('zero')
