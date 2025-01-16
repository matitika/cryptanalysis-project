from spn import *
import pandas as pd

def first_two_nibbles_equal(c1, c2):
    first_two_nibbles_1 = (c1 >> 8)
    first_two_nibbles_2 = (c2 >> 8)
    
    # Check if their values are equal
    return first_two_nibbles_1 == first_two_nibbles_2

def reverse_sbox(input):
    rev_s_box = [14, 3, 6, 1, 15, 0, 8, 11, 13, 7, 2, 12, 10, 5, 4, 9]
    nibbles = [(input >> (4 * i)) & 0xF for i in range(4)]
    nibbles.reverse()
    output = 0
    for nibble in nibbles:
        output = (output << 4) | rev_s_box[nibble]
    
    return output
    
    
def main():

    # Opening the ciphertext pairs file
    with open("ciphertext_pairs.txt") as f:
        pairs = []
        for line in f:
            values = line.strip().split(',')
            if len(values) == 2:  # Ensure there are exactly 2 values
                # Convert the values to the desired type (e.g., int)
                pair = (int(values[0].strip(), 16), int(values[1].strip(), 16))
                pairs.append(pair)

    # Desired ciphertext difference in hex
    difference = 0x0088

    # Find pairs that have 0 difference in the first 8 bits
    possible_pairs = []
    for c1, c2 in pairs:
        if first_two_nibbles_equal(c1, c2):
            possible_pairs.append((c1, c2))
    
    key_count = [0] * 256
    for i in range(256):
        for c1, c2 in possible_pairs:
            # Reverse key mixing
            reversed_c1 = c1 ^ i
            reversed_c2 = c2 ^ i
            # If the difference at the entrance of the fourth round matches the differential characteristic
            if reverse_sbox(reversed_c1) ^ reverse_sbox(reversed_c2) == difference:
                key_count[i] += 1   # increment the count for that value
    
    probabilities = [count / 5000 for count in key_count]
    data = {
        'Partial subkey (hex)': [hex(i) for i in range(256)],
        'Probability': probabilities
    }

    df = pd.DataFrame(data)

    # Set options to display the full DataFrame
    pd.set_option('display.max_rows', None)  # Show all rows
    pd.set_option('display.max_columns', None)  # Show all columns (if applicable)
    pd.set_option('display.float_format', '{:.4f}'.format)  # Format float display

    # Display the DataFrame
    print(df.to_string(index=False))
    
    # The predicted value for the last byte of the fith subkey is the one with the highest occurrences of the desired difference
    predicted_byte = hex(key_count.index(max(key_count)))
    print(f"Predicted byte for fith round key: {predicted_byte}")

if __name__ == "__main__":
    main()