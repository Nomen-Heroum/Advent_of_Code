import src
from collections import Counter

STRINGS = src.read()
POINTS = set()
for S in STRINGS:
    X, Y = [int(n) for n in S.split(', ')]
    POINTS.add(X + Y * 1j)


def find_closest_total(position: complex, points: set):
    """Closest complex manhattan distance, returns None in case of a tie. Also returns total distance."""
    closest = None
    point = None
    total = 0
    for p in points:
        distance = abs((position - p).real) + abs((position - p).imag)
        total += distance
        if closest is None or distance < closest:
            closest = distance
            point = p
        elif distance == closest:
            point = None
    return point, total


def find_areas(points: set, distance=10_000):
    min_x = int(min(z.real for z in points))
    max_x = int(max(z.real for z in points))
    min_y = int(min(z.imag for z in points))
    max_y = int(max(z.imag for z in points))

    infinite = set()
    areas = Counter()
    region_size = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            position = x + y*1j
            closest, total = find_closest_total(position, points)
            if total < distance:
                region_size += 1
            if x in (min_x, max_x) or y in (min_y, max_y):
                infinite.add(closest)
            else:
                areas[closest] += 1
    for point in infinite:
        del areas[point]  # Remove all infinite areas
    del areas[None]  # Remove the count for tied points
    return max(areas.values()), region_size


def main(points=None):
    points = points or POINTS

    ans1, ans2 = find_areas(points)
    print("Part One:")
    print(f"The largest finite area is {ans1}.")  # 3260

    print("\nPart Two:")
    print(f"The size of the region is {ans2}.")  # 42535
    src.copy(ans2)


if __name__ == '__main__':
    main()
