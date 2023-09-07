import cryptography
from cryptography.fernet import Fernet

file = open("file.txt", "a")

key = str(Fernet.generate_key())
file.(key)
print(key)