import src  # My utility functions
import parse
from copy import deepcopy

PATTERN = parse.compile('{:d},{:d},{:d},{:d}')
POINTS = {PATTERN.parse(s).fixed for s in src.read()}


def count_constellations(points):
    def distance(p1, p2):
        return sum(abs(x1 - x2) for x1, x2 in zip(p1, p2))

    constellations = set()
    for point in points:
        new_constellation = frozenset({point})  # Frozen set to store in set
        for const in deepcopy(constellations):  # Copy to manage mutations during iteration
            if any(distance(point, p) <= 3 for p in const):
                new_constellation |= const
                constellations.remove(const)
        constellations.add(new_constellation)

    return len(constellations)


def main(points=None):
    points = points or POINTS

    print("Part One:")
    ans1 = count_constellations(points)  # 396
    print(f"There are {ans1} constellations in this data.")
    src.clip(ans1)


if __name__ == '__main__':
    main()
