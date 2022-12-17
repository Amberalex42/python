def digits_sum(num_str):
    return sum(map(int, filter(lambda x: x != '.', num_str)))


print(digits_sum('123,45'))
