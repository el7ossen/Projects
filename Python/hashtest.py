import string, bcrypt

pwd = b"Testp@ssword321"

salt = b'$2b$12$8FEPKAv0B9kToM0dlcghiO'

hashed = b'$2b$12$8FEPKAv0B9kToM0dlcghiOdKbzvjWaNjApxcIeXr.1q5CDDloB7qW'

chars = str(string.ascii_letters + string.digits + string.punctuation)

for char in chars:

    print(char)

    print(bcrypt.hashpw(password=char, salt=salt))

    # if hash(char) == hash_pwd:
    #     print(char)`