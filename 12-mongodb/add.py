import pymongo

import dotenv
import os

dotenv.load_dotenv()
user = os.getenv('MONGODB_ATLAS_USER')
password = os.getenv('MONGODB_ATLAS_PASSWORD')

client = pymongo.MongoClient("mongodb+srv://"+user+":"+password+"@cluster0.zae6j.mongodb.net/?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = client.company

print(db)

employees = db.employees
print(employees)

employee = {
    "last_name": "Mary",
    "first_name": "Ann",
    "age": 32,
    "position": "marketing"
}

employees.insert_one(employee)