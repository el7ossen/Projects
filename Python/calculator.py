import math, decimal, fractions

while True:
    print(
        "\nChoose an operation:\n\n",
        "Quit\n",
        "1 Addition\n",
    )

    op = str(input("Option: "))

    if op == "q" or op == "quit":
        break

    elif op == "1":
        print("Number A is? ")
        A = decimal.Decimal(input())
        print("Number B is? ")
        B = decimal.Decimal(input())
        Add = A + B
        print("Your answer is ", Add)
    
    ret = str(input("Would you like to retry? y/n "))
    if ret == "y":
        continue
    else:
        break