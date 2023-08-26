#!python

import string, random, pyperclip, sys

data = open("./txt/plist", "a")
char = (string.ascii_letters + string.digits + "!@#$-_")
while True:
    try:
        length = int(sys.argv[1])
    except ValueError:
        print("Please input a positive integer! \n")
        continue
    if length > 0: break
    else:
        print("Please input a postitive integer!\n") 
        continue
passw = random.choices(char, k=length)

password = "".join(passw)

data.write(password + "\n")

print(password)

pyperclip.copy(password)
print("Copied to clipboard.")