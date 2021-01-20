import src
import itertools
from collections import defaultdict
from copy import copy

STRINGS = src.read()


def make_grid(strings, dimensions=3):
    """Returns a defaultdict with coordinate tuples valued 1 for every # in the input."""
    assert dimensions >= 2, "At least 2 dimensions needed."
    grid = defaultdict(int)
    for x, string in enumerate(strings):
        for y, char in enumerate(string):
            if char == '#':
                grid[(x, y) + (0,) * (dimensions-2)] = 1
    return grid


def neighbours(grid, coord):
    """Yields all neighbouring values of a coordinate from a defaultdict grid"""
    coords = ([i-1, i, i+1] for i in coord)
    for site in itertools.product(*coords):
        if site != coord:
            yield grid[site]


def iterate(strings, steps=1, dimensions=3):
    """Makes a starting grid from a list of strings and iterates over it n times."""
    grid = make_grid(strings, dimensions)
    for _ in range(steps):
        new_grid = defaultdict(int)
        ones = copy(grid)
        for key in ones:
            if sum(neighbours(grid, key)) in [2, 3]:
                new_grid[key] = 1
        zeros = [k for k, v in grid.items() if v == 0]
        for key in zeros:
            if sum(neighbours(grid, key)) == 3:
                new_grid[key] = 1
        grid = copy(new_grid)
    return sum(grid.values())


def main(strings=STRINGS):
    print("Part One:")
    ans1 = iterate(strings, 6)
    print(f"The number of active cubes after six cycles is {ans1}.")
    
    print("\nPart Two:")
    ans2 = iterate(strings, 6, 4)
    print(f"In the four dimensional case the end number is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
