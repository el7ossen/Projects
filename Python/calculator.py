import math, fractions
from decimal import Decimal

while True:
    print(
        "\nChoose an operation:\n\n",
        "Quit\n",
        "1 Addition\n",
        "2 Subtraction\n",
        "3 Multiplication\n",
        "4 Division\n",
    )

    op = str(input("Option: "))

    if op == "q" or op == "quit":
        break

    elif op == "1":
        print("Number A is? ")
        A = Decimal(input())
        print("Number B is? ")
        B = Decimal(input())
        Add = A + B
        print("Your answer is ", Add)

    elif op == "2":
        print("Number A is? ")
        A = Decimal(input())
        print("Number B is? ")
        B = Decimal(input())
        Sub = A - B
        print("Your answer is ", Sub)
    
    elif op == "3":
        print("Number A is? ")
        A = Decimal(input())
        print("Number B is? ")
        B = Decimal(input())
        Mult = A * B
        print("Your answer is ", Mult)

    elif op == "4":
        print("Number A is? ")
        A = Decimal(input())


    ret = str(input("Would you like to retry? y/n "))
    if ret == "y":
        continue
    else:
        break
