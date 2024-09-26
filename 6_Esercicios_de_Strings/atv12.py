"""
Valida e corrige número de telefone. Faça um programa que leia um número de
telefone, e corrija o número no caso deste conter somente 7 dígitos,
acrescentando o '3' na frente. O usuário pode informar o número com ou sem o
traço separador.

    Valida e corrige número de telefone
    Telefone: 461-0133
    Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
    Telefone corrigido sem formatação: 34610133
    Telefone corrigido com formatação: 3461-0133
"""

numero = list(input("Telefone: "))

if '-' in numero:
    if len(numero) == 8:
        print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")  # noqa E261
        numero.insert(0, '3')
else:
    if len(numero) == 7:
        print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")  # noqa E261
        numero.insert(0, '3')
print(''.join(numero))
