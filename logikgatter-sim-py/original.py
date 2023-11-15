def logical_and(a, b):
    return a and b


def logical_or(a, b):
    return a or b


def logical_not(a):
    return not a


# User input for boolean values
a = bool(int(input("Enter 0 or 1 for A: ")))
b = bool(int(input("Enter 0 or 1 for B: ")))

# Apply logical operations
result_and = logical_and(a, b)
result_or = logical_or(a, b)
result_not_a = logical_not(a)
result_not_b = logical_not(b)

print(
    f"A AND B: {result_and}, A OR B: {result_or}, NOT A: {result_not_a}, NOT B: {result_not_b}"
)
