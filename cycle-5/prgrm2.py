class Bank_Account:
    def __init__(self,name,account_type):
        self.balance = 0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Net Available Balance=", self.balance)
a = input("Enter the name of the customer: ")
b = int(input("Enter the account number: "))
s = Bank_Account(a,b)
s.deposit()
s.withdraw()
s.display()