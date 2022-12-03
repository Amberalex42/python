# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.


def get_prime_dividers(n):
    res = []
    i = 2
    for i in range(2, int(n**0.5) + 1):
        while not n % i:
            res.append(i)
            n //= i
    if n != 1:
        res.append(n)
    return res


print(*get_prime_dividers(256800005642000))
