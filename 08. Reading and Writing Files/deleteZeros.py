import re, os, shutil

# DeleteZeros.py - Program usuwa zera z nazw pliku

# Pattern na nazwe pliku zawierajaca zera
filenamePattern = re.compile(r'''^(.*?)
(\d+)
(.*?)$
''', re.VERBOSE)

# Iteracja przez nazwy plikow i sprawdzanie czy wzor sie do nich wpasuje
for zfilename in os.listdir('.'):
    wZeros = filenamePattern.search(zfilename)

    # Jesli wzor nie pasuje sprawdz nastepny plik
    if wZeros is None:
        continue

    # Grupy z nazwy pliku
    beforePart = wZeros.group(1) # Przed liczbami
    numPart = wZeros.group(2).strip('0') # Usuwanie zer
    afterPart = wZeros.group(3) # Po liczbach

    # Nowa nazwa pliku
    nozFilename = beforePart + numPart + afterPart

    abs_w_path = os.path.abspath('.') # Sciezka absolutna do folderu z plikami
    withZ = os.path.join(abs_w_path, zfilename) # Sciezka do pliku z zerami
    withoutZ = os.path.join(abs_w_path, nozFilename) # Sciezka do pliku bez zer

    print(f'Usuwam zera z pliku {withZ} na {withoutZ}...')
    # shutil.move(withZ, withoutZ) # Usun kometarz po zakonczeniu testow.