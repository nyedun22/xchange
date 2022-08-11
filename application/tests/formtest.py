import unittest
import sys
sys.path.append('C:/Users/giann/PycharmProjects/xchange/application')  #update to be route in your own folder

from functions import new_balance, hash_password
from api_file import Currency


class TestFunc(unittest.TestCase):

    def test_valid_balance_calc(self):
        self.assertEqual(new_balance(1000, 50), 950)   #VALID

    def test_invalid_balance_calc(self):
        self.assertEqual(new_balance(50, 25), 50)      #INVALID

    def test_password_hash(self):
        password = 'string'
        hashed_password = hash_password(password)
        self.assertIsNot(password, hashed_password)     #VALID

    def test_exchange_amount(self):
        c = Currency()
        rate = 2
        self.assertEqual(c.exchange_amount(300), 600)    #not working right now need to change



if __name__ == '__main__':
    unittest.main()