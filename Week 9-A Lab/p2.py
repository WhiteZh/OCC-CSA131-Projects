try:
    with open("data.txt", "r") as f:
        content = f.read()
        print(content, end=('' if content[-1] == '\n' else '\n'))
except FileNotFoundError:
    print("The file was not found.")
