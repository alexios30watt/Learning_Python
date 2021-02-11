print("Tag des Datums eingeben")
day = int(input())    
print("Monat des Datums eingeben")
month = int(input())
print("Jahr des Datums eingeben")
year = int(input())

if day < 1 or day > 31:
    print("Falsches Datum")
elif month < 1 or month > 12: 
    print("Falsches Datum")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("Letzer Tag 30")
    if day < 1 or day > 30:
        print("Falsches Datum")
    else: 
        print("Richtiges Datum")
elif month == 2: 
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        print("Letzter Tag: 29")
        if day < 1 or day > 29:
            print("Falsches Datum")
        else: 
            print("Richtiges Datum")
else:
    print("Letzer Tag: 31")
    if day < 1 or day > 31:
        print("Falsches Datum")
    else:
        print("Richtiges Datum")
print("Sie haben das Datum", day, ".", month, ".", year, "eingegeben.") 