from db_models import foreign_account, user_details, bank_details, foreign_account, currency_codes, transactions_record
from sqlalchemy.orm import Session
from db_models import db

session = Session()

currencies_list = [
    ['AED', 'UAE Dirham', 'United Arab Emirates'],
    ['AFN', 'Afghan Afghani', 'Afghanistan'],
    ['ALL', 'Albanian Lek', 'Albania'],
    ['AMD', 'Armenian Dram', 'Armenia'],
    ['ANG', 'Netherlands Antillian Guilder', 'Netherlands Antilles'],
    ['AOA', 'Angolan Kwanza', 'Angola'],
    ['ARS', 'Argentine Peso', 'Argentina'],
    ['AUD', 'Australian Dollar', 'Australia'],
    ['AWG', 'Aruban Florin', 'Aruba'],
    ['AZN', 'Azerbaijani Manat', 'Azerbaijan'],
    ['BAM', 'Bosnia and Herzegovina Mark', 'Bosnia and Herzegovina'],
    ['BBD', 'Barbados Dollar', 'Barbados'],
    ['BDT', 'Bangladeshi Taka', 'Bangladesh'],
    ['BGN', 'Bulgarian Lev', 'Bulgaria'],
    ['BHD', 'Bahraini Dinar', 'Bahrain'],
    ['BIF', 'Burundian Franc', 'Burundi'],
    ['BMD', 'Bermudian Dollar', 'Bermuda'],
    ['BND', 'Brunei Dollar', 'Brunei'],
    ['BOB', 'Bolivian Boliviano', 'Bolivia'],
    ['BRL', 'Brazilian Real', 'Brazil'],
    ['BSD', 'Bahamian Dollar', 'Bahamas'],
    ['BTN', 'Bhutanese Ngultrum', 'Bhutan'],
    ['BWP', 'Botswana Pula', 'Botswana'],
    ['BYN', 'Belarusian Ruble', 'Belarus'],
    ['BZD', 'Belize Dollar', 'Belize'],
    ['CAD', 'Canadian Dollar', 'Canada'],
    ['CDF', 'Congolese Franc', 'Democratic Republic of the Congo'],
    ['CHF', 'Swiss Franc', 'Switzerland'],
    ['CLP', 'Chilean Peso', 'Chile'],
    ['CNY', 'Chinese Renminbi', 'China'],
    ['COP', 'Colombian Peso', 'Colombia'],
    ['CRC', 'Costa Rican Colon', 'Costa Rica'],
    ['CUP', 'Cuban Peso', 'Cuba'],
    ['CVE', 'Cape Verdean Escudo', 'Cape Verde'],
    ['CZK', 'Czech Koruna', 'Czech Republic'],
    ['DJF', 'Djiboutian Franc', 'Djibouti'],
    ['DKK', 'Danish Krone', 'Denmark'],
    ['DOP', 'Dominican Peso', 'Dominican Republic'],
    ['DZD', 'Algerian Dinar', 'Algeria'],
    ['EGP', 'Egyptian Pound', 'Egypt'],
    ['ERN', 'Eritrean Nakfa', 'Eritrea'],
    ['ETB', 'Ethiopian Birr', 'Ethiopia'],
    ['EUR', 'Euro', 'European Union'],
    ['FJD', 'Fiji Dollar', 'Fiji'],
    ['FKP', 'Falkland Islands', 'Pound Falkland Islands'],
    ['FOK', 'Faroese Króna', 'Faroe Islands'],
    ['GBP', 'Pound Sterling', 'United Kingdom'],
    ['GEL', 'Georgian Lari', 'Georgia'],
    ['GGP', 'Guernsey Pound', 'Guernsey'],
    ['GHS', 'Ghanaian Cedi', 'Ghana'],
    ['GIP', 'Gibraltar Pound', 'Gibraltar'],
    ['GMD', 'Gambian Dalasi', 'The Gambia'],
    ['GNF', 'Guinean Franc', 'Guinea'],
    ['GTQ', 'Guatemalan Quetzal', 'Guatemala'],
    ['GYD', 'Guyanese Dollar', 'Guyana'],
    ['HKD', 'Hong Kong Dollar', 'Hong Kong'],
    ['HNL', 'Honduran Lempira', 'Honduras'],
    ['HRK', 'Croatian Kuna', 'Croatia'],
    ['HTG', 'Haitian', 'Gourde Haiti'],
    ['HUF', 'Hungarian Forint', 'Hungary'],
    ['IDR', 'Indonesian Rupiah', 'Indonesia'],
    ['ILS', 'Israeli New Shekel', 'Israel'],
    ['IMP', 'Manx Pound', 'Isle of Man'],
    ['INR', 'Indian Rupee', 'India'],
    ['IQD', 'Iraqi Dinar', 'Iraq'],
    ['IRR', 'Iranian Rial', 'Iran'],
    ['ISK', 'Icelandic Króna', 'Iceland'],
    ['JEP', 'Jersey Pound', 'Jersey'],
    ['JMD', 'Jamaican Dollar', 'Jamaica'],
    ['JOD', 'Jordanian Dinar', 'Jordan'],
    ['JPY', 'Japanese Yen', 'Japan'],
    ['KES', 'Kenyan Shilling', 'Kenya'],
    ['KGS', 'Kyrgyzstani Som', 'Kyrgyzstan'],
    ['KHR', 'Cambodian Riel', 'Cambodia'],
    ['KID', 'Kiribati Dollar', 'Kiribati'],
    ['KMF', 'Comorian Franc', 'Comoros'],
    ['KRW', 'South Korean Won', 'South Korea'],
    ['KWD', 'Kuwaiti Dinar', 'Kuwait'],
    ['KYD', 'Cayman Islands Dollar', 'Cayman Islands'],
    ['KZT', 'Kazakhstani Tenge', 'Kazakhstan'],
    ['LAK', 'Lao Kip', 'Laos'],
    ['LBP', 'Lebanese Pound', 'Lebanon'],
    ['LKR', 'Sri Lanka Rupee', 'Sri Lanka'],
    ['LRD', 'Liberian Dollar', 'Liberia'],
    ['LSL', 'Lesotho Loti', 'Lesotho'],
    ['LYD', 'Libyan Dinar', 'Libya'],
    ['MAD', 'Moroccan Dirham', 'Morocco'],
    ['MDL', 'Moldovan Leu', 'Moldova'],
    ['MGA', 'Malagasy Ariary', 'Madagascar'],
    ['MKD', 'Macedonian Denar', 'North Macedonia'],
    ['MMK', 'Burmese Kyat', 'Myanmar'],
    ['MNT', 'Mongolian Tögrög', 'Mongolia'],
    ['MOP', 'Macanese Pataca', 'Macau'],
    ['MRU', 'Mauritanian Ouguiya', 'Mauritania'],
    ['MUR', 'Mauritian Rupee', 'Mauritius'],
    ['MVR', 'Maldivian Rufiyaa', 'Maldives'],
    ['MWK', 'Malawian Kwacha', 'Malawi'],
    ['MXN', 'Mexican Peso', 'Mexico'],
    ['MYR', 'Malaysian Ringgit', 'Malaysia'],
    ['MZN', 'Mozambican Metical', 'Mozambique'],
    ['NAD', 'Namibian Dollar', 'Namibia'],
    ['NGN', 'Nigerian Naira', 'Nigeria'],
    ['NIO', 'Nicaraguan Córdoba', 'Nicaragua'],
    ['NOK', 'Norwegian Krone', 'Norway'],
    ['NPR', 'Nepalese Rupee', 'Nepal'],
    ['NZD', 'New Zealand Dollar', 'New Zealand'],
    ['OMR', 'Omani Rial', 'Oman'],
    ['PAB', 'Panamanian Balboa', 'Panama'],
    ['PEN', 'Peruvian Sol', 'Peru'],
    ['PGK', 'Papua New Guinean Kina', 'Papua New Guinea'],
    ['PHP', 'Philippine Peso', 'Philippines'],
    ['PKR', 'Pakistani Rupee', 'Pakistan'],
    ['PLN', 'Polish Złoty', 'Poland'],
    ['PYG', 'Paraguayan Guaraní', 'Paraguay'],
    ['QAR', 'Qatari Riyal', 'Qatar'],
    ['RON', 'Romanian Leu', 'Romania'],
    ['RSD', 'Serbian Dinar', 'Serbia'],
    ['RUB', 'Russian Ruble', 'Russia'],
    ['RWF', 'Rwandan Franc', 'Rwanda'],
    ['SAR', 'Saudi Riyal', 'Saudi Arabia'],
    ['SBD', 'Solomon Islands Dollar', 'Solomon Islands'],
    ['SCR', 'Seychellois Rupee', 'Seychelles'],
    ['SDG', 'Sudanese Pound', 'Sudan'],
    ['SEK', 'Swedish Krona', 'Sweden'],
    ['SGD', 'Singapore Dollar', 'Singapore'],
    ['SHP', 'Saint Helena Pound', 'Saint Helena'],
    ['SLE', 'Sierra Leonean Leone', 'Sierra Leone'],
    ['SOS', 'Somali Shilling', 'Somalia'],
    ['SRD', 'Surinamese Dollar', 'Suriname'],
    ['SSP', 'South Sudanese Pound', 'South Sudan'],
    ['STN', 'São Tomé and Príncipe Dobra', 'São Tomé and Príncipe'],
    ['SYP', 'Syrian Pound', 'Syria'],
    ['SZL', 'Eswatini Lilangeni', 'Eswatini'],
    ['THB', 'Thai Baht', 'Thailand'],
    ['TJS', 'Tajikistani Somoni', 'Tajikistan'],
    ['TMT', 'Turkmenistan Manat', 'Turkmenistan'],
    ['TND', 'Tunisian Dinar', 'Tunisia'],
    ['TOP', 'Tongan Paanga', 'Tonga'],
    ['TRY', 'Turkish Lira', 'Turkey'],
    ['TTD', 'Trinidad and Tobago Dollar', 'Trinidad and Tobago'],
    ['TVD', 'Tuvaluan Dollar', 'Tuvalu'],
    ['TWD', 'New Taiwan Dollar', 'Taiwan'],
    ['TZS', 'Tanzanian Shilling', 'Tanzania'],
    ['UAH', 'Ukrainian Hryvnia', 'Ukraine'],
    ['UGX', 'Ugandan Shilling', 'Uganda'],
    ['USD', 'United States Dollar', 'United States'],
    ['UYU', 'Uruguayan Peso', 'Uruguay'],
    ['UZS', 'Uzbekistani Som', 'Uzbekistan'],
    ['VES', 'Venezuelan Bolívar Soberano', 'Venezuela'],
    ['VND', 'Vietnamese Đồng', 'Vietnam'],
    ['VUV', 'Vanuatu Vatu', 'Vanuatu'],
    ['WST', 'Samoan Tālā', 'Samoa'],
    ['XAF', 'Central African CFA Franc', 'CEMAC'],
    ['XCD', 'East Caribbean Dollar', 'Organisation of Eastern Caribbean States'],
    ['XDR', 'Special Drawing Rights', 'International Monetary Fund'],
    ['XOF', 'West African CFA franc', 'CFA'],
    ['XPF', 'CFP Franc', 'Collectivités dOutre-Mer'],
    ['YER', 'Yemeni Rial', 'Yemen'],
    ['ZAR', 'South African Rand', 'South Africa'],
    ['ZMW', 'Zambian Kwacha', 'Zambia'],
    ['ZWL', 'Zimbabwean Dollar', 'Zimbabwe']
]
all_currencies = []
for currency in currencies_list:
    currency_insert = currency_codes(currency_three_letters=currency[0], currency_name=currency[1], country=currency[2])
    all_currencies.append(currency_insert)

