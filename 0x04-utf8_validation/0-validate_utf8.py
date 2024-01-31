#!usr/bin/python3
""" UTF-8 Validation"""

def validUTF8(data):
    a = 0

    while a < len(data):
        # Determine the number of bytes for the current character
        if (data[a] & 0b10000000) == 0b00000000:  # 1 byte character
            length = 1
        elif (data[a] & 0b11100000) == 0b11000000:  # 2 byte character
            length = 2
        elif (data[a] & 0b11110000) == 0b11100000:  # 3 byte character
            length = 3
        elif (data[a] & 0b11111000) == 0b11110000:  # 4 byte character
            length = 4
        else:
            return False  # Invalid start byte

        # Check for the validity of continuation bytes
        for b in range(1, length):
            if a + b >= len(data) or (data[a + b] & 0b11000000) != 0b10000000:
                return False  # Invalid continuation byte

        a += length

    return True
