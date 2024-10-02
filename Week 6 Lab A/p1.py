from math import pi

def calculate_area(radius):
    return radius ** 2 * pi

def calculate_circumference(radius):
    return radius * 2 * pi

def main():
    r = float(input("Enter the radius of the circle: "))
    print()

    print(f"The area of the circle is: {calculate_area(r):.2f}")
    print(f"The circumference of the circle is: {calculate_circumference(r):.2f}")


if __name__ == '__main__':
    main()
