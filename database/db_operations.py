import sqlite3

database_path = "./database/database.db"

class Database:
    def __init__(self):
        self.conn = None

    def init_db(self):
        conn = sqlite3.connect(database_path)
        with open("./database/schema.sql") as file:
            command = file.read()
        conn.executescript(command)
        conn.close()

    def get_records(self, query):
        conn = sqlite3.connect(database_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query)
        return cur.fetchall()

    def execute_query(self, query):
        success = False
        try:
            with sqlite3.connect(database_path) as conn:
                cur = conn.cursor()
                cur.execute(query)
                conn.commit()
                success = True
        except Exception as e:
            print(e)
            conn.rollback()
            success = False
        finally:
            conn.close()
            return success

    def add_record(self, login, password):
        success = False
        try:
            with sqlite3.connect(database_path) as conn:
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

    def get_all_names(self, table="users"):
        conn = sqlite3.connect(database_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        command = f"SELECT login FROM {table}"
        cur.execute(command)
        return cur.fetchall()

    def get_password(self, login):
        conn = sqlite3.connect(database_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        command = f"SELECT login,password FROM users WHERE login='{login}'"
        cur.execute(command)
        return cur.fetchall()

db = Database()
db.init_db()