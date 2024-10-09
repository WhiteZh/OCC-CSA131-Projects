ls = []

while (x := int(input("> "))) != 0:
    ls.append(x)

print(ls)
print("sum:", sum(ls))
print("minimum:", min(ls))
print("maximum:", max(ls))
ls.pop()
print("modified:", ls)
