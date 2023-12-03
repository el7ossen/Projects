from sys import exit
from decimal import Decimal as dec
from math import sqrt

K = dec(9e+9)

def var(x):
    while True:
        y = input(f"{x}=")
        if y == "":
            break
        try:
            y = dec(y)
            break
        except:
            print("Please input a number")
            continue
    var.y = y

def one():
    n = 0
    while True:
        print("\nif not available press Enter\n")
        var("F")
        F = var.y
        if var.y == "": n += 1

        var("qA")
        qA = var.y
        if var.y == "": n += 1
        
        var("qB")
        qB = var.y
        if var.y == "": n += 1
        
        var("r")
        r = var.y
        if var.y == "": n += 1
        
        if n > 1:
            print("Insuffecient Information!")
            break
        elif F == "":
            F = (K * qA * qB) / (r * r)
            print("%.3E" % F, "N")
            break
        elif qA == "":
            qA = (F * r * r) / (K * qB)
            print("%.3E" % qA, "C")
            break
        elif qB == "":
            qB = (F * r * r) / (K * qA)
            print("%.3E" % qB, "C")
            break
        elif r == "":
            r = sqrt((qA * qB * K) / (F))
            print("%.3E" % r, "m")
            break
        else:
            print("you've answered it already")
            break

def two():
    n = 0
    while True:
        print("\nif not available press Enter\n")

        var("E")
        E = var.y
        if var.y == "": n += 1

        var("F")
        F = var.y
        if var.y == "": n += 1
        
        var("q")
        q = var.y
        if var.y == "": n += 1
        
        if n > 1:
            print("Insufficient Information!")
            break
        elif E == "":
            E = F / q
            print("%.3E" % E, "N/C")
            break
        elif F == "":
            F = E * q
            print("%.3E" % F, "N")
            break
        elif q == "":
            q = F / E
            print("%.3E" % q, "C")
            break
        else:
            print("you've already solved it")
            break

def three():
    n = 0
    while True:
        print("\nIf not available press enter\n")

        var("V")
        V = var.y
        if var.y == "": n += 1

        var("W")
        W = var.y
        if var.y == "": n += 1

        var("q")
        q = var.y
        if var.y == "": n += 1

        if n > 1:
            print("Insufficient information!")
            break
        elif V == "":
            V = W / q
            print("%.3E" % V, "V")
            break
        elif W == "":
            W = V * q
            print("%.3E" % W, "J")
            break
        elif q == "":
            q = W / V
            print("%.3E" % q, "C")
            break
        else:
            print("you've already solved it")
            break

def four():
    n = 0
    while True:
        print("\nIf not available press Enter")

        var("V")
        V = var.y
        if var.y == "": n += 1

        var("E")
        E = var.y
        if var.y == "": n += 1

        var("d")
        d = var.y
        if var.y == "": n += 1

        if n > 1:
            print("Insufficient information")
            break
        elif V == "":
            V = E * d
            print("%.3E" % V, "V")
            break
        elif E == "":
            E = V / d
            print("%.3E" % E, "N/C")
            break
        elif d == "":
            d = V / E
            print("%.3E" % d, "m")
            break
        else:
            print("you've already solved it")
            break

def five():
    n = 0
    while True:
        print("\nIf not available press Enter")

        var("C")
        C = var.y
        if var.y == "": n += 1

        var("q")
        q = var.y
        if var.y == "": n += 1

        var("V")
        V = var.y
        if var.y == "": n += 1

        if n > 1:
            print("Insufficient information!")
            break
        elif C == "":
            C = q / V
            print("%.3E" % C, "F")
            break
        elif q == "":
            q = C * V
            print("%.3E" % q, "C")
            break
        elif V == "":
            V = q / C
            print("%.3E" % V, "V")
            break
        else:
            print("you've already solved it")
            break

while True:
    op = print(
        "\nPlease choose an option:\n"
        "1. F = K*qᴀ*qʙ/r²\n"
        "2. E = F/q\n"
        "3. ΔV = W/q\n"
        "4. ΔV = Ed\n"
        "5. C = q/ΔV\n"
        "6. exit\n"
        "Option:",
        end="",
    )

    op = input()

    if op == "1":
        one()
    elif op == "2":
        two()
    elif op == "3":
        three()
    elif op == "4":
        four()
    elif op == "5":
        five()
    elif op == "6":
        exit("exiting...")
    else:
        print("\nThat is not an option!")
        continue
    con = str(input("Would you like to continue? y/n "))

    if con == "y" or con == "yes":
        continue
    elif con == "n" or con == "no":
        exit("exiting...")
    else:
        exit("too bad lol")