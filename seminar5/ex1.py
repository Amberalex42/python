# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не
# хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

with open("input1.txt", "r", encoding="utf-8") as file:
    lst = list(map(int, file.read().split()))

for i in range(1, len(lst)):
    if lst[i] - 1 != lst[i - 1]:
        break
print(lst[i] - 1)
