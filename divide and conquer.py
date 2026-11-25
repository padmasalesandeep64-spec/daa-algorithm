items = [
    ("Laptop", 5, 60),
    ("Books", 4, 40),
    ("Camera", 6, 70),
    ("Shoes", 3, 30),
    ("Headphones", 2, 25)
]
capacity = 17

def generate_subsets(items):
    result = [(0, 0, [])]

    for name, weight, value in items:
        additions = []
        for old_weight, old_value, selected in result:
            additions.append((
                old_weight + weight,
                old_value + value,
                selected + [name]
            ))
        result += additions

    return result


def divide_and_conquer(items, capacity):
    middle = len(items) // 2
    left = [s for s in generate_subsets(items[:middle])
            if s[0] <= capacity]
    right = [s for s in generate_subsets(items[middle:])
             if s[0] <= capacity]
    right.sort(key=lambda x: x[0])

    best_right = []
    best = (0, 0, [])

    for subset in right:
        if subset[1] > best[1]:
            best = subset
        best_right.append(best)

    answer = (0, 0, [])

    for left_weight, left_value, left_items in left:
        limit = capacity - left_weight
        low, high = 0, len(right) - 1
        index = -1

        while low <= high:
            mid = (low + high) // 2
            if right[mid][0] <= limit:
                index = mid
                low = mid + 1
            else:
                high = mid - 1

        if index >= 0:
            right_weight, right_value, right_items = best_right[index]
            candidate = (
                left_weight + right_weight,
                left_value + right_value,
                left_items + right_items
            )
        else:
            candidate = (left_weight, left_value, left_items)

        if candidate[1] > answer[1]:
            answer = candidate

    return answer


weight, value, selected = divide_and_conquer(items, capacity)
print("Maximum Weight:", weight)
print("Maximum Value:", value)
print("Selected Parcels:", selected)
