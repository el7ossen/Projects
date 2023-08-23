num = str(input("Your credit card number please:) : "))

repnum = "************"

num = num.replace(num[0 : 12], repnum, 1)
                  
print(num)