import Aufgabe8_a


A1 = Aufgabe8_a.Anschrift("Gewerbepark", "5", "0000", "Merbitz")

M1 = Aufgabe8_a.Mitarbeiter("Schmidt", "Tom", "01.01.1990", A1)
M2 = Aufgabe8_a.Mitarbeiter("Muller", "Tom", "01.01.1990", A1)
M3 = Aufgabe8_a.Mitarbeiter("Blauen", "Tom", "01.01.1990", A1)

G1 = Aufgabe8_a.Gruppe("Test",M1)
G1.addMitarbeiter(M2)
G1.addMitarbeiter(M3)

G2 = Aufgabe8_a.Gruppe("Development",M1)
G2.addMitarbeiter(M2)
G2.addMitarbeiter(M3)

Ab1 = Aufgabe8_a.Abteilung("Software", M1)
Ab1.addGruppe(G1)
Ab1.addGruppe(G2)
Ab1.addGruppe(G2)
