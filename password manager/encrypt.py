from cryptography.fernet import Fernet

def enc():

    with open('txt/filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open('txt/plist.txt', 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open('txt/plist.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    encrypted_file.close()

enc()