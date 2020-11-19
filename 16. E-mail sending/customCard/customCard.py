# CustomCards.py

import os
from PIL import Image, ImageDraw, ImageFont


def sign_guest(person):
    max_width = 360, 288
    fonts_folder = 'C:\\Windows\\Fonts'
    bradhitc_font = ImageFont.truetype(os.path.join(fonts_folder,
                                                    'BRADHITC.ttf'), 32)

    flower_img = Image.open('flowers.jpg')
    flowers_resized = flower_img.copy()
    flowers_resized.thumbnail(max_width, Image.ANTIALIAS)

    card = ImageDraw.Draw(flowers_resized)
    card.rectangle((0, 0, 360, 240), outline='black', width=3)

    draw_name = ImageDraw.Draw(flowers_resized)
    draw_name.text((150, 100), person, fill='black', font=bradhitc_font)
    flowers_resized.save(os.path.join('guests', f'{person}.png'))


os.makedirs('guests', exist_ok=True)

with open('guests.txt') as file:
    guests = list(map(lambda x: x.strip(), file.readlines()))

for guest in guests:
    sign_guest(guest)
