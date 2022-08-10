import requests
from pprint import pprint as pp

url = 'https://v6.exchangerate-api.com/v6/867729e3b3de9dca04462186/latest/GBP'

r = requests.get(url)
# print(r.status_code)
data = r.json()

class Currency:
    def __init__(self):
        self.rate = 0
        self.foreign_amount = 0
        self.currency_code = None

    def get_rate(self, currency_code):
        """
        Allows the user to select the desired currency, and returns the exchange rate from GBP along with a timestamp for the date of transaction
        """
        self.currency_code = currency_code
        if r.status_code == 200:
            self.output = r.json()
            self.rate = (self.output['conversion_rates'][currency_code])
            print(self.rate)
            return self.rate


    def exchange_amount(self, GBP_amount):
        """
        The user then inputs the amount to be exchanged, which shows as e.g. 100 GDP = 119.72 USD (rounded to 2 dp)
        """
        foreign_amount = (GBP_amount * self.rate)
        return round(foreign_amount, 2)

