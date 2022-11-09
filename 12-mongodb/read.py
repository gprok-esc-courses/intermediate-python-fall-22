import pymongo
# INSTALL:  python -m pip install "pymongo[snappy,gssapi,srv,tls]"
import dotenv
# INSTALL: pip install python-dotenv
import os

dotenv.load_dotenv()
user = os.getenv('MONGODB_ATLAS_USER')
password = os.getenv('MONGODB_ATLAS_PASSWORD')

print(pymongo.version)


client = pymongo.MongoClient("mongodb+srv://"+user+":"+password+"@cluster0.zae6j.mongodb.net/?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = client.company

print(db)

employees = db.employees
print(employees)

employee = employees.find_one({"last_name": "Willis"})
print(employee)
