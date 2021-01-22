import src  # My utility functions
import re
import json

STRING = src.read()[0]


def sum_numbers(string):
    numbers = re.findall(r'-?\d+', string)
    return sum(int(n) for n in numbers)


def sum_red(struct):
    total = 0
    if isinstance(struct, int):
        total += struct
    elif isinstance(struct, list):
        total += sum(sum_red(s) for s in struct)
    elif isinstance(struct, dict):
        vals = struct.values()
        if 'red' not in vals:
            total += sum(sum_red(s) for s in vals)
    return total


def main(string=STRING):
    print("Part One:")
    total = sum_numbers(string)
    print(f"Total of numbers: {total}")

    print("\nPart Two:")
    structure = json.loads(string)
    no_red = sum_red(structure)
    print(f"Total of red-free numbers: {no_red}")
    src.clip(no_red)


if __name__ == '__main__':
    main()
