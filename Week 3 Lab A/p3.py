age = int(input("age: "))

if age < 0:
    print("Invalid input!")
else:
    t = "infant"
    if age >= 65:
        t = "senior"
    elif age >= 20:
        t = "adult"
    elif age >= 13:
        t = "teenager"
    elif age >= 2:
        t = "child"
    print("=>", t)
