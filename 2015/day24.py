import src
import itertools
import math

WEIGHTS = [int(s) for s in src.read()]


def configure(weights: list, groups=3):
    assert sum(weights) % groups == 0, f"Total weight is not a multiple of {groups}."
    target = sum(weights) // groups
    for size in itertools.count(1):
        qe_list = [math.prod(c) for c in itertools.combinations(weights, size) if sum(c) == target]
        if qe_list:
            return min(qe_list)


def main(weights=None):
    weights = weights or WEIGHTS

    print("Part One:")
    ans1 = configure(weights)
    print(f"The best configuration has a QE of {ans1}.")

    print("\nPart Two:")
    ans2 = configure(weights, groups=4)
    print(f"The best QE is now {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
