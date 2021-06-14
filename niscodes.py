BESTANDSNAAM = '../REFNIS_2019.csv'

with open(BESTANDSNAAM, mode='r', encoding='utf_8_sig') as csvfile:
    # We gebruiken '_' voor variabelen waarvan we de waarde niet gebruiken
    # Op de vijfde regel staat de eerste echte gemeente
    for _ in range(5):
        regel = csvfile.readline()
    items = regel.split(';')  # scheidingsteken is ';'
    for item in items:
        print(item)           # print de gegevens van Anderlecht