import requests
from lxml import html
import time
import json
import re
import pymongo
import os

#Setup mongo collection
storename = os.environ['storename']    
token = os.environ['token']    
#with open ("storename", "r") as storenamefile:
#    storename = storenamefile.read()
#with open ("token", "r") as tokenfile:
#    token = tokenfile.read()

#Establish connection
uri = 'mongodb://{}:{}@{}.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&retrywrites=false&appName=@{}@'.format(storename, token, storename, storename)
client = pymongo.MongoClient(uri)
db = client["heroesDB"]
col = db["heroesCollection2"]

heroes_dict = {'time': time.asctime()}

r = requests.get('https://api.opendota.com/api/heroes')
for hero in r.json():
    url = ('http://www.dota2protracker.com/hero/{}'.format(hero["localized_name"]))
    page = requests.get(url)
    tree = html.fromstring(page.content)
    hero_dict = {
        hero["localized_name"]: {
            "Carry": {
                "frequency": "0",
                "winrate": "0"
            },
            "Mid": {
                "frequency": "0",
                "winrate": "0"
            },
            "Offlane": {
                "frequency": "0",
                "winrate": "0"
            },
            "Support (4)": {
                "frequency": "0",
                "winrate": "0"
            },
            "Support (5)": {
                "frequency": "0",
                "winrate": "0"
            }
        }
    }
    for element in tree.xpath('//div[@class = "role_box_left"]'):
        subelements = element.getchildren()
        role_to_json = {
            subelements[0].text: {
                'frequency': re.match("[0-9.]*", subelements[1].text)[0],
                'winrate': re.match("[0-9.]*", subelements[2].text)[0]
            }
        }
        hero_dict[hero["localized_name"]].update(role_to_json)
    heroes_dict.update(hero_dict)
x = col.insert_one(heroes_dict)
print('{} all done'.format(time.asctime()))