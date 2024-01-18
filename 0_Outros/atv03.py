"""
Faça um programa, com uma função sem argumento. A função retorna o valor de caractere 'P', se for um numero 
positivo, e 'N' se for negativo e 'Z' se for zero.
"""

def valida_num(num):
    if num > 0:
        return print('P')
    elif num < 0:
        return print('N')
    else:
        return print('Z')