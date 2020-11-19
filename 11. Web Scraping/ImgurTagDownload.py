#  ImgurTagDownload.py - Downloads images from imgur by a provided tag. 

import os
import requests
from bs4 import BeautifulSoup

tag = input('Enter a tag: ')
amount = int(input('How many photos: '))
url = 'https://imgur.com/search?q=' + str(tag)
os.makedirs('%s' % tag, exist_ok=True)

for img in range(amount):

    #  Website download.
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, features='lxml')

    #  Image downloading.
    imgElem = soup.select('.image-list-link img')[img]
    if not imgElem:
        print('No photos found.')
    else:
        imgUrl = 'https:' + str(imgElem.get('src'))

        print('Downloading image: %s' % imgUrl)
        res = requests.get(imgUrl)
        res.raise_for_status()

        #  File saving.
        imageFile = open(os.path.join('%s' % tag, os.path.basename(imgUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

print('Done!')


