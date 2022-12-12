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
                    VALUES ({row["first_name"]}, {row["last_name"]}, 
                            {row["position"]}, {row["salary"]}, {row["bonus"]});''')
