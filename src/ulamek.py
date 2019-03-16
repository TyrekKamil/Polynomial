class Ulamek:
    licznik = float(0)
    mianownik = float(0)

    def __init__(self, l, m):
        self.licznik = l
        self.mianownik = m

    def setLicznik(self, l):
        self.licznik = l

    def setMianownik(self, m):
        self.mianownik = m

    def getUlamek(self):
        return self.licznik, "/", self.mianownik



def wspolnyMianownik(u1, u2):
    l1 = u1.licznik * u2.mianownik
    l2 = u2.licznik * u1.mianownik
    u1.licznik = l1
    u2.licznik = l2
    u1.mianownik = u2.mianownik = u1.mianownik * u2.mianownik


def dodajUlamek(u1, u2):
    wspolnyMianownik(u1, u2)
    l = u1+u2
    m = u1+u2
    return Ulamek(l, m)


def mnozenieUlamek(u1, u2):
    return Ulamek(u1.licznik * u2.licznik, u1.mianownik * u2.mianownik)


def potegujUlamek(u1, x):
    l = u1.licznik
    m = u1.mianownik
    return Ulamek(l ** 5, m ** 5)

