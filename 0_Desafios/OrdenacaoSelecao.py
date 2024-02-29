import random

lista = [random.randint(1, 1000) for x in range(20)]
print(lista)


def pega_menor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i

    return menor_indice


def order_select(arr):
    novo_arr = []

    for _ in range(len(arr)):
        indice_do_menor = pega_menor(arr)
        novo_arr.append(arr.pop(indice_do_menor))
    return novo_arr


lista_ordenada = order_select(lista)
print(lista_ordenada)


def busca_binaria(arr, numero, maior=None, menor=0):
    if maior is None:
        maior = len(arr) - 1

    meio = (menor + menor) // 2
    chute = arr[meio]
    if menor <= maior:
        if numero == chute:
            return meio
        if numero > chute:
            return busca_binaria(arr, numero, maior=maior, menor=meio + 1)
        return busca_binaria(arr, numero, maior=meio - 1, menor=menor)
    return None


NUM = None
while NUM not in lista_ordenada:
    NUM = abs(int(input(f"digite um numero dentre esses {lista_ordenada}: ")))


print(busca_binaria(lista_ordenada, NUM, maior=None, menor=0))
