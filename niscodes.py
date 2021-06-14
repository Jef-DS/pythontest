BESTANDSNAAM = '../REFNIS_2019.csv'

with open(BESTANDSNAAM, mode='r', encoding='utf_8_sig') as csvfile:
    regel = csvfile.readline()
    print(regel)