import src  # My utility functions

STRINGS = [s.split() for s in src.read()]
SORTED = [[tuple(sorted(s)) for s in p] for p in STRINGS]


def count_valid(strings):
    return sum(len(phrase) == len(set(phrase)) for phrase in strings)


def main():
    print("Part One:")
    ans1 = count_valid(STRINGS)  # 337
    print(f"There are {ans1} valid passphrases.")

    print("\nPart Two:")
    ans2 = count_valid(SORTED)  # 231
    print(f"With the new policy there are {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
