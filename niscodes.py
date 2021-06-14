import csv

BESTANDSNAAM = '../REFNIS_2019.csv'
NIS_CODE = 'Code NIS'
GEMEENTENAAM = 'Administratieve eenheden'

with open(BESTANDSNAAM, mode='r', newline='', encoding='utf_8_sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    totaal_aantal = 0
    het_rijk = 0
    aantal_gewesten = 0
    aantal_provincies = 0
    aantal_arrondissementen = 0
    aantal_gemeenten = 0
    for record in reader:
        totaal_aantal = totaal_aantal + 1
        if record[NIS_CODE] == '01000':
            het_rijk = het_rijk + 1
        elif record[NIS_CODE][0] == '0':
            aantal_gewesten = aantal_gewesten + 1
        elif record[NIS_CODE][-4:-1] == '000':
            aantal_provincies = aantal_provincies + 1
        elif record[NIS_CODE][-3:] == '000':
            aantal_arrondissementen = aantal_arrondissementen + 1
        else:
            aantal_gemeenten = aantal_gemeenten + 1
    print("Totaal:", totaal_aantal)
    print("Het rijk:", het_rijk)
    print("Aantal gewesten:", aantal_gewesten)
    print("Aantal provincies: ", aantal_provincies)
    print("Aantal arrondissementen: ", aantal_arrondissementen)
    print("Aantal gemeenten:", aantal_gemeenten)
