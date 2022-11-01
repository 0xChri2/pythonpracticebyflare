#does not work right now
from re import T
from urllib import request
import requests 
from bs4 import BeautifulSoup
import csv

#header 
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
url = "https://www.amazon.de/Netgear-GS305P-5-Port-Gigabit-Ethernet/dp/B07ZPG1Q2F/?content-id=amzn1.sym.d2bf7528-602b-4eba-aea2-23f8633d771d"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# auslesen von class title
title = soup.find("title").text
# auslesen von class price
price = soup.find("span", {"class": "a-section a-spacing-none aok-align-center"})
# auslesen von class rating
# in string umwandeln
title = str(title)
price = str(price)
print(title, price)

#einlesen von csv
with open('test.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([title, price])


