# Faça um Programa que peça dois números e imprima o maior deles.


num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))

if num1 == num2:
    print('os numeros são iguais')
elif num1 > num2:
    print(f'O numero {num1} e maior')
else:
    print(f'O numero {num2} e maior')