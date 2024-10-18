with open("numbers.txt", "w") as f:
    f.write(''.join(map(lambda x: str(x) + '\n', range(1, 51))))

with open("numbers.txt", "r") as f:
    lines = f.readlines()
    print("The numbers:", ', '.join(map(str.rstrip, lines)))

with open("numbers.txt", "r") as f:
    lines = f.readlines()
    print("The sum:", sum(map(lambda x: int(x.rstrip()), lines)))
    
