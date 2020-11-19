from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.newegg.com/global/sg-en/p/pl?d=graphic+card").text

soup = BeautifulSoup(source, 'html')

item_container = soup.findAll("div", {"class": "item-container"})
prices = {}

for item in item_container:
    brand = item.find("a", class_="item-brand").img['title']
    title = item.a.img["title"]
    price = item.find('li', 'price-current').strong.text
    if ',' in price:
        coma = price.index(',')
        price = price[0:coma] + price[coma+1:]
        prices[title] = price
    prices[title] = price
    print("-------------------------------")
    print("BRAND: " + brand)
    print("TITLE: " + title)
    print("PRICE: $" + price)

keyP = min(prices, key=prices.get)

print(f'\nThe cheaper one is: {keyP} and it goes for: {prices[keyP]}$.')