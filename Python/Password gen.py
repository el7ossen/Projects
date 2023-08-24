import string, random, pyperclip
char = ((string.ascii_letters + string.digits + "!@#$-_"))
while True:
    try:
        length = int(input("Choose the length of your password: "))
    except ValueError:
        print("Please input a positive number! \n")
        continue
    if length > 0: break
    else:
        print("Please input a postitive number!\n") 
        continue
passw = random.choices(char, k=length)

password = "".join(passw)

print(password)

pyperclip.copy(password)
print("Copied to clipboard.")