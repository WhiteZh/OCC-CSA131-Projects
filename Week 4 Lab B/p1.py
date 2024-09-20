sum = 0
n = int(input("> "))

for x in range(1, n+1):
    if x % 2 == 0:
        sum += x

print(sum)

