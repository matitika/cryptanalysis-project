from spn import *
from attack import first_two_nibbles_equal

def combine_nibbles_to_integer(nibbles):
    result = 0
    for nibble in nibbles:
        result = (result << 4) | nibble  # Shift left and add the nibble
    return result

# Example usage with decimal nibbles
nibbles = [1, 2, 3, 4]  # Example list of decimal nibbles
decimal_integer = combine_nibbles_to_integer(nibbles)
print(decimal_integer)  # Output: 190

print(spn(0xffff, [0xffff, 0xffff, 0xffff, 0xffff, 0xffff]))