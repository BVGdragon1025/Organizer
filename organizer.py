import datetime  # Użyję później do sortowania, lub czegoś innego

import os  # Przydatne do paru rzeczy :)


def paths():
    notes_path = "notes"
    tasks_path = "tasks"
    user_notes_list = "notes/notes_list"
    user_tasks_list = "tasks/tasks_list"
    return notes_path, tasks_path, user_notes_list, user_tasks_list


def main():  # Główne menu, które powinno sie pojawiać najpierw, ale zrobiłem to coś na górze :)
    login()
    wybor_opcji(login())


def login():
    temp = []
    if os.path.exists("user.txt"):
        with open("user.txt", "r") as user_check:
            read_user = user_check.readline().strip()
            temp.append(read_user)
    else:
        print("Witaj, Użytkowniku! Widzimy się pierwszy raz!")
        user_name = str(input("Wpisz proszę, jak mamy cię nazywać?: "))
        with open("user.txt", "x") as create_user:
            create_user.write(user_name.lower())
            temp.append(user_name)

    return temp


def wybor_opcji(temp):  # Wybór opcji.
    print("Witaj,", temp[0].capitalize(), "!")
    while True:
        choice2 = str(input("Wybierz którą kategorię chcesz wybrać: "
                            "[1]Notatki, "
                            "[2]Zadania, "
                            "[3]Pomoc, "
                            "[q]Wyloguj: "))
        if choice2 == "1":
            menu_notatki()
        elif choice2 == "2":
            menu_zadania()
        elif choice2 == "3":
            menu_pomoc()
        elif choice2 == "4":
            pass
        # Specjalnie zrobione do testowania funkcji
        elif choice2 == "q" or choice2 == "Q":
            print("Żegnaj,", temp[0].capitalize(), "!")
            break
        else:
            print("Zły wybór")


def menu_zadania():
    while True:
        menu2 = str(input("Wybierz opcję: [1]Utwórz..., "
                          "[2]Wyświetl... "
                          "[3]Usuń..., "
                          "[4]Modyfikuj... , "
                          "[q]Wyjdź z menu: "))
        if menu2 == "1":
            menu_utworz_zadanie()
        elif menu2 == "2":
            menu_wyswietl_zadanie()
        elif menu2 == "3":
            menu_usun_zadanie()
        elif menu2 == "4":
            menu_modyfikuj()
        elif menu2 == "q" or menu2 == "Q":
            break
        else:
            print("Zły wybór!")


def menu_notatki():
    while True:
        menu1 = str(input("Wybierz opcję: [1]Dodaj..., "
                          "[2]Wyświetl..., "
                          "[3]Usuń..., "
                          "[4]Modyfikuj..., "
                          "[q]Wyjdź z menu: "))
        if menu1 == "1":
            menu_dodaj_notatke()
        elif menu1 == "2":
            menu_wyswietl_notatke()
        elif menu1 == "3":
            menu_usun_notatke()
        elif menu1 == "4":
            menu_modyfikuj2()
        elif menu1 == "q" or menu1 == "Q":
            break
        else:
            print("Zły wybór!")


def dodaj_notatke():  # Dodaje notatkę do pliku.
    # Dopisalem wszelkie zabezpieczenia na wypadek braku pliku etc.
    # Notatki są w lokalizacji "notes/nazwa_użytkownika/notes.txt"
    notatka = str(input("Wpisz swoją notatkę: "))
    if os.path.exists(paths()[0]):
        if os.path.exists("notes/notes.txt"):
            with open("notes/notes.txt", "a") as addnote:
                addnote.write(notatka + "\n")
                print("Notatka dodana!")
        else:
            with open("notes/notes.txt", "x") as addnote:
                addnote.write(notatka + "\n")
                print("Notatka dodana!")
    else:
        os.makedirs("notes")
        with open("notes/notes.txt", "x") as addnote:
            addnote.write(notatka + "\n")
            print("Notatka dodana!")


