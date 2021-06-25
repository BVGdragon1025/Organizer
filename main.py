import sqlite3
import os
from core import notes, tasks, notes_list, tasks_list

conn = sqlite3.connect("organizer.db")
cursor = conn.cursor()

if not os.path.exists("organizer.db"):
    with conn:
        conn.execute('CREATE TABLE "users"('
                     '"user_id" INTEGER NOT NULL,'
                     '"username" TEXT NOT NULL UNIQUE,'
                     '"password" TEXT NOT NULL,'
                     'PRIMARY KEY("user_id" AUTOINCREMENT));')
        conn.commit()
        conn.execute('CREATE TABLE "notes"('
                     '"note_id" INTEGER NOT NULL,'
                     '"note" TEXT NOT NULL,'
                     '"user" INTEGER NOT NULL,'
                     'PRIMARY KEY ("note_id" AUTOINCREMENT),'
                     'FOREIGN KEY ("user") REFERENCES "users"("user_id") ON DELETE CASCADE);')
        conn.commit()
        conn.execute('CREATE TABLE "tasks"('
                     '"task_id" INTEGER NOT NULL,'
                     '"task" TEXT NOT NULL,'
                     '"exp_date" TEXT NOT NULL,'
                     '"user" INTEGER NOT NULL,'
                     'PRIMARY KEY ("task_id" AUTOINCREMENT),'
                     'FOREIGN KEY ("user") REFERENCES "users"("user_id") ON DELETE CASCADE);')
        conn.commit()
        conn.execute('CREATE TABLE "notes_list"('
                     '"nlist_id" INTEGER NOT NULL,'
                     '"title" TEXT NOT NULL,'
                     '"user" INTEGER NOT NULL,'
                     'PRIMARY KEY ("nlist_id" AUTOINCREMENT)'
                     'FOREIGN KEY ("user") REFERENCES "users"("user_id") ON DELETE CASCADE);')
        conn.commit()
        conn.execute('CREATE TABLE "tasks_list"('
                     '"tlist_id" INTEGER NOT NULL,'
                     '"title" TEXT NOT NULL,'
                     '"exp_date" TEXT NOT NULL,'
                     '"user" INTEGER NOT NULL,'
                     'PRIMARY KEY ("tlist_id" AUTOINCREMENT)'
                     'FOREIGN KEY ("user") REFERENCES "users"("user_id") ON DELETE CASCADE);')
        conn.commit()
        conn.execute('CREATE TABLE "nlist_content"('
                     '"ncontent_id" INTEGER NOT NULL,'
                     '"note" TEXT NOT NULL,'
                     '"tick" INTEGER NOT NULL,'
                     '"nlist" INTEGER NOT NULL,'
                     'PRIMARY KEY("ncontent_id" AUTOINCREMENT)'
                     'FOREIGN KEY ("nlist") REFERENCES "notes_list"("nlist_id") ON DELETE CASCADE);')
        conn.commit()
        conn.execute('CREATE TABLE "tlist_content"('
                     '"tcontent_id" INTEGER NOT NULL,'
                     '"task" TEXT NOT NULL,'
                     '"complete" INTEGER NOT NULL,'
                     '"tlist" INTEGER NOT NULL,'
                     'PRIMARY KEY("ncontent_id" AUTOINCREMENT)'
                     'FOREIGN KEY ("tlist") REFERENCES "tasks_list"("tlist_id") ON DELETE CASCADE);')
        conn.commit()
