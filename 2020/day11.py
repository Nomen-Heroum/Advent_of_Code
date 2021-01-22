import src  # My utility functions
import numpy as np

STRINGS = src.read()


def grid_seats(strings=STRINGS):
    seats = np.pad(np.array(
        [np.fromstring(
            ','.join(s.translate(str.maketrans('.L', '01'))),
            dtype=int,
            sep=','
        ) for s in strings]
    ), 1, constant_values=1) == 1
    grid = np.zeros_like(seats, dtype=int)
    return grid, seats


ARRAY, SEATS = grid_seats()


def next_seat(pos: tuple, xdir: int, ydir: int):
    x, y, grid, seats = pos
    y += xdir
    x += ydir
    while not seats[x, y]:
        y += xdir
        x += ydir
    return grid[x, y]


def neighbouring_seats(x: int, y: int, grid: np.ndarray, seats: np.ndarray):
    pos = (x, y, grid, seats)
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx, dy) != (0, 0):
                yield next_seat(pos, dx, dy)


def next_value(x: int, y: int, grid: np.ndarray, seats: np.ndarray, version=1):
    if version == 1:
        neighs = src.neighbours(x, y, grid)
        staycond = range(4)
    else:
        neighs = neighbouring_seats(x, y, grid, seats)
        staycond = range(5)
    seated_neighs = sum(neighs)
    if grid[x, y] == 1 and seated_neighs in staycond:
        return 1
    elif grid[x, y] == 0 and seated_neighs == 0:
        return 1
    return 0


def iterate(grid: np.ndarray, seats: np.ndarray, version=1):
    xsize, ysize = grid.shape
    while True:
        copy = np.zeros_like(grid)
        for x in range(1, xsize - 1):
            for y in range(1, ysize - 1):
                if seats[x, y]:
                    copy[x, y] = next_value(x, y, grid, seats, version)
        if np.array_equal(grid, copy):
            return grid
        grid = copy


def main(grid=ARRAY, seats=SEATS):
    print("Part One:")
    final_seats = iterate(grid, seats).sum()
    print(f"{final_seats} seats are occupied in the final configuration.")

    print("\nPart Two:")
    final_2 = iterate(grid, seats, version=2).sum()
    print(f"{final_2} seats are occupied in this version.")
    src.clip(final_2)


if __name__ == '__main__':
    main()
