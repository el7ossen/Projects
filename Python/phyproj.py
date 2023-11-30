import math, decimal, sys
from decimal import Decimal as dec

K = dec(9000000000)

print("Please choose an option:\n"
        "1. F = K*qᴀ*qʙ/r²\n"
        "2. E = F/q\n"
        "3. ΔV = W/q\n"
        "4. ΔV = Ed\n"
        "5. C = q/ΔV"
)

op = input()

while True:
    if op == "1":
        print("if not available press Enter\n")
        while True:
            F = input("F=")
            if F=="": break
            try:
                F = dec(F)
                break
            except:
                print("Please input a number!")
                continue
        while True:
            qA = input("qᴀ=")
            if qA=="": break
            try:
                qA = dec(qA)
                break
            except:
                print("Please input a number!")
                continue
        while True:
            qB = input("qʙ=")
            if qB == "": break
            try:
                qB = dec(qB)
                break
            except:
                print("Please input a number!")
                continue
        while True:
            r = input("r=")
            if r == "": break
            try:
                r = dec(r)
                break
            except:
                print("Please input a number!")
                continue
        if F == "":
            F = (K*qA*qB)/(r*r)
            print(F, "N")
        elif qA == "":
            qA = (F*r*r)/(K*qB)
            print(qA, "C")
        elif qB == "":
            qB = (F*r*r)/(K*qA)
            print(qB, "C")
        elif r == "":
            r = math.sqrt((qA*qB)/(F*K))
            print(r, "m")
    