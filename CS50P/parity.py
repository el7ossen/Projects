def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")


def is_even(n):
    return n % 2 == 0
main()