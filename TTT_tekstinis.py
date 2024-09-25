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

    if all(all(vieta != " " for vieta in eilute) for eilute in lentele):
        return True
    else:
        return False


def zaidimas():
    lentele = [[" " for _ in range(3)] for _ in range(3)]
    zaidejas = "X"

    while True:
        einamoji_lentele(lentele)
        eilute = int(input(f"Žaidėjau {zaidejas}, įveskite eilutės numerį (0, 1, 2): "))
        stulpelis = int(input(f"Žaidėjau {zaidejas}, įveskite stulpelio numerį (0, 1, 2): "))

        if lentele[eilute][stulpelis] == " ":
            lentele[eilute][stulpelis] = zaidejas
        else:
            print("Ši vieta jau užimta. Pasirinkite kitą vietą.")
            continue

        if laimetojas(lentele, zaidejas):
            einamoji_lentele(lentele)
            print(f"Pergalė ! Laimėjo žaidėjas {zaidejas} !!!")
            break
        elif ar_lygios(lentele):
            einamoji_lentele(lentele)
            print("Lygiosios !!!")
            break

        if zaidejas == "X":
            zaidejas = "O"
        else:
            zaidejas = "X"


zaidimas()
