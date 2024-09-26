import random
import time

def einamoji_lentele(lentele):
    for eilute in lentele:
        print(" | ".join(eilute))
        print("-" * 9)

def laimetojas(lentele, simbolis):
    for eilute in lentele:
        if all(s == simbolis for s in eilute):
            return True
    for stulpelis in range(3):
        if all(eilute[stulpelis] == simbolis for eilute in lentele):
            return True
    if all(lentele[i][i] == simbolis for i in range(3)) or all(lentele[i][2 - i] == simbolis for i in range(3)):
        return True
    return False

def ar_lygios(lentele):
    if all(all(langelis != " " for langelis in eilute) for eilute in lentele):
        return True
    else:
        return False

def langelio_pasirinkimas(pranesimas):
    while True:
        try:
            ivestis = int(input(pranesimas))
            if ivestis in [0, 1, 2]:
                return ivestis
            else:
                print("Pasirinkimas negalimas. Prašome įvesti 0, 1 arba 2.")
        except ValueError:
            print("Pasirinkimas negalimas. Prašome įvesti 0, 1 arba 2.")

def ar_kartoti(pranesimas):
    while True:
        pasirinkimas = input(pranesimas).lower()
        if pasirinkimas in ["y", "n"]:
            return pasirinkimas
        else:
            print("Neteisinga įvestis. Prašome įvesti 'y' arba 'n'.")

def koks_rezimas():
    while True:
        try:
            rezimas = int(input("Pasirinkite žaidimo režimą (1 - žaidėjas prieš žaidėją, 2 - žaidėjas prieš kompiuterį): "))
            if rezimas in [1, 2]:
                return rezimas
            else:
                print("Neteisinga įvestis. Prašome įvesti 1 arba 2.")
        except ValueError:
            print("Neteisinga įvestis. Prašome įvesti skaičių 1 arba 2.")

def kompiuterio_ejimas(lentele):
    print("Kompiuterio ėjimas...")
    time.sleep(1.5)
    for i in range(3):
        for j in range(3):
            if lentele[i][j] == " ":
                lentele[i][j] = "O"
                if laimetojas(lentele, "O"):
                    return
                lentele[i][j] = " "
    for i in range(3):
        for j in range(3):
            if lentele[i][j] == " ":
                lentele[i][j] = "X"
                if laimetojas(lentele, "X"):
                    lentele[i][j] = "O"
                    return
                lentele[i][j] = " "
    while True:
        i, j = random.randint(0, 2), random.randint(0, 2)
        if lentele[i][j] == " ":
            lentele[i][j] = "O"
            return

def zaidimas():
    zaidejas_x_pergales = 0
    zaidejas_o_pergales = 0
    lygiosios = 0
    rezimas = koks_rezimas()

    while True:
        lentele = [[" " for _ in range(3)] for _ in range(3)]
        zaidejas = random.choice(["X", "O"])

        while True:
            einamoji_lentele(lentele)
            if rezimas == 1 or (rezimas == 2 and zaidejas == "X"):
                eilute = langelio_pasirinkimas(f"Žaidėjau {zaidejas}, įveskite eilutės numerį (0, 1, 2): ")
                stulpelis = langelio_pasirinkimas(f"Žaidėjau {zaidejas}, įveskite stulpelio numerį (0, 1, 2): ")

                if lentele[eilute][stulpelis] == " ":
                    lentele[eilute][stulpelis] = zaidejas
                else:
                    print("Šis langelis jau užimtas. Pasirinkite kitą vietą.")
                    continue
            else:
                kompiuterio_ejimas(lentele)

            if laimetojas(lentele, zaidejas):
                einamoji_lentele(lentele)
                print(f"Pergalė! Laimėjo žaidėjas {zaidejas}!!!")
                if zaidejas == "X":
                    zaidejas_x_pergales += 1
                else:
                    zaidejas_o_pergales += 1
                break
            elif ar_lygios(lentele):
                einamoji_lentele(lentele)
                print("Lygiosios!!!")
                lygiosios += 1
                break

            if zaidejas == "X":
                zaidejas = "O"
            else:
                zaidejas = "X"

        print(f"Žaidėjas X: {zaidejas_x_pergales} pergalės")
        print(f"Žaidėjas O: {zaidejas_o_pergales} pergalės")
        print(f"Lygiosios: {lygiosios}")

        pasirinkimas = ar_kartoti("Ar norite žaisti dar kartą? (y/n): ")
        if pasirinkimas == "n":
            break

zaidimas()
