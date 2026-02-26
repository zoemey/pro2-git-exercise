from eingabe import fach_eingeben, fach_suchen
from berechnung import gewichteter_schnitt, beste_drei, schlechteste_drei
from ausgabe import faecher_ausgeben, schnitt_ausgeben

faecher = []  # Liste von Dicts: {"name": str, "note": float, "ects": int}


def gewichteter_schnitt(liste):
    if not liste:
        return None

    summe_gewichtet = sum(f["note"] * f["ects"] for f in liste)
    summe_ects = sum(f["ects"] for f in liste)

    if summe_ects == 0:
        return None

    return summe_gewichtet / summe_ects


while True:
    print("\n--- Notenverwaltung ---")
    print("1: Fächer mit zugehörigen Noten eingeben")
    print("2: Notendurchschnitt berechnen")
    print("3: Drei beste Fächer ausgeben + Durchschnitt berechnen")
    print("4: Drei schlechteste Fächer ausgeben + Durchschnitt berechnen")
    print("5: Bonus: Nach Fach suchen + Durchschnitt berechnen")
    print("0: Exit")

    eingabe = input("Ihre Wahl: ").strip()

    if eingabe == "0":
        break

    elif eingabe == "1":
        fach_eingeben(faecher)
        
    elif eingabe == "2":
        schnitt_ausgeben(gewichteter_schnitt(faecher))

    elif eingabe == "3":
        faecher_ausgeben(beste_drei(faecher))
        schnitt_ausgeben(gewichteter_schnitt(beste_drei(faecher)))

    elif eingabe == "4":
        faecher_ausgeben(schlechteste_drei(faecher))
        schnitt_ausgeben(gewichteter_schnitt(schlechteste_drei(faecher)))

    elif eingabe == "5":
        gefunden = fach_suchen(faecher)
        faecher_ausgeben(gefunden)
        schnitt_ausgeben(gewichteter_schnitt(gefunden))

    else:
        print("Ungültige Eingabe.")