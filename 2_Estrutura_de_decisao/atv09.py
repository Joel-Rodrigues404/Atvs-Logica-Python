# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))
num3 = float(input("digite o terceiro numero: "))  

print(num1, num2, num3, sep=' | ')

primeiro = None
segundo = None
terceiro = None

if num1 >= num2 and num1 >= num3:
    primeiro = num1
    if num2 >= num3:
        segundo = num2
        terceiro = num3
    else:
        segundo = num3
        terceiro = num2
elif num2 >= num1 and num2 >= num3:
    primeiro = num2
    if num1 >= num3:
        segundo = num1
        terceiro = num3
    else:
        segundo = num3
        terceiro = num3
else:
    primeiro = num3
    if num1 >= num2:
        segundo = num1
        terceiro = num2
    else:
        segundo = num2
        terceiro = num1

print(f"""
primeiro > {primeiro}
segundo > {segundo}
terceiro > {terceiro}
""")

print(primeiro, segundo, terceiro, sep=' | ')