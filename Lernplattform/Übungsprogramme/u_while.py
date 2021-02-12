cm = 2.54
inchinput = float(input("Programm wird gestartet. Geben Sie die erste Inchzahl ein:"))
while inchinput != 0:
    ergebnis = cm * inchinput
    print(ergebnis)
    inchinput = float(input("Geben Sie die Inchzahl ein:"))
abbruch = input("Wollen Sie wirklich abbrechen?")
if abbruch == "Ja":
    print("Das Programm wird beendet")
else: 
    print("Starten Sie das Programm neu!")