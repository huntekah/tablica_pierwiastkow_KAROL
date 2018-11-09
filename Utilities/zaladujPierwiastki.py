from Data.listaPierwiastkow import *
from Data.pierwiastki import Pierwiastek


def zaladuj_pierwiastki():
    pierwiastki = []
    for pierwiastek in lista_pierwiastkow:
        pierwiastki.append(Pierwiastek(*pierwiastek))
    return pierwiastki
