specials = ['.', ',', '?', '!']

with open("sample.txt", "r") as f:
    content = f.read()

print('\n'.join(filter(lambda x: x != "", map(lambda x: ''.join(filter(lambda x: x not in specials, x)), content.split()))))
