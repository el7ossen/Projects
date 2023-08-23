lst = []

n = int(input("list limit is: "))

for _ in range(n):
    num = int(input())
    lst.append(num)

sort = str(input("asc, desc, none: "))

if sort == "asc":
    lst.sort(reverse=False)
    print(lst)

elif sort == "desc":
    lst.sort(reverse=True)
    print(lst)

else:
    print(lst)
