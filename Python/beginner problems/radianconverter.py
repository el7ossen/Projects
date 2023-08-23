import math, decimal 

rad = int(input("rad = "))

deg = decimal.Decimal(rad * 180 / math.pi)

print("degrees = ", "{:.2f}".format(deg))