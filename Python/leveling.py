import sys, random

try:
    data = open("level.txt", "r").readlines()
except:
    data = open("level.txt", "x")
    data = open("level.txt", "w")
    data.write("0\n0\n0")
    data.close()
    data = open("level.txt", "r").readlines()

try:
    lvl = max(1, int(data[0]))
except:
    lvl = 1

try:
    currentXp = max(0, int(data[1]))
except:
    currentXp = 0

try:
    lvlNext = max(25, int(data[2]))
except:
    lvlNext = int(25 * 1.5 ** (lvl - 1))

while True:
    print("Enter XP gained (quit to quit):", end=" ")
    xpGained = input()
    if xpGained == "quit":
        break
    elif xpGained == "done" or xpGained == "d":
        xpGained = random.randint(15, 40)
    elif not xpGained.isnumeric() or int(xpGained) <= 0:
        print("XP must be a positive integer.")
        continue
    currentXp += int(xpGained)
    while int(currentXp) >= lvlNext:
        lvl += 1
        currentXp -= int(lvlNext)
        lvlNext = int(25 * 1.5 ** (lvl - 1))
    print("Level:", lvl)
    print("Exp:", currentXp)
    print("Next:", lvlNext)
    data = open("level.txt", "w")
    data.write(str(lvl) + "\n" + str(currentXp) + "\n" + str(lvlNext))
    data.close()
