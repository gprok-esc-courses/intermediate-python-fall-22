from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass

class Clerk(Employee):
    def get_salary(self):
        print("clerk salary")

class Manager(Employee):
    def get_payments(self):
        print("manager salary")
    def get_salary(self):
        self.get_payments()

class Contractor(Employee):
    def get_comission(self):
        print("contractor salary")
    def get_salary(self):
        self.get_comission()

class Secretery(Employee):
    def get_salary(self):
        print("secretery salary")


class EmployeeFactory:
    @classmethod
    def get_employee(cls, employee_type):
        if employee_type == "clerk":
            return Clerk()
        elif employee_type == "manager":
            return Manager()
        elif employee_type == "secretery":
            return Secretery()
        elif employee_type == "contractor":
            return Contractor()




if __name__ == '__main__':
    personel = []
    personel.append(EmployeeFactory.get_employee("clerk"))
    personel.append(EmployeeFactory.get_employee("manager"))
    personel.append(EmployeeFactory.get_employee("clerk"))
    personel.append(EmployeeFactory.get_employee("secretery"))
    personel.append(EmployeeFactory.get_employee("contractor"))

    # print payroll
    for person in personel:
        person.get_salary()