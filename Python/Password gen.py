import string, random
while True:
    try:
        length = int(input("Choose the length of your password: "))
        break
    except ValueError:
        print("Please input a number! \n")
        continue
char = ((string.ascii_letters + string.digits + "!@#$-_") * 10000)
password = random.sample(char, length)
print("".join(password))