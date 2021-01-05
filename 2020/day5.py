import src
import re

STRINGS = src.read()


def seat_id(string):
    ones = re.sub(r'B|R', '1', string)
    binary = re.sub(r'F|L', '0', ones)
    return int(binary, 2)


def main(strings=STRINGS):
    print("Part One:")
    ids = [seat_id(s) for s in strings]
    highest = max(ids)
    print(f"Highest seat ID out of {len(strings)} tickets: {highest}")

    print("\nPart Two:")
    lowest = min(ids)
    seat_range = range(lowest, highest + 1)
    for seat in seat_range:
        if seat not in ids:
            print(f"My seat number is {seat}!")
            src.copy(seat)


if __name__ == '__main__':
    main()
