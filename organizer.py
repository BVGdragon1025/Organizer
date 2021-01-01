import datetime  # Użyję później do sortowania, lub czegoś innego

import os.path  # Przydatne do paru rzeczy :)

#  import tkinter : Na ten moment tego nie używam
#  Plus moja wiedza o klasach i obiektach jest na poziomie przypominania sobie


class Organizer:
    """def dane_user(self,user,psw):
        user = str(input("Podaj nazwę użytkownika: "))
        psw = str(input("Podaj hasło: "))
"""
    def rejestracja(self):
        user = str(input("Podaj nazwę użytkownika: "))
        psw = str(input("Podaj hasło: "))
        with open("users.txt", "r") as users:
            readusers = users.read()
            if os.path.exists("users.txt"):
                if user.lower() in readusers:
                    print("Podany użytkownik istnieje. Uzyj opcji \"Logowanie\"")
                elif user in readusers:
                    print("Podany użytkownik istnieje. Uzyj opcji \"Logowanie\"")
                else:
                    with open("users.txt", "a") as addusers:
                        addusers.write(user.lower() + " " + psw + "\n")
                        print("Użytkownik dodany!")
            else:
                with open("users.txt", "x") as createusers:
                    createusers.write(user.lower() + " " + psw + "\n")
                    print("Użytkownik dodany!")

    def logowanie(self):
        user = str(input("Podaj nazwę użytkownika: "))
        psw = str(input("Podaj hasło: "))
        with open("users.txt", "r") as users:
            checkusers = users.readlines()
            if (user.lower() + " " + psw + "\n") in checkusers:
                print("Witaj, " + user + "!")
                Organizer.wybor_opcji(self)
            elif (user + " " + psw + "\n") in checkusers:
                print("Witaj, " + user + "!")
                Organizer.wybor_opcji(self)
            else:
                print("Zły login lub hasło!")
        return user

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
                              "[q]Wyjdź z menu: "))
            if menu2 == "1":
                Organizer.dodaj_zadanie(self)
            elif menu2 == "2":
                Organizer.wyswietl_zadania(self)
            elif menu2 == "3":
                Organizer.usun_zadanie(self)
            elif menu2 == "4":
                Organizer.usun_zadania(self)
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
        if os.path.exists("notes/notes.txt"):
            with open("notes/notes.txt", "a") as addnote:
                addnote.write(notatka + "\n")
                print("Notatka dodana!")
        else:
            os.makedirs("notes")
            with open("notes/notes.txt", "x") as addnote:
                addnote.write(notatka + "\n")
                print("Notatka dodana!")

    def dodaj_zadanie(self):
        zadanie = str(input("Wpisz zadanie: "))
        data = str(input("Wpisz datę (RRRR-MM-DD): "))
        if os.path.exists("tasks/tasks.txt"):
            with open("tasks/tasks.txt", "a") as addtask:
                addtask.write(zadanie + " " + data + "\n")
                print("Zadanie dodane!")
        else:
            os.makedirs("tasks")
            with open("tasks/tasks.txt", "x") as addtask:
                addtask.write(zadanie + " " + data + "\n")
                print("Zadanie dodane!")

    def wyswietl_notatki(self):
        if os.path.exists("notes/notes.txt"):
            with open("notes/notes.txt", "r") as readnotes:
                for lines in readnotes:
                    print(lines)
        else:
            print("Brak notatek!")

    def wyswietl_zadania(self):
        if os.path.exists("tasks/tasks.txt"):
            with open("tasks/tasks.txt", "r") as readtasks:
                for lines in readtasks:
                    print(lines)
        else:
            print("Brak notatek!")

    def usun_zadania(self):
        if os.path.exists("tasks/tasks.txt"):
            check = str(input("Czy chcesz trwale usunąć wszystkie zadania? [y]Tak, [n]Nie: "))
            if check == "y" or check.lower() == "y" or check.upper() == "Y":
                with open("tasks/tasks.txt", "w") as deletetasks:
                    deletetasks.close()
                print("Zadania zosatały usunięte!")
            elif check == "n" or check.lower() == "n" or check.upper() == "N":
                pass
        else:
            print("Brak zadań do usunięcia!")

    def usun_zadanie(self):
        if os.path.exists("tasks/tasks.txt"):
            dtask = str(input("Wpisz nazwę zadania: "))
            dtaskdate = str(input("Wpisz datę tego zadania (RRRR-MM-DD): "))
            with open("tasks/tasks.txt", "r") as readtask:
                readtaskls = readtask.readlines()
            with open("tasks/tasks.txt", "w") as writelines:
                for line in readtaskls:
                    if line.strip("\n") != (dtask + " " + dtaskdate):
                        writelines.write(line)
                        print("Zadanie usunięte!")
        else:
            print("Brak zadań do usunięcia!")

    def usun_notatki(self):
        if os.path.exists("notes/notes.txt"):
            check2 = str(input("Czy chcesz trwale usunąć wszystkie notatki? [y]Tak, [n]Nie: "))
            if check2 == "y" or check2.lower() == "y" or check2.upper() == "Y":
                with open("notes/notes.txt", "w") as deletenotes:
                    deletenotes.close()
                print("Notatki zostały usunięte!")
            elif check2 == "n" or check2.lower() == "n" or check2.upper() == "N":
                pass
        else:
            print("Brak notatek do usunięcia!")

    def usun_notatke(self):
        if os.path.exists("notes/notes.txt"):
            dnote = str(input("Wpisz którą notatkę usunąć: "))
            with open("notes/notes.txt", "r") as readnote:
                readnotels = readnote.readlines()
            with open("notes/notes.txt", "w") as writelines:
                for line in readnotels:
                    if line.strip("\n") != dnote:
                        writelines.write(line)
                        print("Notatka usunięta!")


while True:
    choice = str(input("Wybierz co chcesz zrobić: [1]Rejestracja, [2]Logowanie, [q]Wyjście: "))
    lg = Organizer()
    if choice == "1":
        lg.rejestracja()
    elif choice == "2":
        lg.logowanie()
    elif choice == "q" or choice.lower == "q" or choice.upper() == "Q":
        print("Żegnaj!")
        break
    else:
        print("Zły wybór!")
