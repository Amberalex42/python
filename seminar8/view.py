def get_user_ans():
    return input("Выберите пункт меню:\n"
                 "1 - добавление сотрудника,\n"
                 "2 - просмотр всех сотрудников,\n"
                 "3 - найти сотрудника по фамилии,\n"
                 "4 - найти сотрудника по должности,\n"
                 "5 - изменить зарплату,\n"
                 "6 - общий фонд зарплаты\n")


def get_new_person():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    position = input("Введите должность: ")
    salary = float(input("Введите зарплату: "))
    bonus = int(input("Введите размер премии в процентах: "))
    return first_name, last_name, position, salary, bonus
