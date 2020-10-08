import requests
from bs4 import BeautifulSoup

#website = input('Enter the URL that you would like to verify the links for: ')
website = 'https://pasja-informatyki.pl'
res = requests.get(website)
res.raise_for_status()

soup = BeautifulSoup(res.text, features='lxml')
links = soup.select('a')
fof = [] #  List for 404 errored links.

for link in links:
    li = link.get('href')

    if str(li).startswith('/'):
        li = website + li

    elif str(li).startswith('#'):
        li = website + li

    elif not (str(li).startswith('/') or str(li).startswith('/') or str(li).startswith('http')):
        li = website + '/' + str(li)

    res = requests.get(li)
    print(f'Checking {li}...')

    if res.status_code == 404:
        fof.append(li)

print(f'List of found 404 errors: {fof}')