"""
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
"""

from random import randint


def soma_dados():
    dado_1 = randint(1, 6)
    dado_2 = randint(1, 6)

    return dado_1 + dado_2


def craps():
    soma = soma_dados()
    if soma in [7, 11]:
        return "ganhou"
    elif soma in [2, 3, 12]:
        return "perdeu"
    else:
        numero = soma
        print(numero)
        nova_soma = 1
        while numero != nova_soma:
            print("aq")
            if nova_soma == 7:
                return "perdeu"
            nova_soma = soma_dados()
        return "ganhou"


print(craps())
