import json
from bson import BSON
from bson import json_util

from pymongo import MongoClient
client = MongoClient('mongodb+srv://carolyn:bdatcarolyn@bigdata.mtnre.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client.bitcoin

collection = db['bitcoin']
cursor = collection.find({})
for document in cursor:
    final = json.dumps(document, indent=4, default=json_util.default)
    print(final)
exit()