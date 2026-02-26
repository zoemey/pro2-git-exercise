def gewichteter_schnitt(liste):
    if not liste:
        return None
    summe_gewichtet = sum(f["note"] * f["ects"] for f in liste)
    summe_ects = sum(f["ects"] for f in liste)
    if summe_ects == 0:
        return None
    return summe_gewichtet / summe_ects

def beste_drei(faecher):
    sortiert = sorted(faecher, key=lambda f: f["note"], reverse=True)
    return sortiert[:3]

def schlechteste_drei(faecher):
    sortiert = sorted(faecher, key=lambda f: f["note"])
    return sortiert[:3]