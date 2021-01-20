import src
from parse import parse

STRINGS = src.read()


def initialize(strings, version=1):
    mem = {}
    zeros = 2**36 - 1
    ones = 0
    floats = [0]
    for s in strings:
        if 'mask' in s:
            zeros = 2**36 - 1
            ones = 0
            floats = [0]
            for i, char in enumerate(s[:-37:-1]):
                if char == '0' and version == 1:
                    zeros -= 2**i
                elif char == '1':
                    ones += 2**i
                elif char == 'X' and version > 1:
                    zeros -= 2**i
                    floats += [n + 2**i for n in floats]
        else:
            address, value = parse('mem[{:d}] = {:d}', s)
            if version == 1:
                mem[address] = (value & zeros) | ones
            else:
                for f in floats:
                    mem[((address & zeros) | ones) + f] = value

    return sum(mem.values())


def main(strings=STRINGS):
    print("Part One:")
    ans1 = initialize(strings)
    print(f"The sum of numbers stored in the memory is {ans1}.")
    
    print("\nPart Two:")
    ans2 = initialize(strings, 2)
    print(f"The sum is {ans2} for version 2.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
