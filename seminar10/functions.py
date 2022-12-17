def digits_sum(num_str):
    return sum(map(int, filter(lambda x: x != '.', num_str)))


def find_max(num_str):
    return max(map(int, num_str.split()))


# Функция отбирает из массива чисел только те, что образуют строго возрастающую последовательность
def filter_asc(lst):
    if not lst:
        return []
    else:
        result = [lst[0]]
        for i in range(1, len(lst)):
            if lst[i] > max(result):
                result.append(lst[i])
        return result
