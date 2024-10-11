ls = [x ** 2 for x in range(10)]

print(f"List of squares: {ls}")
print(f"Sum of elements: {sum(ls)}")
print(f"Maximum value: {max(ls)}")

sls = [x for x in ls if x > 50]
if len(sls) > 0:
    print(f"The first number greater than 50 is located at index {len(ls) - len(sls)}")
else:
    print("No number is greater than 50 in the list")
print(f"Numbers greater than 50: {sls}")
print(f"Count of numbers greater than 50: {len(sls)}")
