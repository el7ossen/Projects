from cryptography.fernet import Fernet
import pyperclip

key = str(Fernet.generate_key())
pyperclip.copy(key)