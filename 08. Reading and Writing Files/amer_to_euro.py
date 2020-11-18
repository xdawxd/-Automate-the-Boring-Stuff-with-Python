import re, shutil, os

# renameDates.py - Zamienia nazwe pliku wraz z data w formacie amerykanskim (MM-DD-RRRR)
# na date w formacie europejskim (DD-MM-RRRR).

datePattern = re.compile(r'''^(.*?) 
(([01])?\d)-
(([0123])?\d)-
((19|20)\d\d)
(.*?)$
''', re.VERBOSE)

# Iteracja przez pliki znajdujace sie w katalogu.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Pomieniecie plikow bez daty.
    if mo == None:
        continue

    # Pobranie poszczegolnych fragmentow nazwy pliku.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Przygotowanie nazwy pliku zawierajacej date w formacie europejskim.
    euroFilename = beforePart + dayPart + '-'\
                   + monthPart + '-' + yearPart + afterPart

    # Pobranie pelnych, bezwzglednych sciezek dostepu pliku.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Zmiana nazwy plikow.
    print("Zmieniam nazwe '%s' na '%s'..." % (amerFilename, euroFilename))
    # shutil.move(amerFilename, euroFilename) # Usun komentarz po zakonczeniu testow
