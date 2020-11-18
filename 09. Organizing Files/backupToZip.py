
# backupToZip.py - Katalog z cala zawartoscia zostaje umieszczony
# w archiwum ZIP, ktorego nazwa jest inkrementowana za kazdym razem.

import zipfile, os

def backupToZip(folder):
    # Umieszczenie w archiwum Zip calej zawartosci katalogi

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Utworzenie archiwum ZIP
    print('Tworzenie archiwum %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Przejscie przez cale drzewo katalogi i kompresja plikow we weszystkich podkatalogach.
    for dirpath, dirnames, filenames in os.walk(folder):
        print('Dodawanie plikow w %s...' % (dirpath))
        # Dodanie biezacego katalogu do archiwum ZIP
        backupZip.write(dirpath)
        # Dodanie wszystkich plikow znajdujacych sie w tym katalogu do archiwum ZIP.
        for filename in filenames:
            newBase = os.path.basename(folder)
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # W archiwum nie umieszczamy plikow innych archiwow.
            backupZip.write(os.path.join(dirpath, filename))
    backupZip.close()
    print('Gotowe')

backupToZip('C:\\Users\\Dawid\\Desktop\\Python\\automatyzacja')