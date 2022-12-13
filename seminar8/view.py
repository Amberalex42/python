def get_user_ans():
    return input("\nВыберите пункт меню:\n"
                 "1 - добавление сотрудника,\n"
                 "2 - просмотр всех сотрудников,\n"
                 "3 - найти сотрудника по фамилии,\n"
                 "4 - найти сотрудника по должности,\n"
                 "5 - изменить зарплату,\n"
                 "6 - общий фонд зарплаты\n"
                 "q - выход\n")


def get_new_person():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    position = input("Введите должность: ")
    salary = float(input("Введите зарплату: "))
    bonus = int(input("Введите размер премии в процентах: "))
    return first_name, last_name, position, salary, bonus


def get_seek_sname():
    return input("Введите фамилию для поиска: ")


def get_seek_position():
    return input("Введите должность для поиска: ")


def get_new_salary():
    return float(input("Введите новую зарплату: "))
