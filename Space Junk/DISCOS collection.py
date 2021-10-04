#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Julian
#
# Created:     28/09/2021
# Copyright:   (c) Julian 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from pprint import pprint
import requests
import pandas
import time

counter = 0
for x in range(1,585,2):

    URL = 'https://discosweb.esoc.esa.int'
    token = #<Token>   Ik kan de mijne geven als je wilt. Laat hem hier uit.

    response = requests.get(
        f'{URL}/api/objects',
        headers={
            'Authorization': f'Bearer {token}',
            'DiscosWeb-Api-Version': '2',
        },
        params={
            'sort': "-cosparId",
            'page[size]' : 100,
            'page[number]' : x

        },
    )

    if counter == 10:
        #print("Zzzzzzz")
        time.sleep(61)
        counter=0
    else:
        counter+=1
    doc = response.json()
    if response.ok:
        #pprint(doc['data'])
        df = pandas.DataFrame(doc['data'])
        df.to_csv("C:/Users/Julian/Documents/Traineeship Projecten/Eindproject/DISCOS Data.txt", sep = ',', mode='a', index=False)
    else:
        pprint(doc['errors'])
        break

