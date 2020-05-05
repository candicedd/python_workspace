class Anschrift:
    def __init__(self, Strasse, Hausnummer, PLZ, Ort):
        self.Strasse = Strasse
        self.Hausnummer = Hausnummer
        self.PLZ = PLZ
        self.Ort = Ort
    
class Mitarbeiter:
    def __init__(self, Name, Vorname, Geburtsdatum, Anschrift):
        self.Name = Name
        self.Vorname = Vorname
        self.Geburtsdatum = Geburtsdatum
        self.Anschrift = Anschrift

class Gruppe:
    def __init__(self, Name, Gruppenleiter):
        self.Name = Name
        self.Gruppenleiter = Gruppenleiter
        self.Mitarbeiterliste = []
        self.AnzahlMitarbeiter = 0
    def addMitarbeiter(self, mitarbeiter):
        self.Mitarbeiterliste.append(mitarbeiter)
        self.AnzahlMitarbeiter = len(self.Mitarbeiterliste)

class Abteilung:
    def __init__(self, Name, Abteilungsleiter):
        self.Name = Name
        self.Abteilungsleiter = Abteilungsleiter
        self.Gruppenliste = []
        self.AnzahlGruppen = 0
        self.AnzahlAbteilungsMiarbeiter = 0

    def addGruppe(self, gruppe):
        self.Gruppenliste.append(gruppe)
        self.AnzahlGruppen = len(self.Gruppenliste)
        self.AnzahlAbteilungsMiarbeiter += gruppe.AnzahlMitarbeiter


""" A1 = Anschrift("Gewerbepark", "5", "0000", "Merbitz")

M1 = Mitarbeiter("Schmidt", "Tom", "01.01.1990", A1)
M2 = Mitarbeiter("Muller", "Tom", "01.01.1990", A1)
M3 = Mitarbeiter("Blauen", "Tom", "01.01.1990", A1)

G1 = Gruppe("Test",M1)
G1.addMitarbeiter(M2)
G1.addMitarbeiter(M3)

G2 = Gruppe("Development",M1)
G2.addMitarbeiter(M2)
G2.addMitarbeiter(M3)

Ab1 = Abteilung("Software", M1)
Ab1.addGruppe(G1)
Ab1.addGruppe(G2)
Ab1.addGruppe(G2)

print (G1.AnzahlMitarbeiter)
print (G2.AnzahlMitarbeiter)
print (Ab1.AnzahlGruppen)
print(Ab1.AnzahlAbteilungsMiarbeiter) """