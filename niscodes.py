BESTANDSNAAM = '../REFNIS_2019.csv'

with open(BESTANDSNAAM, mode='r') as csvfile:
    regel = csvfile.readline()
    print(regel)