from cryptography.fernet import Fernet

def dec():


    fernet = Fernet("98ynLvTdueiIo9oERYwLDrJc4HqzZwTh7ES1QO75iHg=")

    with open("plist.txt", "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open("plist.txt", "wb") as dec_file:
        dec_file.write(decrypted)
    dec_file.close()

dec()