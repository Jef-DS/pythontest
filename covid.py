from niscodes import *
import logging

def main():
    naam = input("Geef gemeentenaam: ")
    code = zoek_gemeente(naam)
    if code:
        print(f"De NIS-code van {naam} is {code}")
    else:
         print(f"Gemeente {naam} is niet gevonden.")

if __name__ == '__main__':
    logging.basicConfig(filename='covid.log',level=logging.ERROR)
    main()