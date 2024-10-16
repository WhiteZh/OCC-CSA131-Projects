medal_table = [
        ["USA", 3, 2, 1],
        ["China", 2, 1, 0],
        ["Japan", 1, 0, 1],
]


def total_medals(table, index):
    return sum(table[index][1:])


print(f"Total medals for USA:", total_medals(medal_table, 0))
print(f"Total medals for China:", total_medals(medal_table, 1))
