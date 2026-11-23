items = [
    ("Laptop", 5, 60),
    ("Books", 4, 40),
    ("Camera", 6, 70),
    ("Shoes", 3, 30),
    ("Headphones", 2, 25)
]
capacity = 15

def greedy(items, capacity):
    ordered = sorted(items, key=lambda x: x[2] / x[1], reverse=True)

    total_weight = 0
    total_value = 0
    selected = []

    for name, weight, value in ordered:
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value
            selected.append(name)

    return total_weight, total_value, selected


weight, value, selected = greedy(items, capacity)
print("Total Weight:", weight)
print("Total Value:", value)
print("Selected Parcels:", selected)
