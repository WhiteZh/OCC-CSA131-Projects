def F(n):
    if n < 0:
        raise ValueError("`n` should be greater than or equal to 0")
    if n <= 1:
        return n
    return F(n-1) + F(n-2)

n = int(input("Please enter an integer as `n`: "))
print(f"The result is: {F(n)}")
