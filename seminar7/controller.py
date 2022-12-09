import model
import view


def menu():
    while True:
        user_choice = view.type_nums()
        a, b = 0, 0
        if user_choice == '1':
            a, b = complex_nums()
        elif user_choice == '2':
            a, b = int_nums()
        elif user_choice == 'q':
            print('До свидания')
            break
        oper = view.get_operation()
        model.init(a, b)
        result = 0
        if oper == "+":
            result = model.summ()
        elif oper == "-":
            result = model.sub()
        elif oper == "*":
            result = model.mult()
        elif oper == "/":
            result = model.div()

        view.view_data(result, "result")


def complex_nums():
    value_a = view.get_complex_value()
    value_b = view.get_complex_value()
    return value_a, value_b


def int_nums():
    value_a = view.get_value()
    value_b = view.get_value()
    return value_a, value_b
