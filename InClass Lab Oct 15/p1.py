prime_numbers = (2, 3, 5, 7, 11)

print("Second prime number is:", prime_numbers[1])

try:
    prime_numbers[0] = 1  # This will fail because the elements inside a tuple are immutable. Tuple must be changed as a whole.
except:
    print("Error: 'tuple' object does not support item assignment (explained in comment)")


def get_student_details():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    student_id = int(input("Student ID: "))
    
    return (first_name, last_name, student_id)


print(f"Student Details: {get_student_details()}")
