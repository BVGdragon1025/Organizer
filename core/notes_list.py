import sqlite3

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
            self.note = input(f"Podaj treść tej pozycji (jeszcze {how_much - i}): ")
            conn.execute(
                f"INSERT INTO nlist_content (note,tick,nlist) VALUES('{self.note}','0',"
                f"(SELECT nlist_id FROM notes_list WHERE title = '{self.title}'));"
            )
            conn.commit()
            i += 1
        print("Lista dodana!")

    def menu(self, username):
        while True:
            print("Wybierz co chcesz zrobić:\n"
                  "[1]Dodać nową listę,\n"
                  "[2]Dodać nowe rzeczy do listy,\n"
                  "[3]Wyświetlić listy,\n"
                  "[4]Usunąć listę,\n"
                  "[5]Usunąć wszystkie listy\n"
                  "[q]Wyjść\n")
            choice = input("Wybierz: ")
            if choice == "1":
                NotesList.add_notes_list(self, username)
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "q" or choice.lower == "q":
                break
            else:
                print("Błędny wybór!")
