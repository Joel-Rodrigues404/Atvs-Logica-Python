vetor = [x for x in range(0, 100, 2)]
vetor2 = []
print(vetor)


def busca_binaria(lista, item, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio <= fim:
        meio = (inicio + fim) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute < item:
            return busca_binaria(lista, item, meio + 1, fim)
        else:
            return busca_binaria(lista, item, inicio, meio - 1)
    return None


print(busca_binaria(vetor, 2))
