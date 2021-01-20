import src
import heapq
import hashlib
from collections import deque

PASSWORD = 'udskfozm'
START = 0
TARGET = 3+3j
INSTRUCTIONS = {'U': -1j, 'D': 1j, 'L': -1, 'R': 1}
OPEN_CHARS = {'b', 'c', 'd', 'e', 'f'}


def heuristic(node, target):
    """Simple Manhattan distance, admissible."""
    diff = target - node
    return diff.real + diff.imag


def neighbours(node, path: str, instructions=None, open_chars=None):
    instructions = instructions or INSTRUCTIONS
    open_chars = open_chars or OPEN_CHARS

    md5 = hashlib.md5(path.encode('utf-8')).hexdigest()
    for i, (k, v) in enumerate(instructions.items()):
        new_node = node + v
        if 0 <= new_node.real <= 3 and 0 <= new_node.imag <= 3 and md5[i] in open_chars:
            yield new_node, path + k


def a_star(start, target, h, neighs, password=PASSWORD):
    """A* pathfinding algorithm from src.py, adapted for today's problem. Contains only the admissible algorithm."""
    guess = h(start, target)  # Best guess for the shortest path length
    entry_id = 0

    # Priority queue: f(n) is prioritised, with ties broken first by h(n), then by last inserted.
    queue = [(guess, guess, entry_id, start, password)]  # (f(n), h(n), entry, node, path)

    while queue:
        _f, _h, _id, node, path = heapq.heappop(queue)
        for neigh, new_path in neighs(node, path):
            if neigh == target:  # Return straight away when we touch the target node
                return new_path[8:]
            entry_id -= 1  # Negative to ensure LIFO
            h_n = h(neigh, target)
            f_n = len(new_path) - 8 + h_n  # Total path cost
            heapq.heappush(queue, (f_n, h_n, entry_id, neigh, new_path))

    # If every possible node has been visited
    raise EOFError("No path to the target could be found.")


def find_longest(start, target, neighs, password=PASSWORD):
    """Pathfinding that maximises length, for part 2. Searches the entire space."""
    queue = [(start, password, 0)]  # (node, path, g(n))

    lengths = set()

    while queue:
        node, path, g = queue.pop(-1)
        for neigh, new_path in neighs(node, path):
            g_n = g + 1
            if neigh == target:  # Return straight away when we touch the target node
                lengths.add(g_n)
                continue
            queue.append((neigh, new_path, g_n))

    return max(lengths)


def main():
    print("Part One:")
    ans1 = a_star(START, TARGET, heuristic, neighbours)
    print(f"The shortest path to the vault is {ans1}.")

    print("\nPart Two:")
    ans2 = find_longest(START, TARGET, neighbours)
    print(f"The longest path has length {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
