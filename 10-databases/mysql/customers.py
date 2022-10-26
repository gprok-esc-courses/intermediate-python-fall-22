import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="vehicles", password="1111", database="vehicles"
)


def view():
    query = "SELECT * FROM customers"
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    for row in data:
        print(row[0], row[1], row[2])


def add():
    ssn = input("SSN: ")
    name = input("Name: ")
    query = "INSERT INTO customers (ssn, name) VALUES ('" + ssn + "', '" + name + "')"
    # query = "INSERT INTO customers (ssn, name) VALUES ('{}', '{}')".format(ssn, name)
    # query = f"INSERT INTO customers (ssn, name) VALUES ('{ssn}', '{name}')"
    print(query)
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    print("Customer added")


def add_prepared():
    ssn = input("SSN: ")
    name = input("Name: ")
    query = "INSERT INTO customers (ssn, name) VALUES (%s, %s)"
    values = (ssn, name)
    cursor = db.cursor()
    cursor.execute(query, values)
    db.commit()
    print("Customer added")


def delete():
    ssn = input("SSN to delete: ")
    query = "DELETE FROM customers WHERE ssn='" + ssn + "'"
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    print("SSN", ssn, "deleted")


def update():
    ssn = input("SSN to update: ")
    name = input("Give new name: ")
    query = "UPDATE customers SET name='" +name + "' WHERE ssn='" + ssn + "'"
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    print("SSN", ssn, "updated")


if __name__ == '__main__':
    while True:
        print("1. View Customers")
        print("2. Add Customer")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("0. EXIT")
        choice = input("Choose: ")

        if choice == '1':
            view()
        elif choice == '2':
            add()
        elif choice == '3':
            update()
        elif choice == '4':
            delete()
        elif choice == '0':
            print('bye!')
            break
        else:
            print("Wrong choice")

