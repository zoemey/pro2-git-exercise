def faecher_ausgeben(liste):
    for f in liste:
        print(f"- {f['name']} | Note: {f['note']} | ECTS: {f['ects']}")

def schnitt_ausgeben(schnitt):
    if schnitt is None:
        print("Kein Durchschnitt berechenbar.")
    else:
        print(f"Durchschnitt (ECTS-gewichtet): {schnitt:.2f}")