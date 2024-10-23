balance: int = 200

try:
    withdraw = int(input("Withdraw Amount: $"))
    balance -= withdraw
    
    if balance < 0:
        raise ValueError("You don't have enough money!")
except ValueError as e:
    print(f"Error: {e}")
else:
    print("Withdraw successful!")
    print(f"Your current balance is ${balance}.")
