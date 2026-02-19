mathe = 5
englisch = 4
programmieren = 2
statistik = 6

durchschnitt = (mathe+englisch+programmieren+statistik)/4

noten = {
    "mathe": 5, "englisch": 4, "programmieren": 2, "statistik": 6
}



summe = 0

for i in range(3):
    schlechtestes_fach = ""
    schlechteste_note = 6

    for fach in noten:
        if noten[fach] < schlechteste_note:
            schlechteste_note = noten[fach]
            schlechtestes_fach = fach

    summe += schlechteste_note
    del noten[schlechtestes_fach]

durchschnitt = summe / 3
print("Durchschnitt der 3 schlechtesten:", durchschnitt)
