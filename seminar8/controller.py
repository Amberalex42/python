import view
import model
import sqlite3


def menu():
    con = model.init_db("test.db")
    while True:
        user_ans = view.get_user_ans()
        if user_ans == '1':
            model.insert_to_db(con, view.get_new_person())
        elif user_ans == '2':
            res_all = model.get_info_from_db(con)
            print("Сотрудники: ")
            for el in res_all.fetchall():
                model.print_el(el)
        elif user_ans == '3':
            seeking_man = view.get_seek_sname()
            res_all = model.get_info_from_db(con)
            for el in res_all.fetchall():
                if el[1] == seeking_man:
                    model.print_el(el)
        elif user_ans == '4':
            seeking_position = view.get_seek_position()
            res_all = model.get_info_from_db(con)
            for el in res_all.fetchall():
                if el[2] == seeking_position:
                    model.print_el(el)
        elif user_ans == '5':
            seeking_man = view.get_seek_sname()
            new_salary = view.get_new_salary()
            model.update_info_in_db(con, seeking_man, new_salary)
        elif user_ans == '6':
            res_all = model.get_total_salary(con)
            print(f"Общий фонд заработной платы составляет: {res_all.fetchone()[0]} руб.")
        elif user_ans == 'q':
            break
    model.close_connection(con)
