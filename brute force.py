items = [
    ("Laptop", 5, 60),
    ("Books", 4, 40),
    ("Camera", 6, 70),
    ("Shoes", 3, 30),
    ("Headphones", 2, 25)
]
capacity = 15

def brute_force(items, capacity):
    n = len(items)
    max_value = 0
    best_items = []

    for mask in range(2 ** n):
        weight = 0
        value = 0
        selected = []

        for j in range(n):
            if mask & (1 << j):
                weight += items[j][1]
                value += items[j][2]
                selected.append(items[j][0])

        if weight <= capacity and value > max_value:
            max_value = value
            best_items = selected

    return max_value, best_items


value, selected = brute_force(items, capacity)
print("Maximum Value:", value)
print("Selected Parcels:", selected)
