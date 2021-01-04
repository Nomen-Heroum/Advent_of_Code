import src
from itertools import groupby
import numpy as np

NUMBERS = [int(S) for S in src.read(10)]


def jolt(numbers=None):
    if numbers is None:
        numbers = NUMBERS

    numbers += [0, max(numbers) + 3]
    return sorted(numbers)


def differences(joltages):
    return [j - joltages[i] for i, j in enumerate(joltages[1:])]


def part_one(joltages: list):
    diff = differences(joltages)
    return diff.count(1) * diff.count(3)


def part_two(joltages: list):
    groups = [list(g) for _, g in groupby(differences(joltages))]
    sizes = [len(g) for g in groups if g[0] == 1]
    orders = 2**np.array([s - 1 for s in sizes if s > 1])
    orders = orders.clip(max=7)
    return np.prod(orders)


def main(joltages=None):
    if joltages is None:
        joltages = jolt()

    print("Part One:")
    ans1 = part_one(joltages)
    print(f"The first answer is {ans1}.")

    print("\nPart Two:")
    ans2 = part_two(joltages)
    print(f"There are {ans2} possible arrangements of chargers.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
