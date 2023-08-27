from cryptography.fernet import Fernet

def dec():
    with open("filekey.key", "rb") as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open("plist.txt", "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open("plist.txt", "wb") as dec_file:
        dec_file.write(decrypted)
    dec_file.close()

dec()