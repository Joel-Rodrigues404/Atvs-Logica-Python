"""
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""


def reverso_num_int(num: int):
    """
    127 >> 721
    logica 01 Fail
        [0, ... 10] - 127 == 120 + [0, ... 10]
            7       - 127 == 120 +      7
    logica 02 Fail
        1 / 127 =
    logica 03

    """
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10

    return digits


print(reverso_num_int(127))


# print(127 % 10)  # fica com o resto da div 7
# print(127 // 10)  # fica com tudo e tira o resto 12
