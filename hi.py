def assign_categories(lst):
    # Sort the list in descending order
    lst.sort(reverse=True)
    
    c1 = []
    c2 = []
    c3 = []

    category_index = 0
    while lst:
        if category_index == 0:
            c1.append(lst.pop(0))
        elif category_index == 1:
            c2.append(lst.pop(0))
        else:
            c3.append(lst.pop(0))
        category_index = (category_index + 1) % 3

    return c1, c2, c3

# Example usage
numbers = [9, 5, 8, 3, 6, 2, 7, 4, 1]
c1, c2, c3 = assign_categories(numbers)
print("c1:", c1)
print("c2:", c2)
print("c3:", c3)
