def wybierz_typ_testu():
    typ = ""
    while typ not in [0,1]:
        typ = input("Wybierz tryb gry:\n\t0 - nazwy\n\t1 - symbole")
        if typ.isdigit():
            typ = int(typ)
    return typ
