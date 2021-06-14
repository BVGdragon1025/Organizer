import sqlite3
import os

conn = sqlite3.connect("organizer.db")

if not os.path.exists("organizer.db"):
    with conn:
        conn.execute("CREATE TABLE notes("
                     "id INTEGER NOT NULL, "
                     "title TEXT NOT NULL, "
                     "PRIMARY KEY (id AUTOINCREMENT));")
        conn.commit()
        conn.execute("CREATE TABLE tasks("
                     "id INTEGER NOT NULL,"
                     "title TEXT NOT NULL,"
                     "exp_date TEXT NOT NULL,"
                     "PRIMARY KEY (id AUTOINCREMENT));")
        conn.commit()
        conn.execute("CREATE TABLE users("
                     "id INTEGER NOT NULL,"
                     "username TEXT NOT NULL,"
                     "password TEXT NOT NULL,"
                     "PRIMARY KEY(id AUTOINCREMENT));")
        conn.commit()
else:
    with conn:
        conn.execute("CREATE TABLE IF NOT EXISTS notes("
                     "id INTEGER NOT NULL, "
                     "title TEXT NOT NULL, "
                     "PRIMARY KEY (id AUTOINCREMENT));")
        conn.commit()
        conn.execute("CREATE TABLE IF NOT EXISTS tasks("
                     "id INTEGER NOT NULL,"
                     "title TEXT NOT NULL,"
                     "exp_date TEXT NOT NULL,"
                     "PRIMARY KEY (id AUTOINCREMENT));")
        conn.commit()
        conn.execute("CREATE TABLE IF NOT EXISTS users("
                     "id INTEGER NOT NULL,"
                     "username TEXT NOT NULL,"
                     "password TEXT NOT NULL,"
                     "PRIMARY KEY(id AUTOINCREMENT));")
        conn.commit()


class Main:
    def __init__(self, username, password, title, exp_date):
        self.username = username
        self.password = password
        self.title = title
        self.exp_date = exp_date