def dodaj_zadanie():  # Dodaje zadanie do pliku.
    # Dopisalem wszelkie zabezpieczenia na wypadek braku pliku etc.
    # Notatki są w lokalizacji "tasks/nazwa_użytkownika/tasks.txt"
    zadanie = str(input("Wpisz zadanie: "))
    data = str(input("Wpisz datę (RRRR-MM-DD): "))
    if os.path.exists("tasks"):
        if os.path.exists("tasks/tasks.txt"):
            with open("tasks/tasks.txt", "a") as addtask:
                addtask.write(data + " " + zadanie + "\n")
                print("Zadanie dodane!")
        else:
            with open("tasks/tasks.txt", "x") as addtask:
                addtask.write(data + " " + zadanie + "\n")
                print("Zadanie dodane!")
    else:
        os.makedirs("tasks")
        with open("tasks/tasks.txt", "x") as addtask:
            addtask.write(data + " " + zadanie + "\n")
            print("Zadanie dodane!")


def wyswietl_notatki():  # Jak nazwa wskazuje
    if os.path.exists("notes"):
        if os.path.exists("notes/notes.txt"):
            with open("notes/notes.txt", "r") as readnotes:
                for lines in readnotes:
                    print(lines.rstrip())  # Obcina puste linie powstałe przez "\n"
        else:
            print("Brak notatek!")
    else:
        print("Brak notatek!")


def wyswietl_zadania():
    if os.path.exists("tasks/tasks.txt"):
        if os.path.exists("notes/notes.txt"):
            with open("tasks/tasks.txt", "r") as readtasks:
                for lines in readtasks:
                    print(lines.rstrip())  # Obcina puste linie powstałe przez "\n"
        else:
            print("Brak zadań!")
    else:
        print("Brak zadań!")


def usun_wsz_zadania():  # Działanie jest proste:
    # Otwórz plik w trybie zapisu i zamknij go. Wszelkie dane zostaną nadpisane :)
    if os.path.exists("tasks/tasks.txt"):
        check = str(input("Czy chcesz trwale usunąć wszystkie zadania? [y]Tak, [n]Nie: "))
        if check == "y" or check.lower() == "y":
            with open("tasks/tasks.txt", "w") as deletetasks:
                deletetasks.close()
            print("Zadania zosatały usunięte!")
        elif check == "n" or check.lower() == "n":
            pass
    else:
        print("Brak zadań do usunięcia!")


def usun_zadanie():  # Usuwa zadanie. Aby usunęło odpowiednie, stwierdziłem, że spytam usera o nazwę i datę.
    if os.path.exists("tasks/tasks.txt"):
        wyswietl_zadania()
        dtask = str(input("Wpisz nazwę zadania: "))
        dtaskdate = str(input("Wpisz datę tego zadania (RRRR-MM-DD): "))
        with open("tasks/tasks.txt", "r") as readtask:
            readtaskls = readtask.readlines()
        with open("tasks/tasks.txt", "w") as writelines:
            for line in readtaskls:
                if line.strip("\n") != (dtaskdate + " " + dtask) \
                        and line.strip("\n") != (dtaskdate + " " + dtask + " (Zrobione)"):
                    # zapisuje wszystkie linie po za tą wpisaną przez usera
                    writelines.write(line)
        print("Zadanie usunięte!")
    else:
        print("Brak zadań do usunięcia!")


def usun_wsz_notatki():  # jak przy usun_wszystkie_zadania()
    if os.path.exists("notes/notes.txt"):
        check2 = str(input("Czy chcesz trwale usunąć wszystkie notatki? [y]Tak, [n]Nie: "))
        if check2 == "y" or check2.lower() == "y":
            with open("notes/notes.txt", "w") as deletenotes:
                deletenotes.close()
            print("Notatki zostały usunięte!")
        elif check2 == "n" or check2.lower() == "n":
            pass
    else:
        print("Brak notatek do usunięcia!")


def usun_notatke():
    if os.path.exists("notes/notes.txt"):
        wyswietl_notatki()
        dnote = str(input("Wpisz którą notatkę usunąć: "))
        with open("notes/notes.txt", "r") as readnote:
            readnotels = readnote.readlines()
        with open("notes/notes.txt", "w") as writelines:
            for line in readnotels:
                if line.strip("\n") != dnote:
                    writelines.write(line)
        print("Notatka usunięta!")


