# Найти максимальное из пяти чисел.

num = int(input("Введите 1 число: "))
maxx = num
for i in range(1, 5):
    num = int(input(f"Введите {i + 1} число: "))
    if num > maxx:
        maxx = num
print(f"Максимальное из введенных чисел: {maxx}")
