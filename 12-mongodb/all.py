import ssl

import pymongo

client = pymongo.MongoClient("mongodb+srv://temp:4vadeTQfsi62Z7b@cluster0.zae6j.mongodb.net/?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = client.company

employees = db.employees

all = employees.find({})

for e in all:
    print(e)
    print(e['last_name'] + ", " + e['first_name'])