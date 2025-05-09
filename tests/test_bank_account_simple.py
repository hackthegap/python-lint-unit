# a test is a class
# we need to follow the name of the class
# we will do assertions
# we need to test the happy path and the unhappy path

# command:
# python3 -m unittest discover -s tests

import unittest
from bank.simple_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Alice", 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_withdraw_success(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

    def test_withdraw_more_than_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1000)

if __name__ == "__main__":
    unittest.main()

