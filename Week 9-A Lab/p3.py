try:
    a = float(input("First Number: "))
    b = float(input("Second Number: "))

    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
except ValueError:
    print("Error: Inputs must be numbers!")
except ZeroDivisionError:
    print("Error: Divisor cannot be 0!")
finally:
    print("All operations complete.")
