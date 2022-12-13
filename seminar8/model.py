import sqlite3


def init_db(filename):
    con = sqlite3.connect(filename)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS staff 
                    (id INTEGER PRIMARY KEY, 
                    first_name TEXT, 
                    last_name varchar(20), 
                    position varchar(20), 
                    salary real, 
                    bonus integer);''')
    return con


def close_connection(con):
    con.close()


def insert_to_db(con, row):
    cur = con.cursor()
    cur.execute(f'''INSERT INTO staff (first_name, last_name, position, salary, bonus) 
                            VALUES (?, ?, ?, ?, ?);''', row)
    con.commit()


def get_info_from_db(con):
    cur = con.cursor()
    return cur.execute('''SELECT first_name, last_name, position, salary, bonus FROM staff;''')


def get_total_salary(con):
    cur = con.cursor()
    return cur.execute('''SELECT SUM(salary) as total FROM staff''')


def update_info_in_db(con, last_name, new_salary):
    cur = con.cursor()
    cur.execute(f'''UPDATE staff SET salary = {new_salary} WHERE last_name = "{last_name}"''')
    con.commit()


def print_el(el):
    first_name, last_name, position, salary, bonus = el
    print(f"{first_name} {last_name}, {position}. Зарплата: {round(salary, 2)} руб., премия: {bonus}%.")

