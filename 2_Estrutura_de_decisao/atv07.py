# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))
num3 = int(input("digite o terceiro numero: "))

if num1 < num2 and num1 < num3:
    print('O primeiro e menor')
elif num2 < num1 and num2 < num3:
    print("o segundo e menor")
elif num3 < num1 and num3 < num2:
    print("o terceiro e menor")
else:
    print("a numeros iguais tente novamente")