def sortowanie_zadan():  # Sortowanie zadań od najwcześniejszego.
    # W sumie nie jest to przydatne, bo nie zaimplementowałem funkcji wyświetlania ile zostało czasu.
    # Ale kto wie, może się zawsze przydać
    if os.path.exists("tasks/tasks.txt"):
        with open("tasks/tasks.txt", "r") as readtasks:
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


def dodaj_notatki():
    ilosc = int(input("Ile notatek chcesz dodać (liczbowo): "))
    i = 0
    while i != ilosc:  # Prosty while, aby nie musieć przepisywać kodu, który już mam
        # Co i tak uczyniłem w późniejszych
        dodaj_notatke()
        i += 1


def dodaj_zadania():
    ilosc = int(input("Ile zadań chcesz dodać (liczbowo): "))
    i = 0
    while i != ilosc:
        dodaj_zadanie()
        i += 1


def usun_zadania():
    print("Twoje zadania: ")
    wyswietl_zadania()
    ilosc = int(input("Ile zadań chcesz usunąć (liczbowo): "))
    i = 0
    while i != ilosc:
        usun_zadanie()
        i += 1


def usun_notatki():
    print("Twoje notatki: ")
    wyswietl_notatki()
    ilosc = int(input("Ile notatek chcesz usunąć (liczbowo): "))
    i = 0
    while i != ilosc:
        usun_notatke()
        i += 1


def menu_utworz_zadanie():
    while True:
        menu = str(input("Wybierz opcję: "
                         "[1]Utwórz zadanie, "
                         "[2]Utwórz kilka zadań, "
                         "[3]Utwórz listę zadań, "
                         "[4]Dodaj podzadania do listy zadań, "
                         "[q]Wyjdź z menu: "))
        if menu == "1":
            dodaj_zadanie()
        elif menu == "2":
            dodaj_zadania()
        elif menu == "3":
            lista_zadan()
        elif menu == "4":
            dodaj_podzadania()
        elif menu == "q" or menu == "Q":
            break
        else:
            print("Zły wybór!")


def menu_dodaj_notatke():
    while True:
        menu = str(input("Wybierz opcję: "
                         "[1]Dodaj notatkę, "
                         "[2]Dodaj kilka notatek, "
                         "[3]Stwórz listę rzeczy, "
                         "[4]Dodaj pozycje do listy rzeczy, "
                         "[q]Wyjdź z menu: "))
        if menu == "1":
            dodaj_notatke()
        elif menu == "2":
            dodaj_notatki()
        elif menu == "3":
            lista_rzeczy()
        elif menu == "4":
            dodaj_pozycje()
        elif menu == "q" or menu == "Q":
            break
        else:
            print("Zły wybór")


def menu_wyswietl_zadanie():
    while True:
        menu = str(input("Wybierz opcję: "
                         "[1]Wyświetl zadania, "
                         "[2]Wyświetl listę zadań, "
                         "[3]Wyświetl zadania (od nadchodzących), "
                         "[4]Wyświetl aktywne zadania, "
                         "[5]Wyswietl ukończone zadania, "
                         "[q]Wyjdź z menu: "))
        if menu == "1":
            wyswietl_zadania()
        elif menu == "2":
            wyswietl_liste_zadan()
        elif menu == "3":
            sortowanie_zadan()
        elif menu == "4":
            wyswietl_aktywne()
        elif menu == "5":
            wyswietl_ukonczone()
        elif menu == "q" or menu == "Q":
            break
        else:
            print("Zły wybór")


def menu_wyswietl_notatke():
    while True:
        menu = str(input("Wybierz opcję: "
                         "[1]Wyświetl notatki, "
                         "[2]Wyświetl listę rzeczy, "
                         "[q]Wyjdź z menu: "))
        if menu == "1":
            wyswietl_notatki()
        elif menu == "2":
            wyswietl_liste_rzeczy()
        elif menu == "q" or menu == "Q":
            break
        else:
            print("Zły wybór")


