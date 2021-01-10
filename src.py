"""
This file contains general use functions for all exercises.
"""
import heapq
import inspect
import os
import re
import numpy as np


def read(split='\n'):
    """Returns a list containing one string for each line of the day's input file."""
    day = re.findall(r'\d+', inspect.stack()[1].filename)[-1]  # Last number in the filename of the caller
    with open(f"Input/input{day}.txt") as f:
        strings = f.read().strip().split(split)
    return strings


def copy(text):
    """Outputs text to the system clipboard as a string."""
    string = str(text)
    with os.popen('xclip -selection c', 'w') as out:
        out.write(string)


def neighbours(x: int, y: int, grid: np.ndarray):
    """Yields all neighbours of a point in a 2D NumPy array."""
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx, dy) != (0, 0):
                yield grid[x + dx, y + dy]


def repeat(f, x, n: int):
    """Applies f to x successively n times."""
    for i in range(n):
        x = f(x)
    return x


def a_star(start, target, h, neighbours_costs, admissible=True):
    """Generic A* pathfinding algorithm. Does not return a path, only the discovered path length.

    A binary heap (heapq) is used for the priority queue. f(n) = g(n) + h(n) is prioritised as always.
    In case of a tie, the node with the lowest heuristic h(n) is prioritised. Further ties are handled
    in reverse insertion order (Last In, First Out).

    Different algorithms are used for admissible and non-admissible heuristics; the admissible case is
    faster, but it breaks for improper heuristics.

    Nodes are stored in sets, so they must be hashable.

    Args:
        start: The starting node.
        target: The target node.
        h: A function that returns the heuristic h(n) of a given node. Takes two arguments: (node, target)
        neighbours_costs: A single-argument function that takes the current node, and yields tuples containing
            each neighbouring node and its distance from the current node: (neighbour, cost)
        admissible (optional): True if the heuristic is admissible (default), False otherwise. Must be set to
            False for non-admissible heuristics to prevent breakage.

    Returns:
        The length of the discovered path.
    """
    print("Working...\r", end='')

    guess = h(start, target)  # Best guess for the shortest path length
    entry_id = 0

    # Priority queue: f(n) is prioritised, with ties broken first by h(n), then by last inserted.
    queue = [(guess, guess, entry_id, start, 0)]  # (f(n), h(n), entry, node, g(n))

    if admissible:  # Faster, more breakable algorithm
        visited = {start}

        while queue:
            _f, _h, _id, node, g = heapq.heappop(queue)
            for neigh, cost in neighbours_costs(node):
                if neigh == target:  # Return straight away when we touch the target node
                    return g + cost
                if neigh not in visited:
                    entry_id -= 1  # Negative to ensure LIFO
                    g_n = g + cost
                    h_n = h(neigh, target)
                    f_n = g_n + h_n  # Total path cost
                    heapq.heappush(queue, (f_n, h_n, entry_id, neigh, g_n))
                    visited.add(neigh)  # We mark the neighbours as visited to prevent duplicates

    else:  # Slower, more resilient algorithm
        visited = set()

        while queue:
            _f, _h, _id, node, g = heapq.heappop(queue)
            if node == target:  # Only return once the target node is current
                return g
            if node not in visited:
                visited.add(node)  # Without an admissible h(n) we have to mark the current node as visited
                for neigh, cost in neighbours_costs(node):
                    if neigh not in visited:
                        entry_id -= 1  # Negative to ensure LIFO
                        g_n = g + cost
                        h_n = h(neigh, target)
                        f_n = g_n + h_n  # Total path cost
                        heapq.heappush(queue, (f_n, h_n, entry_id, neigh, g_n))

    # If every possible node has been visited
    raise EOFError("No path to the target could be found.")


def orientations(tile: np.ndarray):
    """Yields all different orientations of a 2D NumPy array."""
    for direction in (1, -1):  # Tile is not flipped/flipped
        for rotation in range(4):  # CCW quarter turns
            yield np.rot90(tile, k=rotation)[:, ::direction]
