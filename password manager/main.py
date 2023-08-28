import string, random, pyperclip, sys
from cryptography.fernet import Fernet

_ = open("./plist.txt", "a")
_.close()

def dec():

    fernet = Fernet("98ynLvTdueiIo9oERYwLDrJc4HqzZwTh7ES1QO75iHg=")

    with open("./plist.txt", "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open("./plist.txt", "wb") as dec_file:
        dec_file.write(decrypted)
    dec_file.close()

def enc():

    fernet = Fernet("98ynLvTdueiIo9oERYwLDrJc4HqzZwTh7ES1QO75iHg=")

    with open('./plist.txt', 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open('./plist.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    encrypted_file.close()

def len():
    while True:
        length = input("Length of you password: ")
        if length == "":
            length = 20
            break
        try:
            length = int(length)
            break
        except:
            print("exc")

    len.length = length

def urlmail():
    while True:
        url = str(input("What site is this password for? "))
        if url == "":
            print("Please input a url\n")
            continue
        else:
            break

    while True:
        email = str(input("What E-mail are you using? "))
        if email == "":
            print("Please input an email\n")
            continue
        else:
            break

    urlmail.url = url
    urlmail.email = email

data = open("./plist.txt", "a")
char = (string.ascii_letters + string.digits + "!@#$-_")

with open("./plist.txt", "r") as test:
    test = test.read()

if test == "":
    None
else:
    dec()

urlmail()
len()

password = "".join(random.choices(char, k=len.length))

data.write(urlmail.url + "\n" + urlmail.email + "\n" + password + "\n\n")
data.close()

print(
    "url: " + urlmail.url + "\n" +
    "email: " + urlmail.email + "\n" +
    "password: " + "****" + "\n" 
      )

pyperclip.copy(password)
print("Password copied to clipboard.")

enc()