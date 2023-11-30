import math, sys
from decimal import Decimal as dec

# functions ------------------
def one():
    n = 0
    while True:
        print("\nif not available press Enter\n")
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
            qA = input("qᴀ=")
            if qA == "":
                n += 1
                break
            try:
                qA = dec(qA)
                break
            except:
                print("Please input a number!")
                continue
        while True:
            qB = input("qʙ=")
            if qB == "":
                n += 1
                break
            try:
                qB = dec(qB)
                break
            except:
                print("Please input a number!")
                continue
        while True:
            r = input("r=")
            if r == "":
                n += 1
                break
            try:
                r = dec(r)
                break
            except:
                print("Please input a number!")
                continue
        if n > 1:
            print("Insuffecient Information!")
            break
        elif F == "":
            F = (9000000000 * qA * qB) / (r * r)
            print(F, "N")
        elif qA == "":
            qA = (F * r * r) / (9000000000 * qB)
            print(qA, "C")
        elif qB == "":
            qB = (F * r * r) / (9000000000 * qA)
            print(qB, "C")
        elif r == "":
            r = math.sqrt((qA * qB) / (F * 9000000000))
            print(r, "m")
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
            E = F/q
            print(E)
        elif F == "":
            F = E*q
            print(F)
        elif q == "":
            q = F/E
            print(q)
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
            V = W/q
            print(V)
        elif W == "":
            W = V*q
            print(W)
        elif q == "":
            q = W/V
            print(q)
        else:
            print("you've already solved it")
            break

print(
    "Please choose an option:\n"
    "1. F = K*qᴀ*qʙ/r²\n"
    "2. E = F/q\n"
    "3. ΔV = W/q\n"
    "4. ΔV = Ed\n"
    "5. C = q/ΔV"
)

op = input()