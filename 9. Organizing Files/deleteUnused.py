# deleteUnused.py - Usun nieuzywane pliki o wyznaczonych wielkosciach.

import os, send2trash

def deleteUnused(path, sizeInMb):
    sizeInMb *= 1000000
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if os.path.getsize(os.path.join(dirpath, filename)) >= sizeInMb:
                send2trash.send2trash(os.path.join(dirpath, filename))

deleteUnused('C:\\Users\\Dawid\\Desktop\\delete', 1.4)
