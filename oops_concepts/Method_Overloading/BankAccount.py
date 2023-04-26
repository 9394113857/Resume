# Method Overloading in Python is a concept where multiple methods in a class have the same name but different parameters. It is a form of polymorphism that allows a class to have multiple methods with the same name but different signature (parameter types, number of parameters, or order of parameters).
#
# A real-time scenario where method overloading could be used is in a banking application where different types of accounts have different requirements for opening an account. For example, a savings account requires a minimum deposit, while a current account requires a letter of credit from a reputable organization.
#
# Let's see how we can implement Method Overloading in Python:
class BankAccount:

    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"Deposit of {amount} made to account {self.account_no}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} made from account {self.account_no}. New balance is {self.balance}.")

    def get_balance(self):
        print(f"Current balance of account {self.account_no} is {self.balance}.")

# In this implementation, the BankAccount class has an __init__ method that takes an account number and an optional balance parameter. The default value of the balance parameter is 0.
#
# The class also has three other methods: deposit, withdraw, and get_balance. The deposit method takes an amount parameter and adds it to the account's balance if the amount is greater than zero. If the amount is zero or negative, the method prints an error message.
#
# The withdraw method takes an amount parameter and subtracts it from the account's balance if there are sufficient funds and the amount is greater than zero. If there are insufficient funds, the method prints an error message. If the amount is zero or negative, the method also prints an error message.
#
# The get_balance method simply prints the current balance of the account.
#
# Here's an example of how you can use this class:
# Create a new bank account with account number "12345"
account1 = BankAccount("12345")

# Deposit $1000 into the account
account1.deposit(1000)

# Withdraw $500 from the account
account1.withdraw(500)

# Check the current balance of the account
account1.get_balance()

# Attempt to withdraw an amount greater than the balance
account1.withdraw(10000)

# Attempt to deposit a negative amount
account1.deposit(-500)
