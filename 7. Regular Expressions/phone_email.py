#! python3
#phoneAndEmail.py - Wyszukuje numery telefonow i adresy e-mail w schowki.

import pyperclip, re, os

#phone number regex
phoneNumRegex = re.compile(r'''
(\+\d{2}\s?)?
(\d{3})
(\s|-|\.)?
(\d{3})
(\s|-|\.)?
(\d{3})
''', re.VERBOSE | re.DOTALL)

#e-mail regex
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.I | re.DOTALL | re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneNumRegex.findall(text):
    phoneNum = ' '.join([groups[0], groups[1], groups[3], groups[5]])
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Skopiowanie do schowka
'''if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to the clipboard.')
    print('\n'.join(matches))
else:
    print('No phone numbers or e-mail addresses found.')'''\

with open('numbers_emails.txt', 'a+') as info:
    info.seek(0)
    elements = list(map(lambda x: x.strip(), info.readlines()))

    for match in matches:
        if match not in elements:
            info.write(match + '\n')

