﻿import sqlite3

conn = sqlite3.connect("organizer.db")


class NotesList:
    def __init__(self, title, note, tick):
        self.title = title
        self.note = note
        self.tick = tick

    def add_notes_list(self, username):
        i = 0
        self.title = input("Nadaj tytuł liście: ")
        conn.execute(
            f"INSERT INTO notes_list (title, user) VALUES('{self.title}',"
            f"(SELECT user_id FROM users WHERE username='{username}'));"
        )
        conn.commit()

        how_much = int(input("Ile chcesz dodać pozycji (możesz później dodać więcej): "))
        while i != how_much:
            self.note = input(f"Podaj treść tej pozycji (jeszcze {how_much-i}): ")
            conn.execute(
                f"INSERT INTO nlist_content (note,tick,nlist) VALUES('{self.note}','0',"
                f"(SELECT nlist_id FROM notes_list WHERE title = '{self.title}'));"
            )
            conn.commit()
        print("Lista dodana!")

    def menu(self, username):
        while True:
            print()

