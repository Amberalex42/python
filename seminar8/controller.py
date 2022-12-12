import view
import model


def menu():
    con = model.init_db("test.db")
    user_ans = view.get_user_ans()
    if user_ans == '1':
        cur = con.cursor()
        cur.execute('''INSERT INTO staff (first_name, last_name, position, salary, bonus) 
                            VALUES (?, ?, ?, ?, ?);''', view.get_new_person())
        # print(view.get_new_person())
        # model.insert_to_db(con, view.get_new_person())
    elif user_ans == '2':
        pass
    elif user_ans == '3':
        pass
    elif user_ans == '4':
        pass
    elif user_ans == '5':
        pass
    elif user_ans == '6':
        pass
    model.close_connection(con)
