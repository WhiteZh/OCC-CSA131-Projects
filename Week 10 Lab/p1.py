from random import randint
num_list = [randint(-15, 15) for _ in range(12)]
print(f"Before removing duplication: {num_list}")
num_list = list(set(num_list))
print(f"After removing duplication: {num_list}")
