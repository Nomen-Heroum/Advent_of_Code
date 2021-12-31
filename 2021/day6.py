import src  # My utility functions
from collections import Counter

FISH = src.read(split=',', ints=True)


def procreate(fish, days=80):
    counts = Counter(fish)
    for _ in range(days):
        counts = Counter({days_left - 1: count for days_left, count in counts.items()})
        if counts[-1]:
            new = counts.pop(-1)
            counts[8] = new
            counts[6] += new
    return sum(counts.values())


def main(fish=FISH):
    print("Part One:")
    ans1 = procreate(fish)  # 391888
    print(f"After 80 days there are {ans1} lanternfish.")

    print("\nPart Two:")
    ans2 = procreate(fish, 256)  # 1754597645339
    print(f"After 256 days there are {ans2} lanternfish.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
