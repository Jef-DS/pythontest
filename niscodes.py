import csv

BESTANDSNAAM = '../REFNIS_2019.csv'
NIS_CODE = 'Code NIS'
GEMEENTENAAM = 'Administratieve eenheden'

with open(BESTANDSNAAM, mode='r', newline='', encoding='utf_8_sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    # de next() functie gaat naar het volgende item van de iterator
    record = next(reader) 
    print(record[NIS_CODE], record[GEMEENTENAAM])