def menu_usun_zadanie():
    while True:
        menu = str(input("Wybierz opcję: "
                         "[1]Usuń zadanie, "
                         "[2]Usuń kilka zadań, "
                         "[3]Usuń wszystkie zadania, "
                         "[4]Usuń listę zadań, "
                         "[5]Usuń skończone zadania, "
                         "[q]Wyjdź z menu: "))
        if menu == "1":
            usun_zadanie()
        elif menu == "2":
            usun_zadania()
        elif menu == "3":
            usun_wsz_zadania()
        elif menu == "4":
            usun_liste_zadan()
        elif menu == "5":
            usun_skonczone_zadania()
        elif menu == "q" or menu == "Q":
            break
        else:
            print("Zły wybór")


def menu_usun_notatke():
    while True:
        menu = str(input("Wybierz opcję: "
                         "[1]Usuń notatkę, "
                         "[2]Usuń kilka notatek, "
                         "[3]Usuń wszystkie notatki, "
                         "[4]Usuń listę rzeczy, "
                         "[q]Wyjdź z menu: "))
        if menu == "1":
            usun_notatke()
        elif menu == "2":
            usun_notatki()
        elif menu == "3":
            usun_wsz_notatki()
        elif menu == "4":
            usun_liste_rzeczy()
        elif menu == "q" or menu == "Q":
            break
        else:
            print("Zły wybór")


def lista_rzeczy():  # Na to miałem pomysł, aby to było jako osobna lista rzeczy.
    # W tym celu tworzy osobny folder w lokalizacji z notatkami o nazwie "notes_list"
    # Nazwa listy to tytuł, który user podaje
    # Większość tego kodu to tylko upewnienie się, że plik istnieje, a jak nie to zostanie utworzony
    tytul = str(input("Podaj tytuł listy: "))
    ilosc = int(input("Podaj ilość pozycji (numerycznie): "))
    i = 0
    if os.path.exists("notes"):
        if os.path.exists("notes/notes_list"):
            with open("notes/notes_list/" + tytul + ".txt", "x") as create_list:
                create_list.write(tytul + ":\n")
            with open("notes/notes_list/" + tytul + ".txt", "a") as make_list:
                while i != ilosc:
                    poz = str(input("Wpisz coś (jeszcze " + str(ilosc - i) + "): "))
                    make_list.write(poz + "\n")
                    i += 1
            print("Lista stworzona!")
        else:
            os.makedirs("notes/notes_list")
            with open("notes/notes_list/" + tytul + ".txt", "x") as create_list:
                create_list.write(tytul + ":\n")
            with open("notes/notes_list/" + tytul + ".txt", "a") as make_list:
                while i != ilosc:
                    poz = str(input("Wpisz coś (jeszcze " + str(ilosc - i) + "): "))
                    make_list.write(poz + "\n")
                    i += 1
            print("Lista stworzona!")
    else:
        os.makedirs("notes/notes_list")
        with open("notes/notes_list/" + tytul + ".txt", "x") as create_list:
            create_list.write(tytul + ":\n")
        with open("notes/notes_list/" + tytul + ".txt", "a") as make_list:
            while i != ilosc:
                poz = str(input("Wpisz coś (jeszcze " + str(ilosc - i) + "): "))
                make_list.write(poz + "\n")
                i += 1
        print("Lista stworzona!")


