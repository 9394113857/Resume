# Sure, here's an example of how to write unittest code for the BankAccount class:
import unittest
from oops_concepts.Method_Overloading.BankAccount import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account1 = BankAccount("12345", 1000)

    def test_deposit_positive_amount(self):
        self.account1.deposit(500)
        self.assertEqual(self.account1.balance, 1500)

    def test_deposit_zero_amount(self):
        self.account1.deposit(0)
        self.assertEqual(self.account1.balance, 1000)

    def test_deposit_negative_amount(self):
        self.account1.deposit(-500)
        self.assertEqual(self.account1.balance, 1000)

    def test_withdraw_positive_amount(self):
        self.account1.withdraw(500)
        self.assertEqual(self.account1.balance, 500)

    def test_withdraw_zero_amount(self):
        self.account1.withdraw(0)
        self.assertEqual(self.account1.balance, 1000)

    def test_withdraw_negative_amount(self):
        self.account1.withdraw(-500)
        self.assertEqual(self.account1.balance, 1000)

    def test_withdraw_insufficient_funds(self):
        self.account1.withdraw(2000)
        self.assertEqual(self.account1.balance, 1000)

    def test_get_balance(self):
        self.assertEqual(self.account1.get_balance(), "Current balance of account 12345 is 1000.")


if __name__ == '__main__':
    unittest.main()

