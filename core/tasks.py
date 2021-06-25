import sqlite3

conn = sqlite3.connect("organizer.db")


class Tasks:
    def __init__(self, task, exp_date):
        self.task = task
        self.exp_date = exp_date

    def add_task(self, username):
        self.task = input("Co to za zadanie?: ")
        self.exp_date = input("Kiedy deadline?: ")
        conn.execute(
            f"INSERT INTO `tasks` (task, exp_date, user) VALUES ('{self.task}', '{self.exp_date}',"
            f"(SELECT user_id FROM users WHERE username='{username}'));"
        )
        conn.commit()
        print("Zadanie dodane!")

    def show_tasks(self, username):
        cursor = conn.execute(f"SELECT task_id,task,exp_date FROM tasks,users WHERE username='{username}';")
        for row in cursor.fetchall():
            print(row)
        print("\n")

    def delete_task(self, username):
        Tasks.show_tasks(self, username)
        task_del_id = input("Wpisz numer zadania do usunięcia: ")
        confirm = input(f'Czy na pewno chcesz usunąć zadanie z numerem "{task_del_id}"? [y]Tak, [n]Nie: ')
        if confirm == "y" or confirm.lower() == "y":
            conn.execute(
                f"DELETE FROM `tasks` WHERE task_id='{task_del_id}';"
            )
            conn.commit()
            print("Zadanie usunięte!")
        elif confirm == "n" or confirm.lower() == "n":
            print("Usuwanie przerwane! W ostatniej chwili!\n")

    def delete_all_tasks(self, username):
        Tasks.show_tasks(self, username)
        choice = input("Czy na pewno chcesz usunąć WSZYSTKIE zadania?\n"
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

    def menu(self, username):
        while True:
            print("Wybierz co chcesz zrobić:\n"
                  "[1]Dodać zadanie,\n"
                  "[2]Zobaczyć zadania,\n"
                  "[3]Usunąć zadanie,\n"
                  "[4]Usunąć wszystkie zadania\n"
                  "[q]Wyjść\n")
            choice = input("Wybierz: ")
            if choice == "1":
                Tasks.add_task(self, username)
            elif choice == "2":
                Tasks.show_tasks(self, username)
            elif choice == "3":
                Tasks.delete_task(self, username)
            elif choice == "4":
                Tasks.delete_all_tasks(self, username)
            elif choice == "q" or choice.lower == "q":
                break
            else:
                print("Błędny wybór!")

    def test(self):
        print("Zadania działają")
