import os

i = 0
while i < 5:
    pin = input("Please neter your pin: ")
    if pin == "0000":
        print("yes")
        break
    else:
        i += 1
        print("no")

if i == 5:
    os.remove(__file__)