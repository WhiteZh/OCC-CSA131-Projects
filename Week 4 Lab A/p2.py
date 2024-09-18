from math import inf

min = inf
while (x := float(input("> "))) >= 0:
    if x < min:
        min = x
print(min)