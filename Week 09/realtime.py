import requests
import time
import json

from pymongo import MongoClient

try: 
    client = MongoClient('mongodb+srv://carolyn:bdatcarolyn@bigdata.mtnre.mongodb.net/bitcoin?retryWrites=true&w=majority')
    print("Connected succesfully.")
except:
    print("Could not connect to MongoDB.")

db = client['bitcoin']
collection = db['bitcoin']


while True:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if r.status_code ==200:
        data = r.json()
        print(data)
        db.bitcoin.insert_one(data)
        time.sleep(60)
    else:
        exit()