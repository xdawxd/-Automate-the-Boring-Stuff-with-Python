# MultidownloadXkcd.py - Downloads comics from xkcd.com, with mutlithreading.

import requests
import os
from bs4 import BeautifulSoup
import threading

os.makedirs('xkcd', exist_ok=True)


def download_xkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Downloading the website.
        print('Pobieranie strony https://xkcd.com/%s' % urlNumber)
        res = requests.get('https://xkcd.com/%s' % urlNumber)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, features='lxml')

        # Getting the img URL.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Nie udalo sie odnalesc obrazu.')
        else:
            comicUrl = 'https:' + comicElem[0].get('src')
            # Img downloading.
            print('Pobieranie obrazu %s...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Saving an img in ./xkcd path.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


# Making of and running threading objects.
threads = []
for i in range(0, 1400, 100):  # Making 14 threads.
    thread = threading.Thread(target=download_xkcd, args=[i, i + 99])
    threads.append(thread)
    threadhread.start()

# Closing all threads.
for thread in threads:
    thread.join()
print('Gotowe!')
