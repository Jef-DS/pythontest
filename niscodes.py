import csv, logging



def _lees_nis_bestand():
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
        logging.debug("%d  gemeenten ingelezen", aantal_gemeenten)
    return gemeenten

_gemeenten = {}
def zoek_gemeente(gemeentenaam):
    global _gemeenten
    if len(_gemeenten) == 0:
        _gemeenten = _lees_nis_bestand()
    naam = gemeentenaam.upper()
    logging.debug("Zoek gemeente %s.", naam)
    try:
        code = _gemeenten[naam]
        return code
    except KeyError:
        logging.debug("Gemeente %s niet gevonden.", naam)
        return False


if __name__ == '__main__':
    logging.basicConfig(level = logging.DEBUG)
    for _ in range(2):
        naam = input("Geef gemeentenaam: ")
        code = zoek_gemeente(naam)
        if code:
            logging.debug("code is %s", code)
        else:
            logging.debug("%s is niet gevonden", naam)