def lista_zadan():  # Na to miałem pomysł, aby to było jako osobna lista zadań.
    # W tym celu tworzy osobny folder w lokalizacji z zadaniami o nazwie "tasks_list"
    # Nazwa listy to tytuł, który user podaje
    # Większość tego kodu to tylko upewnienie się, że plik istnieje, a jak nie to zostanie utworzony
    tytul = str(input("Podaj tytuł listy zadań: "))
    ilosc = int(input("Podaj ilość zadań (numerycznie): "))
    czas = str(input("Podaj datę (RRRR-MM-DD): "))
    i = 0
    if os.path.exists("tasks"):
        if os.path.exists("tasks/tasks_list"):
            with open("tasks/tasks_list/" + tytul + ".txt", "x") as create_list:
                create_list.write(czas + " " + tytul + "\n")
            with open("tasks/tasks_list/" + tytul + ".txt", "a") as make_list:
                while i != ilosc:
                    poz = str(input("Wpisz zadanie (jeszcze " + str(ilosc - i) + "): "))
                    make_list.write(poz + "\n")
                    i += 1
            print("Lista stworzona!")
        else:
            os.makedirs("tasks/tasks_list")
            with open("tasks/tasks_list/" + tytul + ".txt", "x") as create_list:
                create_list.write(czas + " " + tytul + "\n")
            with open("tasks/tasks_list/" + tytul + ".txt", "a") as make_list:
                while i != ilosc:
                    poz = str(input("Wpisz zadanie (jeszcze " + str(ilosc - i) + "): "))
                    make_list.write(poz + "\n")
                    i += 1
            print("Lista stworzona!")
    else:
        os.makedirs("tasks/tasks_list")
        with open("tasks/tasks_list/" + tytul + ".txt", "x") as create_list:
            create_list.write(czas + " " + tytul + "\n")
        with open("tasks/tasks_list/" + tytul + ".txt", "a") as make_list:
            while i != ilosc:
                poz = str(input("Wpisz zadanie (jeszcze " + str(ilosc - i) + "): "))
                make_list.write(poz + "\n")
                i += 1
        print("Lista stworzona!")


def wyswietl_ukonczone():
    tag = "(Zrobione)"
    if os.path.exists("tasks/tasks.txt"):
        with open("tasks/tasks.txt", "r") as readtasks:
            for lines in readtasks:
                if tag in lines:
                    print(lines.rstrip())  # Obcina puste linie powstałe przez "\n"
    else:
        print("Brak zadań!")


def wyswietl_aktywne():
    tag = "(Zrobione)"
    if os.path.exists("tasks/tasks.txt"):
        with open("tasks/tasks.txt", "r") as readtasks:
            for lines in readtasks:
                if tag not in lines:
                    print(lines.rstrip())  # Obcina puste linie powstałe przez "\n"
    else:
        print("Brak zadań!")


def wyswietl_liste_zadan():  # Proste wyświetlenie konkretnego pliku (jego zawartości)
    if os.path.exists("tasks/tasks_list"):
        listy = os.listdir("tasks/tasks_list")
        if len(listy) == 0:
            print("Brak list zadań!")
        else:
            print("Twoje listy zadań: ")
            print(listy)
            nazwa_listy = str(input("Wpisz nazwę listy do wyświetlenia (bez .txt): "))
            if os.path.exists("tasks/tasks_list/" + nazwa_listy + ".txt"):
                with open("tasks/tasks_list/" + nazwa_listy + ".txt", "r") as read_list:
                    for line in read_list:
                        print(line.rstrip())
            else:
                print("Nie ma takiej listy!")
    else:
        print("Brak list zadań!")


def wyswietl_liste_rzeczy():
    if os.path.exists("notes/notes_list"):
        listy = os.listdir("notes/notes_list")
        if len(listy) == 0:
            print("Brak list rzeczy!")
        else:
            print("Twoje listy rzeczy: ")
            print(listy)
            wybor = str(input("Wpisz nazwę listy do wyświetlenia (bez.txt): "))
            if os.path.exists("notes/notes_list/" + wybor + ".txt"):
                with open("notes/notes_list/" + wybor + ".txt", "r") as read_list:
                    for line in read_list:
                        print(line.rstrip())
            else:
                print("Nie ma takiej listy!")
    else:
        print("Brak list rzeczy!")


def usun_liste_zadan():  # Usuwa plik. Tyle.
    if os.path.exists("tasks/tasks_list"):
        listy = os.listdir("tasks/tasks_list")
        if len(listy) == 0:
            print("Brak list zadań!")
        else:
            print("Twoje listy zadań: ")
            print(listy)
            wybor = str(input("Wpisz nazwę listy do usunięcia (bez.txt): "))
            check = str(input("Czy chcesz trwale usunąć listę zadań? [y]Tak, [n]Nie: "))
            if check == "y" or check.lower() == "y":
                if os.path.exists("tasks/tasks_list/" + wybor + ".txt"):
                    os.remove("tasks/tasks_list/" + wybor + ".txt")
                    print("Lista zadań usunięta!")
                else:
                    print("Nie ma takiej listy do usunięcia!")
            else:
                print("Usunięcie anulowane!")


