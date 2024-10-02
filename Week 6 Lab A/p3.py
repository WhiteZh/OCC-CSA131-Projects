def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return (length + width) * 2

def main():
    l = float(input("Enter the length of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    print()
    print(f"The area of the rectangle is: {calculate_area(l, w)}")
    print(f"The perimeter of the rectangle is: {calculate_perimeter(l, w)}")


if __name__ == '__main__':
    main()
