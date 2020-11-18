# umbrella_reminder.py - program which updates you on weather and reminds when to take an umbrella with you.

import smtplib
import requests
import json
import os

# You can pass your email and password to these variables or store them in env variables.
my_email = os.getenv('EMAIL_USER')
my_pas = os.getenv('EMAIL_PASS')
localisation = 'YOUR LOCALISATION'
API_KEY = 'INSERT YOUR API KEY HERE'
url = f'https://api.openweathermap.org/data/2.5/weather?q={localisation}&appid={API_KEY}'  #  You can add '&lang=pl' at the end to change the json file language.
res = requests.get(url)
res.raise_for_status()

weather_data = json.loads(res.text)

conditions = weather_data['weather'][0]['main']

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(my_email, my_pas)

if conditions in ['drizzle', 'rain', 'thunderstorm']:
    msg = f'Subject: The weather: {conditions}.\nYou should bring your umbrella with you.'
    sendmail_status = smtp_obj.sendmail(my_email, 'THE EMAIL U WANT THE MESSAGE TO BE SEND TO.', msg)

    if sendmail_status != {}:
        print('An ERROR occurred while sending mail.')
smtp_obj.quit()
