

q = int(input("what number would you like to convert? "))

lst = []
while q > 0:
    m = q%2
    lst.append(m) 
    q = q//2

lst.reverse()
print(*lst, sep="")