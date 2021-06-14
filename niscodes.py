import csv

BESTANDSNAAM = '../REFNIS_2019.csv'


with open(BESTANDSNAAM, mode='r', newline='', encoding='utf_8_sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    print(reader.fieldnames)