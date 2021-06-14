from niscodes import *

for _ in range(2):
    naam = input("Geef gemeentenaam: ")
    code = zoek_gemeente(naam)
    if code:
        print(f"De NIS-code van {naam} is {code}")
    else:
        print(f"Gemeente {naam} is niet gevonden.")