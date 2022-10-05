
class Clerk:
    def get_salary(self):
        print("clerk salary")

class Manager:
    def get_payments(self):
        print("manager salary")

class Contractor:
    def get_comission(self):
        print("contractor salary")


if __name__ == '__main__':
    personel = []
    personel.append(Clerk())
    personel.append(Manager())
    personel.append(Clerk())
    personel.append(Contractor())

    # print payroll
    for person in personel:
        if type(person) is Clerk:
            person.get_salary()
        elif type(person) is Manager:
            person.get_payments()
        elif type(person) is Contractor:
            person.get_comission()