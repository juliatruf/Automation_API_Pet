import time

new_user_credentials = {
    "email": f'test{int(time.time())}@mail.com',
    "password": '1234',
    "confirm_password": '1234'
}

valid_users = [
    {"email": 'test2j@mail.com', "password": '12345'},
    {"email": 'a@b.com', "password": '12345678'},
    {"email": 'user+alias@subdomain.example.com', "password": '12345aA!'}
]

comment_message = [
    "What do you feed your pet?",
    "?"
]

pet_payload = {
    "name": "Kleo",
    "type": "dog"
}