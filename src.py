"""
This file contains general use functions for all exercises.
"""

import os
import re

import numpy as np


def read(day: int, split='\n'):
    """Returns a list containing one string for each line of the day's input file."""
    with open(f"Input/input{day}.txt") as f:
        strings = f.read().strip().split(split)
    return strings


def copy(text):
    """Outputs text to the system clipboard as a string."""
    string = str(text)
    with os.popen('xclip -selection c', 'w') as out:
        out.write(string)


def one():
    print("Part One:")


def two():
    print("\nPart Two:")


def neighbours(x: int, y: int, grid: np.ndarray):
    yield grid[x, y - 1]
    yield grid[x, y + 1]
    yield grid[x - 1, y]
    yield grid[x + 1, y]
    yield grid[x - 1, y - 1]
    yield grid[x - 1, y + 1]
    yield grid[x + 1, y - 1]
    yield grid[x + 1, y + 1]


def repeat(f, x, n: int):
    for i in range(n):
        x = f(x)
    return x
