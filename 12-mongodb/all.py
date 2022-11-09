import pymongo

import dotenv
import os

dotenv.load_dotenv()
user = os.getenv('MONGODB_ATLAS_USER')
password = os.getenv('MONGODB_ATLAS_PASSWORD')

client = pymongo.MongoClient("mongodb+srv://"+user+":"+password+"@cluster0.zae6j.mongodb.net/?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = client.company

employees = db.employees

all = employees.find({})

for e in all:
    print(e)
    print(e['last_name'] + ", " + e['first_name'])