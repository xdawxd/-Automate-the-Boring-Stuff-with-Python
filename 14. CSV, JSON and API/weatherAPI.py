# weatherAPI.py - Displays weather in the localization you passed inside a terminal.

import json
import requests
import sys

if len(sys.argv) < 2:
    print('Uzycie: weatherAPI.py lokalizacja')
    sys.exit()
location = ' '.join(sys.argv[1:])

url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&appid={API_KEY}}&lang=pl' % location
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)

w = weatherData['list']

print('Aktualna pogoda w %s: ' % location)
print()
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Jutro: ')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Pojutrze: ')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
