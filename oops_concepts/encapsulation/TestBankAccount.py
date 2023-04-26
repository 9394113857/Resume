# To write a unit test for the BankAccount class, we can use the built-in unittest module in Python. We will create a test case that tests the deposit, withdraw, and get_balance methods of the class.
import unittest
from oops_concepts.encapsulation.BankAccount import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(12345, 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 800)

    def test_insufficient_balance(self):
        self.account.withdraw(1500)
        self.assertEqual(self.account.get_balance(), 1000)


if __name__ == '__main__':
    unittest.main()

# In the above code, we import the unittest module and create a test case class called TestBankAccount. In the setUp method, we create an instance of the BankAccount class with an account number of 12345 and a balance of 1000.
#
# We then define three test methods - test_deposit, test_withdraw, and test_insufficient_balance.
#
# The test_deposit method tests the deposit method by depositing 500 into the account and then checking if the balance is 1500.
#
# The test_withdraw method tests the withdraw method by withdrawing 200 from the account and then checking if the balance is 800.
#
# The test_insufficient_balance method tests the withdraw method by trying to withdraw 1500 from the account, which should result in an insufficient balance error message. We then check if the balance is still 1000.
#
# Finally, we use the unittest.main() method to run the test case.
#
# When we run the above test code, it will output the results of the tests. If all the tests pass, it means that our BankAccount class is working as expected. If any of the tests fail, we need to go back and fix the code to make it work correctly.
#
# Overall, unit testing is an important practice in software development because it helps us to catch bugs and ensure that our code is working as expected. By writing test cases for our classes and functions, we can be more confident in the reliability and correctness of our code.
