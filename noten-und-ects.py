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
        name = input("Name des Fachs: ").strip()
        note = float(input("Note: ").strip())
        ects = int(input("ECTS: ").strip())

        faecher.append({
            "name": name,
            "note": note,
            "ects": ects
        })

        print("Fach gespeichert.")

    elif eingabe == "2":
        schnitt = gewichteter_schnitt(faecher)

        if schnitt is None:
            print("Keine Daten vorhanden.")
        else:
            print(f"Notendurchschnitt (ECTS-gewichtet): {schnitt:.2f}")

    elif eingabe == "3":
        if not faecher:
            print("Keine Daten vorhanden.")
            continue

        # Schweizer System: 6.0 = beste Note
        beste = sorted(faecher, key=lambda f: f["note"], reverse=True)[:3]

        print("Drei beste Fächer:")
        for f in beste:
            print(f"- {f['name']} | Note: {f['note']} | ECTS: {f['ects']}")

        schnitt = gewichteter_schnitt(beste)
        print(f"Durchschnitt (beste 3, ECTS-gewichtet): {schnitt:.2f}")

    elif eingabe == "4":
        if not faecher:
            print("Keine Daten vorhanden.")
            continue

        schlechteste = sorted(faecher, key=lambda f: f["note"])[:3]

        print("Drei schlechteste Fächer:")
        for f in schlechteste:
            print(f"- {f['name']} | Note: {f['note']} | ECTS: {f['ects']}")

        schnitt = gewichteter_schnitt(schlechteste)
        print(f"Durchschnitt (schlechteste 3, ECTS-gewichtet): {schnitt:.2f}")

    elif eingabe == "5":
        suche = input("Nach welchem Fach suchen Sie? ").strip().lower()

        gefunden = [
            f for f in faecher
            if f["name"].lower() == suche
        ]

        if not gefunden:
            print("Nichts gefunden.")
        else:
            print("Gefunden:")
            for f in gefunden:
                print(f"- {f['name']} | Note: {f['note']} | ECTS: {f['ects']}")

            schnitt = gewichteter_schnitt(gefunden)

            if schnitt is None:
                print("Kein Durchschnitt berechenbar.")
            else:
                print(f"Durchschnitt (gefunden, ECTS-gewichtet): {schnitt:.2f}")

    else:
        print("Ungültige Eingabe.")