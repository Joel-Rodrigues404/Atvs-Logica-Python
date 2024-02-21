my_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2  # 2
        chute = lista[meio]  # 5
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


print(busca_binaria(my_lista, 7))
print(busca_binaria(my_lista, -1))
