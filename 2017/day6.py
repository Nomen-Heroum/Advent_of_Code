import src  # My utility functions
from copy import copy

BANKS = src.read('	', ints=True)split='\t')]


def redistribute(banks):
    n = len(banks)
    seen = {tuple(banks): 0}
    steps = 0
    while True:
        steps += 1
        most = max(banks)
        index = banks.index(most)
        banks[index] = 0
        for i in range(1, most + 1):
            banks[(index + i) % n] += 1
        tup = tuple(banks)
        if tup in seen:
            return steps, steps - seen[tup]
        seen[tup] = steps


def main(banks=None):
    banks = banks or BANKS

    ans1, ans2 = redistribute(copy(banks))
    print("Part One:")
    print(f"A repeat is achieved after {ans1} steps.")  # 4074

    print("\nPart Two:")
    print(f"The infinite loop has {ans2} cycles.")  # 2793
    src.clip(ans2)


if __name__ == '__main__':
    main()