db.session.add_all(all_currencies)
db.session.commit()

# Adding dummy data to user_details

user1 = user_details(user_id=1, first_name="Maria", last_name="Sanchez", email="sat@gmail.com", address_line_1="77b Mill Road", postcode="RH158DY", username='MariaS', pass_word='Iamsotired')
user2 = user_details(user_id=2, first_name="Alba", last_name="Simmonds", email="sar@gmail.com", address_line_1="77c Mill Road", postcode="RH158DY", username='AlbaS', pass_word='butwewillmakeit')
user3 = user_details(user_id=3, first_name="Rory", last_name="Mack", email="sas@gmail.com", address_line_1="77d Mill Road", postcode="RH158DY", username='RoryM', pass_word='codingishard!')
users = [user1, user2, user3]

db.session.add_all(users)
db.session.commit()


# Adding dummy data to bank_details

account1 = bank_details(account_number=11111111,user_id=1, sort_code=111111, main_account_balance=100.00)
account2 = bank_details(account_number=22222222,user_id=2, sort_code=222222, main_account_balance=200.00)
account3 = bank_details(account_number=33333333,user_id=3,sort_code=333333, main_account_balance=300.00)
accounts= [account1, account2, account3]

db.session.add_all(accounts)
db.session.commit()

# Adding dummy data to foreign_account