def usun_liste_rzeczy():  # Usuwa plik. Tyle.
    if os.path.exists("notes/notes_list"):
        listy = os.listdir("notes/notes_list")
        if len(listy) == 0:
            print("Brak list rzeczy!")
        else:
            print("Twoje listy rzeczy: ")
            print(listy)
            wybor = str(input("Wpisz nazwę listy do usunięcia (bez.txt): "))
            check = str(input("Czy chcesz trwale usunąć wszystkie zadania? [y]Tak, [n]Nie: "))
            if check == "y" or check.lower() == "y":
                if os.path.exists("notes/notes_list/" + wybor + ".txt"):
                    os.remove("notes/notes_list/" + wybor + ".txt")
                    print("Lista zadań usunięta!")
                else:
                    print("Nie ma takiej listy do usunięcia!")
            else:
                print("Usunięcie anulowane!")


def menu_modyfikuj():
    while True:
        menu = str(input("Wybierz opcję: "
                         "[1]Oznacz zadanie jako ukończone, "
                         "[2]Oznacz zadanie z listy jako ukończone, "
                         "[3]Oznacz listę zadań jako skończoną, "
                         "[q]Wyjdź z menu: "))
        if menu == "1":
            ukoncz_zadanie()
        elif menu == "2":
            ukoncz_zadanie_lista()
        elif menu == "3":
            ukoncz_liste()
        elif menu == "q" or menu == "Q":
            break
        else:
            print("Zły wybór")


def menu_modyfikuj2():
    while True:
        menu = str(input("Wybierz opcję: "
                         "[1]Oznacz pozycję jako skreśloną, "
                         "[q]Wyjdź z menu: "))
        if menu == "1":
            oznacz_pozycje()
        elif menu == "q" or menu == "Q":
            break
        else:
            print("Zły wybór")


def ukoncz_zadanie():  # Dodaje coś a'la tag (Zrobione) do zadania. Przyda się później
    wyswietl_zadania()
    wybor = str(input("Wybierz ukończone zadanie: "))
    with open("tasks/tasks.txt", "r") as readtask:
        odczyt = readtask.readlines()  # Odczytuje wartości
        with open("tasks/tasks.txt", "w") as activatetask:
            for line in odczyt:
                if wybor in line:  # Szuka lini w pliku. Chyba wykorzystam to wyżej
                    # Jedyny minus to fakt, że nie może być dwóch identycznych zadań w pliku
                    # Dlatego też dodałem listy zadań
                    activatetask.write(line.rstrip() + " (Zrobione)" + "\n")
                    print("Zadanie ukończone!")
                else:
                    activatetask.write(line)


def oznacz_pozycje():
    tag = "(Tick)"
    if os.path.exists("notes/notes_list"):
        listy = os.listdir("notes/notes_list")
        if len(listy) == 0:
            print("Brak list rzeczy!")
        else:
            print("Twoje listy rzeczy: ")
            print(listy)
            nazwa_listy = str(input("Wpisz nazwę listy do modyfikacji (bez .txt): "))
            if os.path.exists("notes/notes_list/" + nazwa_listy + ".txt"):
                with open("notes/notes_list/" + nazwa_listy + ".txt", "r") as read_list:
                    odczyt_poz = read_list.readlines()
                    for lines in odczyt_poz:
                        print(lines.rstrip())
                    sk_poz = str(input("Wpisz którą pozycję chcesz \"skreślić\": "))
                    with open("notes/notes_list/" + nazwa_listy + ".txt", "w") as \
                            write_line:
                        for lines in odczyt_poz:
                            if sk_poz in lines:
                                write_line.write(lines.rstrip() + " " + tag + "\n")
                            else:
                                write_line.write(lines.rstrip() + "\n")
                        print("Pozycja oznaczona jako skreślona!")
            else:
                print("Nie ma takiej listy!")
    else:
        print("Brak list zadań!")


