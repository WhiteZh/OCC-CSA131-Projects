sum = 0.0
n = 0
while (x := float(input("> "))) >= 0:
    sum += x
    n += 1
print(sum / n)