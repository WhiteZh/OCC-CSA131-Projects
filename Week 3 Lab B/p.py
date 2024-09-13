print("Please enter some text:")

text = input()
print()
text_caseless = text.lower()

if text_caseless.startswith("dear"):
    print("Formal letter.")

if text_caseless.endswith("?") and "help" in text_caseless:
    print("Request for help.")

print(f"The word 'python' appears {(pc := text_caseless.count('python'))} time(s).")

if (i := text_caseless.find("programming")) >= 0:
    print(f"The word 'programming' starts at index {i}.")
    
    if pc > 0:
        print("Python programming mentioned.")
else:
    print("No 'programming' found.")

if text_caseless.isalnum():
    print("Alphanumeric content found.")
