# 5 Создайте программу для игры в "Крестики-нолики".
def start_game():
    def draw_board():
        print("\t \t|\t \t|\t \t")
        print(f"\t{1}\t|\t{2}\t|\t{3}\t")
        print("________|_______|________")
        print("\t \t|\t \t|\t \t")
        print(f"\t{4}\t|\t{5}\t|\t{6}\t")
        print("________|_______|________")
        print("\t \t|\t \t|\t \t")
        print(f"\t{7}\t|\t{8}\t|\t{9}\t")
        print("\t \t|\t \t|\t \t")

    print("Начинаем новую игру!")
    board = [i for i in range(1, 10)]
    draw_board()


start_game()
