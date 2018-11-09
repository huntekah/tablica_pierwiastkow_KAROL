#!/usr/bin/python
from Data.historia import Historia


class Statystyka(Historia):
    def __init__(self, pytan_na_test):
        super().__init__()
        self._liczba_pytan = 0
        self.pytan_na_test = pytan_na_test
        self.biezacy_wynik = self.Wynik()
        self.kartkowka_wynik = self.Wynik()
        self._dodatkowych_pytan = 0

    # def __str__(self):
    #     return "\nNa to pytanie odpowiadasz ze skutecznoscia {0:.2f}%" \
    #            "\nWynik testu {0:.1f}%" \
    #         .format("TODO", self.biezacy_wynik)  # TODO

    def dodaj_odpowiedz(self, odpowiedz, wzorzec, jest_poprawna):
        super().dodaj_odpowiedz(odpowiedz, wzorzec, jest_poprawna)
        self._liczba_pytan += 1
        self.aktualizuj_wyniki()

    def zeruj_biezacy_wynik(self):
        self.biezacy_wynik = 0

    # def statystyka_pytania(self):
    #     pass  # TODO

    def aktualizuj_wyniki(self):
        jest_poprawna = self.odpowiedzi[-1].jest_poprawna
        self.biezacy_wynik.aktualizuj_wynik(self.biezacy_wynik.punkty + int(jest_poprawna),
                                            self._liczba_pytan)
        self.aktualizuj_wynik_kartkowki()

    def aktualizuj_wynik_kartkowki(self):
        jest_poprawna = self.odpowiedzi[-1].jest_poprawna
        if self.ile_blednych(self.odpowiedzi[-1].wzorzec) == 0:
            self.kartkowka_wynik.aktualizuj_wynik(self.kartkowka_wynik.punkty + int(jest_poprawna), self.pytan_na_test)

    def zwieksz_liczbe_pytan(self):
        self._dodatkowych_pytan += 1


    class Wynik:
        procent = 0.0
        punkty = 0.0

        def aktualizuj_wynik(self, punkty, liczba_pytan):
            self.punkty = int(punkty)
            self.procent = 100 * punkty / liczba_pytan if liczba_pytan > 0 else 0
