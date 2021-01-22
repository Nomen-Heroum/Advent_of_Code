import src  # My utility functions
import numpy as np
import re

STRINGS = src.read()


def unpack(string):
    inst, x1, y1, _, x2, y2 = re.split(r"[ ,]", string)[-6:]
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2) + 1
    y2 = int(y2) + 1
    return inst, x1, y1, x2, y2


def apply_instruction(string, grid):
    inst, x1, y1, x2, y2 = unpack(string)
    if inst == 'on':
        grid[x1:x2, y1:y2] = 1
    elif inst == 'off':
        grid[x1:x2, y1:y2] = -1
    elif inst == 'toggle':
        grid[x1:x2, y1:y2] *= -1
    else:
        raise ValueError("Unknown instruction encountered.")


def count_lights(strings=STRINGS, grid=-np.ones((1000, 1000))):
    for s in strings:
        apply_instruction(s, grid)
    count = int((grid.sum() + grid.size) / 2)
    print(f"After {len(strings)} instructions, {count} lights are on.")
    return count


def apply_2(string, grid):
    inst, x1, y1, x2, y2 = unpack(string)
    if inst == 'on':
        grid[x1:x2, y1:y2] += 1
    elif inst == 'off':
        grid[x1:x2, y1:y2] -= 1
        grid[grid < 0] = 0
    elif inst == 'toggle':
        grid[x1:x2, y1:y2] += 2
    else:
        raise ValueError("Unknown instruction encountered.")


def total_lights(strings=STRINGS, grid=np.zeros((1000, 1000))):
    for s in strings:
        apply_2(s, grid)
    total = int(grid.sum())
    print(f"After {len(strings)} instructions, the total brightness is {total}.")
    return total


src.clip(count_lights())

print("\nPart Two:")
src.clip(total_lights())
