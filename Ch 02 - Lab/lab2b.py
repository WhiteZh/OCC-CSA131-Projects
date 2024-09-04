due = 411
received = 693

tmp = received - due

dollar = int(tmp / 100)
tmp = tmp - dollar * 100

quarter = int(tmp / 25)
tmp = tmp - quarter * 25

dime = int(tmp / 10)
tmp = tmp - dime * 10

nickel = int(tmp / 5)
tmp = tmp - nickel * 5

pennie = tmp

print("Due:", due, "Received:", received)
print()
print("The change is:")
print(dollar, "dollar(s)")
print(quarter, "quarter(s)")
print(dime, "dime(s)")
print(nickel, "nickel(s)")
print(pennie, "pennie(s)")
