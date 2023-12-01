import math, sys, time
from decimal import Decimal as dec

K = dec(9e+9)

# functions ------------------

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
            r = math.sqrt((qA * qB * K) / (F))
            print("%.3E" % r, "m")
            break
        else:
            print("you've answered it already")
            break


def two():
    n = 0
    while True:
        print("\nif not available press Enter\n")

        while True:
            E = input("E=")
            if E == "":
                n += 1
                break
            try:
                E = dec(E)
                break
            except:
                print("Please input a number!")
                continue
        while True:
            F = input("F=")
            if F == "":
                n += 1
                break
            try:
                F = dec(F)
                break
            except:
                print("Please input a number!")
                continue
        while True:
            q = input("q=")
            if q == "":
                n += 1
                break
            try:
                q = dec(q)
                break
            except:
                print("Please input a number!")
                continue
        if n > 1:
            print("Insufficient Information!")
            break
        elif E == "":
            E = F / q
            print("%.3f" % E, "N/C")
            break
        elif F == "":
            F = E * q
            print("%.3f" % F, "N")
            break
        elif q == "":
            q = F / E
            print("%.3f" % q, "C")
            break
        else:
            print("you've already solved it")
            break


def three():
    n = 0
    while True:
        print("\nIf not available press enter\n")

        while True:
            V = input("V=")
            if V == "":
                n += 1
                break
            try:
                V = dec(V)
                break
            except:
                print("Please input a number!")
                continue
        while True:
            W = input("W=")
            if W == "":
                n += 1
                break
            try:
                W = dec(W)
                break
            except:
                print("Please input a number!")
                continue
        while True:
            q = input("q=")
            if q == "":
                n += 1
                break
            try:
                q = dec(q)
                break
            except:
                print("Please input a number!")
                continue
        if n > 1:
            print("Insufficient information!")
            break
        elif V == "":
            V = W / q
            print("%.3f" % V, "V")
            break
        elif W == "":
            W = V * q
            print("%.3f" % W, "J")
            break
        elif q == "":
            q = W / V
            print("%.3f" % q, "C")
            break
        else:
            print("you've already solved it")
            break


def four():
    n = 0
    while True:
        print("\nIf not available press Enter")

        while True:
            V = input("V=")
            if V == "":
                n += 1
                break
            try:
                V = dec(V)
                break
            except:
                print("Please input a number!")
                continue
        while True:
            E = input("E=")
            if E == "":
                n += 1
                break
            try:
                E = dec(E)
                break
            except:
                print("Please input a number!")
                continue
        while True:
            d = input("d=")
            if d == "":
                n += 1
                break
            try:
                d = dec(d)
                break
            except:
                print("Please input a number!")
                continue
        if n > 1:
            print("Insufficient information")
            break
        elif V == "":
            V = E * d
            print("%.3f" % V, "V")
            break
        elif E == "":
            E = V / d
            print("%.3f" % E, "N/C")
            break
        elif d == "":
            d = V / E
            print("%.3f" % d, "m")
            break
        else:
            print("you've already solved it")
            break


def five():
    n = 0
    while True:
        print("\nIf not available press Enter")

        while True:
            C = input("C=")
            if C == "":
                n += 1
                break
            try:
                C = dec(C)
                break
            except:
                print("Please input a number!")
                continue
        while True:
            q = input("q=")
            if q == "":
                n += 1
                break
            try:
                q = dec(q)
                break
            except:
                print("Please input a number!")
                continue
        while True:
            V = input("V=")
            if V == "":
                n += 1
                break
            try:
                V = dec(V)
                break
            except:
                print("Please input a number!")
                continue
        if n > 1:
            print("Insufficient information!")
            break
        elif C == "":
            C = q / V
            print("%.3f" % C, "F")
            break
        elif q == "":
            q = C * V
            print("%.3f" % q, "C")
            break
        elif V == "":
            V = q / C
            print("%.3f" % V, "V")
            break
        else:
            print("you've already solved it")
            break


while True:
    print(
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
        print("exiting...")
        time.sleep(0.125)
        sys.exit()
    else:
        print("\nThat is not an option!")
        continue
    con = str(input("Would you like to continue? y/n "))

    if con == "y" or con == "yes":
        continue
    elif con == "n" or con == "no":
        print("exiting...")
        time.sleep(0.125)
        sys.exit()
    else:
        sys.exit("too bad lol")