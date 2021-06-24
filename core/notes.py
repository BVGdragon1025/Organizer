import sqlite3

conn = sqlite3.connect("organizer.db")


class Notes:
    def __init__(self, note):
        self.note = note

    def add_note(self, username):
        self.note = input("Co chcesz zapisać?: ")
        conn.execute(
            f"INSERT INTO notes (note,user) VALUES('{self.note}',"
            f"(SELECT id FROM users WHERE username='{username}'));"
        )
        conn.commit()
        print("Notatka zapisana!\n")

    def show_notes(self, username):
        cursor = conn.execute(f"SELECT * FROM notes,users WHERE username={username};")
        for row in cursor.fetchall():
            print(row)
        print("\n")

    def delete_notes(self, username):
        Notes.show_notes(self, username)
        note_del_id = input("Wpisz numer notatki do usunięcia: ")
        confirm = input(f'Czy na pewno chcesz usunąć notatkę z numerem "{note_del_id}"? [y]Tak, [n]Nie: ')
        if confirm.lower() == "y" or confirm == "y":
            conn.execute(
                f"DELETE FROM notes WHERE id='{note_del_id}';"
            )
            conn.commit()
            print("Notatka usunięta!")
        elif confirm.lower() == "n" or confirm == "n":
            print("Usuwanie przerwane! W ostatniej chwili!\n")

    def delete_all_notes(self, username):
        Notes.show_notes(self,username)
        choice = input("Czy na pewno chcesz usunąć WSZYSTKIE notatki?\n"
                       "Operacji tej nie da się cofnąć!\n"
                       "[y]Tak, [n]Nie: ")
        if choice == "y" or choice.lower() == "y":
            conn.execute(
                f"DELETE FROM `notes`;"
            )
            conn.commit()
            print("Notatki zostały usunięte!\n")
        elif choice == "n" or choice.lower() == "n":
            print("Usunięcie anulowane! W ostatniej chwili!\n")

    def menu(self, username):
        while True:
            print("Wybierz co chcesz zrobić:\n"
                  "[1]Dodać notatkę,\n"
                  "[2]Zobaczyć notatki,\n"
                  "[3]Usunąć notatkę,\n"
                  "[4]Usunąć wszystkie notatki\n"
                  "[q]Wyjść\n")
            choice = input("Wybierz: ")
            if choice == "1":
                Notes.add_note(self, username)
            elif choice == "2":
                Notes.show_notes(self, username)
            elif choice == "3":
                Notes.delete_notes(self, username)
            elif choice == "4":
                Notes.delete_all_notes(self, username)
            elif choice == "q" or choice.lower == "q":
                break
            else:
                print("Błędny wybór!")

    def test(self):
        print("Notatki działają")
