import src  # My utility functions
import numpy as np

STRINGS = src.read()


def neighbours(x, y):
    for diff in (-1, 1):
        yield x + diff, y
        yield x, y + diff


def low_points_risk(height_map):
    size = len(height_map)
    risk = 0
    low_points = []
    for x in range(1, size - 1):
        for y in range(1, size - 1):
            height = height_map[x, y]
            if height < min(height_map[neigh] for neigh in neighbours(x, y)):
                risk += height + 1
                low_points.append((x, y))
    return risk, low_points


def find_basins(height_map, low_points=None):
    if not low_points:
        low_points = low_points_risk(height_map)[1]

    basin_sizes = []
    for point in low_points:
        visited = {point}
        queue = [point]

        while queue:
            node = queue.pop(0)
            for neigh in neighbours(*node):
                if height_map[neigh] < 9 and neigh not in visited:
                    visited.add(neigh)
                    queue.append(neigh)

        basin_sizes.append(len(visited))

    return np.prod(sorted(basin_sizes)[-3:])


def main(strings=STRINGS):
    height_map = np.genfromtxt(strings, int, delimiter=1)
    height_map = np.pad(height_map, 1, constant_values=9)
    print("Part One:")
    ans1, low_points = low_points_risk(height_map)  # 462
    print(f"The sum of risk levels for all low points is {ans1}.")

    print("\nPart Two:")
    ans2 = find_basins(height_map, low_points)  # 1397760
    print(f"The three largest basin sizes multiply to {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
