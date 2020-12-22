import src
import parse

STRINGS = src.read(16)
PATTERN = parse.compile("Sue {}: {}: {:d}, {}: {:d}, {}: {:d}")
SUES = {}
for s in STRINGS:
    num, k1, v1, k2, v2, k3, v3 = PATTERN.parse(s)
    SUES[num] = {k1: v1, k2: v2, k3: v3}

MFCSAM = {
    'children': lambda x: x == 3,
    'cats': lambda x: x == 7,
    'samoyeds': lambda x: x == 2,
    'pomeranians': lambda x: x == 3,
    'akitas': lambda x: x == 0,
    'vizslas': lambda x: x == 0,
    'goldfish': lambda x: x == 5,
    'trees': lambda x: x == 3,
    'cars': lambda x: x == 2,
    'perfumes': lambda x: x == 1
}
MFCSAM2 = {
    'children': lambda x: x == 3,
    'cats': lambda x: x > 7,
    'samoyeds': lambda x: x == 2,
    'pomeranians': lambda x: x < 3,
    'akitas': lambda x: x == 0,
    'vizslas': lambda x: x == 0,
    'goldfish': lambda x: x < 5,
    'trees': lambda x: x > 3,
    'cars': lambda x: x == 2,
    'perfumes': lambda x: x == 1
}


def find_sue(mfcsam=None):
    mfcsam = mfcsam or MFCSAM

    for sue in SUES:
        data = SUES[sue]
        if all(mfcsam[key](data[key]) for key in data):
            return sue
    raise EOFError("All Sues checked without match.")


def main():
    src.one()
    sue = find_sue()
    print(f"The real Sue is Sue {sue}.")

    src.two()
    sue2 = find_sue(MFCSAM2)
    print(f"The REAL Sue is Sue {sue2}.")
    src.copy(sue2)


if __name__ == '__main__':
    main()
