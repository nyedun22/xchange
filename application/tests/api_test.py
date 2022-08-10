import unittest
import requests

# Testing API

class ApiTest (unittest.TestCase):
    url = 'https://v6.exchangerate-api.com/v6/867729e3b3de9dca04462186/latest/GBP'
    
    def test_1_get_all_fields(self):
        resp = requests.get(self.url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 9)
        print("Test 1 completed successfully")  # This test is successful because there are 9 fields in my API



if __name__ == "__main__":
    tester = ApiTest()

    tester.test_1_get_all_fields()



