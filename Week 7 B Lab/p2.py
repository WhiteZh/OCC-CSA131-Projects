def calculate_sum(ls: list[int]) -> int:
    sum = 0
    for each in ls:
        sum += each
    return sum


def double_elements(ls: list[int], factor: int) -> None:
    for i, v in enumerate(ls):
        ls[i] = v * factor


def create_square_list(n: int) -> list[int]:
    return [x ** 2 for x in range(n)]


ls = [5, 6, 7, 8, 9]
print(f"Original list: {ls}")
print(f"The sum of the elements is: {calculate_sum(ls)}")
double_elements(ls, 2)
print(f"Modified list after doubling: {ls}")
print(f"List of squares up to 5: {create_square_list(5)}")
