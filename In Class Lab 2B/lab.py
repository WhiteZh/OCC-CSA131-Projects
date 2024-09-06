string = "Java1"

string_length = len(string)
string_replaced = string.replace('a', 'A')
string_capitalized = string.upper()
string_second_char = string[1]
string_last_char = string[-1]
string_middle_char = string[int(len(string) / 2)]

print("The string is", string)
print("*_*_*_*_*_*_*_*_*_*_*")
print("The length of the string is", string_length)
print("The replaced string is", string_replaced)
print("The capitalized string is", string_capitalized)
print("The second character is", string_second_char)
print("The last character is", string_last_char)
print("The middle character is", string_middle_char)
