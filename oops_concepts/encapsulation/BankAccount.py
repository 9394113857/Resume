# Encapsulation is one of the fundamental principles of object-oriented programming (OOP). It refers to the practice of hiding the internal details of an object and only exposing the necessary information through well-defined interfaces. In Python, encapsulation can be achieved using access modifiers.
#
# Let's take a real-time scenario of a bank account class to demonstrate encapsulation. In this scenario, we will create a bank account class that has two attributes - account number and balance. We will also define two methods - deposit and withdraw - to update the balance.
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

# In the above code, we have used double underscores before the attribute names, which makes them private. This means that they can only be accessed within the class and not from outside the class. We have also defined two methods - deposit and withdraw - to update the balance.
#
# The deposit method takes an amount as input and adds it to the balance. The withdraw method takes an amount as input and subtracts it from the balance, but only if the balance is sufficient. If the balance is insufficient, it prints an error message.
#
# The get_balance method is a getter method that returns the current balance. Since the balance attribute is private, we cannot access it directly from outside the class. Hence, we need a getter method to access the balance.
#
# Now, let's create an object of the BankAccount class and test it out.

account = BankAccount(12345, 1000)
print(account.get_balance())    # Output: 1000

account.deposit(500)
print(account.get_balance())    # Output: 1500

account.withdraw(200)
print(account.get_balance())    # Output: 1300

account.withdraw(1500)          # Output: Insufficient balance


# In the above code, we create an object of the BankAccount class with an account number of 12345 and a balance of 1000. We then deposit 500 into the account, followed by a withdrawal of 200. Finally, we try to withdraw 1500, which results in an error message since the balance is insufficient.
#
# As we can see, encapsulation allows us to hide the internal details of the BankAccount class and only expose the necessary information through well-defined interfaces. This makes the code more secure and easier to maintain.