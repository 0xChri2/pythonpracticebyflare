from urllib import request
import BeautifulSoup
import csv
#idealo preisvergleich auslesen
url = "https://www.idealo.de/preisvergleich/OffersOfProduct/201545266_-gp-aeohubv3eu-aeotec.html"
page = request.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#preis auslesen
preis = soup.find("span", {"class": "price"})
#preis in string umwandeln
preis = str(preis)
#preis in liste umwandeln
preis = preis.split(">")
#preis in string umwandeln
preis = preis[1]
#preis in liste umwandeln
preis = preis.split("<")
#preis in string umwandeln
preis = preis[0]
#preis in float umwandeln
preis = float(preis)
#preis in liste umwandeln
preis = preis.split(",")
#preis in string umwandeln

#preis in csv schreiben
with open('preis.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(preis)



