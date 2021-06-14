BESTANDSNAAM = '../REFNIS_2019.csv'

with open(BESTANDSNAAM, mode='r', encoding='utf_8_sig') as csvfile:
    # We gebruiken '_' voor variabelen waarvan we de waarde niet gebruiken
    # Op de vijfde regel staat de eerste echte gemeente
    for _ in range(5):
        regel = csvfile.readline()
    items = regel.split(';')  # scheidingsteken is ';'
    print(items[3], items[4])          # print de NIS-code en de naam van Anderlecht