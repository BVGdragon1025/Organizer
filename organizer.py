import datetime  # Użyję później do sortowania, lub czegoś innego

import os.path  # Przydatne do paru rzeczy :)


#  import tkinter : Na ten moment tego nie używam
#  Plus moja wiedza o klasach i obiektach jest na poziomie przypominania sobie


class Organizer:  # Użyłem klasy tylko dlatego, że mogę odnosić się do dowolnej funkcji kiedy tylko chcę

    def __init__(self):  # Użyłem tego tylko dlatego, by móc odnosić się do nazwy użytkownika.
        # To było najprostrze rozwiązanie dla mnie
        user = str(input("Podaj nazwę użytkownika: "))
        psw = str(input("Podaj hasło: "))
        self.user = user
        self.psw = psw

    def main(self):
        while True:
            choice = str(input("Wybierz co chcesz zrobić: [1]Rejestracja, [2]Logowanie, [q]Wyjście: "))
            if choice == "1":
                Organizer.rejestracja(self)
            elif choice == "2":
                Organizer.logowanie(self)
            elif choice == "q" or choice.lower == "q" or choice.upper() == "Q":
                print("Żegnaj!")
                break
            else:
                print("Zły wybór!")

    def rejestracja(self):
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as users:
                readusers = users.read()
                if self.user.lower() in readusers:
                    print("Podany użytkownik istnieje. Uzyj opcji \"Logowanie\"")
                elif self.user in readusers:
                    print("Podany użytkownik istnieje. Uzyj opcji \"Logowanie\"")
                else:
                    with open("users.txt", "a") as addusers:
                        addusers.write(self.user.lower() + " " + self.psw + "\n")
                        print("Użytkownik dodany!")
        else:
            with open("users.txt", "x") as createusers:
                createusers.write(self.user.lower() + " " + self.psw + "\n")
                print("Użytkownik dodany!")

    def logowanie(self):
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as users:
                checkusers = users.readlines()
                if (self.user.lower() + " " + self.psw + "\n") in checkusers:
                    print("Witaj, " + self.user + "!")
                    Organizer.wybor_opcji(self)
                elif (self.user + " " + self.psw + "\n") in checkusers:
                    print("Witaj, " + self.user + "!")
                    Organizer.wybor_opcji(self)
                else:
                    print("Zły login lub hasło!")
        else:
            print("Brak użytkowników! Użyj opcji \"Zarejestruj\"")

    def wybor_opcji(self):
        while True:
            choice2 = str(input("Wybierz którą kategorię chcesz wybrać: [1]Notatki, [2]Zadania, [q]Wyloguj: "))
            if choice2 == "1":
                Organizer.menu_notatki(self)
            elif choice2 == "2":
                Organizer.menu_zadania(self)
            elif choice2 == "3":
                print(datetime.date.today())
            elif choice2 == "q" or choice2.lower == "q" or choice2.upper() == "Q":
                break
            else:
                print("Zły wybór")

    def menu_zadania(self):
        while True:
            menu2 = str(input("Wybierz opcję: [1]Utwórz zadanie, "
                              "[2]Wyświetl zadania, "
                              "[3]Usuń zadanie, "
                              "[4]Usuń wszystkie zadania, "
                              "[5]Wyświetl zadania (od nadchodzących) "
                              "[q]Wyjdź z menu: "))
            if menu2 == "1":
                Organizer.dodaj_zadanie(self)
            elif menu2 == "2":
                Organizer.wyswietl_zadania(self)
            elif menu2 == "3":
                Organizer.usun_zadanie(self)
            elif menu2 == "4":
                Organizer.usun_zadania(self)
            elif menu2 == "5":
                Organizer.sortowanie_zadan(self)
            elif menu2 == "q" or menu2.lower == "q" or menu2.upper() == "Q":
                break
            else:
                print("Zły wybór!")

    def menu_notatki(self):
        while True:
            menu1 = str(input("Wybierz opcję: [1]Stwórz notatkę, "
                              "[2]Wyświetl notatki, "
                              "[3]Usuń notatkę, "
                              "[4]Usuń wszystkie notatki, "
                              "[q]Wyjdź z menu: "))
            if menu1 == "1":
                Organizer.dodaj_notatke(self)
            elif menu1 == "2":
                Organizer.wyswietl_notatki(self)
            elif menu1 == "3":
                Organizer.usun_notatke(self)
            elif menu1 == "4":
                Organizer.usun_notatki(self)
            elif menu1 == "q" or menu1.lower == "q" or menu1.upper() == "Q":
                break
            else:
                print("Zły wybór!")

    def dodaj_notatke(self):
        notatka = str(input("Wpisz swoją notatkę: "))
        if os.path.exists("notes"):
            if os.path.exists("notes/%s.txt" % self.user.lower()):
                with open("notes/%s.txt" % self.user.lower(), "a") as addnote:
                    addnote.write(notatka + "\n")
                    print("Notatka dodana!")
            else:
                with open("notes/%s.txt" % self.user.lower(), "x") as addnote:
                    addnote.write(notatka + "\n")
                    print("Notatka dodana!")
        else:
            os.makedirs("notes")
            with open("notes/%s.txt" % self.user.lower(), "x") as addnote:
                addnote.write(notatka + "\n")
                print("Notatka dodana!")

    def dodaj_zadanie(self):
        zadanie = str(input("Wpisz zadanie: "))
        data = str(input("Wpisz datę (RRRR-MM-DD): "))
        if os.path.exists("tasks"):
            if os.path.exists("tasks/%s.txt" % self.user.lower()):
                with open("tasks/%s.txt" % self.user.lower(), "a") as addtask:
                    addtask.write(data + " " + zadanie + "\n")
                    print("Zadanie dodane!")
            else:
                with open("tasks/%s.txt" % self.user.lower(), "x") as addtask:
                    addtask.write(data + " " + zadanie + "\n")
                    print("Zadanie dodane!")
        else:
            os.makedirs("tasks")
            with open("tasks/%s.txt" % self.user.lower(), "x") as addtask:
                addtask.write(data + " " + zadanie + "\n")
                print("Zadanie dodane!")

    def wyswietl_notatki(self):
        if os.path.exists("notes/%s.txt" % self.user.lower()):
            with open("notes/%s.txt" % self.user.lower(), "r") as readnotes:
                for lines in readnotes:
                    print(lines.rstrip())
        else:
            print("Brak notatek!")

    def wyswietl_zadania(self):
        if os.path.exists("tasks/%s.txt" % self.user.lower()):
            with open("tasks/%s" % self.user.lower(), "r") as readtasks:
                for lines in readtasks:
                    print(lines.rstrip())
        else:
            print("Brak notatek!")

    def usun_zadania(self):
        if os.path.exists("tasks/%s.txt" % self.user):
            check = str(input("Czy chcesz trwale usunąć wszystkie zadania? [y]Tak, [n]Nie: "))
            if check == "y" or check.lower() == "y" or check.upper() == "Y":
                with open("tasks/%s.txt" % self.user, "w") as deletetasks:
                    deletetasks.close()
                print("Zadania zosatały usunięte!")
            elif check == "n" or check.lower() == "n" or check.upper() == "N":
                pass
        else:
            print("Brak zadań do usunięcia!")

    def usun_zadanie(self):
        if os.path.exists("tasks/%s.txt" % self.user):
            dtask = str(input("Wpisz nazwę zadania: "))
            dtaskdate = str(input("Wpisz datę tego zadania (RRRR-MM-DD): "))
            with open("tasks/%s.txt" % self.user, "r") as readtask:
                readtaskls = readtask.readlines()
            with open("tasks/%s.txt" % self.user, "w") as writelines:
                for line in readtaskls:
                    if line.strip("\n") != (dtaskdate + " " + dtask):
                        writelines.write(line)
                        print("Zadanie usunięte!")
        else:
            print("Brak zadań do usunięcia!")

    def usun_notatki(self):
        if os.path.exists("notes/%s.txt" % self.user):
            check2 = str(input("Czy chcesz trwale usunąć wszystkie notatki? [y]Tak, [n]Nie: "))
            if check2 == "y" or check2.lower() == "y" or check2.upper() == "Y":
                with open("notes/%s.txt" % self.user, "w") as deletenotes:
                    deletenotes.close()
                print("Notatki zostały usunięte!")
            elif check2 == "n" or check2.lower() == "n" or check2.upper() == "N":
                pass
        else:
            print("Brak notatek do usunięcia!")

    def usun_notatke(self):
        if os.path.exists("notes/%s.txt" % self.user):
            dnote = str(input("Wpisz którą notatkę usunąć: "))
            with open("notes/%s.txt" % self.user, "r") as readnote:
                readnotels = readnote.readlines()
            with open("notes/%s.txt" % self.user, "w") as writelines:
                for line in readnotels:
                    if line.strip("\n") != dnote:
                        writelines.write(line)
                        print("Notatka usunięta!")

    def sortowanie_zadan(self):
        with open("tasks/%s.txt" % self.user, "r") as readtasks:
            task_temp = []
            for line in readtasks:
                temp_lines = line.splitlines()
                for i in temp_lines:
                    task_temp.append(i)
            task_temp.sort()
            for i in task_temp:
                print(i)
            task_temp.clear()


Organizer().main()
