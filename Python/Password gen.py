import string, random

while True:
    try:
        len = int(input("Choose the length of your password: "))
        break

    except ValueError:
        print("Please input a number! \n")
        continue

char = string.ascii_letters + string.digits + "!@#$-_"

password = random.sample(char, len)

print("".join(password))