def ukoncz_liste():  # Ukończenie listy. Kod poniżej to lekka modyfikacja kodu z wyswietl_liste_zadan
    # Ogólnie ma to sprawdzać czy zadania na liście są skończone. Jeśli tak - można skończyć listę.
    # Jak nie - użytkownik dostaje informację ile zadań ma, a ile skończył
    line_count = 0
    count = 0
    tag = "(Zrobione)"
    if os.path.exists("tasks/tasks_list"):
        listy = os.listdir("tasks/tasks_list")
        if len(listy) == 0:
            print("Brak list zadań!")
        else:
            print("Twoje listy zadań: ")
            print(listy)
            nazwa_listy = str(input("Wpisz nazwę listy do ukończenia (bez .txt): "))
            if os.path.exists("tasks/tasks_list/" + nazwa_listy + ".txt"):
                with open("tasks/tasks_list/" + nazwa_listy + ".txt", "r") as read_list:
                    odczyt_zadan = read_list.readlines()
                    for lines in odczyt_zadan:
                        lines.splitlines()
                        line_count += 1
                        if tag in lines:
                            count += 1
                    # print(count, " ", line_count) Pomocnicze
                    if count != (line_count - 1):
                        print("Zostało zadań do ukończenia: ", ((line_count - 1) - count))
                    else:
                        with open("tasks/tasks_list/" + nazwa_listy + ".txt",
                                  "w") as write_line:
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


def ukoncz_zadanie_lista():  # Ukończenie zadania z listy
    # Zaimplementowałem ze względu na to wyżej
    # Na ten moment użytkownik może edytować jedno zadanie na raz
    tag = "(Zrobione)"
    if os.path.exists("tasks/tasks_list"):
        listy = os.listdir("tasks/tasks_list")
        if len(listy) == 0:
            print("Brak list zadań!")
        else:
            print("Twoje listy zadań: ")
            print(listy)
            nazwa_listy = str(input("Wpisz nazwę listy do modyfikacji (bez .txt): "))
            if os.path.exists("tasks/tasks_list/" + nazwa_listy + ".txt"):
                with open("tasks/tasks_list/" + nazwa_listy + ".txt", "r") as read_list:
                    odczyt_zadan = read_list.readlines()
                    for lines in odczyt_zadan:
                        print(lines.rstrip())
                    uk_zadanie = str(input("Wpisz które zadanie chcesz ukończyć: "))
                    with open("tasks/tasks_list/" + nazwa_listy + ".txt", "w") as \
                            write_line:
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


def usun_skonczone_zadania():  # Usuwa skończone zadania.
    tag = "(Zrobione)"
    print("")
    print("Czy chcesz usunąć wszystkie ukończone zadania?")
    print("Usunie to tylko pojedyńcze skończone zadania.")
    choice = str(input("[y]Tak, [n]Nie: "))
    if choice == "y" or choice.lower == "y":
        if os.path.exists("tasks/tasks.txt"):
            with open("tasks/tasks.txt", "r") as file_read:
                odczyt = file_read.readlines()
            with open("tasks/tasks.txt", "w") as write_line:
                for lines in odczyt:
                    if tag not in lines:
                        write_line.write(lines.rstrip() + "\n")
            print("Ukończone zadania zostały usunięte!")
        else:
            print("Brak zadań!")
    else:
        print("Usunięcie anulowane!")


def dodaj_podzadania():  # dodaje podzadania do listy zadań.
    # Zawiera dodatkową funkcję sprawdzania, czy lista jest zrobiona.
    # Jeśli tak, użytkownik nie może dodać zadania, bo by to nie miało sensu.
    i = 0
    tag = "(Zrobione)"
    if os.path.exists("tasks/tasks_list"):
        listy = os.listdir("tasks/tasks_list")
        if len(listy) == 0:
            print("Brak list zadań!")
        else:
            print("Twoje listy zadań: ")
            print(listy)
            nazwa_listy = str(input("Wpisz nazwę listy do modyfikacji (bez .txt): "))
            if os.path.exists("tasks/tasks_list/" + nazwa_listy + ".txt"):
                with open("tasks/tasks_list/" + nazwa_listy + ".txt", "r") as read_file:
                    odczyt = read_file.readline()
                    if tag in odczyt:
                        print("To zadanie jest ukończone! Nie możesz do niego dodawać podzadań!")
                    else:
                        print("Podzadania są dodawane na koniec kolejki!")
                        ile = int(input("Ile podzadań chcesz dodać (numerycznie): "))
                        while i != ile:
                            podzadanie = str(input("Wpisz podzadanie (jeszcze " + str(ile - i) + "): "))
                            with open("tasks/tasks_list/" + nazwa_listy + ".txt", "a") as add_task:
                                add_task.write(podzadanie + "\n")
                                print("Podzadanie dodane!")
                            i += 1
            else:
                print("Nie ma takiej listy!")
    else:
        print("Brak list zadań!")


