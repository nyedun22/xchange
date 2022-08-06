from db_setup import user_details,Session,engine

users=[
    {
       "user_ID":2,
       "first_name": "Maria",
       "last_name": "Diaz",
       "username": "MariaD",
       "email": "MariaD@gmail.com",
       "pass_word": "qwerty",
       "address_line_1": "70 London Road",
       "postcode": "BN69JS"
    },
    {
       "user_ID":3,
       "first_name": "Mario",
       "last_name": "Lundberg",
       "username": "MarioL",
       "email": "MarioL@gmail.com",
       "pass_word": "zxcvb",
       "address_line_1": "77 London Road",
       "postcode": "BN66JS"
    }
]
local_session=Session(bind=engine)

# new_user=user_details(user_ID=1,first_name="Aurora",last_name="Sanchez", username="AuroraS", email="aurora@gmail.com", pass_word="abcdefg", address_line_1="77 Mill Road", postcode="RH158DY")

# local_session.add(new_user)

# local_session.commit()

for u in users:
    new_user=user_details(user_ID=u["user_ID"],first_name=u["first_name"],last_name=u["last_name"],username=u["username"],email=u["email"], pass_word=u["pass_word"], address_line_1=u["address_line_1"], postcode=u["postcode"])
    print(new_user)

    local_session.add(new_user)

    local_session.commit()

    print(f"Added {u['username']}")