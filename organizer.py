# import datetime   Użyję później do sortowania, lub czegoś innego

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

    def main(self):  # Główne menu, które powinno sie pojawiać najpierw, ale zrobiłem to coś na górze :)
        while True:
            choice = str(input("Wybierz co chcesz zrobić: [1]Rejestracja, [2]Logowanie, [q]Wyjście: "))
            if choice == "1":
                Organizer.rejestracja(self)
            elif choice == "2":
                Organizer.logowanie(self)
            elif choice == "q" or choice.lower == "q":
                print("Żegnaj!")
                break
            else:
                print("Zły wybór!")

    def rejestracja(self):  # Zapisuje login i hasło do pliku "users.txt"
        #  Na ten moment jest to kompletnie nie szyfrowane :)
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as users:  # Zamiast users = file.open("users.txt", "r")
                readusers = users.read()
                if self.user.lower() in readusers:  # Tak samo jak wyżej
                    print("Podany użytkownik istnieje. Uzyj opcji \"Logowanie\"")
                elif self.user in readusers:
                    print("Podany użytkownik istnieje. Uzyj opcji \"Logowanie\"")
                else:
                    with open("users.txt", "a") as addusers:  # Dodaje login i hasło w takim formacie do pliku
                        addusers.write(self.user.lower() + " " + self.psw + "\n")
                        print("Użytkownik dodany!")
        else:  # Na wypaddek gdyby nie było pliku
            with open("users.txt", "x") as createusers:
                createusers.write(self.user.lower() + " " + self.psw + "\n")
                print("Użytkownik dodany!")

    def logowanie(self):  # Sprawdza czy kombinacja loginu i hasła jest w pliku "users.txt"
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as users:
                checkusers = users.readlines()  # Odczytuje linie w pliku
                if (self.user.lower() + " " + self.psw + "\n") in checkusers:
                    print("Witaj, " + self.user + "!")
                    Organizer.wybor_opcji(self)  # Funkcja wyświetlająca menu wyboru
                elif (self.user + " " + self.psw + "\n") in checkusers:
                    print("Witaj, " + self.user + "!")
                    Organizer.wybor_opcji(self)
                else:
                    print("Zły login lub hasło!")
        else:
            print("Brak użytkowników! Użyj opcji \"Zarejestruj\"")

    def wybor_opcji(self):  # Wybór opcji.
        while True:
            choice2 = str(input("Wybierz którą kategorię chcesz wybrać: "
                                "[1]Notatki, "
                                "[2]Zadania, "
                                "[3]Pomoc, "
                                "[q]Wyloguj: "))
            if choice2 == "1":
                Organizer.menu_notatki(self)
            elif choice2 == "2":
                Organizer.menu_zadania(self)
            elif choice2 == "3":
                Organizer.menu_pomoc(self)
            elif choice2 == "q" or choice2.lower == "q":
                break
            else:
                print("Zły wybór")

    def menu_zadania(self):
        while True:
            menu2 = str(input("Wybierz opcję: [1]Utwórz..., "
                              "[2]Wyświetl... "
                              "[3]Usuń..., "
                              "[4]Modyfikuj... , "
                              "[q]Wyjdź z menu: "))
            if menu2 == "1":
                Organizer.menu_utworz_zadanie(self)
            elif menu2 == "2":
                Organizer.menu_wyswietl_zadanie(self)
            elif menu2 == "3":
                Organizer.menu_usun_zadanie(self)
            elif menu2 == "4":
                Organizer.menu_modyfikuj(self)
            elif menu2 == "q" or menu2.lower == "q":
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
            elif menu1 == "q" or menu1.lower == "q":
                break
            else:
                print("Zły wybór!")

    def dodaj_notatke(self):  # Dodaje notatkę do pliku.
        # Dopisalem wszelkie zabezpieczenia na wypadek braku pliku etc.
        # Notatki są w lokalizacji "notes/nazwa_użytkownika/notes.txt"
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

    def dodaj_zadanie(self):  # Dodaje zadanie do pliku.
        # Dopisalem wszelkie zabezpieczenia na wypadek braku pliku etc.
        # Notatki są w lokalizacji "tasks/nazwa_użytkownika/tasks.txt"
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

    def wyswietl_notatki(self):  # Jak nazwa wskazuje
        if os.path.exists("notes/"+self.user.lower()+"/%s.txt" % self.user.lower()):
            with open("notes/"+self.user.lower()+"/%s.txt" % self.user.lower(), "r") as readnotes:
                for lines in readnotes:
                    print(lines.rstrip())  # Obcina puste linie powstałe przez "\n"
        else:
            print("Brak notatek!")

    def wyswietl_zadania(self):
        if os.path.exists("tasks/"+self.user.lower()+"/%s.txt" % self.user.lower()):
            with open("tasks/"+self.user.lower()+"/%s.txt" % self.user.lower(), "r") as readtasks:
                for lines in readtasks:
                    print(lines.rstrip())  # Obcina puste linie powstałe przez "\n"
        else:
            print("Brak notatek!")

    def usun_wsz_zadania(self):  # Działanie jest proste:
        # Otwórz plik w trybie zapisu i zamknij go. Wszelkie dane zostaną nadpisane :)
        if os.path.exists("tasks/"+self.user.lower()+"/%s.txt" % self.user):
            check = str(input("Czy chcesz trwale usunąć wszystkie zadania? [y]Tak, [n]Nie: "))
            if check == "y" or check.lower() == "y":
                with open("tasks/"+self.user.lower()+"/%s.txt" % self.user, "w") as deletetasks:
                    deletetasks.close()
                print("Zadania zosatały usunięte!")
            elif check == "n" or check.lower() == "n":
                pass
        else:
            print("Brak zadań do usunięcia!")

    def usun_zadanie(self):  # Usuwa zadanie. Aby usunęło odpowiednie, stwierdziłem, że spytam usera o nazwę i datę.
        if os.path.exists("tasks/"+self.user.lower()+"/%s.txt" % self.user):
            Organizer.wyswietl_zadania(self)
            dtask = str(input("Wpisz nazwę zadania: "))
            dtaskdate = str(input("Wpisz datę tego zadania (RRRR-MM-DD): "))
            with open("tasks/"+self.user.lower()+"/%s.txt" % self.user, "r") as readtask:
                readtaskls = readtask.readlines()
            with open("tasks/"+self.user.lower()+"/%s.txt" % self.user, "w") as writelines:
                for line in readtaskls:
                    if line.strip("\n") != (dtaskdate + " " + dtask)\
                            and line.strip("\n") != (dtaskdate + " " + dtask + " (Zrobione)"):
                        # zapisuje wszystkie linie po za tą wpisaną przez usera
                        writelines.write(line)
            print("Zadanie usunięte!")
        else:
            print("Brak zadań do usunięcia!")

    def usun_wsz_notatki(self):  # jak przy usun_wszystkie_zadania()
        if os.path.exists("notes/"+self.user.lower()+"/%s.txt" % self.user):
            check2 = str(input("Czy chcesz trwale usunąć wszystkie notatki? [y]Tak, [n]Nie: "))
            if check2 == "y" or check2.lower() == "y":
                with open("notes/"+self.user.lower()+"/%s.txt" % self.user, "w") as deletenotes:
                    deletenotes.close()
                print("Notatki zostały usunięte!")
            elif check2 == "n" or check2.lower() == "n":
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

    def sortowanie_zadan(self):  # Sortowanie zadań od najwcześniejszego.
        # W sumie nie jest to przydatne, bo nie zaimplementowałem funkcji wyświetlania ile zostało czasu.
        # Ale kto wie, może się zawsze przydać
        if os.path.exists("tasks/"+self.user.lower()+"/%s.txt" % self.user.lower()):
            with open("tasks/"+self.user.lower()+"/%s.txt" % self.user, "r") as readtasks:
                task_temp = []  # Tymczasowa tablica do przechowania zadań
                for line in readtasks:  # Odczytanie lini w pliku
                    temp_lines = line.splitlines()  # Przepisanie wszystkich lini bez "\n"
                    for i in temp_lines:
                        task_temp.append(i)  # Zapisanie wszystkiego do tej tablicy
                task_temp.sort()  # Sortowanie, jeden z powodów dlaczego data jest na początku zadania
                for i in task_temp:
                    print(i)  # Wyświetlenie wszystkiego w ładnej kolejności
            task_temp.clear()  # Wyczyszczenie tablicy na wszelki wypadek
        else:
            print("Brak zadań do posortowania!")

    def dodaj_notatki(self):
        ilosc = int(input("Ile notatek chcesz dodać (liczbowo): "))
        i = 0
        while i != ilosc:  # Prosty while, aby nie musieć przepisywać kodu, który już mam
            # Co i tak uczyniłem w późniejszych
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
                             "[5]Usuń skończone zadania, "
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

    def lista_rzeczy(self):  # Na to miałem pomysł, aby to było jako osobna lista rzeczy.
        # W tym celu tworzy osobny folder w lokalizacji z notatkami o nazwie "notes_list"
        # Nazwa listy to tytuł, który user podaje
        # Większość tego kodu to tylko upewnienie się, że plik istnieje, a jak nie to zostanie utworzony
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

    def lista_zadan(self):  # Na to miałem pomysł, aby to było jako osobna lista zadań.
        # W tym celu tworzy osobny folder w lokalizacji z zadaniami o nazwie "tasks_list"
        # Nazwa listy to tytuł, który user podaje
        # Większość tego kodu to tylko upewnienie się, że plik istnieje, a jak nie to zostanie utworzony
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

    def wyswietl_liste_zadan(self):  # Proste wyświetlenie konkretnego pliku (jego zawartości)
        if os.path.exists("tasks/"+self.user.lower()+"/tasks_list"):
            listy = os.listdir("tasks/" + self.user.lower() + "/tasks_list")
            print("Twoje listy zadań: ")
            print(listy)
            nazwa_listy = str(input("Wpisz nazwę listy do wyświetlenia (bez .txt): "))
            if os.path.exists("tasks/"+self.user.lower()+"/tasks_list/"+nazwa_listy+".txt"):
                with open("tasks/"+self.user.lower()+"/tasks_list/"+nazwa_listy+".txt", "r") as read_list:
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

    def usun_liste_zadan(self):  # Usuwa plik. Tyle.
        if os.path.exists("tasks/"+self.user.lower()+"/tasks_list"):
            listy = os.listdir("tasks/"+self.user.lower()+"/tasks_list")
            print("Twoje listy zadań: ")
            print(listy)
            wybor = str(input("Wpisz nazwę listy do usunięcia (bez.txt): "))
            check = str(input("Czy chcesz trwale usunąć listę zadań? [y]Tak, [n]Nie: "))
            if check == "y" or check.lower() == "y":
                if os.path.exists("tasks/" + self.user.lower() + "/tasks_list/" + wybor + ".txt"):
                    os.remove("tasks/" + self.user.lower() + "/tasks_list/" + wybor + ".txt")
                    print("Lista zadań usunięta!")
                else:
                    print("Nie ma takiej listy do usunięcia!")

    def usun_liste_rzeczy(self):  # Usuwa plik. Tyle.
        if os.path.exists("notes/"+self.user.lower()+"/notes_list"):
            listy = os.listdir("tasks/" + self.user.lower() + "/notes_list")
            print("Twoje listy rzeczy: ")
            print(listy)
            wybor = str(input("Wpisz nazwę listy do usunięcia (bez.txt): "))
            check = str(input("Czy chcesz trwale usunąć wszystkie zadania? [y]Tak, [n]Nie: "))
            if check == "y" or check.lower() == "y":
                if os.path.exists("notes/" + self.user.lower() + "/notes_list/" + wybor + ".txt"):
                    os.remove("notes/" + self.user.lower() + "/notes_list/" + wybor + ".txt")
                    print("Lista zadań usunięta!")
                else:
                    print("Nie ma takiej listy do usunięcia!")

    def menu_modyfikuj(self):
        while True:
            menu = str(input("Wybierz opcję: "
                             "[1]Oznacz zadanie jako ukończone, "
                             "[2]Oznacz zadanie z listy jako ukończone, "
                             "[3]Oznacz listę zadań jako skończoną, "
                             "[q]Wyjdź z menu: "))
            if menu == "1":
                Organizer.ukoncz_zadanie(self)
            elif menu == "2":
                Organizer.ukoncz_zadanie_lista(self)
            elif menu == "3":
                Organizer.ukoncz_liste(self)
            elif menu == "q" or menu.lower == "q":
                break
            else:
                print("Zły wybór")

    def ukoncz_zadanie(self):  # Dodaje coś a'la tag (Zrobione) do zadania. Przyda się później
        Organizer.wyswietl_zadania(self)
        wybor = str(input("Wybierz ukończone zadanie: "))
        with open("tasks/"+self.user.lower()+"/%s.txt" % self.user.lower(), "r") as readtask:
            odczyt = readtask.readlines()  # Odczytuje wartości
            with open("tasks/"+self.user.lower()+"/%s.txt" % self.user.lower(), "w") as activatetask:
                for line in odczyt:
                    if wybor in line:  # Szuka lini w pliku. Chyba wykorzystam to wyżej
                        # Jedyny minus to fakt, że nie może być dwóch identycznych zadań w pliku
                        # Dlatego też dodałem listy zadań
                        activatetask.write(line.rstrip() + " (Zrobione)" + "\n")
                        print("Zadanie ukończone!")
                    else:
                        activatetask.write(line)

    def ukoncz_liste(self):  # Ukończenie listy. Kod poniżej to lekka modyfikacja kodu z wyswietl_liste_zadan
        # Ogólnie ma to sprawdzać czy zadania na liście są skończone. Jeśli tak - można skończyć listę.
        # Jak nie - użytkownik dostaje informację ile zadań ma, a ile skończył
        line_count = 0
        count = 0
        tag = "(Zrobione)"
        if os.path.exists("tasks/"+self.user.lower()+"/tasks_list"):
            listy = os.listdir("tasks/" + self.user.lower() + "/tasks_list")
            print("Twoje listy zadań: ")
            print(listy)
            nazwa_listy = str(input("Wpisz nazwę listy do ukończenia (bez .txt): "))
            if os.path.exists("tasks/"+self.user.lower()+"/tasks_list/"+nazwa_listy+".txt"):
                with open("tasks/"+self.user.lower()+"/tasks_list/"+nazwa_listy+".txt", "r") as read_list:
                    odczyt_zadan = read_list.readlines()
                    for lines in odczyt_zadan:
                        lines.splitlines()
                        line_count += 1
                        if tag in lines:
                            count += 1
                    # print(count, " ", line_count) Pomocnicze
                    if count != (line_count-1):
                        print("Zostało zadań do ukończenia: ", ((line_count - 1) - count))
                    else:
                        with open("tasks/"+self.user.lower()+"/tasks_list/"+nazwa_listy+".txt", "w") as write_line:
                            for lines in odczyt_zadan:
                                if nazwa_listy in lines:
                                    write_line.write(lines.rstrip() + " (Zrobione)" + "\n")
                                else:
                                    write_line.write(lines.rstrip() + "\n")
                        print("Lista zadań ukończona! Gratulacje!")
            else:
                print("Nie ma takiej listy!")
        else:
            print("Brak list zadań!")

    def ukoncz_zadanie_lista(self):  # Ukończenie zadania z listy
        # Zaimplementowałem ze względu na to wyżej
        # Na ten moment użytkownik może edytować jedno zadanie na raz
        tag = "(Zrobione)"
        if os.path.exists("tasks/" + self.user.lower() + "/tasks_list"):
            listy = os.listdir("tasks/" + self.user.lower() + "/tasks_list")
            print("Twoje listy zadań: ")
            print(listy)
            nazwa_listy = str(input("Wpisz nazwę listy do modyfikacji (bez .txt): "))
            if os.path.exists("tasks/" + self.user.lower() + "/tasks_list/" + nazwa_listy + ".txt"):
                with open("tasks/" + self.user.lower() + "/tasks_list/" + nazwa_listy + ".txt", "r") as read_list:
                    odczyt_zadan = read_list.readlines()
                    for lines in odczyt_zadan:
                        print(lines.rstrip())
                    uk_zadanie = str(input("Wpisz które zadanie chcesz ukończyć: "))
                    with open("tasks/" + self.user.lower() + "/tasks_list/" + nazwa_listy + ".txt", "w") as write_line:
                        for lines in odczyt_zadan:
                            if uk_zadanie in lines:
                                write_line.write(lines.rstrip() + " " + tag + "\n")
                            else:
                                write_line.write(lines.rstrip() + "\n")
                        print("Podzadanie oznaczone jako zrobione!")
            else:
                print("Nie ma takiej listy!")
        else:
            print("Brak list zadań!")

    def menu_pomoc(self):
        # Stwierdziłem że po co robić osobne funkcje z opisami i wstawiłem je normalnie do środka
        while True:
            wybor = str(input("Wybierz temat:"
                              "[1]Notatki, "
                              "[2]Zadania, "
                              "[3]Listy rzeczy, "
                              "[4]Listy zadań, "
                              "[q]Wyjdź z pomocy: "))
            if wybor == "1":
                print("")
                print("Opcja \"Notatki\" pozwala zapisywać, edytować i usuwać twoje notatki.")
                print("W tym przypadku zachowuje się jak zapisana pojedyńcza myśl.")
                print("Przydatna kiedy chcesz zapisać na szybko jedną rzecz")
                print("")
            elif wybor == "2":
                print("")
                print("Opcja \"Zadania\" pozwala zapisywać, edytować i usuwać twoje zadania.")
                print("W tym przypadku zachowuje się jak zapisanie pojedyńczej czynności do zrobienia.")
                print("Przydatna kiedy chcesz zapisać pojedyńcze zadanie do wykonania")
                print("Każde zadanie ma swoją datę wykonania, którą możesz sprecyzować")
                print("Dodatkowo menu \"Modyfikuj\" pozwala oznaczyć zadanie jako ukończone")
                print("")
            elif wybor == "3":
                print("")
                print("\"Listy rzeczy\" pozwalają zapisywać ciąg notatek w osobnym pliku")
                print("Zachowują się dzięki temu jak np. listy zakupowe lub listy anime do obejrzenia")
                print("Listy rzeczy można jedynie tworzyć i usuwać, lecz może to ulec zmianie w przyszłości")
                print("")
            elif wybor == "4":
                print("")
                print("\"Listy zadań\" pozwalają zapisywać ciąg zadań w osobnym pliku")
                print("Zachowują się dzięki temu jak np. kroki do osiągnięcia celu lub listy kontrolne")
                print("Listy zadań można jedynie tworzyć i usuwać, lecz może to ulec zmianie w przyszłości")
                print("Każda z nich ma przypisaną datę ukończenia, którą możesz sprecyzować ")
                print("")
            elif wybor.lower() == "q" or wybor == "q":
                break
            else:
                print("Zły wybór!")


Organizer().main()
