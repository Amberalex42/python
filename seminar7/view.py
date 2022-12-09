def view_data(data, title):
    print(f"{title} = {data}")


def type_nums():
    return input("Выберите пункт меню: 1 - комплексные числа, 2 - вещественные числа, q - выход из программы: ")


def get_value():
    return int(input("value = "))


def get_complex_value():
    return complex(input("value = "))


def get_operation():
    return input("Выберите действие: ")
