from random import shuffle

from Data.pierwiastki import Pierwiastek
from Data.statystyka import Statystyka
from Utilities.clear_screen import clear
from Utilities.zaladujPierwiastki import zaladuj_pierwiastki
from Utilities.coloredString import red, green, yellow

class Test(Statystyka):
    def __init__(self, typ_testu):
        self.pierwiastki = zaladuj_pierwiastki()
        super().__init__(pytan_na_test=len(self.pierwiastki))
        self.typ_testu = typ_testu
        self.wylosowany_pierwiastek = Pierwiastek("", "", "")

    def zadaj_pytanie(self):
        self.losuj_pierwiastek()
        self.wyswietl_pytanie()
        self.wczytaj_odpowiedz()
        self.analizuj_odpowiedz()
        self.wyswietl_komunikat()

    def wiadomosc_koncowa(self):
        print(green("\n" * 5 + "Gratki, z klasowki otrzymabys:\n"
                         " {:.0f}/{}pkt czyli {:.0f}%\n"
                         "Ocena: {}\n"
                         "U mnie miales {:.0f}% poprawnych odpowiedzi").format(
            self.kartkowka_wynik.punkty,
            self.pytan_na_test,
            self.kartkowka_wynik.procent,
            self.ocena(),
            self.biezacy_wynik.procent))

    def losuj_pierwiastek(self):
        shuffle(self.pierwiastki)
        self.wylosowany_pierwiastek = self.pierwiastki[0]

    def wyswietl_pytanie(self):
        print("\n")
        print(self.tekst_pytania())

    def wczytaj_odpowiedz(self):
        self.odpowiedz = input()

    def analizuj_odpowiedz(self):
        self.jest_poprawna = self.sprawdz_odpowiedz(self.odpowiedz)
        self.dodaj_odpowiedz(self.odpowiedz, self.wzorzec, self.jest_poprawna)
        if self.jest_poprawna:
            self.przygotuj_nowy_zbior_pytan()
        else:
            self.zwieksz_liczbe_pytan()

    def wyswietl_komunikat(self):
        if self.jest_poprawna:
            podpowiedz = "Gratuluję, \"{}\" to inaczej \"{}\"".format(green(self.wzorzec),
                                                                      yellow(self.wylosowany_pierwiastek.nazwa_symbolu))
        else:
            podpowiedz = "Próbuj dalej. Odp: \"{}\" (czyli inaczej \"{}\")".format(red(self.wzorzec),
                                                                                   yellow(self.wylosowany_pierwiastek.nazwa_symbolu))
        statystyka = "Twoj wynik to {0:.2f}%".format(self.biezacy_wynik.procent)
        clear()
        print(podpowiedz)
        print(statystyka)

    def jest_koniec_testu(self):
        if not len(self.pierwiastki):
            return True
        else:
            return False

    def przygotuj_nowy_zbior_pytan(self):
        del self.pierwiastki[0]

    def tekst_pytania(self):
        if self.typ_testu:
            return "{}. Jaki jest symbol pierwiasteka {}".format(len(self.pierwiastki),
                                                                 green(self.wylosowany_pierwiastek.nazwa))
        else:
            return "{}. Jaki nazwe ma symbol {}".format(len(self.pierwiastki),
                                                        green(self.wylosowany_pierwiastek.symbol))

    def sprawdz_odpowiedz(self, odpowiedz):
        if self.typ_testu:
            self.wzorzec = self.wylosowany_pierwiastek.symbol
            return self.wylosowany_pierwiastek.porownaj_symbol(odpowiedz)
        else:
            self.wzorzec = self.wylosowany_pierwiastek.nazwa
            return self.wylosowany_pierwiastek.porownaj_nazwa(odpowiedz)

    def ocena(self):
        if self.kartkowka_wynik.procent < 30:
            return "1"
        elif self.kartkowka_wynik.procent < 35:
            return "2-"
        elif self.kartkowka_wynik.procent < 45:
            return "2"
        elif self.kartkowka_wynik.procent < 50:
            return "2+"
        elif self.kartkowka_wynik.procent < 55:
            return "3-"
        elif self.kartkowka_wynik.procent < 65:
            return "3"
        elif self.kartkowka_wynik.procent < 70:
            return "3+"
        elif self.kartkowka_wynik.procent < 75:
            return "4-"
        elif self.kartkowka_wynik.procent < 80:
            return "4"
        elif self.kartkowka_wynik.procent < 85:
            return "4+"
        elif self.kartkowka_wynik.procent < 90:
            return "5-"
        elif self.kartkowka_wynik.procent < 95:
            return "5"
        elif self.kartkowka_wynik.procent < 100:
            return "5+"
        elif self.kartkowka_wynik.procent == 100:
            return "6"
