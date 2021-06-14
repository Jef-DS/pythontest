import csv

BESTANDSNAAM = '../REFNIS_2019.csv'
NIS_CODE = 'Code NIS'
GEMEENTENAAM = 'Administratieve eenheden'

with open(BESTANDSNAAM, mode='r', newline='', encoding='utf_8_sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    totaal_aantal = 0
    aantal_gemeenten = 0
    for record in reader:
        totaal_aantal = totaal_aantal + 1
        if record[NIS_CODE][-3:] == '000':
            print(record[NIS_CODE], record[GEMEENTENAAM])
        else:
            aantal_gemeenten = aantal_gemeenten + 1
    print("Totaal:", totaal_aantal)
    print("Gemeenten", aantal_gemeenten)