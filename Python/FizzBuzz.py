for x in range(1,101):

    output=""

    if x%3==0: 
        output = output + "Fizz"
    if x%5==0: 
        output = output + "Buzz"

    if output=="": print(x)

    else: print(output)
