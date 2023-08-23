string = str(input("whats the sentence? "))

x = string.count("x")
o = string.count("o")

if x == o:
    print("True")
else:
    print("False")