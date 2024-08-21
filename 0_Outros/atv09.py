"""Escreva um código em Python que receba um número inteiro e retorne True se o número for primo, ou False caso contrário.
Um recurso útil para implementação é o módulo (ou resto). O operador de módulo (ou resto) em Python é o “%”. Por exemplo: 1
% 5 -> 4; 14 % 4 -> 3, 10 % 2 -> 0."""


def numero_primo(num: int):
    if num == 1:
        return None
    divisores = 0
    for x in range(1, num + 1):
        if num % x == 0:
            divisores += 1

    if divisores == 2:
        return True
    return False


for i in range(1, 101):
    print(f"{i} e primo? {numero_primo(i)}")
