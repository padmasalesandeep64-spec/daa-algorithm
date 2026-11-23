items = [
    ("Laptop", 5, 60),
    ("Books", 4, 40),
    ("Camera", 6, 70),
    ("Shoes", 3, 30),
    ("Headphones", 2, 25)
]
capacity = 15

def dynamic_programming(items, capacity):
    n = len(items)
    table = [[0 for _ in range(capacity + 1)]
             for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, weight, value = items[i - 1]

        for current_capacity in range(capacity + 1):
            table[i][current_capacity] = table[i - 1][current_capacity]

            if weight <= current_capacity:
                take = value + table[i - 1][current_capacity - weight]
                table[i][current_capacity] = max(
                    table[i][current_capacity], take
                )

    selected = []
    current_capacity = capacity

    for i in range(n, 0, -1):
        if table[i][current_capacity] != table[i - 1][current_capacity]:
            selected.append(items[i - 1][0])
            current_capacity -= items[i - 1][1]

    selected.reverse()
    return table[n][capacity], selected


value, selected = dynamic_programming(items, capacity)
print("Maximum Value:", value)
print("Selected Parcels:", selected)
