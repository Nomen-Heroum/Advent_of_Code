import src
from itertools import chain, combinations

VOLUMES = [int(s) for s in src.read()]
POWER = chain.from_iterable(combinations(VOLUMES, r) for r in range(4, len(VOLUMES) + 1))


def efficient_ways(volumes):
    for i in range(len(volumes)+1):
        power = combinations(volumes, i)
        ways = sum(sum(s) == 150 for s in power)
        if ways:
            return ways, i


def main():
    print("Part One:")
    ways = sum(sum(s) == 150 for s in POWER)
    print(f"There are {ways} ways to store 150 liters of eggnog in your fridge.")

    print("\nPart Two:")
    nice_ways, n = efficient_ways(VOLUMES)
    print(f"There are {nice_ways} ways to fit the eggnog in {n} bins.")
    src.copy(nice_ways)


if __name__ == '__main__':
    main()
