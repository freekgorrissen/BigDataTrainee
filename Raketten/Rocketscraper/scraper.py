import requests
from bs4 import BeautifulSoup
from datetime import datetime


URL = 'https://en.wikipedia.org/wiki/Comparison_of_orbital_launch_systems'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
tabellen = soup.find_all('tbody')[0:2]


# print starttijd, sla starttijd op
from timeprint import printtime
start = datetime.now()
printtime(True)

# main loop: haal alle raketten op
import rocket

raketten = []
for tabel in tabellen:
    rijen = tabel.find_all('tr')
    for rij in rijen[2:]:
        raketten.append(rocket.get(rij))

print()
printtime(False)
minutes = (datetime.now() - start).seconds // 60    #floor division by 60
seconds = (datetime.now() - start).seconds %  60    #modulo by 60
aantal = len(raketten)
print('Tijd verstreken: ' + str(minutes) + ' minuten, ' + str(seconds) + ' seconden.')
print('Aantal raketten: ' + str(aantal) + '. Tijd per raket: ' + str(round(seconds/aantal, 2)) + ' seconden.')