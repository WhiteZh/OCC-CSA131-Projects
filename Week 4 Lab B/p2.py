from math import log10

n = int(input("> "))
while n <= 0:
    print("Positive integer please")
    n = int(input("> "))

print(f"Multiplication table for {n}:")
print()

width = int(log10(n * n)) + 1

print(" " * int(log10(n)+1), end=' ')
print(" ".join([f"{i:>{width}}" for i in range(1, n+1)]))

for i in range(1, n+1):
    print(f"{i:>{int(log10(n)+1)}}", end=' ')
    print(" ".join([f"{j * i:>{width}}" for j in range(1, n+1)]))

