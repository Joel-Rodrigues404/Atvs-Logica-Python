"""
JOGO DA VELHA
"""

"""
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

# linha | coluna
matriz = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"],
]


def mostra_tabela(matriz):

    print('Começe com linhas e depois colunas.')
    print('  0  1  2')

    for i, x in enumerate(matriz):
        for j, y in enumerate(x):
            print(f'{i if j == 0 else ''} {
                  'x' if y == 1 else 'o' if y == 0 else y}', end='\n' if j == 2 else '|')


def edita_tabela():

    linha = abs(int(input("digite a linha: ")))
    coluna = abs(int(input("digite a coluna: ")))
    valor = abs(int(input("digite o valor: ")))

    erros = [
        valor not in [1, 0],
        coluna not in [1, 0, 2],
        linha not in [1, 0, 2],
    ]

    if any(erros):
        print('Erro!! digite novamente!')
        edita_tabela()

    matriz[linha][coluna] = valor

    mostra_tabela(matriz)


def soma_listas(lista):
    if sum(lista) == 3:
        return "Jogador 1"
    elif sum(lista) == 0:
        return "Jogador 2"
    return False


def verifica_linhas(matriz):
    try:
        for x in matriz:
            return soma_listas(x)
        return False
    except:
        return False


def verifica_colunas(matriz):
    try:
        coluna = []
        for x in range(0, 3):
            for y in range(0, 3):
                num = matriz[y][x]
                coluna.append(num if type(num) is int else 3)

            return soma_listas(coluna)

            coluna = []

        return False
    except:
        return False


def verifica_diagonais(matriz):
    try:
        diagonal = []
        for x in range(0, 3):
            num = matriz[x][x]
            diagonal.append(num if type(num) is int else 3)

        return soma_listas(diagonal)
        diagonal = [matriz[2][0], matriz[1][1], matriz[0][2]]

        return soma_listas(diagonal)

        return False
    except:
        return False


def verifica_vencedor(matriz):
    verifica_linhas_var = verifica_linhas(matriz=matriz)
    verifica_colunas_var = verifica_colunas(matriz=matriz)
    verifica_diagonais_var = verifica_diagonais(matriz=matriz)

    if verifica_linhas_var is not False:
        print(f'O ganhador e {verifica_diagonais_var}')
        return verifica_linhas_var

    if verifica_colunas_var is not False:
        print(f'O ganhador e {verifica_colunas_var}')
        return verifica_colunas_var

    if verifica_diagonais_var is not False:
        print(f'O ganhador e {verifica_diagonais_var}')
        return verifica_diagonais_var

    return False


# mostra_tabela(matriz=matriz)
for x in range(1, 10):
    if x % 2 == 0:
        print('=-=-' * 10)
        print('Jogador 2')
        print('=-=-' * 10)
    else:
        print('=-=-' * 10)
        print('Jogador 1')
        print('=-=-' * 10)

    if x == 1:
        mostra_tabela(matriz=matriz)
    edita_tabela()

    if x > 2:
        if verifica_vencedor(matriz=matriz) is not False:
            break
