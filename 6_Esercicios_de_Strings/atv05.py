"""
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

    FULANO
    FULAN
    FULA
    FUL
    FU
    F
"""

nome = input("digite seu nome: ").upper()

[print(nome[0:len(nome) - i]) for i, x in enumerate(nome)]
