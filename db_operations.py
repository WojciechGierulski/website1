import sqlite3


class Database:
    def __init__(self):
        self.conn = None

    def init_db(self):
        conn = sqlite3.connect("database.db")
        with open("schema.sql") as file:
            command = file.read()
        conn.execute(command)
        conn.close()

    def add_record(self, login, password):
        success = False
        try:
            with sqlite3.connect("database.db") as conn:
                cur = conn.cursor()
                command = f"INSERT INTO users (login,password) VALUES ('{login}','{password}')"
                cur.execute(command)
                conn.commit()
                success = True
        except:
            conn.rollback()
            success = False
        finally:
            conn.close()
            return success

    def get_all_names(self):
        conn = sqlite3.connect("database.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        command = f"SELECT login FROM users"
        cur.execute(command)
        return cur.fetchall()

    def get_password(self, login):
        conn = sqlite3.connect("database.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        command = f"SELECT login,password FROM users WHERE login='{login}'"
        cur.execute(command)
        return cur.fetchall()