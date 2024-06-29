"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""


def P_ou_N(num):
    if num > 0:
        return "P"
    if num == 0:
        return "ZERO"
    return "N"


print(P_ou_N(1))
