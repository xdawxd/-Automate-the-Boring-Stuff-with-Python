# PhotoFolderFinder.py
"""
Prints an absolute path to a folder that appears to be a photo-folder.
A folder is considered a photo-folder if the number of photos inside
is greater that the number of files.
"""

import os
from PIL import Image

for dirpath, dirnames, filenames in os.walk('C:\\'):
    photo_counter = 0
    nonphoto_counter = 0

    for filename in filenames:
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
            nonphoto_counter += 1
            continue
        try:
            img = Image.open(filename)
            width, height = img.size
        except FileNotFoundError as exc:
            continue

        if width > 500 and height > 500:
            photo_counter += 1
        else:
            nonphoto_counter += 1

    if photo_counter > nonphoto_counter:
        print(f'The folder is a photo-folder and its destination is {os.path.abspath(dirpath)}')
