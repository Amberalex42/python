# 4 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не
# более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
import random


def start_game(deck=100):

    def make_move(player):
        if player != "Bot":
            while True:
                try:
                    amount = int(input("Сколько конфет вы хотите взять? Введите число от 1 до 28: "))
                    if amount < 1 or amount > 28:
                        raise Exception
                except Exception:
                    print("Нужно ввести число от 1 до 28! Попробуйте еще раз!")
                else:
                    break
            return amount
        else:
            if deck < 29:
                return deck
            else:
                return max(deck % 29, 1)

    def end_game():
        print(f"Игрок {players[cur_player]} победил!")
        while True:
            try:
                user_ans = int(input("Сыграем еще раз? 1 - да, 0 - нет: "))
                if user_ans not in (0, 1):
                    raise Exception
            except Exception:
                print("Введите 0 или 1! Попробуйте еще раз!")
            else:
                break
        if user_ans == 1:
            start_game()
        else:
            print("Спасибо за игру! До свидания!")

    players = ['Human1']
    print('Начинаем новую игру!')
    while True:
        try:
            user_ans = int(input("Второй игрок человек или компьютер? 1 - человек, 0 - компьютер: "))
            if user_ans not in (0, 1):
                raise Exception
        except Exception:
            print("Введите 0 или 1! Попробуйте еще раз!")
        else:
            break
    players.append('Human2' if user_ans == 1 else 'Bot')
    cur_player = random.randint(0, 1)
    while deck > 0:
        cur_player = 1 - cur_player
        print(f'На столе {deck} конфет.')
        print('Ход игрока ' + players[cur_player])
        move = make_move(players[cur_player])
        print(f"Игрок {players[cur_player]} взял {move} конфет.")
        print()
        deck -= move
    end_game()


start_game(100)
