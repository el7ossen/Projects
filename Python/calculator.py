from decimal import Decimal as D

while True:
    print(
        "\nChoose an operation:\n\n",
        "1 Quit\n",
        "2 Addition\n",
        "3 Subtraction\n",
        "4 Multiplication\n",
        "5 Division\n",
    )

    try:
        op = int(input("Option: "))
        if op < 0:
            print("Please input an option!")
            continue
    except ValueError:
        print("Please input an option!")
        continue

    if op == 1:
        break

    A = D(input("Number A is? "))
    B = D(input("Number B is? "))

    if op == 2:
        print("Your answer is: ", A + B)
    elif op == 3:
        print("Your answer is: ", A - B)
    elif op == 4:
        print("Your answer is: ", A * B)
    elif op == 5:
        print("Your answer is: ", A / B)

    ret = str(input("Would you like to retry? y/n "))
    if ret == "y":
        continue
    else:
        break