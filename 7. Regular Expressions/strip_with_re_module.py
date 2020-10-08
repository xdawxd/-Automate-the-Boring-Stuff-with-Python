import re


def re_strip(text, characters=0):
    '''
    None and 0: default strip spaces from LEFT and RIGHT
    1: strip LEFT spaces
    2: strip RIGHT spaces
    '''
    if characters == 0:
        text_regex = re.compile(r'^\s+ | \s+$', re.I | re.DOTALL)
        return text_regex.sub('', text)

    if characters == 1:
        text_regex = re.compile(r'^\s+', re.I | re.DOTALL)
        return text_regex.sub('', text)

    if characters == 2:
        text_regex = re.compile(r'\s+$', re.I | re.DOTALL)
        return text_regex.sub('', text)
