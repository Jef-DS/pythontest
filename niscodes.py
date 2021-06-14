import csv

BESTANDSNAAM = '../REFNIS_2019.csv'
NIS_CODE = 'Code NIS'
GEMEENTENAAM = 'Administratieve eenheden'

with open(BESTANDSNAAM, mode='r', newline='', encoding='utf_8_sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    gemeenten = {} # initialiseer een dictionary
    aantal_gemeenten = 0
    for record in reader:
        if record[NIS_CODE] == '01000':
            pass  # het rijk
        elif record[NIS_CODE][0] == '0':
            pass # een gewest
        elif record[NIS_CODE][-4:-1] == '000':
            pass # een provincie
        elif record[NIS_CODE][-3:] == '000':
            pass # een arrondissement
        else:
            aantal_gemeenten += 1
            nis_code = record[NIS_CODE]
            gemeentenaam = record[GEMEENTENAAM].upper()
            gemeenten[gemeentenaam] = nis_code
    print(f"{aantal_gemeenten} gemeenten ingelezen")
    naam = input("Geef gemeentenaam: ")
    code = gemeenten[naam.upper()]
    print(f"Gemeente {naam} heeft als NIS code {code}")
