import src
import numpy as np

STRINGS = src.read()
ARRAY = np.pad(np.array(
    [np.fromstring(
        ','.join(s.translate(str.maketrans('.#', '01'))),
        dtype=int,
        sep=','
    ) for s in STRINGS]
), 1)


def next_value(x: int, y: int, grid: np.ndarray):
    live_neighs = sum(src.neighbours(x, y, grid))
    if grid[x, y] == 1 and live_neighs in [2, 3]:
        return 1
    elif grid[x, y] == 0 and live_neighs == 3:
        return 1
    return 0


def iterate(steps=1, grid=ARRAY, version=1):
    if version > 1:
        grid[1, 1] = grid[1, 100] = grid[100, 1] = grid[100, 100] = 1
    for i in range(steps):
        copy = np.zeros_like(grid)
        for x in range(1, 101):
            for y in range(1, 101):
                copy[x, y] = next_value(x, y, grid)
        grid = copy
        if version > 1:
            grid[1, 1] = grid[1, 100] = grid[100, 1] = grid[100, 100] = 1
    return grid


def main():
    print("Part One:")
    final_on = iterate(100).sum()
    print(f"{final_on} lights are on in the final configuration.")

    print("\nPart Two:")
    final_on2 = iterate(100, version=2).sum()
    print(f"{final_on2} lights are on in this version.")
    src.clip(final_on2)


if __name__ == '__main__':
    main()
