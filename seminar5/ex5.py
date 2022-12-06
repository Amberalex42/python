# 5 Создайте программу для игры в "Крестики-нолики".
import random


def start_game():
    def draw_board():
        print("\t \t|\t \t|\t \t")
        print(f"\t{board[0]}\t|\t{board[1]}\t|\t{board[2]}\t")
        print("________|_______|________")
        print("\t \t|\t \t|\t \t")
        print(f"\t{board[3]}\t|\t{board[4]}\t|\t{board[5]}\t")
        print("________|_______|________")
        print("\t \t|\t \t|\t \t")
        print(f"\t{board[6]}\t|\t{board[7]}\t|\t{board[8]}\t")
        print("\t \t|\t \t|\t \t")

    def make_move(player):
        while True:
            user_ans = int(input("Введите номер ячейки: "))
            if 1 <= user_ans <= 9 and isinstance(board[user_ans - 1], int):
                board[user_ans - 1] = player
                players_moves[player].append(user_ans)
                break

    def check_end():
        for el in winning:
            if all(j in players_moves["X"] for j in el):
                print("Выиграл X")
                return True
            elif all(j in players_moves["O"] for j in el):
                print("Выиграл O")
                return True
        if len(players_moves["X"]) + len(players_moves["O"]) == 9:
            print("Ничья")
            return True
        return False

    print("Начинаем новую игру!")
    board = [i for i in range(1, 10)]
    players_moves = {"X": [], "O": []}
    winning = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    cur_player = ["X", "O"][random.randint(0, 1)]
    draw_board()
    while not check_end():
        print(f"Ход игрока {cur_player}")
        make_move(cur_player)
        draw_board()
        cur_player = "X" if cur_player == "O" else "O"


start_game()
