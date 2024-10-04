def factorial(n):
    if n < 0:
        raise ValueError("`n` should be greater than or equal to 0")
    if n <= 1:
        return 1
    return n * factorial(n-1)

def main():
    n = int(input("Enter a number: "))
    print(f"The factorial of {n} is {factorial(n)}")


if __name__ == '__main__':
    main()
