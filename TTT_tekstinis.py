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

def gauti_teisinga_ivesti(pranesimas):
    while True:
        try:
            ivestis = int(input(pranesimas))
            if ivestis in [0, 1, 2]:
                return ivestis
            else:
                print("Neteisinga įvestis. Prašome įvesti 0, 1 arba 2.")
        except ValueError:
            print("Neteisinga įvestis. Prašome įvesti skaičių 0, 1 arba 2.")

def gauti_teisinga_pasirinkima(pranesimas):
    while True:
        pasirinkimas = input(pranesimas).lower()
        if pasirinkimas in ["taip", "ne"]:
            return pasirinkimas
        else:
            print("Neteisinga įvestis. Prašome įvesti 'taip' arba 'ne'.")

def zaidimas():
    zaidejas_x_pergales = 0
    zaidejas_o_pergales = 0
    lygiosios = 0

    while True:
        lentele = [[" " for _ in range(3)] for _ in range(3)]
        zaidejas = "X"

        while True:
            einamoji_lentele(lentele)
            eilute = gauti_teisinga_ivesti(f"Žaidėjau {zaidejas}, įveskite eilutės numerį (0, 1, 2): ")
            stulpelis = gauti_teisinga_ivesti(f"Žaidėjau {zaidejas}, įveskite stulpelio numerį (0, 1, 2): ")

            if lentele[eilute][stulpelis] == " ":
                lentele[eilute][stulpelis] = zaidejas
            else:
                print("Ši vieta jau užimta. Pasirinkite kitą vietą.")
                continue

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

        pasirinkimas = gauti_teisinga_pasirinkima("Ar norite žaisti dar kartą? (y/n): ")
        if pasirinkimas != "y":
            break

zaidimas()
