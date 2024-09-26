# Inicializa o tabuleiro
board = [" " for _ in range(9)]

# Função para imprimir o tabuleiro


def print_board():
    for i in range(0, 9, 3):
        print(board[i] + "|" + board[i+1] + "|" + board[i+2])
        if i < 6:
            print("-----")

# Função para verificar se há um vencedor


def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                      (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Função principal do jogo


def play_game():
    current_player = "X"
    for turn in range(9):
        print_board()
        move = int(
            input(f"Jogador {current_player}, escolha uma posição (0-8): "))

        if board[move] == " ":
            board[move] = current_player
        else:
            print("Posição inválida! Tente novamente.")
            continue

        if check_winner(current_player):
            print_board()
            print(f"Jogador {current_player} venceu!")
            return

        current_player = "O" if current_player == "X" else "X"

    print("Empate!")


# Inicia o jogo
play_game()
