import decimal, math

print("Choose from these options")
print("1 P(A∩B) independent")
print("2 P(A∩B) dependent")
print("3 P(A|B)")
print("4 P(A∪B) non-mutually exclusive")
print("5 P(A∪B) mutually exclusive")
print("6 P(A')")
print("7 nPr")
print("8 nCr")

choice = str(input("Option: "))

if choice == "1":
    print("P(A)= ")
    PA = decimal.Decimal(input())
    print("P(B)= ")
    PB = decimal.Decimal(input())
    totalAB = decimal.Decimal(PA) * decimal.Decimal(PB)
    AnB = decimal.Decimal(totalAB)
    print("your probability is", "%.2f" % (AnB * 100), "%")

elif choice == "2":
    print("P(A)= ")
    PA = decimal.Decimal(input())
    print("P(B)= ")
    PB = decimal.Decimal(input())
    totalAB = (
        decimal.Decimal(PA)
        * decimal.Decimal(PA)
        * decimal.Decimal(PB)
        / decimal.Decimal(PB)
    )
    AnB = decimal.Decimal(totalAB)
    print("your probability is", "%.2f" % (AnB * 100), "%")

elif choice == "3":
    print("P(A)= ")
    PA = decimal.Decimal(input())
    print("P(B)= ")
    PB = decimal.Decimal(input())
    totalAB = decimal.Decimal(PA) * decimal.Decimal(PB) / decimal.Decimal(PB)
    A_B = decimal.Decimal(totalAB)
    print("your probability is", "%.2f" % (A_B * 100), "%")

elif choice == "4":
    print("P(A)= ")
    PA = decimal.Decimal(input())
    print("P(B)= ")
    PB = decimal.Decimal(input())
    totalAB = (
        decimal.Decimal(PA)
        + decimal.Decimal(PB)
        - (decimal.Decimal(PA) * decimal.Decimal(PB))
    )
    AuB = decimal.Decimal(totalAB)
    print("your probability is", "%.2f" % (AuB * 100), "%")

elif choice == "5":
    print("P(A)= ")
    PA = decimal.Decimal(input())
    print("P(B)= ")
    PB = decimal.Decimal(input())
    totalAB = decimal.Decimal(PA) + decimal.Decimal(PB)
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

else:
    print("wrong input")
