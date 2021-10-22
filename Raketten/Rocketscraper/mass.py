import requests
from bs4 import BeautifulSoup

unit_conversion = {'kg': 1,
                   'kilogram': 1,
                   'kilograms': 1,
                   'lb': 0.454,
                   'pounds': 0.454,
                   'pound': 0.454,
                   't': 1000,
                   'tonne': 1000,
                   'tons': 1000,
                   }

def get(URL):
    mass = 0  # default waarde, wordt veranderd als deze wordt gevonden

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    tabel = soup.find('table', {'class': 'infobox hproduct'})
    headers = tabel.find_all('th', {'class': 'infobox-label'})
    datarijen = tabel.find_all('td', {'class': 'infobox-data'})
    rijen = tabel.find_all('tr')

    # range bepalen van de elementen die onder de size header vallen
    size_header_index = 0
    next_header_index = 0

    header_found = False
    for i in range(len(rijen)):
        header = rijen[i].find('th', {'class': 'infobox-header'})
        if header:  # check of de de rij een header is
            if header.text == "Size":
                size_header_index = i
                header_found = True
            elif header_found:
                next_header_index = i
                break
            # elif header.text.strip() == "Capacity":
            #     capacity_header_index = i

    if size_header_index:  # check of de size header en cap header zijn gevonden
        # index van raket massa ophalen
        for i in range(size_header_index, next_header_index):
            header = rijen[i].find('th')
            content = rijen[i].find('td')

            # check of de betreffende rij een header is
            if header:
                if header.text == "Mass":  # check of het de juiste header is
                    mass_line = content.text
                    mass_line = mass_line.replace("–", " ")
                    mass_line = mass_line.replace("-", " ")
                    mass_line = mass_line.split()
                    unit_index = 0
                    unit = None
                    for key in unit_conversion.keys():
                        try:
                            unit_index = mass_line.index(key)
                            unit = key
                            break  # breaks out of for loop if key is found
                        except:
                            continue

                    if unit_index != 0:
                        mass = mass_line[unit_index - 1]
                        mass = mass.replace(',', '')
                        mass = int(mass) * unit_conversion[unit]
                        mass = int(mass)

    return mass