else:
    with conn:
        conn.execute('CREATE TABLE IF NOT EXISTS"users"('
                     '"user_id" INTEGER NOT NULL,'
                     '"username" TEXT NOT NULL UNIQUE,'
                     '"password" TEXT NOT NULL,'
                     'PRIMARY KEY("user_id" AUTOINCREMENT));')
        conn.commit()
        conn.execute('CREATE TABLE IF NOT EXISTS "notes"('
                     '"note_id" INTEGER NOT NULL,'
                     '"note" TEXT NOT NULL,'
                     '"user" INTEGER NOT NULL,'
                     'PRIMARY KEY ("note_id" AUTOINCREMENT),'
                     'FOREIGN KEY ("user") REFERENCES "users"("user_id") ON DELETE CASCADE);')
        conn.commit()
        conn.execute('CREATE TABLE IF NOT EXISTS "tasks"('
                     '"task_id" INTEGER NOT NULL,'
                     '"task" TEXT NOT NULL,'
                     '"exp_date" TEXT NOT NULL,'
                     '"user" INTEGER NOT NULL,'
                     'PRIMARY KEY ("task_id" AUTOINCREMENT),'
                     'FOREIGN KEY ("user") REFERENCES "users"("user_id") ON DELETE CASCADE);')
        conn.commit()
        conn.execute('CREATE TABLE IF NOT EXISTS "notes_list"('
                     '"nlist_id" INTEGER NOT NULL,'
                     '"title" TEXT NOT NULL,'
                     '"user" INTEGER NOT NULL,'
                     'PRIMARY KEY ("nlist_id" AUTOINCREMENT)'
                     'FOREIGN KEY ("user") REFERENCES "users"("user_id") ON DELETE CASCADE);')
        conn.commit()
        conn.execute('CREATE TABLE IF NOT EXISTS "tasks_list"('
                     '"tlist_id" INTEGER NOT NULL,'
                     '"title" TEXT NOT NULL,'
                     '"user" INTEGER NOT NULL,'
                     'PRIMARY KEY ("tlist_id" AUTOINCREMENT)'
                     'FOREIGN KEY ("user") REFERENCES "users"("user_id") ON DELETE CASCADE);')
        conn.commit()
        conn.execute('CREATE TABLE IF NOT EXISTS "nlist_content"('
                     '"ncontent_id" INTEGER NOT NULL,'
                     '"note" TEXT NOT NULL,'
                     '"tick" INTEGER NOT NULL,'
                     '"nlist" INTEGER NOT NULL,'
                     'PRIMARY KEY("ncontent_id" AUTOINCREMENT)'
                     'FOREIGN KEY ("nlist") REFERENCES "notes_list"("nlist_id") ON DELETE CASCADE);')
        conn.commit()
        conn.execute('CREATE TABLE IF NOT EXISTS "tlist_content"('
                     '"tcontent_id" INTEGER NOT NULL,'
                     '"task" TEXT NOT NULL,'
                     '"complete" INTEGER NOT NULL,'
                     '"tlist" INTEGER NOT NULL,'
                     'PRIMARY KEY("tcontent_id" AUTOINCREMENT)'
                     'FOREIGN KEY ("tlist") REFERENCES "tasks_list"("tlist_id") ON DELETE CASCADE);')
        conn.commit()


class Main:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        table_check = cursor.execute("SELECT * FROM users ; ")
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
            conn.execute(f"INSERT INTO users (username, password) VALUES ('{self.username}', '{self.password}');")
            conn.commit()
            Main.menu(self)
        elif table_check.fetchall() is not None:
            print("Witaj ponownie!")
            self.username = input("Podaj swoją nazwę (login): ")
            self.password = input("Podaj swoje hasło: ")
            while True:
                user_check = conn.execute(
                    f"SELECT username, password FROM `users` "
                    f"WHERE username = '{self.username}' AND password = '{self.password}';"
                )
                if user_check.fetchone() is not None:
                    print(f"Witamy ponownie, {self.username}")
                    Main.menu(self)
                    break
                else:
                    print("Brak takiego użytkownika, spróbuj jeszcze raz")
                    self.username = input("Podaj swoją nazwę (login): ")
                    self.password = input("Podaj swoje hasło: ")
        else:
            print("Błąd")
        return self.username

    def menu(self):
        while True:
            print("Gdzie chciałbyś teraz się przenieść?\n"
                  "[1]Notatki, \n"
                  "[2]Zadania, \n"
                  "[q]Wyjść \n")
            choice = input("Wybierz: ")
            if choice == "1":
                notes.Notes.menu(notes.Notes, self.username)
            elif choice == "2":
                tasks.Tasks.menu(tasks.Tasks, self.username)
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "q" or choice.lower() == "q":
                print(f"Żegnaj, {self.username}!")
                conn.close()
                break
            else:
                print("Brak takiej opcji. Spróbuj jeszcze raz!")

    def test(self):
        print("Działa")


Main.login(Main)

