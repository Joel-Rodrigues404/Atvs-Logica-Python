"""
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes 
entre 1 e um número inteiro informado pelo usuário
"""

# TODO FAZER ESSA
num = abs(int(input("digite um numero: ")))

# cont = 1
# divisores = 0
# lista_primos = list()
# while cont <= num:
#     if num % cont == 0:
#         divisores += 1
#         lista_primos.append(cont)
#     cont += 1

# if divisores == 2:
#     print("primo")
#     print(lista_primos)

primos = list()
divisores = [1, 2, 3, 5, 7, 11]
div = 0
for x in range(1, num + 1):
    for y in divisores:
        if x % y == 0:
            div += 1

print(primos)
