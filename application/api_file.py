import requests
from datetime import datetime
from pprint import pprint as pp


url = 'https://v6.exchangerate-api.com/v6/867729e3b3de9dca04462186/latest/GBP'

r = requests.get(url)
# print(r.status_code)
data = r.json()


Rate_Info = {}
GBP_amount = 0

class Currency:
    def __init__(self):
        self.rate = 0
        self.foreign_amount = 0
        self.currency_code = ''

    def get_rate(self):
        """
        Allows the user to select the desired currency, and returns the exchange rate from GBP along with a timestamp for the date of transaction
        """
        # self.currency_code = str(input("Enter currency code: "))
        Rate_Info['Currency'] = self.currency_code
        if r.status_code == 200:
            self.output = r.json()
            self.rate = (self.output['conversion_rates'][self.currency_code])
            print(self.rate)
            Rate_Info['Rate'] = self.rate
            ts = datetime.now()  # timestamp
            print('at ', (ts.strftime('%I:%M:%S, %d/%m/%Y')))

    def exchange_amount(self):
        """
        The user then inputs the amount to be exchanged, which shows as e.g. 100 GDP = 119.72 USD (rounded to 2 dp)
        """
        global GBP_amount
        enter_amount = int(input("Enter amount: £"))
        GBP_amount = enter_amount
        Rate_Info['AmountGBP'] = enter_amount
        foreign_amount = (enter_amount * self.rate)
        Rate_Info['Foreign_Amount'] = round(foreign_amount, 2)
        print(f'{enter_amount} GBP = ')
        print(round(foreign_amount, 2), self.currency_code)

c = Currency()
c.get_rate()
c.exchange_amount()
# print(Rate_Info)
print(GBP_amount)