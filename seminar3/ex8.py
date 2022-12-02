# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input("Введите количество элементов: "))


def get_fibo(n, neg=False):
    n0 = 0
    n1 = 1
    result = []
    for i in range(n):
        result.append(n1)
        if neg:
            n0, n1 = n1, n0 - n1
        else:
            n0, n1 = n1, n0 + n1
    if neg:
        result = result[::-1]
    return result


print(get_fibo(n, neg=True) + [0] + get_fibo(n))
