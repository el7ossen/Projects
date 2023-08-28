from cryptography.fernet import Fernet

def enc():


    fernet = Fernet("98ynLvTdueiIo9oERYwLDrJc4HqzZwTh7ES1QO75iHg=")

    with open('plist.txt', 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open('plist.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    encrypted_file.close()

enc()