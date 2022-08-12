import hashlib


def new_balance(bank_balance, exchange_amount):
    new_bank_balance = int(bank_balance) - int(exchange_amount)
    return int(new_bank_balance)

def hash_password(pass_word):
    hash_pass = hashlib.md5(pass_word.encode())
    hashed_password = hash_pass.hexdigest()
    return hashed_password


