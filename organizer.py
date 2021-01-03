import datetime  # Użyję później do sortowania, lub czegoś innego

import os  # Przydatne do paru rzeczy :)


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
            menu2 = str(input("Wybierz opcję: [1]Utwórz..., "
                              "[2]Wyświetl... "
                              "[3]Usuń..., "
                              "[4]Modyfikuj..."
                              "[q]Wyjdź z menu: "))
            if menu2 == "1":
                Organizer.menu_utworz_zadanie(self)
            elif menu2 == "2":
                Organizer.menu_wyswietl_zadanie(self)
            elif menu2 == "3":
                Organizer.menu_usun_zadanie(self)
            elif menu2 == "4":
                pass
            elif menu2 == "q" or menu2.lower == "q" or menu2.upper() == "Q":
                break
            else:
                print("Zły wybór!")

    def menu_notatki(self):
        while True:
            menu1 = str(input("Wybierz opcję: [1]Dodaj..., "
                              "[2]Wyświetl..., "
                              "[3]Usuń..., "
                              "[q]Wyjdź z menu: "))
            if menu1 == "1":
                Organizer.menu_dodaj_notatke(self)
            elif menu1 == "2":
                Organizer.menu_wyswietl_notatke(self)
            elif menu1 == "3":
                Organizer.menu_usun_notatke(self)
            elif menu1 == "q" or menu1.lower == "q" or menu1.upper() == "Q":
                break
            else:
                print("Zły wybór!")

    def dodaj_notatke(self):
        notatka = str(input("Wpisz swoją notatkę: "))
        if os.path.exists("notes"):
            if os.path.exists("notes/" + self.user.lower()):
                if os.path.exists("notes/"+self.user.lower()+"/%s.txt" % self.user.lower()):
                    with open("notes/"+self.user.lower()+"/%s.txt" % self.user.lower(), "a") as addnote:
                        addnote.write(notatka + "\n")
                        print("Notatka dodana!")
                else:
                    with open("notes/"+self.user.lower()+"/%s.txt" % self.user.lower(), "x") as addnote:
                        addnote.write(notatka + "\n")
                        print("Notatka dodana!")
            else:
                os.makedirs("notes/"+self.user.lower())
                with open("notes/"+self.user.lower()+"/%s.txt" % self.user.lower(), "x") as addnote:
                    addnote.write(notatka + "\n")
                    print("Notatka dodana!")
        else:
            os.makedirs("notes/"+self.user.lower())
            with open("notes/"+self.user.lower()+"/%s.txt" % self.user.lower(), "x") as addnote:
                addnote.write(notatka + "\n")
                print("Notatka dodana!")

    def dodaj_zadanie(self):
        zadanie = str(input("Wpisz zadanie: "))
        data = str(input("Wpisz datę (RRRR-MM-DD): "))
        if os.path.exists("tasks"):
            if os.path.exists("tasks/"+self.user.lower()):
                if os.path.exists("tasks/"+self.user.lower()+"/%s.txt" % self.user.lower()):
                    with open("tasks/"+self.user.lower()+"/%s.txt" % self.user.lower(), "a") as addtask:
                        addtask.write(data + " " + zadanie + "\n")
                        print("Zadanie dodane!")
                else:
                    with open("tasks/"+self.user.lower()+"/%s.txt" % self.user.lower(), "x") as addtask:
                        addtask.write(data + " " + zadanie + "\n")
                        print("Zadanie dodane!")
            else:
                os.makedirs("tasks/"+self.user.lower())
                with open("tasks/"+self.user.lower()+"/%s.txt" % self.user.lower(), "x") as addtask:
                    addtask.write(data + " " + zadanie + "\n")
                    print("Zadanie dodane!")
        else:
            os.makedirs("tasks/"+self.user.lower())
            with open("tasks/"+self.user.lower()+"/%s.txt" % self.user.lower(), "x") as addtask:
                addtask.write(data + " " + zadanie + "\n")
                print("Zadanie dodane!")

    def wyswietl_notatki(self):
        if os.path.exists("notes/"+self.user.lower()+"/%s.txt" % self.user.lower()):
            with open("notes/"+self.user.lower()+"/%s.txt" % self.user.lower(), "r") as readnotes:
                for lines in readnotes:
                    print(lines.rstrip())
        else:
            print("Brak notatek!")

    def wyswietl_zadania(self):
        if os.path.exists("tasks/"+self.user.lower()+"/%s.txt" % self.user.lower()):
            with open("tasks/"+self.user.lower()+"/%s.txt" % self.user.lower(), "r") as readtasks:
                for lines in readtasks:
                    print(lines.rstrip())
        else:
            print("Brak notatek!")

    def usun_wsz_zadania(self):
        if os.path.exists("tasks/"+self.user.lower()+"/%s.txt" % self.user):
            check = str(input("Czy chcesz trwale usunąć wszystkie zadania? [y]Tak, [n]Nie: "))
            if check == "y" or check.lower() == "y" or check.upper() == "Y":
                with open("tasks/"+self.user.lower()+"/%s.txt" % self.user, "w") as deletetasks:
                    deletetasks.close()
                print("Zadania zosatały usunięte!")
            elif check == "n" or check.lower() == "n" or check.upper() == "N":
                pass
        else:
            print("Brak zadań do usunięcia!")

    def usun_zadanie(self):
        if os.path.exists("tasks/"+self.user.lower()+"/%s.txt" % self.user):
            Organizer.wyswietl_zadania(self)
            dtask = str(input("Wpisz nazwę zadania: "))
            dtaskdate = str(input("Wpisz datę tego zadania (RRRR-MM-DD): "))
            with open("tasks/"+self.user.lower()+"/%s.txt" % self.user, "r") as readtask:
                readtaskls = readtask.readlines()
            with open("tasks/"+self.user.lower()+"/%s.txt" % self.user, "w") as writelines:
                for line in readtaskls:
                    if line.strip("\n") != (dtaskdate + " " + dtask):
                        writelines.write(line)
            print("Zadanie usunięte!")
        else:
            print("Brak zadań do usunięcia!")

    def usun_wsz_notatki(self):
        if os.path.exists("notes/"+self.user.lower()+"/%s.txt" % self.user):
            check2 = str(input("Czy chcesz trwale usunąć wszystkie notatki? [y]Tak, [n]Nie: "))
            if check2 == "y" or check2.lower() == "y" or check2.upper() == "Y":
                with open("notes/"+self.user.lower()+"/%s.txt" % self.user, "w") as deletenotes:
                    deletenotes.close()
                print("Notatki zostały usunięte!")
            elif check2 == "n" or check2.lower() == "n" or check2.upper() == "N":
                pass
        else:
            print("Brak notatek do usunięcia!")

    def usun_notatke(self):
        if os.path.exists("notes/"+self.user.lower()+"/%s.txt" % self.user):
            Organizer.wyswietl_notatki(self)
            dnote = str(input("Wpisz którą notatkę usunąć: "))
            with open("notes/"+self.user.lower()+"/%s.txt" % self.user, "r") as readnote:
                readnotels = readnote.readlines()
            with open("notes/"+self.user.lower()+"/%s.txt" % self.user, "w") as writelines:
                for line in readnotels:
                    if line.strip("\n") != dnote:
                        writelines.write(line)
            print("Notatka usunięta!")

    def sortowanie_zadan(self):
        if os.path.exists("tasks/"+self.user.lower()+"/%s.txt" % self.user.lower()):
            with open("tasks/"+self.user.lower()+"/%s.txt" % self.user, "r") as readtasks:
                task_temp = []
                for line in readtasks:
                    temp_lines = line.splitlines()
                    for i in temp_lines:
                        task_temp.append(i)
                task_temp.sort()
                for i in task_temp:
                    print(i)
            task_temp.clear()
        else:
            print("Brak zadań do posortowania!")

    def dodaj_notatki(self):
        ilosc = int(input("Ile notatek chcesz dodać (liczbowo): "))
        i = 0
        while i != ilosc:
            Organizer.dodaj_notatke(self)
            i += 1

    def dodaj_zadania(self):
        ilosc = int(input("Ile zadań chcesz dodać (liczbowo): "))
        i = 0
        while i != ilosc:
            Organizer.dodaj_zadanie(self)
            i += 1

    def usun_zadania(self):
        print("Twoje zadania: ")
        Organizer.wyswietl_zadania(self)
        ilosc = int(input("Ile zadań chcesz usunąć (liczbowo): "))
        i = 0
        while i != ilosc:
            Organizer.usun_zadanie(self)
            i += 1

    def usun_notatki(self):
        print("Twoje notatki: ")
        Organizer.wyswietl_notatki(self)
        ilosc = int(input("Ile notatek chcesz usunąć (liczbowo): "))
        i = 0
        while i != ilosc:
            Organizer.usun_notatke(self)
            i += 1

    def menu_utworz_zadanie(self):
        while True:
            menu = str(input("Wybierz opcję: "
                             "[1]Utwórz zadanie, "
                             "[2]Utwórz kilka zadań, "
                             "[3]Utwórz listę zadań, "
                             "[q]Wyjdź z menu: "))
            if menu == "1":
                Organizer.dodaj_zadanie(self)
            elif menu == "2":
                Organizer.dodaj_zadania(self)
            elif menu == "3":
                Organizer.lista_zadan(self)
            elif menu == "q" or menu.lower() == "q":
                break
            else:
                print("Zły wybór!")

    def menu_dodaj_notatke(self):
        while True:
            menu = str(input("Wybierz opcję: "
                             "[1]Dodaj notatkę, "
                             "[2]Dodaj kilka notatek, "
                             "[3]Stwórz listę rzeczy, "
                             "[q]Wyjdź z menu: "))
            if menu == "1":
                Organizer.dodaj_notatke(self)
            elif menu == "2":
                Organizer.dodaj_notatki(self)
            elif menu == "3":
                Organizer.lista_rzeczy(self)
            elif menu == "q" or menu.lower == "q":
                break
            else:
                print("Zły wybór")

    def menu_wyswietl_zadanie(self):
        while True:
            menu = str(input("Wybierz opcję: "
                             "[1]Wyświetl zadania, "
                             "[2]Wyświetl listę zadań, "
                             "[3]Wyświetl zadania (od nadchodzących), "
                             "[4]Wyświetl aktywne zadania, "
                             "[5]Wyświetl ukończone zadania, "
                             "[q]Wyjdź z menu: "))
            if menu == "1":
                Organizer.wyswietl_zadania(self)
            elif menu == "2":
                Organizer.wyswietl_liste_zadan(self)
            elif menu == "3":
                Organizer.sortowanie_zadan(self)
            elif menu == "4":
                pass
            elif menu == "5":
                pass
            elif menu == "q" or menu.lower == "q":
                break
            else:
                print("Zły wybór")

    def menu_wyswietl_notatke(self):
        while True:
            menu = str(input("Wybierz opcję: "
                             "[1]Wyświetl notatki, "
                             "[2]Wyświetl listę rzeczy, "
                             "[q]Wyjdź z menu: "))
            if menu == "1":
                Organizer.wyswietl_notatki(self)
            elif menu == "2":
                Organizer.wyswietl_liste_rzeczy(self)
            elif menu == "q" or menu.lower == "q":
                break
            else:
                print("Zły wybór")

    def menu_usun_zadanie(self):
        while True:
            menu = str(input("Wybierz opcję: "
                             "[1]Usuń zadanie, "
                             "[2]Usuń kilka zadań, "
                             "[3]Usuń wszystkie zadania, "
                             "[4]Usuń listę zadań, "
                             "[5]Usuń ukończone zadania, "
                             "[q]Wyjdź z menu: "))
            if menu == "1":
                Organizer.usun_zadanie(self)
            elif menu == "2":
                Organizer.usun_zadania(self)
            elif menu == "3":
                Organizer.usun_wsz_zadania(self)
            elif menu == "4":
                Organizer.usun_liste_zadan(self)
            elif menu == "5":
                pass
            elif menu == "q" or menu.lower == "q":
                break
            else:
                print("Zły wybór")

    def menu_usun_notatke(self):
        while True:
            menu = str(input("Wybierz opcję: "
                             "[1]Usuń notatkę, "
                             "[2]Usuń kilka notatek, "
                             "[3]Usuń wszystkie notatki, "
                             "[4]Usuń listę rzeczy, "
                             "[q]Wyjdź z menu: "))
            if menu == "1":
                Organizer.usun_notatke(self)
            elif menu == "2":
                Organizer.usun_notatki(self)
            elif menu == "3":
                Organizer.usun_wsz_notatki(self)
            elif menu == "4":
                Organizer.usun_liste_rzeczy(self)
            elif menu == "q" or menu.lower == "q":
                break
            else:
                print("Zły wybór")

    def lista_rzeczy(self):
        tytul = str(input("Podaj tytuł listy: "))
        ilosc = int(input("Podaj ilość pozycji (numerycznie): "))
        i = 0
        if os.path.exists("notes"):
            if os.path.exists("notes/"+self.user.lower()+"/notes_list"):
                with open("notes/"+self.user.lower()+"/notes_list/"+tytul+".txt", "x") as create_list:
                    create_list.write(tytul + ":\n")
                with open("notes/"+self.user.lower()+"/notes_list/"+tytul+".txt", "a") as make_list:
                    while i != ilosc:
                        poz = str(input("Wpisz coś (jeszcze "+str(ilosc-i)+"): "))
                        make_list.write(poz+"\n")
                        i += 1
                print("Lista stworzona!")
            else:
                os.makedirs("notes/"+self.user.lower()+"/notes_list")
                with open("notes/" + self.user.lower() + "/notes_list/" + tytul + ".txt", "x") as create_list:
                    create_list.write(tytul + ":\n")
                with open("notes/" + self.user.lower() + "/notes_list/" + tytul + ".txt", "a") as make_list:
                    while i != ilosc:
                        poz = str(input("Wpisz coś (jeszcze "+str(ilosc-i)+"): "))
                        make_list.write(poz+"\n")
                        i += 1
                print("Lista stworzona!")
        else:
            os.makedirs("notes/"+self.user.lower()+"/notes_list")
            with open("notes/" + self.user.lower() + "/notes_list/" + tytul + ".txt", "x") as create_list:
                create_list.write(tytul + ":\n")
            with open("notes/" + self.user.lower() + "/notes_list/" + tytul + ".txt", "a") as make_list:
                while i != ilosc:
                    poz = str(input("Wpisz coś (jeszcze "+str(ilosc-i)+"): "))
                    make_list.write(poz+"\n")
                    i += 1
            print("Lista stworzona!")

    def lista_zadan(self):
        tytul = str(input("Podaj tytuł listy zadań: "))
        ilosc = int(input("Podaj ilość zadań (numerycznie): "))
        czas = str(input("Podaj datę (RRRR-MM-DD): "))
        i = 0
        if os.path.exists("tasks"):
            if os.path.exists("tasks/"+self.user.lower()+"/tasks_list"):
                with open("tasks/"+self.user.lower()+"/tasks_list/"+tytul+".txt", "x") as create_list:
                    create_list.write(czas+" "+tytul+"\n")
                with open("tasks/" + self.user.lower() + "/tasks_list/" + tytul + ".txt", "a") as make_list:
                    while i != ilosc:
                        poz = str(input("Wpisz zadanie (jeszcze "+str(ilosc-i)+"): "))
                        make_list.write(poz+"\n")
                        i += 1
                print("Lista stworzona!")
            else:
                os.makedirs("tasks/"+self.user.lower()+"/tasks_list")
                with open("tasks/"+self.user.lower()+"/tasks_list/"+tytul+".txt", "x") as create_list:
                    create_list.write(czas + " " + tytul+"\n")
                with open("tasks/"+self.user.lower()+"/tasks_list/"+tytul+".txt", "a") as make_list:
                    while i != ilosc:
                        poz = str(input("Wpisz zadanie (jeszcze "+str(ilosc-i)+"): "))
                        make_list.write(poz+"\n")
                        i += 1
                print("Lista stworzona!")
        else:
            os.makedirs("tasks/"+self.user.lower()+"/tasks_list")
            with open("tasks/" + self.user.lower() + "/tasks_list/" + tytul + ".txt", "x") as create_list:
                create_list.write(czas + " " + tytul+"\n")
            with open("tasks/" + self.user.lower() + "/tasks_list/" + tytul + ".txt", "a") as make_list:
                while i != ilosc:
                    poz = str(input("Wpisz zadanie (jeszcze " + str(ilosc - i) + "): "))
                    make_list.write(poz+"\n")
                    i += 1
            print("Lista stworzona!")

    def wyswietl_liste_zadan(self):
        if os.path.exists("tasks/"+self.user.lower()+"/tasks_list"):
            listy = os.listdir("tasks/" + self.user.lower() + "/tasks_list")
            print("Twoje listy zadań: ")
            print(listy)
            wybor = str(input("Wpisz nazwę listy do wyświetlenia (bez .txt): "))
            if os.path.exists("tasks/"+self.user.lower()+"/tasks_list/"+wybor+".txt"):
                with open("tasks/"+self.user.lower()+"/tasks_list/"+wybor+".txt", "r") as read_list:
                    for line in read_list:
                        print(line.rstrip())
            else:
                print("Nie ma takiej listy!")
        else:
            print("Brak list zadań!")

    def wyswietl_liste_rzeczy(self):
        if os.path.exists("notes/"+self.user.lower()+"/notes_list"):
            listy = os.listdir("tasks/" + self.user.lower() + "/notes_list")
            print("Twoje listy rzeczy: ")
            print(listy)
            wybor = str(input("Wpisz nazwę listy do wyświetlenia (bez.txt): "))
            if os.path.exists("notes/"+self.user.lower()+"/notes_list/"+wybor+".txt"):
                with open("notes/"+self.user.lower()+"/notes_list/"+wybor+".txt", "r") as read_list:
                    for line in read_list:
                        print(line.rstrip())
            else:
                print("Nie ma takiej listy!")
        else:
            print("Brak list rzeczy!")

    def usun_liste_zadan(self):
        if os.path.exists("tasks/"+self.user.lower()+"/tasks_list"):
            listy = os.listdir("tasks/"+self.user.lower()+"/tasks_list")
            print("Twoje listy zadań: ")
            print(listy)
            wybor = str(input("Wpisz nazwę listy do usunięcia (bez.txt): "))
            if os.path.exists("tasks/" + self.user.lower() + "/tasks_list/" + wybor + ".txt"):
                os.remove("tasks/" + self.user.lower() + "/tasks_list/" + wybor + ".txt")
                print("Lista zadań usunięta!")
            else:
                print("Nie ma takiej listy do usunięcia!")

    def usun_liste_rzeczy(self):
        if os.path.exists("notes/"+self.user.lower()+"/notes_list"):
            listy = os.listdir("tasks/" + self.user.lower() + "/notes_list")
            print("Twoje listy rzeczy: ")
            print(listy)
            wybor = str(input("Wpisz nazwę listy do usunięcia (bez.txt): "))
            if os.path.exists("notes/" + self.user.lower() + "/notes_list/" + wybor + ".txt"):
                os.remove("notes/" + self.user.lower() + "/notes_list/" + wybor + ".txt")
                print("Lista zadań usunięta!")
            else:
                print("Nie ma takiej listy do usunięcia!")


Organizer().main()
