def square_number(num: int) -> int:
    return num ** 2

def main():
    n = int(input("Enter a number to square: "))
    print(f"The square of {n} is {square_number(n)}")


if __name__ == '__main__':
    main()