faccount1 = foreign_account(foreign_account_number=55555555,account_number=11111111,foreign_account_balance=10.00,foreign_currency='EUR')
faccount2 = foreign_account(foreign_account_number=66666666,account_number=22222222,foreign_account_balance=20.00,foreign_currency='EUR')
faccount3 = foreign_account(foreign_account_number=77777777,account_number=33333333,foreign_account_balance=30.00,foreign_currency='USD')
faccounts = [faccount1, faccount2, faccount3]

db.session.add_all(faccounts)
db.session.commit()

# Adding dummy data to transactions

tran1 = transactions_record(transaction_ID=1,foreign_account_number=55555555,account_number=11111111,foreign_currency='EUR',gbp_amount=10.00, foreign_currency_amount=8.00, exchange_rate=0.08)
tran2 = transactions_record(transaction_ID=2,foreign_account_number=66666666,account_number=22222222,foreign_currency='EUR', gbp_amount=10.00,foreign_currency_amount=8.00, exchange_rate=0.10)
tran3 = transactions_record(transaction_ID=3,foreign_account_number=77777777,account_number=33333333,foreign_currency='USD', gbp_amount=10.00,foreign_currency_amount=15.00, exchange_rate=0.25)


all_transactions = [tran1, tran2, tran3]
db.session.add_all(all_transactions)
db.session.commit()