def dodaj_pozycje():  # Analogicznie do tego, co wyżej, ale bez sprawdzania skończenia listy
    # Bo listy rzeczy nie można "zrobić" według narzuconej w tym programie logiki.
    i = 0
    if os.path.exists("notes/notes_list"):
        listy = os.listdir("notes/notes_list")
        if len(listy) == 0:
            print("Brak list rzeczy!")
        else:
            print("Twoje listy rzeczy: ")
            print(listy)
            nazwa_listy = str(input("Wpisz nazwę listy do modyfikacji (bez .txt): "))
            if os.path.exists("notes/notes_list/" + nazwa_listy + ".txt"):
                print("Pozycje są dodawane na koniec kolejki!")
                ile = int(input("Ile pozycji chcesz dodać (numerycznie): "))
                while i != ile:
                    pozycje = str(input("Wpisz coś (jeszcze " + str(ile - i) + "): "))
                    with open("notes/notes_list/" + nazwa_listy + ".txt",
                              "a") as add_note:
                        add_note.write(pozycje + "\n")
                        print("Pozycja dodana!")
                    i += 1
            else:
                print("Nie ma takiej listy!")
    else:
        print("Brak list zadań!")


# Poniższa funkcja miała trafić do gotowego programu, lecz sprawiła mi problemy
# Pozostawiam ją na przyszłość, może ją naprawię
# Jej założeniem było wyświetlanie użytkownikowi nadchodzących zadań na następne 7 dni
# I ta funkcja to robi, ale się psuje bo wykrywa pustą linię i nie wiem jak ją usunąć
# Kiedyś ją naprawię


def nadchodzace():
    count = 0
    if os.path.exists("tasks/tasks.txt"):
        print("Nadchodzące zadania: ")
        with open("tasks/tasks.txt", "r") as read_file:
            for lines in read_file:
                lines.splitlines()
                daty = read_file.readline(10)
                print(datetime.datetime.strptime(daty, "%Y-%m-%d") -
                      datetime.datetime.today())
                if datetime.timedelta(0) < datetime.datetime.strptime(daty, "%Y-%m-%d") - \
                        datetime.datetime.today() <= datetime.timedelta(7):
                    print(lines)
                else:
                    continue
    else:
        print("Brak nadchodzących zadań")


def menu_pomoc():
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
            print("Listy rzeczy można tworzyć, usuwać i dodawać do nich\"pozycje\"")
            print("Każda nowa pozycja jest dodawana na koniec listy.")
            print("Uwaga! Pozycji nie można usuwać! Można jedynie dodawać przy nich tag \"(Tick)\"")
            print("Tag \"(Tick)\" jest równoznaczny z skreśleniem pozycji z listy.")
            print("")
        elif wybor == "4":
            print("")
            print("\"Listy zadań\" pozwalają zapisywać ciąg zadań w osobnym pliku")
            print("Zachowują się dzięki temu jak np. kroki do osiągnięcia celu lub listy kontrolne")
            print("Listy zadań można jedynie tworzyć, usuwać, i dodawać  do nich \"podzadania\"")
            print("Każda z nich ma przypisaną datę ukończenia, którą możesz sprecyzować ")
            print("Dodatkowo możesz oznaczyć podzadania jako skończone.")
            print("Jeśli wszystkie podzadania zostaną ukończone, możesz oznaczyć listę zadań jako skończoną.")
            print("Uwaga! Nie można usuwać podzadań! Można oznaczać je tylko jako skończone!")
            print("")
        elif wybor.lower() == "q" or wybor == "q":
            break
        else:
            print("Zły wybór!")


main()
