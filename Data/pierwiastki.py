from Utilities.porownajTekst import porownaj_tekst

class Pierwiastek:
    """Klasa, ktora reprezentuje pierwiastek"""

    def __init__(self, nazwa: str = "", symbol: str = "", nazwa_symbolu: str = ""):
        """
        Stworz nowy pierwiastek
        :type nazwa: basestring
        :type symbol: basestring
        :type nazwa_symbolu: basestring
        """
        self.symbol = str(symbol)
        self.nazwa = str(nazwa)
        self.nazwa_symbolu = str(nazwa_symbolu)

    def porownaj_symbol(self, symbol):
        return porownaj_tekst(self.symbol, symbol)

    def porownaj_nazwa(self, nazwa):
        return porownaj_tekst(self.nazwa, nazwa)
