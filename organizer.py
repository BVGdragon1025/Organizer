#  import datetime : Uzyję później do sortowania, lub czegoś innego

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
            choice2 = str(input("Wybierz co chcesz zrobić:"
                                "[1]Dodać notatkę "
                                "[2]Dodać zadanie "
                                "[3]Sprawdzic zapisane notatki "
                                "[4]Sprawdzić zadania "
                                "[q]Wylogować się: "))
            if choice2 == "1":
                Organizer.dodaj_notatke(self)
            elif choice2 == "2":
                Organizer.dodaj_zadanie(self)
            elif choice2 == "3":
                Organizer.wyswietl_notatki(self)
            elif choice2 == "4":
                Organizer.wyswietl_zadania(self)
            elif choice2 == "q":
                break
            else:
                print("Zły wybór")
                continue

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
        data = str(input("Wpisz datę (DD/MM/RRR): "))
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


while True:
    choice = str(input("Wybierz co chcesz zrobić: [1]Rejestracja, [2]Logowanie, [q]Wyjście: "))
    lg = Organizer()
    if choice == "1":
        lg.rejestracja()
    elif choice == "2":
        lg.logowanie()
    elif choice == "q":
        print("Żegnaj!")
        break
