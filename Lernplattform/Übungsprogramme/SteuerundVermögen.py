import locale
locale.setlocale( locale.LC_ALL, '' )

print()
print("*-------------------------------*")
print("* Steueramt Flächenlandrepublik *")
print("*-------------------------------*")
print()

GRENZE_1 = 10000.0
GRENZE_2 = 30000.0
GRENZE_3 = 70000.0
STEUERSATZ_1 = 0.40  # 40%
STEUERSATZ_2 = 0.55  # 55%
STEUERSATZ_3 = 0.75  # 75%
STEUERSATZ_4 = 0.82  # 82%
VERMÖGENSSTEUERSATZ_1 = 0.05  # Für Vermögen umter 100.000
VERMÖGENSSTEUERSATZ_2 = 0.08  # Für Vermögen über 100.000 und unter 500.000
VERMÖGENSSTEUERSATZ_3 = 0.13  # Für Vermögen über 500.000 und 1.000.000  
VERMÖGENSSTEUERSATZ_4 = 0.21  # Für Vermögen über 1.000.000
#--------------------------------------------------------------------------------------------------------------------
nachname = input("Nachname des Steuerzahlers: ")
vorname = input("Vorname des Steuerzahlers: ")
#--------------------------------------------------------------------------------------------------------------------
einkommen = 0.0
while einkommen <= 0.0:
    einkommen = float(input("Einkommen (in €): "))
    if einkommen <= 0.0:
        print("Eingabe nicht gültig! Bitte nochmals das Einkommen eingeben: ")

    einkommensteuer = 0.0
    if einkommen <= GRENZE_1:
        einkommensteuer = einkommen * STEUERSATZ_1
    elif einkommen <= GRENZE_2:
        einkommensteuer = einkommen * STEUERSATZ_2
    elif einkommen <= GRENZE_3:
        einkommensteuer = einkommen * STEUERSATZ_3
    else:
        einkommensteuer = einkommen * STEUERSATZ_4 
#-------------------------------------------------------------------------------------------------------------------
vermögen = 0.0
while vermögen <= 0.0:
    vermögen = float(input("Vermögen (in €): "))
    if vermögen <= 0.0:
        print("Eingabe nicht gültig! Bitte nochmals das Einkommen eingeben: ")
    
    vermögenssteuer = 0.0
    if vermögen < 100000:
        vermögenssteuer = vermögen * VERMÖGENSSTEUERSATZ_1
    elif vermögen >=100000 or vermögen <=500000:
        vermögenssteuer = vermögen * VERMÖGENSSTEUERSATZ_2
    elif vermögen >=500000 or vermögen <1000000:
        vermögenssteuer = vermögen * VERMÖGENSSTEUERSATZ_3
    else:
        vermögenssteuer = vermögen * VERMÖGENSSTEUERSATZ_4
#-------------------------------------------------------------------------------------------------------------------
steuerlast = round(vermögenssteuer) + round(einkommensteuer)

print("######################")
print("Steuerberechnung für")
print(vorname, ",", nachname)
print("######################")
print("Zugrunde liegen die Werte des Einkommens in Höhe von", einkommen)
print("######################")
print("Zugrunde liegen die Werte des Vermögens in Höhe von", vermögen)
print("######################")
print(locale.currency(round(einkommensteuer, grouping=True)))
print("######################")
print(round(vermögenssteuer))
print("######################")
print(einkommensteuer+vermögenssteuer)
print("######################")