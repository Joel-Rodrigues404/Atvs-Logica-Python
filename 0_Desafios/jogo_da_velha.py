"""
JOGO DA VELHA

- logica
0 == 0
X == 1
sum([1, 1, 1]) = 3 x vence
se a soma der 3 X vence
se der 0, 0 vence


funcão diagonal
fun (list):
    for x in range(0, 3)
        pega todos na posição [x][x]
        no caso
        [00][11][22] e [02][11][20]
VAZIA
_|_|_
_|_|_
 | |

PREENCHIDO
[0][0]|[0][1]|[0][2]
[1][0]|[1][1]|[1][2]
[2][0]|[2][1]|[2][2]

"""

matriz = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"],
]


def mostra_tabela(matriz):
    print('  0  1  2')
    for i, x in enumerate(matriz):
        for j, y in enumerate(x):
            print(f'{i if j == 0 else ''} {
                  'x' if y == 1 else 'o' if y == 0 else y}', end='\n' if j == 2 else '|')  # noqa E261
    print("\n")


def edita_tabela(valor):
    try:
        linha = abs(int(input("linha: ")))
        coluna = abs(int(input("coluna: ")))

        erros = [
            coluna not in [1, 0, 2],
            linha not in [1, 0, 2],
        ]

        if any(erros):
            raise ValueError()
        if matriz[linha][coluna] in [1, 0]:
            print("Essa posição ja foi escolhida!")
            raise ValueError()

        matriz[linha][coluna] = valor

        mostra_tabela(matriz)

    except Exception:
        print('Digite numeros entre [0, 1, 2]!!!')
        mostra_tabela(matriz)
        edita_tabela(valor=valor)


def soma_listas(lista):
    if sum(lista) == 3:
        return "Jogador 1"
    elif sum(lista) == 0:
        return "Jogador 2"
    return False


def verifica_linhas(matriz):
    for x in matriz:
        try:
            ganhador = soma_listas(x)
        except Exception:
            continue
        if ganhador is not False:
            return ganhador
    return False


def verifica_colunas(matriz):
    try:
        coluna = []
        for x in range(0, 3):
            for y in range(0, 3):
                num = matriz[y][x]
                coluna.append(num if type(num) is int else '_')

            ganhador = soma_listas(coluna)
            if ganhador is not False:
                return ganhador

            coluna = []

        return False
    except Exception:
        return False


def verifica_diagonais(matriz):
    try:
        diagonal = []
        for x in range(0, 3):
            num = matriz[x][x]
            diagonal.append(num if type(num) is int else '_')

        ganhador = soma_listas(diagonal)
        if ganhador is not False:
            return ganhador

        diagonal = [matriz[2][0], matriz[1][1], matriz[0][2]]

        ganhador = soma_listas(diagonal)
        if ganhador is not False:
            return ganhador

        return False
    except Exception:
        return False


def verifica_vencedor(matriz):
    verifica_linhas_var = verifica_linhas(matriz=matriz)
    verifica_colunas_var = verifica_colunas(matriz=matriz)
    verifica_diagonais_var = verifica_diagonais(matriz=matriz)

    if verifica_linhas_var is not False:
        print(f'\nO ganhador e {verifica_linhas_var}')
        return verifica_linhas_var

    elif verifica_colunas_var is not False:
        print(f'\nO ganhador e {verifica_colunas_var}')
        return verifica_colunas_var

    elif verifica_diagonais_var is not False:
        print(f'\nO ganhador e {verifica_diagonais_var}')
        return verifica_diagonais_var
    else:
        print("\nEmpate!")

    return False


for x in range(1, 10):
    if x % 2 == 0:
        print('=-=-' * 10)
        print('JOGADOR 2 == o')
        print('=-=-' * 10)
        print("\n")
        valor = 0
    else:
        print('=-=-' * 10)
        print('JOGADOR 1 == x')
        print('=-=-' * 10)
        print("\n")
        valor = 1

    if x == 1:
        mostra_tabela(matriz=matriz)
    edita_tabela(valor=valor)

    if x > 2:
        if verifica_vencedor(matriz=matriz) is not False:
            break
