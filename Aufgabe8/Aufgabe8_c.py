import Aufgabe8_b
item = input("suchen nach Gruppe order Mitarbeiter? G/M: ")
if item == "G" :
    Gname = input("Bitte wählen Gruppename: Test/Development: ")
    for g in Aufgabe8_b.Ab1.Gruppenliste:
        if g.Name == Gname:
            print("Gruppenleiter: "+ g.Gruppenleiter.Name +" "+ g.Gruppenleiter.Vorname)

elif item =='M':
    Mname = input("Bitte wählen Mitarbeitername: Schmidt/Muller/Blauen: ")
    for g in Aufgabe8_b.Ab1.Gruppenliste:
        for m in g.Mitarbeiterliste :
            if m.Name == Mname:
                print("Mitarbeitername "+ m.Name +" "+ m.Vorname)
                break
        break
else:
    pass
""" 
print (Aufgabe8_b.G1.AnzahlMitarbeiter)
print (Aufgabe8_b.G2.AnzahlMitarbeiter)
print (Aufgabe8_b.Ab1.AnzahlGruppen)
print(Aufgabe8_b.Ab1.AnzahlAbteilungsMiarbeiter) """