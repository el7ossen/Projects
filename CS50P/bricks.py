n = int(input("What's n? "))

def main():
    print_square(n)

def print_square(size):
    for i in range(size):
        print("#" * int(size))

main()