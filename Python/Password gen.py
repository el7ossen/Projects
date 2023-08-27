import string, random, pyperclip, sys

data = open("Python/txt/plist", "a")
char = (string.ascii_letters + string.digits + "!@#$-_")

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

while True:
    length = input("Length of you password: ")
    if length == "":
        length = 12
        break
    try:
        length = int(length)
        break
    except:
        print("exc")

passw = random.choices(char, k=length)

password = "".join(passw)

data.write(url + "\n" + email + "\n" + password + "\n\n")
data.close()

print(
    "url: " + url + "\n" +
    "email: " + email + "\n" +
    "password: " + password + "\n" 
      )

pyperclip.copy(password)
print("Copied to clipboard.")