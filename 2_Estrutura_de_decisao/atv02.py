# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input("digite um numero qualquer: "))

if num == 0:
    print(f'o numero e {num}')

elif num > 0:
    print(f'o numero {num} e positivo')

else:
    print(f'O {num} e negativo')
