n = int(input())
steps = 0

print(n)
while n > 1:
    if n % 2 == 0:
        n = n // 2
        print(n)
    else:
        n = 3 * n + 1
        print(n)
    steps += 1

print(str(steps) + " Steps")
