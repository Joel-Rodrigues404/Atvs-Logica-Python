"""Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
"""

from faker import Faker
import random
from time import sleep
import string


def embaralha(palavra: str):
    palavra = palavra.upper()
    palavra_lista = []
    for x in palavra:
        palavra_lista.append(x)

    tamanho_nova_palavra_lista = len(palavra_lista)
    nova_palavra_lista = [""] * tamanho_nova_palavra_lista
    numbers = [x for x in range(0, tamanho_nova_palavra_lista)]
    for x in palavra_lista:
        num = random.choice(numbers)
        index = numbers.index(num)
        nova_palavra_lista[num] = x
        numbers.pop(index)

    return "".join(nova_palavra_lista)


def gera_palavra_v1():
    palavra = []
    for x in range(random.randint(1, 10)):
        palavra.append(string.ascii_letters[x])
    return "".join(palavra)


def gera_palavra_v2():
    fake = Faker("pt_BR")
    palavra = fake.word()
    return palavra


palavra = gera_palavra_v2()
print(f"A palavra e: {palavra}")
print("embaralhando ...")
sleep(3)
print(f"saida: {embaralha(palavra)}")
