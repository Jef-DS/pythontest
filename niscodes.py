import csv

def lees_nis_bestand():
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
    return gemeenten

def zoek_gemeente(gemeentenaam):
    gemeenten = lees_nis_bestand()
    naam = gemeentenaam.upper()
    try:
        code = gemeenten[naam.upper()]
        return code
    except KeyError:
        return False

naam = input("Geef gemeentenaam: ")
code = zoek_gemeente(naam)
if code:
    print(f"De NIS-code van {naam} is {code}")
else:
    print(f"Gemeente {naam} is niet gevonden.")