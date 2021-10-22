import mass

class Raket:
    naam = ""
    link = ""
    payloadLEO = 0
    jaar = 0
    massa = 0


def get(rij):
    raket = Raket()

    cellen = rij.find_all('td')

    # Naam uitlezen
    naam = cellen[0].text.rstrip()
    raket.naam = naam

    # Link uitlezen (indien mogelijk)
    link = cellen[0].find('a', href=True)
    if link:
        link = 'https://en.wikipedia.org/' + link.get('href')
        raket.link = link
    else:
        raket.link = ''

    # Payload uitlezen
    payload = cellen[3].text
    if '[' in payload:
        loc = payload.index('[')
    else:
        loc = len(payload)
    payload = payload[0:loc].replace(',', '').rstrip()
    if payload.isnumeric():
        raket.payloadLEO = int(payload)
    else:
        raket.payloadLEO = 0

    jaar = cellen[7].text
    jaar = jaar[0:min(4, len(jaar))].rstrip()
    if jaar.isnumeric():
        raket.jaar = int(jaar)
    else:
        raket.jaar = 0

    # massa ophalen met functie, in try/catch blok omdat de functie om verschillende redenen kan falen
    try:
        massa = mass.get(link)
    except:
        massa = 0
    raket.massa = massa

    print(
        'Naam: {:<50} Payload: {:<6} kg. Jaar: {:<6} Massa: {:<8} kg.'.format(raket.naam, raket.payloadLEO, raket.jaar,
                                                                              raket.massa))
    return raket
