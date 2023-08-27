def gen():
    while True:
        length = input("Length of you password: ")
        if length == "":
            length = 12
            break
        try:
            length = int(length)
            break
        except:
            print("exc")

    gen.length = length

gen()