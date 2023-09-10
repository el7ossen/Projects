import cryptography
from cryptography.fernet import Fernet

file = open("key.key", "w")
key = str(Fernet.generate_key())
file.write(key)
print(key)