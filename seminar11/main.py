lst = [1, 2, 2, 4, 3, 5, 2, 1]
result = [lst[i] for i in range(len(lst)) if lst[i] == max(lst[:i + 1]) and lst[:i + 1].count(lst[i]) == 1]
print(result)

