import decimal, math, sys

def pAB():
    print("P(A)= ")
    pAB.PA = decimal.Decimal(input())
    print("P(B)= ")
    pAB.PB = decimal.Decimal(input())
    

while True:
    print(
        "\nPlease choose from these options:",
        "\n1 P(A∩B) independent",
        "\n2 P(A∩B) dependent",
        "\n3 P(A|B)",
        "\n4 P(A∪B) non-mutually exclusive",
        "\n5 P(A∪B) mutually exclusive",
        "\n6 P(A')",
        "\n7 nPr",
        "\n8 nCr",
        "\nexit"
          )

    choice = str(input("Option: "))

    if choice == "1":
        pAB()
        totalAB = decimal.Decimal(pAB.PA) * decimal.Decimal(pAB.PB)
        AnB = decimal.Decimal(totalAB)
        print("your probability is", "%.2f" % (AnB * 100), "%")

    elif choice == "2":
        pAB()
        totalAB = (
            decimal.Decimal(pAB.PA)
            * decimal.Decimal(pAB.PA)
            * decimal.Decimal(pAB.PB)
            / decimal.Decimal(pAB.PB)
        )
        AnB = decimal.Decimal(totalAB)
        print("your probability is", "%.2f" % (AnB * 100), "%")

    elif choice == "3":
        pAB()
        totalAB = decimal.Decimal(pAB.PA) * decimal.Decimal(pAB.PB) / decimal.Decimal(pAB.PB)
        A_B = decimal.Decimal(totalAB)
        print("your probability is", "%.2f" % (A_B * 100), "%")

    elif choice == "4":
        pAB()
        totalAB = (
            decimal.Decimal(pAB.PA)
            + decimal.Decimal(pAB.PB)
            - (decimal.Decimal(pAB.PA) * decimal.Decimal(pAB.PB))
        )
        AuB = decimal.Decimal(totalAB)
        print("your probability is", "%.2f" % (AuB * 100), "%")

    elif choice == "5":
        pAB()
        totalAB = decimal.Decimal(pAB.PA) + decimal.Decimal(pAB.PB)
        AuB = decimal.Decimal(totalAB)
        print("your probability is", "%.2f" % (AuB * 100), "%")

    elif choice == "6":
        print("P(A)= ")
        PA = decimal.Decimal(input())
        PA_ = decimal.Decimal(1) - decimal.Decimal(PA)
        print("your probability is", "%.2f" % (PA_ * 100), "%")

    elif choice == "7":
        print("n= ")
        n = int(input())
        print("r= ")
        r = int(input())
        print("n(A)= ")
        nA = int(input())
        nPr = math.factorial(n) / math.factorial((n - r))
        nAnS = decimal.Decimal(nA) / decimal.Decimal(nPr)
        print("your probability is", "%.2f" % (nAnS * 100), "%")

    elif choice == "8":
        print("n= ")
        n = int(input())
        print("r= ")
        r = int(input())
        print("n(A)= ")
        nA = int(input())
        nCr = math.factorial(n) / (math.factorial((n - r)) * math.factorial(r))
        nAnS = decimal.Decimal(nA) / decimal.Decimal(nCr)
        print("your probability is", "%.2f" % (nAnS * 100), "%")

    elif choice == "exit" or choice == "e":
        sys.exit("Exiting")

    else:
        print("wrong input\n")
        continue

    con = str(input("Would you like to continue? y/n "))
    
    if con == "y" or con == "yes":
        continue
    elif con == "n" or con == "no":
        sys.exit("exiting")