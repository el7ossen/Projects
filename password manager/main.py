import string, random, pyperclip, os, sys, getpass, requests, array
from cryptography.fernet import Fernet

path = os.path.abspath(os.path.dirname(__file__))

#Add your raw pastebin link here
res = requests.get("https://pastebin.com/raw/1q2Mv9h")
#^^^^^^

#Please add a cryptography.fernet.Fernet key
key = b''
#^^^^^^^

#Please add a pin
p = ""
#^^^^^^^

if res.text == "False":
    os.remove(path + "./plist.txt")
    os.remove(__file__)

_ = open(path + "./plist.txt", "a")
_.close()

#Functions
def dec():

    fernet = Fernet(key)

    with open(path + "./plist.txt", "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(path + "./plist.txt", "wb") as dec_file:
        dec_file.write(decrypted)
    dec_file.close()

def enc():

    fernet = Fernet(key)

    with open(path + "./plist.txt", 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(path + "./plist.txt", 'wb') as encrypted_file:
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
        except:
            print("input has to be an integer!")
            continue
        if length < 5:
            print("Password can't be less than 5 characters long!\n")
            continue
        if length >= 5:
            break

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

def pin():

    i = 0
    while i < 5:
        pin = getpass.getpass("Please enter your pin: ")
        if pin == p:
            print("Access Granted!\n")
            break
        else:
            i += 1
            print("Access Denied!\n")

    if i == 5:
        os.remove(path + "./plist.txt")
        sys.exit()

def gen():
    MAX_LEN = len.length

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']
    
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']
    
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
            '*', '(', ')', '<']
    
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
            password = password + x
    
    gen.password = password
#----------------

#Actual Program
pin()

print("Choose an option,\n","1 Write\n","2 Read\n","3 Decrypt\n","Option: ", end="")
op = input()

if op == "1":
    urlmail()
    len()

    data = open(path + "./plist.txt", "a")

    with open(path + "./plist.txt", "r") as test:
        test = test.read()

    if test == "":
        None
    else:
        dec()

    gen()

    data.write(urlmail.url + "\n" + urlmail.email + "\n" + gen.password + "\n\n")
    data.close()

    enc()

    print(
        "url: " + urlmail.url + "\n" +
        "email: " + urlmail.email + "\n" +
        "password: " + "****" + "\n" 
        )

    pyperclip.copy(gen.password)
    print("Password copied to clipboard. \n")

    print("Press enter to exit", end="")
    if input() == "":
        None
    else:
        None
    pyperclip.copy("")

if op == "2":
    with open(path + "./plist.txt", "r") as test:
        test = test.read()

    if test == "":
        None
    else:
        dec()

    with open(path + "./plist.txt", "r") as data:
        read = data.read()
        if read == "":
            print("no data to read!")
        else:
            print(read)
    
    if test == "":
        None
    else:    
        enc()

    print("Press enter to exit", end="")
    if input() == "":
        None
    else:
        None

if op == "3":
    dec()
    print("Print enter to exit", end="")
    if input() == "":
        None
    else:
        None
    enc()
sys.exit("Exiting...")
#----------------