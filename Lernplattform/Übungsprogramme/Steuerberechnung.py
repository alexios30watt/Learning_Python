# Grundwerte
steuersatz1 = 0.26 # > 4000 und ledig
steuersatz2 = 0.22 # > 4000 und verheiratet
steuersatz3 = 0.22 # <= 4000 und ledig
steuersatz4 = 0.18 # <= 4000 und verheiratet

# Ausführung
print("Geben Sie Ihr Bruttogehalt ein")
bruttogehalt = float(input())
print("Bitte geben Sie ihren Familienstand ein: - Sie können entweder leidig oder verheiratet angeben.")
familienestand = input()

# Berechnung
if bruttogehalt > 4000 and familienestand == "ledig":
    print("Sie geben, an", bruttogehalt, "zu verdienen und sind", familienestand, "Ihre Steuerklasse ist 1",
          "Ihr Steuerbetrag beträgt", bruttogehalt * steuersatz1, "€" "." 
          "Entsprechend der Steuerklasse 1 wurde Ihr Gehalt mit dem Satz von", steuersatz1, "vergerechnet.",
          "Ihr Auszahlungsbetrag beträgt", bruttogehalt - (steuersatz1 * bruttogehalt))

elif bruttogehalt > 4000 and familienestand == "verheiratet":
    print("Sie geben, an", bruttogehalt, "zu verdienen und sind", familienestand, "Ihre Steuerklasse ist 2",
          "Ihr Steuerbetrag beträgt", bruttogehalt * steuersatz2, "€" ".",
          "Entsprechend der Steuerklasse 2 wurde Ihr Gehalt mit dem Satz von", steuersatz2, "vergerechnet.",
          "Ihr Auszahlungsbetrag beträgt", bruttogehalt - (steuersatz2 * bruttogehalt))

elif bruttogehalt <= 4000 and familienestand == "ledig":
    print("Sie geben, an", bruttogehalt, "zu verdienen und sind", familienestand, "Ihre Steuerklasse ist 3",
          "Ihr Steuerbetrag beträgt", bruttogehalt * steuersatz3, "€" ".",
          "Entsprechend der Steuerklasse 3 wurde Ihr Gehalt mit dem Satz von", steuersatz3, "vergerechnet.",
          "Ihr Auszahlungsbetrag beträgt", bruttogehalt - (steuersatz3 * bruttogehalt))

elif bruttogehalt < 4000 and familienestand == "verheiratet":
    print("Sie geben, an", bruttogehalt, "zu verdienen und sind", familienestand, "Ihre Steuerklasse ist 4",
          "Ihr Steuerbetrag beträgt", bruttogehalt * steuersatz4, "€" ".",
          "Entsprechend der Steuerklasse 4 wurde Ihr Gehalt mit dem Satz von", steuersatz4, "vergerechnet.",
          "Ihr Auszahlungsbetrag beträgt", bruttogehalt - (steuersatz4 * bruttogehalt))

else:
    print("Berichtigen Sie Ihre Angaben.")
