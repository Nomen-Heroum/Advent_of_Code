import src  # My utility functions
from collections import defaultdict

STRINGS = src.read()


def count_orbits(strings):
    orbits = defaultdict(set)
    for s in strings:
        primary, secondary = s.split(')')
        orbits[primary].add(secondary)

    total = 0
    level = 1
    current = {'COM'}
    while current:
        new = set()
        for body in current:
            new |= orbits[body]
            total += level * len(orbits[body])
        current = new
        level += 1

    return total, orbits


def neighbours(body, orbits, orbiting):
    if body in orbits:
        yield from orbits[body]
    if body in orbiting:
        yield orbiting[body]


def main(strings=STRINGS):
    print("Part One:")
    ans1, orbits = count_orbits(strings)  # 247089
    print(f"The total number of direct and indirect orbits is {ans1}.")

    print("\nPart Two:")
    orbiting = {}
    for s in strings:
        primary, secondary = s.split(')')
        orbiting[secondary] = primary
    ans2 = src.a_star('YOU', 'SAN', lambda _n, _t: 0, neighbours, orbits=orbits, orbiting=orbiting) - 2
    print(f"It takes {ans2} orbital transfers to get to Santa.")  # 442
    src.clip(ans2)


if __name__ == '__main__':
    main()
