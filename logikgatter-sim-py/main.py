def logical_and(a, b):
    return int(a and b)


def logical_or(a, b):
    return int(a or b)


def logical_not(a):
    return int(not a)


def half_adder(a, b):
    sign = int(a ^ b)
    carry = int(a and b)

    return sign, carry


def full_adder(a, b, c=0):
    sign = int(a ^ b ^ c)
    carry = int(((a ^ b) and c) or (a and b))

    return sign, carry


def byte_adder(z1, z2):
    carry = 0
    result = []
    for i in range(8):
        sign, carry = full_adder(z1[i], z2[i], carry)
        result.append(sign)

        print(f"z1: {z1[i]} z2: {z2[i]} carry: {carry} sign: {sign}")

    return result


# User input for boolean values
a = int(int(input("Enter 0 or 1 for A: ")))
b = int(int(input("Enter 0 or 1 for B: ")))

# Apply logical operations
result_and = logical_and(a, b)
result_or = logical_or(a, b)
result_not_a = logical_not(a)
result_not_b = logical_not(b)

byte1 = [1, 0, 1, 0, 1, 0, 1, 0]
byte2 = [0, 1, 1, 1, 1, 1, 1, 1]

print(
    f"""A AND B: {result_and}
    A OR B: {result_or}
    NOT A: {result_not_a}
    NOT B: {result_not_b}

    Half Adder: {half_adder(a,b)}
    Full Adder: {full_adder(a,b)}

    Byte Adder (Links nach Rechts):
         byte1: {byte1}
         byte2: {byte2}
                ----------------------------
        Result: {byte_adder(byte1, byte2)}
"""
)
