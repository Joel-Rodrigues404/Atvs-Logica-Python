"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado. 
"""


def quantidade_de_digitos_num(num: int, cont=0):
    """
    10 / 10 = 1
    100 / 10 = 10 > 1, 10 / 10 = 1 > 2
    123 / 10 = 12,3 > 1 12,3 / 10 = 1,23 > 1
    """
    cont += 1
    num = num / 10
    if num > 10:
        return quantidade_de_digitos_num(num, cont=cont)
    return cont + 1


print(quantidade_de_digitos_num(1234567891011))
