"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

    F
    FU
    FUL
    FULA
    FULAN
    FULANO

"""


nome = input("digite seu nome: ").upper()

[print(nome[0:i + 1]) for i, x in enumerate(nome)]
