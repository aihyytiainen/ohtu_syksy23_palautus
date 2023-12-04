class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._musiti = arvo

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo

#class Summa:
#    def __init__(self, sovelluslogiikka, syote):
#       self.sovelluslogiikka = sovelluslogiikka
#       self.syote = syote

#    def suorita(self):
#       return self.suovelluslogiikka.arvo() + self.syote
