import csv

# Globale lister
emne_liste = []
studieplan = {}

# ------------------ Meny ------------------
def vis_meny():
    print("\n________Meny:_______")
    print("1. Lag et nytt emne.")
    print("2. (kommer senere) Legg til emne i studieplan.")
    print("3. Skriv ut alle registrerte emner.")
    print("4. (kommer senere) Skriv ut studieplan.")
    print("5. (kommer senere) Sjekk om studieplanen er gyldig.")
    print("6. Lagre emner og studieplan til CSV-fil.")
    print("7. Les inn emner og studieplan fra CSV-fil.")
    print("8. Avslutt.")



def lag_nytt_emne():
    """Oppretter og legger til et nytt emne i listen."""
    try:
        emnekode = input("Skriv inn emnekode: ").strip().upper()
        navn = input("Skriv inn navn på emnet: ").strip()

        sesong_input = int(input("Skriv 1 for høst eller 2 for vår: "))
        if sesong_input == 1:
            sesong = "høst"
        elif sesong_input == 2:
            sesong = "vår"
        else:
            print(" Ugyldig valg — velg 1 (høst) eller 2 (vår).")
            return

        studiepoeng = float(input("Skriv inn antall studiepoeng: "))

        emne = {
            "emnekode": emnekode,
            "navn": navn,
            "sesong": sesong,
            "studiepoeng": studiepoeng
        }
        emne_liste.append(emne)
        print(f" Emnet '{navn}' ({emnekode}) ble lagt til.")
    except ValueError:
        print(" Ugyldig input — prøv igjen med riktige verdier.")

def skriv_ut_emner():
    """Skriver ut alle registrerte emner."""
    if not emne_liste:
        print("Ingen emner er registrert ennå.")
        return

    print("\n Emneliste:")
    for emne in emne_liste:
        print(f"Emnekode: {emne['emnekode']}, "
              f"Navn: {emne['navn']}, "
              f"Sesong: {emne['sesong']}, "
              f"Studiepoeng: {emne['studiepoeng']}")


def lagre_til_fil():
    """Lagrer emner og studieplan til CSV-filer."""
    try:
        emne_filnavn = input("Filnavn for emner (uten .csv): ").strip() or "emner"
        plan_filnavn = input("Filnavn for studieplan (uten .csv): ").strip() or "studieplan"

        # Lagre emner
        with open(emne_filnavn + ".csv", "w", newline="", encoding="utf-8") as fil:
            felt_navn = ["emnekode", "navn", "sesong", "studiepoeng"]
            writer = csv.DictWriter(fil, fieldnames=felt_navn)
            writer.writeheader()
            writer.writerows(emne_liste)
        print(f" Emneliste lagret til '{emne_filnavn}.csv'.")

        # Lagre studieplan (hvis den finnes)
        if studieplan:
            with open(plan_filnavn + ".csv", "w", newline="", encoding="utf-8") as fil:
                writer = csv.writer(fil)
                writer.writerow(["semester", "emner"])
                for semester, emner in studieplan.items():
                    writer.writerow([semester, ";".join(emner)])
            print(f" Studieplan lagret til '{plan_filnavn}.csv'.")
        else:
            print("ℹ Ingen studieplan å lagre ennå.")
    except Exception as e:
        print(f" Feil ved lagring: {e}")


def les_fra_fil():
    """Leser inn emner og studieplan fra CSV-filer."""
    global emne_liste, studieplan
    try:
        emne_filnavn = input("Filnavn for emner (uten .csv): ").strip() or "emner"
        plan_filnavn = input("Filnavn for studieplan (uten .csv): ").strip() or "studieplan"

        emne_liste = []
        studieplan = {}

        # Les emner
        with open(emne_filnavn + ".csv", "r", encoding="utf-8") as fil:
            reader = csv.DictReader(fil)
            for rad in reader:
                rad["studiepoeng"] = float(rad["studiepoeng"])
                emne_liste.append(rad)
        print(f" Leste inn {len(emne_liste)} emner fra '{emne_filnavn}.csv'.")

        # Les studieplan
        try:
            with open(plan_filnavn + ".csv", "r", encoding="utf-8") as fil:
                reader = csv.reader(fil)
                next(reader)
                for semester, emner_str in reader:
                    emner = emner_str.split(";") if emner_str else []
                    studieplan[semester] = emner
            print(f" Studieplan lest inn fra '{plan_filnavn}.csv'.")
        except FileNotFoundError:
            print("ℹ Fant ikke studieplanfilen. Hopper over denne delen.")

    except FileNotFoundError:
        print(" Fant ikke filen. Sjekk filnavn og prøv igjen.")
    except Exception as e:
        print(f" En uventet feil oppstod: {e}")


# ------------------ Hovedprogram ------------------
def hovedprogram():
    while True:
        vis_meny()
        try:
            valg = int(input("\nVelg et tall fra menyen: "))
        except ValueError:
            print(" Du må skrive et tall.")
            continue

        if valg == 1:
            lag_nytt_emne()
        elif valg == 2:
            print("Funksjon for studieplan kommer senere.")
        elif valg == 3:
            skriv_ut_emner()
        elif valg == 6:
            lagre_til_fil()
        elif valg == 7:
            les_fra_fil()
        elif valg == 8:
            print("Avslutter programmet. ")
            break
        else:
            print("Ugyldig valg — prøv igjen.")

# Start programmet
hovedprogram()
