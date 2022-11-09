import pymongo

print(pymongo.version)


client = pymongo.MongoClient("mongodb+srv://temp:4vadeTQfsi62Z7b@cluster0.zae6j.mongodb.net/?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = client.company

print(db)

employees = db.employees
print(employees)

employee = {
    "last_name": "Peter",
    "first_name": "Pan",
    "age": 32,
    "position": "manager"
}

employees.insert_one(employee)