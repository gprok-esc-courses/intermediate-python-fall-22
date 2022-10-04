import csv


class ATM:
    def __init__(self):
        self.accounts = {}
        self.current_account = None

    def load_accounts(self):
        # read accounts from the csv file
        with open('bank.csv') as file:
            reader = csv.reader(file)
            counter = 0
            for row in reader:
                if counter > 0:
                    account = Account(row)
                    self.accounts[account.account_no] = account
                counter += 1

    def get_account_no(self):
        # ask user for their account number
        n = input("Account No:")
        if n in self.accounts:
            self.current_account = n
            return True
        else:
            print("Account not found")
            return False

    def display_balance(self):
        print("Balance: ", self.accounts[self.current_account].balance)

    def deposit(self):
        try:
            a = int(input("Amount: "))
            if a < 0:
                print("Positive numbers only please")
            elif a % 5 != 0:
                print("Multiples of 5 only")
            else:
                self.accounts[self.current_account].deposit(a)
        except ValueError:
            print("Integers only please")

    def withdraw(self):
        try:
            a = int(input("Amount: "))
            if a < 0:
                print("Positive numbers only please")
            elif a % 5 != 0:
                print("Multiples of 5 only")
            elif a > self.accounts[self.current_account].balance:
                print("Amount is greater than your balance")
            else:
                self.accounts[self.current_account].withdraw(a)
        except ValueError:
            print("Integers only please")

    def issue_credit_card(self):
        # EX.1: Prerequisites for CC issue:
        # Not be unemployed
        # Balance >= 1000
        if self.accounts[self.current_account].credit_card == "no":
            self.accounts[self.current_account].credit_card = "yes"
            print("Credit card issued")
        else:
            print("You already have your credit card")

    def save(self):
        with open('bank.csv', 'w') as file:
            file.write("account,age,job,marital,education,balance,cc\n")
            for a in self.accounts:
                file.write(self.accounts[a].get_csv())

    def menu(self):
        # EX2: New option, transfer
        # Ask user for another account no, if valid, ask for amount
        # if valid amount withdraw from current and deposit to given account
        print("1. Balance\n2. Deposit\n3. Withdraw\n4. Issue Credit Card\n0. EXIT")
        try:
            v = int(input())
            if v == 1:
                self.display_balance()
            elif v == 2:
                self.deposit()
            elif v == 3:
                self.withdraw()
            elif v == 4:
                self.issue_credit_card()
            elif v == 0:
                self.save()
                print("Bye!")
            else:
                print("Wrong choice")
        except ValueError:
            print("Error: please numbers only")
            v = -1
        return v


class Account:
    def __init__(self, data):
        self.account_no = data[0]
        self.age = data[1]
        self.job = data[2]
        self.marital = data[3]
        self.education = data[4]
        self.balance = int(data[5])
        self.credit_card = data[6]

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_csv(self):
        return self.account_no + ',' + self.age + ',' + self.job + ',' + self.marital + \
                ',' + self.education + ',' + str(self.balance) + ',' + self.credit_card + '\n'

    def __str__(self):
        return self.account_no + ": " + self.balance


if __name__ == '__main__':
    atm = ATM()
    atm.load_accounts()

    if atm.get_account_no():
        while True:
            v = atm.menu()
            if v == 0:
                break;
