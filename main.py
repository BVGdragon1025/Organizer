import sqlite3
import os
from core import notes, tasks

conn = sqlite3.connect("organizer.db")
cursor = conn.cursor()

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
                     "note TEXT NOT NULL, "
                     "PRIMARY KEY (id AUTOINCREMENT));")
        conn.commit()
        conn.execute("CREATE TABLE IF NOT EXISTS tasks("
                     "id INTEGER NOT NULL,"
                     "task TEXT NOT NULL,"
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
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        table_check = cursor.execute("SELECT count(*) FROM users LIMIT 1; ")
        print(table_check.fetchone())
        if table_check.fetchone() is None:
            print("Witaj w Organizerze! Jesteś nowym użytkownikiem, więc poproszę cię o parę rzeczy")
            self.username = input("Jak chcesz się nazywać?: ")
            self.password = input("Jakie chcesz mieć hasło?: ")
            passwd_check = input("Powtórz hasło: ")
            while True:
                if self.password != passwd_check:
                    self.password = input("Podaj ponownie hasło: ")
                    passwd_check = input("Powtórz je ponownie: ")
                else:
                    break
            print(f"Witaj, {self.username}!")
            conn.execute(f"INSERT INTO users (username, password) VALUES ('{self.username}, {self.password});")
            conn.commit()
        else:
            print("Witaj ponownie!")
            self.username = input("Podaj swoją nazwę (login): ")
            self.password = input("Podaj swoje hasło: ")
            conn.execute(f"SELECT * FROM users WHERE username = {self.username} AND password = {self.password}")
            print(f"Witamy ponownie, {self.username}")

    def test(self):
        print("Działa")


Main.login(Main)
notes.Notes.test(notes.Notes)
tasks.Tasks.test(tasks.Tasks)




