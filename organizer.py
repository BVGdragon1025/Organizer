import datetime
import os.path
import tkinter


class Login:

    user = str(input("Podaj nazwę użytkownika: "))
    psw = str(input("Podaj hasło: "))

    @staticmethod
    def rejestracja():
        with open("users.txt", "r") as fr:
            frr = fr.read()
            if os.path.exists("users.txt"):
                if Login.user.lower() in frr:
                    print("Podany użytkownik istnieje. Uzyj opcji \"Logowanie\"")
                elif Login.user in frr:
                    print("Podany użytkownik istnieje. Uzyj opcji \"Logowanie\"")
                else:
                    with open("users.txt", "a") as fa:
                        fa.write(Login.user.lower() + " " + Login.psw + "\n")
                        print("Użytkownik dodany!")
            else:
                fx = open("users.txt", "x")
                fx.write(Login.user.lower() + " " + Login.psw + "\n")
                print("Użytkownik dodany!")

    @staticmethod
    def logowanie():
        with open("users.txt", "r") as f:
            frls = f.readlines()
            if (Login.user.lower() + " " + Login.psw + "\n") in frls:
                print("Witaj, " + Login.user + "!")
            elif (Login.user + " " + Login.psw + "\n") in frls:
                print("Witaj, " + Login.user + "!")
            else:
                print("Zły login lub hasło!")


while True:
    choice = str(input("Wybierz co chcesz zrobić: [1]Rejestracja, [2]Logowanie, [q]Wyjście: "))
    lg = Login()
    if choice == "1":
        lg.rejestracja()
    elif choice == "2":
        lg.logowanie()
    elif choice == "q":
        print("Żegnaj, " + Login.user + "!")
        break
