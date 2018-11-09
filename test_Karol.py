from Test.test import Test
from wyborTypu import wybierz_typ_testu

# wyodrebnic klase "pytanie"
# oczyscic kod z komentarzy
# dodac komentarze dokumentujące

if __name__ == "__main__":
    test_karola = Test(wybierz_typ_testu())

    while not test_karola.jest_koniec_testu():
        test_karola.zadaj_pytanie()
    test_karola.wiadomosc_koncowa()
