import src  # My utility functions
import re

DATA = '10010000000110000'


def find_checksum(data, length):
    data += '0' + data[::-1].translate(str.maketrans('01', '10'))  # First step in string format

    ln = len(data)  # Current length of binary representation
    data = int(data, 2)
    needed = 1 << (length - 1)  # First number of the required length
    while data < needed:
        data = (data << (ln + 1)) + data + (1 << (ln//2))  # Next steps are faster in int format
        ln = 2 * ln + 1  # Update length

    checksum = bin(data)[2:length+2]  # Convert back to string
    while len(checksum) % 2 == 0:
        checksum = re.sub(r'(\d)(\d)', lambda mo: '1' if mo[1] == mo[2] else '0', checksum)

    return checksum


def main(data=DATA):
    print("Part One:")
    ans1 = find_checksum(data, 272)
    print(f"The checksum is {ans1}.")

    print("\nPart Two:")
    ans2 = find_checksum(data, 35651584)
    print(f"The second checksum is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
