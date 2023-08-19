import string, random

len = int(input("Choose the lenght of your password: "))

char = string.ascii_letters + string.digits + "!@#$-_"

password = random.sample(char, len)

print("".join(password))