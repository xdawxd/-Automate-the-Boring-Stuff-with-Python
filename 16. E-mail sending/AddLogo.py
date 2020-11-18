# AddLogo.py
# Had to change the project a little bit because it was changing the size of the main image instead of the logo.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'your_logo_name'

logo_img = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_img.size

os.makedirs('withLogo', exist_ok=True)

for filename in os.listdir('.'):
    if (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')
        or filename.lower().endswith('.gif') or filename.lower().endswith('bmp')) \
            and filename != LOGO_FILENAME:

        img = Image.open(filename)
        width, height = img.size

        if width < SQUARE_FIT_SIZE*2 or height < SQUARE_FIT_SIZE*2:
            continue

        if logo_width > SQUARE_FIT_SIZE and logo_height > SQUARE_FIT_SIZE:
            if logo_width > logo_height:
                logo_height = int((SQUARE_FIT_SIZE / logo_width) * logo_height)
                logo_width = SQUARE_FIT_SIZE
            else:
                logo_width = int((SQUARE_FIT_SIZE / logo_height) * logo_width)
                logo_height = SQUARE_FIT_SIZE
            print(f'Changing the size of a logo {LOGO_FILENAME}...')
            logo_img = logo_img.resize((logo_width, logo_height))

        print(f'Adding a logo to an image {filename}...')
        img.paste(logo_img, (width - logo_width, height - logo_height), logo_img)

        img.save(os.path.join('withLogo', filename))
