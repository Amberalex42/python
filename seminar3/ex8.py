# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input("Введите количество элементов: "))


def get_fibo(n):
    n0 = 0
    n1 = 1
    result = []
    for i in range(n):
        result.append(n1)
        n0, n1 = n1, n0 + n1
    return result


def get_negafibo(n):
    n0 = 0
    n1 = 1
    result = []
    for i in range(n):
        result.append(n1)
        n0, n1 = n1, n0 - n1
    return result


print(get_negafibo(n))
