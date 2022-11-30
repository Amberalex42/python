# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора
# псевдослучайных чисел.
import time


def get_rand(start, end):
    return int((time.time_ns() % 1000000 // 1000 / 1000) * (end - start)) + start


print(get_rand(-5, 5))
