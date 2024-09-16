password = input("Your password: ")

crit_met = 0

if len(password) >= 8:
    crit_met += 1

if any(map(str.isupper, password)):
    crit_met += 1

if any(map(str.islower, password)):
    crit_met += 1

if any(map(str.isdigit, password)):
    crit_met += 1

if not password.isalnum():
    crit_met += 1


if crit_met <= 2:
    strength = "Weak"
elif crit_met >= 4:
    strength = "Strong"
else:
    strength = "Moderate"

print("Your password's strength is", strength)
