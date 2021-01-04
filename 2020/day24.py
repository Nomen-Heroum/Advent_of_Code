import src
import re
from collections import defaultdict
from copy import copy

STRINGS = src.read(24)
INSTRUCTIONS = {
    'e': lambda x, y: (x+1, y),
    'w': lambda x, y: (x-1, y),
    'nw': lambda x, y: (x, y+1),
    'se': lambda x, y: (x, y-1),
    'ne': lambda x, y: (x+1, y+1),
    'sw': lambda x, y: (x-1, y-1)
}


def decorate(strings: list, instructions: dict):
    flipped = defaultdict(int)
    for s in strings:
        xy = (0, 0)
        for instr in re.findall('nw|ne|sw|se|w|e', s):
            xy = instructions[instr](*xy)
        flipped[xy] = (flipped[xy] + 1) % 2
    return sum(flipped.values()), flipped


def neighbours(flipped: dict, instructions: dict, xy: tuple):
    for neigh in instructions.values():
        yield flipped[neigh(*xy)]


def iterate(flipped, instructions, steps=100):
    flipped = defaultdict(int, {k: v for k, v in flipped.items() if v == 1})
    for _ in range(steps):
        new_flipped = defaultdict(int)
        black = copy(flipped)
        for xy in black:
            if sum(neighbours(flipped, instructions, xy)) in [1, 2]:
                new_flipped[xy] = 1
        white = [k for k, v in flipped.items() if v == 0]
        for xy in white:
            if sum(neighbours(flipped, instructions, xy)) == 2:
                new_flipped[xy] = 1
        flipped = copy(new_flipped)
    return sum(flipped.values())


def main(strings=STRINGS, instructions=None):
    instructions = instructions or INSTRUCTIONS

    print("Part One:")
    ans1, flipped = decorate(strings, instructions)
    print(f"The number of black tiles is {ans1}.")

    print("\nPart Two:")
    ans2 = iterate(flipped, instructions)
    print(f"{ans2} tiles are black after 100 days.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
