from datetime import datetime

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=10000, szobaszam=szobaszam)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=15000, szobaszam=szobaszam)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def szoba_hozzaadasa(self, szoba):
        if szoba.szobaszam==102:
            szoba.ar=20000
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class FoglalasKezelo:
    def __init__(self):
        self.foglalasok = []

    def foglalas(self, szalloda, szobaszam, datum):
        for szoba in szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return f"A(z) {szobaszam} számú szoba foglalva {datum}-ra. Ár: {szoba.ar} Ft"
        return "Nincs ilyen szoba az adott szállodában."

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return f"A(z) {szobaszam} számú szoba foglalása {datum}-ra törölve."
        return "Nincs ilyen foglalás."

    def foglalasok_listazasa(self):
        if self.foglalasok:
            return "\n".join([f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}" for foglalas in self.foglalasok])
        else:
            return "Nincsenek foglalások."


szalloda = Szalloda("Modern Szálloda")
szalloda.szoba_hozzaadasa(EgyagyasSzoba(101))
szalloda.szoba_hozzaadasa(EgyagyasSzoba(102))
szalloda.szoba_hozzaadasa(KetagyasSzoba(201))
foglalas_kezelo = FoglalasKezelo()
foglalas_kezelo.foglalas(szalloda, 101, datetime(2024, 5, 10))
foglalas_kezelo.foglalas(szalloda, 201, datetime(2024, 5, 12))
foglalas_kezelo.foglalas(szalloda, 101, datetime(2024, 5, 15))
foglalas_kezelo.foglalas(szalloda, 102, datetime(2024, 5, 20))
foglalas_kezelo.foglalas(szalloda, 102, datetime(2024, 5, 25))


while True:
    print()
    print("\t Üdvözöllek a  Modern Szállodánkban, kérlek válassz az alábbi menüpontok közül!")
    print("\n1\t - \tSzoba foglalás")
    print("2\t -  \tFoglalás törlése")
    print("3\t -  \tFoglalások listázása")
    print("4\t -  \tKilépés")
    valasztas = input("Válassz egy műveletet: ")

    if valasztas == "1":
        szobaszam = int(input("\n 101 - Egyágyas szoba\n 102 -Egyágyas szoba amely a legmodernebb eszközeinket tartalmazza \n 201 - Kétágyas szoba \nAdd meg a foglalni kívánt szoba számát: "))
        datum = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            if datum < datetime.now():
                print("Csak jövőbeli foglalás lehetséges.")
            else:
                print(foglalas_kezelo.foglalas(szalloda, szobaszam, datum))
        except ValueError:
            print("Hibás dátum formátum.")
    elif valasztas == "2":
        szobaszam = int(input("Add meg a törölni kívánt foglalás szoba számát: "))
        datum = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            print(foglalas_kezelo.lemondas(szobaszam, datum))
        except ValueError:
            print("Hibás dátum formátum.")
    elif valasztas == "3":
        print(foglalas_kezelo.foglalasok_listazasa())
    elif valasztas == "4":
        break
    else:
        print("Érvénytelen választás. Kérlek válassz újra.")
