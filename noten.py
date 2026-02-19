mathe = 5
englisch = 4
programmieren = 2
statistik = 6

durchschnitt = (mathe+englisch+programmieren+statistik)/4

noten = {
    "mathe": 5, "englisch": 4, "programmieren": 2, "statistik": 6
}

for i in range(3):
    bestes_fach = ""
    beste_note = 0

    for fach in noten:
        if noten[fach] > beste_note:
            beste_note = noten[fach]
            bestes_fach = fach

    print(bestes_fach, beste_note)
    del noten[bestes_fach]