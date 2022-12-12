import view
import model


def menu():
    database = model.get_dict_from_base("database.txt")
    user_ans = input("Что вы хотите сделать?\n"
                     "1 - Поиск по имени\n"
                     "2 - Поиск по номеру телефона\n"
                     "3 - Добавление нового номера\n"
                     "4 - Экспорт в XML\n"
                     "5 - Экспорт в HTML\n")
    if user_ans == '1':
        seeking_name = view.get_name()
        print(f"{seeking_name}: {', '.join(database[seeking_name])}"
              if seeking_name in database
              else "Такой записи нет!")
    elif user_ans == '2':
        seeking_phone = view.get_num()
        for el in database:
            if seeking_phone in database[el]:
                print(f"{el}: {', '.join(database[el])}")
                break
        else:
            print("Такой записи нет!")
    elif user_ans == '3':
        new_name = view.get_name()
        new_phone = view.get_num()
        database.setdefault(new_name, []).append(new_phone)
        str_to_database = ";".join([f"{k}:{','.join(v)}" for k, v in database.items()])
        model.set_dict_to_base("database.txt", str_to_database)
    elif user_ans == '4':
        model.xml_generator(database)
    elif user_ans == '5':
        model.html_generator(database)

