import os

dir = str(input("please input the path of the folder you'd like to delete: "))

if os.path.exists(dir):
    os.remove(dir)
    print("File deleted successfully.")
else:
    print("File does not exist!")