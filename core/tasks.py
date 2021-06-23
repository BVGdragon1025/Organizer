import sqlite3

conn = sqlite3.connect("organizer.db")


class Tasks:
    def __init__(self, task, exp_date):
        self.task = task
        self.exp_date = exp_date

    def add_task(self):
        self.task = input("Co to za zadanie?: ")
        self.exp_date = input("Kiedy deadline?: ")
        conn.execute(
            f"INSERT INTO `tasks` (task, exp_date) VALUES ('{self.task}', '{self.exp_date}');"
        )
        conn.commit()
        print("Zadanie dodane!")

    def show_tasks(self):
        cursor = conn.execute(f"SELECT * FROM `tasks`;")
        for row in cursor.fetchall():
            print(row)
        print("\n")

    def delete_task(self):
        Tasks.show_tasks(self)
        task_del_id = input("Wpisz numer zadania do usunięcia: ")
        confirm = input(f'Czy na pewno chcesz usunąć zadanie z numerem "{task_del_id}"? [y]Tak, [n]Nie: ')
        if confirm == "y" or confirm.lower() == "y":
            conn.execute(
                f"DELETE FROM `tasks` WHERE id='{task_del_id}';"
            )
            conn.commit()
            print("Zadanie usunięte!")
        elif confirm == "n" or confirm.lower() == "n":
            print("Usuwanie przerwane! W ostatniej chwili!\n")

    def delete_all_tasks(self):
        Tasks.show_tasks(self)
        choice = input("Czy na penwo chcesz usunąć WSZYSTKIE zadania?\n"
                       "Operacji tej nie da się cofnąć!\n"
                       "[y]Tak, [n]Nie: ")
        if choice == "y" or choice.lower() == "y":
            conn.execute(
                f"DELETE FROM `tasks`;"
            )
            conn.commit()
            print("Zadania zostały usunięte!\n")
        elif choice == "n" or choice.lower() == "n":
            print("Usunięcie anulowane! W ostatniej chwili!\n")

    def menu(self):
        while True:
            print("Wybierz co chcesz zrobić:\n"
                  "[1]Dodać zadanie,\n"
                  "[2]Zobaczyć zadania,\n"
                  "[3]Usunąć zadanie,\n"
                  "[4]Usunąć wszystkie zadania\n"
                  "[q]Wyjść\n")
            choice = input("Wybierz: ")
            if choice == "1":
                Tasks.add_task(self)
            elif choice == "2":
                Tasks.show_tasks(self)
            elif choice == "3":
                Tasks.delete_task(self)
            elif choice == "4":
                Tasks.delete_all_tasks(self)
            elif choice == "q" or choice.lower == "q":
                break
            else:
                print("Błędny wybór!")

    def test(self):
        print("Zadania działają")
