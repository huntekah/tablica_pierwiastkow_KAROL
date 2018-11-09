#!/usr/bin/python
from Test.odpowiedz import Odpowiedz

class Historia():

    def __init__(self):
        self.odpowiedzi = []

    def dodaj_odpowiedz(self, odpowiedz: str, wzorzec: str, jest_poprawna: bool) -> None:
        self.odpowiedzi.append(Odpowiedz(odpowiedz,
                                              wzorzec,
                                              jest_poprawna))

    def ile_poprawnych(self, wzorzec=None):
        return self.licz_odpowiedzi(wzorzec, jest_poprawna=True)

    def ile_blednych(self, wzorzec=None):
        return self.licz_odpowiedzi(wzorzec, jest_poprawna=False)

    def licz_odpowiedzi(self, wzorzec, jest_poprawna):
        ilosc_odpowiedzi = 0
        wybrane_odpowiedzi = self.daj_odpowiedzi(wzorzec)
        for odpowiedz in wybrane_odpowiedzi:
            if odpowiedz.jest_poprawna == jest_poprawna:
                ilosc_odpowiedzi += 1
        return ilosc_odpowiedzi

    def daj_odpowiedzi(self, wzorzec=None):
        if wzorzec:
            return self.odpowiedzi_z_wzorcem(wzorzec)
        else:
            return self.odpowiedzi

    def odpowiedzi_z_wzorcem(self, wzorzec):
        odpowiedzi = []
        for odpowiedz in self.odpowiedzi:
            if odpowiedz.wzorzec == wzorzec:
                odpowiedzi.append(odpowiedz)
        return odpowiedzi