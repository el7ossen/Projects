import os, shutil, time

dest = "X:/plist.txt"

def ex():
    path = "O:\plist.txt"

    exists = os.path.exists(path)
    ex.exists = exists
    ex.path = path

while True:
    ex()
    if ex.exists == False:
        print("False")
        continue
    if ex.exists == True:
        shutil.copyfile(ex.path, dest)
        print("True")
        time.sleep(10)